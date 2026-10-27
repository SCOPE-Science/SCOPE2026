"""Exact finite identity checks for common literal successor runs.
Uses only Python's standard library. Scientific limits are documented separately.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, comb

def falling(n,k):
    if not 0 <= k <= n:
        raise ValueError('invalid falling factorial')
    return factorial(n)//factorial(n-k)

def predicted(n,ell):
    m=n-ell
    assert m>0 and 1<=ell<n
    mean=Fraction(m, falling(n,ell))
    second=Fraction(0)
    for d in range(1,min(ell,m-1)+1):
        second+=Fraction(m-d,falling(n,ell+d))
    if m>=ell+2:
        second+=Fraction(comb(m-ell,2),falling(n,2*ell))
    return mean,second

def runs(perm,ell):
    return {tuple(perm[i:i+ell+1]) for i in range(len(perm)-ell)}

def check():
    comparisons=0
    constancy=0
    for n in range(3,9):
        canon=tuple(range(n))
        all_perms=list(permutations(range(n)))
        for ell in range(1,min(4,n-1)+1):
            target=predicted(n,ell)
            base=runs(canon,ell)
            observed_mean=0
            observed_second=0
            positive=0
            for other in all_perms:
                z=len(base & runs(other,ell))
                observed_mean+=z
                observed_second+=comb(z,2)
                positive+=(z>=1)
                comparisons+=1
            assert (Fraction(observed_mean,len(all_perms)),Fraction(observed_second,len(all_perms)))==target, (n,ell,target,observed_mean,observed_second)
            assert target[0]-target[1] <= Fraction(positive,len(all_perms)) <= target[0]
            # The conditionally constant law of a pair of permutations,
            # even with the first permutation prescribed, is the independence input.
            if n<=5:
                firsts=all_perms
            else:
                firsts=[all_perms[1],all_perms[-1]]
            for first in firsts:
                a=runs(first,ell)
                cnt=sum(bool(a & runs(other,ell)) for other in all_perms)
                assert cnt==positive,(n,ell,'conditional invariance')
                constancy+=1
    # Exhaustive count for the critical indicator sum with r=3, n=4, ell=2:
    n,ell=4,2
    Ps=list(permutations(range(n)))
    subset={p:runs(p,ell) for p in Ps}
    counts=[0]*4
    for p in Ps:
        for q in Ps:
            for s in Ps:
                w=int(bool(subset[p]&subset[q]))+int(bool(subset[p]&subset[s]))+int(bool(subset[q]&subset[s]))
                counts[w]+=1
    assert sum(counts)==factorial(n)**3
    marginal=sum(i*x for i,x in enumerate(counts))/factorial(n)**3
    p=sum(bool(subset[Ps[0]]&subset[q]) for q in Ps)/len(Ps)
    assert abs(marginal-3*p)<1e-12
    print('SUCCESSOR_RUN_EXACT_OK',comparisons,constancy,counts)
if __name__=='__main__':
    check()
