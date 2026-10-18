#!/usr/bin/env python3
"""Exact checks for maximal ambiguity of ordered cyclic orbit signatures.
Only Python's standard library is required.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import gcd, factorial


def digit_reverse_order(p, k):
    n = p ** k
    ans = []
    for x in range(n):
        digits = []
        for _ in range(k):
            x, d = divmod(x, p)
            digits.append(d)
        y = 0
        for d in digits:
            y = p*y + d
        ans.append(y)
    return tuple(ans)


def permutation_from_phases(a):
    n=len(a)
    assert sorted(a)==list(range(n)) and a[0]==0
    inv=[None]*n
    for i,x in enumerate(a): inv[x]=i
    return tuple(inv[(x+1)%n] for x in a)


def signature_from_phases(a):
    n=len(a)
    # direct full signatures, no use of the recursive matching relation
    inv=[None]*n
    for i,x in enumerate(a): inv[x]=i
    return tuple(tuple(inv[(a[i]+t)%n] <= i for t in range(n)) for i in range(n))


def signature_from_permutation(f):
    n=len(f)
    ans=[]
    for i in range(n):
        x=i; row=[True]
        for t in range(1,n):
            x=f[x]
            row.append(x<=i)
        ans.append(tuple(row))
    return tuple(ans)


def all_n_cycles(n):
    for rest in permutations(range(1,n)):
        cyc=(0,)+rest
        f=[None]*n
        for i,x in enumerate(cyc):
            f[x]=cyc[(i+1)%n]
        yield tuple(f)


def by_perm_histogram(n):
    counts=Counter()
    for f in all_n_cycles(n):
        counts[signature_from_permutation(f)]+=1
    return Counter(counts.values())


def via_prefix_matching(signature):
    # Enumerate phase arrays from each row as translations of the known prefix.
    n=len(signature)
    sols=[(0,)]
    for i in range(1,n):
        row=signature[i]
        assert row[0]
        wanted=tuple((t!=0) and row[t] for t in range(n))
        next_sols=[]
        for a in sols:
            S=set(a)
            for phase in range(n):
                if phase in S: continue
                if all(((phase+t)%n in S)==wanted[t] for t in range(n)):
                    next_sols.append(a+(phase,))
        sols=next_sols
    for a in sols:
        assert signature_from_phases(a)==signature
    return sols


def upper(n):
    z=1
    for i in range(1,n): z*=gcd(n,i)
    return z


def construction_check(p,k):
    a=digit_reverse_order(p,k)
    n=p**k
    sig=signature_from_phases(a)
    f=permutation_from_phases(a)
    assert signature_from_permutation(f)==sig
    # Every prefix stabilizer attains the largest possible order.
    for i in range(1,n):
        S=set(a[:i]); stabilizer=[h for h in range(n) if {(x+h)%n for x in S}==S]
        assert len(stabilizer)==gcd(n,i),(p,k,i,len(stabilizer))
    sols=via_prefix_matching(sig)
    assert len(sols)==upper(n),(p,k,len(sols),upper(n))
    return n, len(sols)


def main():
    tests=[(2,2),(2,3),(3,2),(2,4),(5,2)]
    for p,k in tests:
        n,count=construction_check(p,k)
        print('prime-power saturation',n,'maximum=',count)
    expected={
        4:{1:4,2:1},
        6:{1:68,2:16,3:4,4:2},
        8:{1:3552,2:544,4:72,8:12,16:1},
        9:{1:37584,3:864,9:16},
    }
    for n,want in expected.items():
        h=by_perm_histogram(n)
        assert h==want,(n,h)
        assert sum(size*m for size,m in h.items())==factorial(n-1)
        assert max(h)<=upper(n)
        print('complete brute n=',n,'signature-fibre histogram:',sorted(h.items()),'U=',upper(n))
    # Independent 9-cycle enumeration: phase orders instead of direct cyclic permutations.
    h2=Counter()
    for tail in permutations(range(1,9)):
        a=(0,)+tail
        h2[signature_from_phases(a)]+=1
    assert Counter(h2.values())==expected[9]
    print('independent phase enumeration n=9 confirmed',len(h2),'signatures')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__': main()
