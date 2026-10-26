#!/usr/bin/env python3
"""Independent finite checks for coloured equivalence-block counting identities.

Python standard library only. All checks are finite and do not certify limits.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import comb, factorial
from fractions import Fraction


def check_joint_exact(b, m, k):
    """Enumerate all binary block colours and compare the multinomial law."""
    assert b > 2*k
    observed = Counter()
    for values in product(range(1 << b), repeat=m):
        reds = [x.bit_count() for x in values]
        observed[(reds.count(k), reds.count(b-k))] += 1
    p = Fraction(comb(b, k), 1 << b)
    for u in range(m+1):
        for v in range(m+1-u):
            weight = Fraction(factorial(m), factorial(u)*factorial(v)*factorial(m-u-v)) * p**(u+v) * (1-2*p)**(m-u-v)
            assert Fraction(observed[(u,v)], 1 << (b*m)) == weight, (b,m,k,u,v)
    return 1 << (b*m)


def model(b, counts):
    vertices=[]
    colors=[]
    for block,reds in enumerate(counts):
        for z in range(b):
            vertices.append(block)
            colors.append(z<reds)
    return tuple(vertices),tuple(colors)


def q_profile(b, counts, q):
    c=Counter((min(x,q),min(b-x,q)) for x in counts)
    return tuple(sorted((r,s,min(num,q)) for (r,s),num in c.items()))


def ef_wins(A,B,q):
    ba,ca=A;bb,cb=B
    @lru_cache(None)
    def rec(k,xs,ys):
        for i in range(len(xs)):
            for j in range(len(xs)):
                if (xs[i]==xs[j]) != (ys[i]==ys[j]):return False
                if (ba[xs[i]]==ba[xs[j]]) != (bb[ys[i]]==bb[ys[j]]):return False
            if ca[xs[i]] != cb[ys[i]]:return False
        if k==0:return True
        for a in range(len(ba)):
            if not any(rec(k-1,xs+(a,),ys+(b,)) for b in range(len(bb))):return False
        for b in range(len(bb)):
            if not any(rec(k-1,xs+(a,),ys+(b,)) for a in range(len(ba))):return False
        return True
    return rec(q,(),())


def check_profiles():
    cases=[]
    for b in range(2,5):
        for m in range(1,4):
            for ct in combinations_with_replacement(range(b+1),m):
                cases.append((b,ct))
    total=0
    for q in (1,2):
        groups=defaultdict(list)
        for b,ct in cases:groups[q_profile(b,ct,q)].append((b,ct))
        for vals in groups.values():
            # All pairs for small EF games, including different block sizes.
            for i,A in enumerate(vals):
                for B in vals[i:]:
                    assert ef_wins(model(*A),model(*B),q),(q,A,B)
                    total+=1
    return total


def check_critical_means():
    checked=0
    for k in range(4):
        means=[]
        for b in (12,16,20,24,28,32):
            if b<=2*k:continue
            m=(factorial(k)*(1<<b))//(b**k)
            mu=Fraction(m*comb(b,k),1<<b)
            means.append(float(mu));checked+=1
        assert abs(means[-1]-1)<0.1,(k,means)
    return checked


def main():
    exact=0
    for b in range(3,7):
        for m in range(1,4):
            if b*m>15:continue
            for k in range((b-1)//2+1):
                exact += check_joint_exact(b,m,k)
    ef=check_profiles()
    critical=check_critical_means()
    print('COLOURED_EQ_EXACT_OK',exact,ef,critical)

if __name__=='__main__':main()
