"""Standalone tests for fixed-anchor linear monotone iteration asymptotics.
Uses Python standard library; exact rational identities plus approximate trajectories.
"""
from fractions import Fraction as Q
from math import sqrt, isfinite


def mv(M,v):
    return [sum(a*x for a,x in zip(row,v)) for row in M]

def inv2(M):
    a,b=M[0]; c,d=M[1]; det=a*d-b*c
    assert det != 0
    return [[d/det,-b/det],[-c/det,a/det]]
def add(a,b): return [x+y for x,y in zip(a,b)]
def scale(a,v): return [a*x for x in v]
def maxabs(a): return max(abs(x) for x in a)
def norm(a): return sqrt(sum(x*x for x in a))
def sub(a,b): return add(a,scale(-1,b))

def coeffs(M,L,g,b):
    R=inv2(M)
    C=scale(g*L,mv(R,b))
    D=scale(-g*(g-Q(1,2))*L*L,mv(R,mv(R,b)))
    E=scale(g*(g-Q(1,2))*(g-1)*L**3,mv(R,mv(R,mv(R,b))))
    return C,D,E

def check_exact():
    n=0
    tests=[([[Q(1),Q(0)],[Q(0),Q(1)]],Q(1)),
           ([[Q(2),Q(0)],[Q(0),Q(1)]],Q(2)),
           ([[Q(0),Q(-1)],[Q(1),Q(0)]],Q(1)),
           ([[Q(3),Q(-4)],[Q(4),Q(3)]],Q(5))]
    for M,L in tests:
        for g in range(2,15):
            for b in [[Q(1),Q(-2)],[Q(2),Q(3)]]:
                C,D,E=coeffs(M,L,Q(g),b)
                assert mv(M,C)==scale(g*L,b); n+=1
                assert mv(M,D)==scale(-(Q(g)-Q(1,2))*L,C); n+=1
                assert mv(M,E)==scale((Q(1)-g)*L,D); n+=1
                discrepancy=add(D,scale(g*g*L*L,mv(inv2(M),mv(inv2(M),b))))
                expected=scale(Q(g,2)*L*L,mv(inv2(M),mv(inv2(M),b)))
                assert discrepancy==expected; n+=1
    return n

def tail(M,L,g,b,N):
    x=[float(z) for z in b]
    for k in range(N):
        s=k+g
        mx=mv(M,x)
        x=[(1-g/s)*v-m/(L*sqrt(s))+(g/s)*bi for v,m,bi in zip(x,mx,b)]
    s=N+g
    C,D,E=coeffs([[Q(z) for z in row] for row in M],Q(L),Q(g),[Q(z) for z in b])
    C=list(map(float,C));D=list(map(float,D));E=list(map(float,E))
    err=sub(x,add(scale(1/sqrt(s),C),scale(1/s,D)))
    # tikhonov equilibrium
    mat=[[M[i][j]+(g*L/sqrt(s) if i==j else 0) for j in range(2)] for i in range(2)]
    v=scale(g*L/sqrt(s),mv(inv2(mat),b))
    lag=scale(s,sub(x,v))
    laglim=scale(g*L*L/2,mv(inv2(M),mv(inv2(M),b)))
    res=scale(sqrt(s),mv(M,x))
    reslim=scale(g*L,b)
    return dict(N=N,lead=maxabs(sub(res,reslim)),second=maxabs(scale(s,err)),lag=maxabs(sub(lag,laglim)),target=norm(reslim))

if __name__=='__main__':
    n=check_exact()
    print('Exact coefficient checks:',n)
    for M,L in [([[1.,0.],[0.,1.]],1.),([[2.,0.],[0.,1.]],2.),([[0.,-1.],[1.,0.]],1.),([[3.,-4.],[4.,3.]],5.)]:
        for g in [2,3,4]:
            a=tail(M,L,g,[1.,-2.],40000)
            c=tail(M,L,g,[1.,-2.],120000)
            assert all(isfinite(v) for v in c.values())
            assert c['lead']<a['lead'] and c['lag']<a['lag']
            assert c['lead']<max(1.,0.2*c['target']) and c['lag']<max(4.,0.5*c['target'])
            n+=3
    print('Total assertions:',n)
