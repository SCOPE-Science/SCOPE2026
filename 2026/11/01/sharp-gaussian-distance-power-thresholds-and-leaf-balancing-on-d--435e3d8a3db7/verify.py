"""Independent numerical checks of double-star distance-power threshold identities.
Python 3; numpy required. This is corroboration, not proof of all sizes.
"""
import math
import numpy as np

def profile(a,b,p):
    t=2.0**p;u=3.0**p
    h=t*(t-2.0)/2.0
    z=u-1.0-t*t/2.0
    return np.array([[h-t/a,z],[z,h-t/b]],dtype=float)

def largest(a,b,p):
    return float(np.linalg.eigvalsh(profile(a,b,p))[-1])

def threshold(a,b):
    lo,hi=1.0,2.0
    if (a,b)==(1,1): return 2.0
    assert largest(a,b,lo)<0 and largest(a,b,hi)>0
    for _ in range(80):
        mid=(lo+hi)/2
        if largest(a,b,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def distance_matrix(a,b):
    n=a+b+2
    # centers 0,1; leaves of first center 2..a+1; leaves of second center a+2..
    out=np.zeros((n,n),dtype=float)
    for i in range(n):
        for j in range(n):
            if i==j:continue
            if {i,j}=={0,1}:d=1
            elif i in (0,1) and j>=2:
                d=1 if ((j<2+a)==(i==0)) else 2
            elif j in (0,1) and i>=2:
                d=1 if ((i<2+a)==(j==0)) else 2
            else:
                d=2 if ((i<2+a)==(j<2+a)) else 3
            out[i,j]=d
    return out

def centered_eigs(a,b,p):
    D=distance_matrix(a,b)**p
    N=D.shape[0]
    H=np.eye(N)-np.ones((N,N))/N
    return np.linalg.eigvalsh(H@D@H)

def reduced_Q(a,b,p,A,B,G):
    t,u=2.0**p,3.0**p
    C=-A-B-G
    return ((1-1/a)*t*A*A+(1-1/b)*t*B*B+2*u*A*B
            +2*A*G+2*B*C+2*t*(A*C+B*G)+2*G*C)

checks=0
for a in range(1,11):
    for b in range(a,12):
        if a+b>18: continue
        root=threshold(a,b)
        assert 1.0<root<=2.0
        assert abs(largest(a,b,root))<1e-11
        if root<2-1e-10:
            assert largest(a,b,(root+1.0)/2)<-1e-9
            assert largest(a,b,(root+2.0)/2)>1e-9
        if a+b<=13:
            for p in [1.0, (1.0+root)/2,root, min(2.0,root+0.03)]:
                eig=centered_eigs(a,b,p)
                # Restrict centered form to sum-zero. One zero eigenvalue is constant.
                eig=eig[:-1] if False else eig
                if p<=root+1e-12:
                    assert eig[-1]<2e-9, (a,b,p,eig[-1])
                elif root<2-1e-10:
                    assert eig[-1]>1e-8, (a,b,p,eig[-1])
                checks+=1
        for A,B in [(0.7,-1.2),(1.3,0.9),(-2.4,0.6)]:
            p=(root+1)/2; t=2**p
            G=-A*t/2 + B*t/2-B
            val=reduced_Q(a,b,p,A,B,G)
            red=np.array([A,B])@profile(a,b,p)@np.array([A,B])
            assert abs(val-red)<3e-11,(a,b,p,val,red)
            checks+=1

for L in range(3,37):
    roots=[threshold(a,L-a) for a in range(1,(L//2)+1)]
    assert all(x+1e-10<y for x,y in zip(roots,roots[1:])),(L,roots)
    checks+=1
for m in range(1,300):
    p=threshold(m,m)
    assert abs(3**p-1-(1+1/m)*2**p)<3e-12
    if m>=3:
        C=2/(3*math.log(3)-2*math.log(2))
        assert abs(m*(p-1)-C)<1/m*3
    checks+=1
print('PASS',checks,'explicit assertions / parameter checks')
for a,b in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(5,5),(1,20),(10,10),(50,50)]:
    print('a,b,critical_p',a,b,'%.12f'%threshold(a,b))
