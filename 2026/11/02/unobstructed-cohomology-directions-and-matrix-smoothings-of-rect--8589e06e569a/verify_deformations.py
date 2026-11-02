"""Finite checks of rectangular-band associative deformation identities.
No finite calculation substitutes for the uniform proof.
"""
from itertools import product

def algebra(r,p,q):
    a=r-1
    ee=0; ui=lambda i:1+i; tj=lambda j:1+a+j
    wij=lambda i,j:1+2*a+i*a+j
    d=r*r
    def base(x,y):
        if x==ee and y==ee:return ee
        if 1<=x<=a and y==ee:return x
        if x==ee and a+1<=y<=2*a:return y
        if 1<=x<=a and a+1<=y<=2*a:return wij(x-1,y-a-1)
        return None
    def qterm(x,y,q):
        def left(x):
            if a+1<=x<=2*a:return (0,x-a-1)
            if x>2*a:return ((x-2*a-1)//a+1,(x-2*a-1)%a)
            return None
        def right(y):
            if 1<=y<=a:return (0,y-1)
            if y>2*a:return ((y-2*a-1)%a+1,(y-2*a-1)//a)
            return None
        L,R=left(x),right(y)
        if L is None or R is None:return None
        k,j=L; l,i=R
        if q[j][i]%p==0:return None
        if k==0 and l==0:return (ee,q[j][i]%p)
        if k==0:return (tj(l-1),q[j][i]%p)
        if l==0:return (ui(k-1),q[j][i]%p)
        return (wij(k-1,l-1),q[j][i]%p)
    def bracket(x,y,t,q):
        v=[0]*d
        z=base(x,y)
        if z is not None:v[z]=(v[z]+1)%p
        z=qterm(x,y,q)
        if z is not None:v[z[0]]=(v[z[0]]+t*z[1])%p
        return v
    def times(v,w,t,q):
        out=[0]*d
        for i,c in enumerate(v):
            if not c:continue
            for j,h in enumerate(w):
                if not h:continue
                z=bracket(i,j,t,q)
                for u,val in enumerate(z):out[u]=(out[u]+c*h*val)%p
        return out
    for t in range(p):
        for x,y,z in product(range(d),repeat=3):
            u=times(bracket(x,y,t,q),[int(i==z) for i in range(d)],t,q)
            v=times([int(i==x) for i in range(d)],bracket(y,z,t,q),t,q)
            assert u==v,(r,p,t,x,y,z,u,v)
        print('ASSOCIATIVE',r,p,t)
    for j in range(a):
        for i in range(a):
            qone=[[int((u,v)==(j,i)) for v in range(a)] for u in range(a)]
            assert qterm(tj(j),ui(i),qone)==(ee,1)
            # x=t_j is a left annihilator, y=u_i is a right annihilator.
            assert all(base(tj(j),s) is None for s in range(d))
            assert all(base(s,ui(i)) is None for s in range(d))
    print('INDEPENDENT_NONCOBOUNDARY_PROBES',r,p,a*a)

for r,p in ((2,2),(2,3),(3,2),(3,3)):
    a=r-1
    q=[[int(i==j) for j in range(a)] for i in range(a)]
    algebra(r,p,q)
print('RECTANGULAR_BAND_DEFORMATIONS_OK')
