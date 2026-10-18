"""Exact-rational checks for a negative-doubling hole's finite-time survival law.
Public scientific verification; no external data required.
"""
from fractions import Fraction as F

A=F(2,5)
B=1-A
MARKOV=((0,0,1,1),(0,1,0,0),(0,0,1,0),(1,1,0,0))


def intersect(i,j):
    lo=max(i[0],j[0]); hi=min(i[1],j[1]);
    return (lo,hi) if lo<hi else None


def fuse(intervals):
    q=sorted(intervals)
    ans=[]
    for l,u in q:
        if ans and l<=ans[-1][1]:ans[-1]=(ans[-1][0],max(ans[-1][1],u))
        else:ans.append((l,u))
    return ans


def preimage(J,a=A):
    S=[(F(0),a),(1-a,F(1))]
    out=[]
    for l,u in J:
        for formula,source in ((1,S[0]),(2,S[1])):
            p=intersect(((F(formula)-u)/2,(F(formula)-l)/2),source)
            if p:out.append(p)
    return fuse(out)


def mass(intervals):return sum((u-l for l,u in intervals),F(0))


def matvec(v):return [sum(MARKOV[i][j]*v[j] for j in range(4)) for i in range(4)]


def check():
    v=[1,1,1,1]
    q=[(F(0),A),(B,F(1))]
    for n in range(24):
        expected=F(2*n+4,5*2**n)
        by_matrix=F(sum(v),5*2**n)
        assert mass(q)==by_matrix==expected,(n,mass(q),expected)
        assert v==[n+1,1,1,n+1],(n,v)
        if n<23:
            q=preimage(q)
            v=matvec(v)
    for a in (F(1,8), F(1,4), F(1,3)):
        state=[(F(0),a),(1-a,F(1))]
        for n in range(16):
            assert mass(state)==2*a/F(2**n),(a,n,mass(state))
            if n<15: state=preimage(state,a)
    def T(x):
        return 1-2*x if x<F(1,2) else 2-2*x
    orbit=[F(2,5),F(1,5),F(3,5),F(4,5)]
    assert [T(x) for x in orbit]==orbit[1:]+orbit[:1]
    for n in range(1,24):
        L0=F(2*n+2,5*2**(n-1));L1=F(2*n+4,5*2**n)
        assert (L0-L1)/F(4,5)==F(n,2**(n+1))
    assert sum((F(n,2**(n+1)) for n in range(1,100)),F(0)) < 1
    assert sum((F(n*n,2**(n+1)) for n in range(1,100)),F(0)) <3
    print('PASS: 24 exact direct-preimage survival counts, 24 Markov counts, 48 small-hole checks, 23 hitting-law checks, period-four boundary orbit.')

if __name__=='__main__': check()
