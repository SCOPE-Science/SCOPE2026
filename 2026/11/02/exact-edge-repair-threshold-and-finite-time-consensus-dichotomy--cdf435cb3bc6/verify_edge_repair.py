"""Exact-rational simulations of the adaptive-confidence HK edge-repair theorem.

Run: python verify_edge_repair.py (Python standard library only).
Finite computations corroborate, but do not replace, the arbitrary-order proof.
"""
from fractions import Fraction as Q


def simulate(n, delta, gamma=Q(1,3), steps=110):
    a, b, c0 = Q(1,10), Q(9,10), Q(13,20)
    others = [Q((3+(j%5)),10) for j in range(n-2)]
    initial=[a,b]+others
    x=initial[:]
    c=[[c0 if i!=j else Q(0) for j in range(n)] for i in range(n)]
    weighted_initial=(n-1)*(a+b)+n*sum(others,Q(0))
    eventual_L=weighted_initial/(n*n-2)
    first=None
    for t in range(steps+1):
        good=[[i!=j and abs(x[i]-x[j])<c[i][j] for j in range(n)] for i in range(n)]
        assert all(good[i][j] for i in range(n) for j in range(i+1,n) if (i,j)!=(0,1))
        if good[0][1] and first is None:
            first=t
        if first is None:
            assert x[1]-x[0]==(b-a)/(n-1)**t
            assert c[0][1]==c0*delta**t
            assert (n-1)*(x[0]+x[1])+n*sum(x[2:],Q(0))==weighted_initial
            if t>=1:
                assert all(z==x[2] for z in x[2:])
                assert x[0]<x[2]<x[1]
            # The stationary weighted average is explicitly conserved until repair.
            assert x[0]<=eventual_L<=x[1]
        if first is not None and t>=first+1:
            assert len(set(x))==1
            assert all(good[i][j] for i in range(n) for j in range(i+1,n))
            return first
        if t==steps: break
        nxt=[]
        for i in range(n):
            group=[x[j] for j in range(n) if i==j or good[i][j]]
            nxt.append(sum(group,Q(0))/len(group))
        for i in range(n):
            for j in range(i+1,n):
                c[i][j]=c[j][i]=(c[i][j]+gamma*(1-c[i][j]) if good[i][j] else delta*c[i][j])
        x=nxt
    return first


def expected(n, delta):
    if (n-1)*delta<=1: return None
    ratio=Q(16,13)  # (b-a)/c0
    power=Q(1)
    t=0
    while power<=ratio:
        t+=1
        power*=(n-1)*delta
        assert t<100
    return t


def main():
    cases=0
    for n in range(3,13):
        critical=Q(1,n-1)
        vals={Q(0),critical,critical*Q(3,4),critical*Q(99,100),
              (critical+1)/2,Q(9,10),Q(3,4)}
        for delta in sorted(v for v in vals if 0<=v<1):
            assert simulate(n,delta)==expected(n,delta), (n,delta)
            cases+=1
    assert simulate(3,Q(1,2)) is None
    assert simulate(3,Q(3,4))==1
    assert simulate(4,Q(1,3)) is None
    assert simulate(4,Q(1,2))==1
    print(f'PASS: {cases} exact-rational instances, n=3..12; all edge states, weighted invariant, sharp thresholds and exact repair times.')


if __name__=='__main__': main()
