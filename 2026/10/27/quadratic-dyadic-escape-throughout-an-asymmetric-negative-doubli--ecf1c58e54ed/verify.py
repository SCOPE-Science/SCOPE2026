#!/usr/bin/env python3
"""Exact rational checks for a five-state open interval map."""
from fractions import Fraction as F

M = ((0, 0, 0, 0, 1),
     (0, 1, 1, 1, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 0, 0),
     (1, 1, 0, 0, 0))


def chamber(a, b):
    return F(11,18)<b<F(2,3) and (3-2*b)/4<a<F(4,9)


def intervals(a, b):
    u, v, w = 1-2*a, 2-2*b, 4*a-1
    return ((F(0),u),(u,a),(b,v),(v,w),(w,F(1)))


def clip(a,b):
    l,r=a
    u,v=b
    x,y=max(l,u),min(r,v)
    return (x,y) if x<y else None


def preimage_survivors(a,b,depth):
    live=[(F(0),a),(b,F(1))]
    answer=[]
    for n in range(depth+1):
        answer.append(sum(y-x for x,y in live))
        nxt=[]
        for x,y in live:
            for p in ((1-y)/2,(1-x)/2), (1-y/2,1-x/2):
                for retained in ((F(0),a),(b,F(1))):
                    t=clip(p,retained)
                    if t is not None:
                        nxt.append(t)
        live=nxt
    return answer


def theorem(a,b,n):
    if n==0:return 1+a-b
    return (2+4*a-4*b+(n-1)*(7*a-4*b)+
            (2-3*b)*(n-1)*(n-2)/2) / (2**n)


def path_counts(n):
    row=[1]*5
    for _ in range(n):
        row=[sum(row[i]*M[i][j] for i in range(5)) for j in range(5)]
    return row


def image(i,pieces,a,b):
    x,y=pieces[i]
    return (1-2*y,1-2*x) if i<2 else (2-2*y,2-2*x)


def check_one(a,b):
    assert chamber(a,b)
    parts=intervals(a,b)
    for x,y in parts:
        assert x<y
    for i in range(5):
        out=image(i,parts,a,b)
        for j in range(5):
            length=clip(out,parts[j])
            positive=length is not None
            assert positive == bool(M[i][j]), (i,j,a,b,out,parts[j])
            if positive:
                assert length==parts[j]
    exact=preimage_survivors(a,b,16)
    lengths=[y-x for x,y in parts]
    for n,v in enumerate(exact):
        assert v==theorem(a,b,n),(a,b,n,v,theorem(a,b,n))
        count=path_counts(n)
        assert v*2**n == sum(count[j]*lengths[j] for j in range(5))
        if n>=1:
            assert count == [1,n+1,1+n*(n+1)//2,n,1]
    return len(exact)


def main():
    tested=0
    for b in [F(31,50),F(5,8),F(13,20),F(21,32),F(33,50)]:
        low=(3-2*b)/4
        for t in (F(1,5),F(1,2),F(4,5)):
            a=low+t*(F(4,9)-low)
            tested+=check_one(a,b)
    print('VERIFY_OK chamber_pairs=15 horizons_per_pair=17 exact_mass_tests=',tested)

if __name__=='__main__':main()
