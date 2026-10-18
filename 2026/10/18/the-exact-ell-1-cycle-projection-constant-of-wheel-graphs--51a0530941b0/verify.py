"""Exact certificates for least l1 cycle projections on finite wheel graphs.
Python 3, standard library only. Usage: python verify.py
"""
from fractions import Fraction as F

CERT={
3: (1,1,[1,1,1],[1,-1,0],[1,0,-1],[1,-1,-1],3),
4: (5,4,[5,5,5,5],[5,-5,-5,1],[4,4,-4,-4],[4,-4,-4,-4],15),
5: (7,5,[7]*5,[7,-7,-5,0,7],[5,5,0,-5,-5],[5,-5,-5,-5,-5],21),
6: (3,2,[3]*6,[3,-3,-3,-2,0,3],[2,2,0,0,-2,-2],[2,-2,-2,-2,-2,-2],9),
7: (3,2,[3]*7,[3,-3,-3,-2,0,0,3],[2,2,2,0,0,-2,-2],[2,-2,-2,0,0,-2,-2],9)}

def difference(a):
    return [a[k]-a[k-1] for k in range(len(a))]

def adjoint_difference(a):
    return [a[k]-a[(k+1)%len(a)] for k in range(len(a))]

def norm(a):
    return sum(abs(x) for x in a)+sum(abs(x) for x in difference(a))

def cert(n):
    if n in CERT: return CERT[n]
    assert n>=8
    u=[0]*n;v=[0]*n;w=[0]*n;z=[0]*n
    for k in [0,1,2,3,n-2,n-1]:u[k]=3
    u[n-3]=1
    for k,val in [(0,3),(1,-3),(2,-3),(3,-2),(n-1,3)]:v[k]=val
    for k in [0,1,2,3]:w[k]=2
    for k in [n-3,n-2,n-1]:w[k]=-2
    for k,val in [(0,2),(1,-2),(2,-2),(n-2,-2),(n-1,-2)]:z[k]=val
    return (3,2,u,v,w,z,9)

def test(n):
    p,q,u,v,w,z,value=cert(n)
    assert all(abs(x)<=p for x in u+v)
    assert all(abs(x)<=q for x in w+z)
    aux=[x+y for x,y in zip(u,adjoint_difference(v))]
    t=[-x+y+z0 for x,y,z0 in zip(adjoint_difference(aux),w,adjoint_difference(z))]
    assert aux[0]==value,(n,aux[0],value)
    assert all(t[k]==t[n-1-k] for k in range(n)),(n,t)
    if n>=8:
        assert t==[0,1,-1,1]+[0]*(n-8)+[1,-1,1,0],(n,t)
    target=F(value,p+q)
    if n<=5:
        b=[F(n-1-2*k,4*(n-1)) for k in range(n)]
    else:
        b=[F(0)]*n;b[0]=F(3,10);b[n-1]=-F(3,10)
    a=[F(int(k==0))-difference(b)[k] for k in range(n)]
    assert a[0]==F(1,2) if n<=5 else a[0]==F(2,5)
    R=norm(a);S=norm(b)
    assert R==target and S==target,(n,R,S,target)
    assert all(b[k]==-b[n-1-k] for k in range(n))
    assert all(a[k]+b[k]-b[k-1]==F(int(k==0)) for k in range(n))
    # Check exact inequality certificate identity on several rational antisymmetric b.
    for j in range(n//2):
        b0=[F(0)]*n;b0[j]=F(j+1,7);b0[n-j-1]=-F(j+1,7)
        a0=[F(int(k==0))-difference(b0)[k] for k in range(n)]
        val=sum(x*y for x,y in zip(u,a0))+sum(x*y for x,y in zip(v,difference(a0)))+sum(x*y for x,y in zip(w,b0))+sum(x*y for x,y in zip(z,difference(b0)))
        assert val==value,(n,j,val)
    return target

if __name__=='__main__':
    for n in range(3,61):
        v=test(n)
        if n in list(range(3,12))+[50,60]:print(n,str(v))
    print('PASS: all exact primal and dual identities for n=3..60; symbolic template listed for all n>=8')
