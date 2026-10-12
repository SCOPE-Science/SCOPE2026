#!/usr/bin/env python3
"""Exact fourth-replica and seven-triple incidence verification."""
from itertools import combinations, permutations
from fractions import Fraction

FANO = [(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5),
        (1, 4, 6), (2, 3, 6), (2, 4, 5)]
PLANAR = [tuple(sorted(((s+i) % 7 for i in range(3)))) for s in range(7)]

def compose(f, g):
    return tuple(f[g[i]] for i in range(4))

def cycle_count(f):
    unseen = set(range(4)); count = 0
    while unseen:
        count += 1; i = unseen.pop(); j = f[i]
        while j != i:
            unseen.remove(j); j = f[j]
    return count

S4 = list(permutations(range(4)))
IDENTITY = (0, 1, 2, 3)
SWAP01 = (1, 0, 2, 3)
SWAP23 = (0, 1, 3, 2)
BOTH = (1, 0, 3, 2)

def pair_numerator(p, q):
    """Independent S_4 trace, for two 3-site cuts of 7 parties."""
    return sum(p ** (q * cycle_count(compose(s, BOTH))
                      + (3-q)*cycle_count(compose(s, SWAP01))
                      + (3-q)*cycle_count(compose(s, SWAP23))
                      + (1+q)*cycle_count(compose(s, IDENTITY)))
               for s in S4)

def closed_numerator(p, q):
    D=p**7; a=p**3; b=p**4
    R=2*D**3+8*D**2+(D**2+4*D)*(a*a+b*b)
    return R+2*p**(13-2*q)+2*b*b*p**(2*q)

def variance(p, family):
    D=p**7; den=D*(D+1)*(D+2)*(D+3)
    m=len(family)
    total=sum(pair_numerator(p, len(set(a)&set(b)))
              for a in family for b in family)
    return Fraction(total,m*m*den)-Fraction((p**3+p**4)**2,(D+1)**2)


def families_intersect_one():
    """Enumerate every labeled optimum with pairwise intersection one."""
    blocks = list(combinations(range(7),3))
    adj = [set() for _ in blocks]
    for i,a in enumerate(blocks):
        sa=set(a)
        adj[i] = {j for j in range(i+1,len(blocks))
                  if len(sa&set(blocks[j])) == 1}
    count=0
    def dfs(chosen,poss):
        nonlocal count
        if len(chosen)==7:
            count+=1
            return
        if len(chosen)+len(poss)<7:return
        for i in sorted(poss):
            dfs(chosen+[i], poss&adj[i])
    dfs([],set(range(len(blocks))))
    return count


def main():
    assert len({tuple(x) for x in FANO}) == 7
    assert all(len(set(a)&set(b)) == 1 for a,b in combinations(FANO,2))
    assert sorted(len(set(a)&set(b)) for a,b in combinations(PLANAR,2)) == [0]*7+[1]*7+[2]*7
    for p in (2,3,4,5):
        # Compare a direct 24-permutation trace to the independently derived polynomial.
        for q in range(4):
            assert pair_numerator(p,q)==closed_numerator(p,q)
        nums=[pair_numerator(p,q) for q in range(4)]
        assert nums[1] < min(nums[0],nums[2])
        exact=variance(p,FANO)
        planar=variance(p,PLANAR)
        D=p**7; den=D*(D+1)*(D+2)*(D+3)
        predicted_gap=Fraction(4*p**8*(p-1)**2*(p+1)**3,7*den)
        assert planar-exact == predicted_gap
        assert all(variance(p, fam)>=exact for fam in (FANO,PLANAR))
        print(f'p={p}: Fano variance={exact}, planar={planar}, difference={predicted_gap}')
    assert variance(2,FANO)==Fraction(99,3148847)
    assert variance(2,PLANAR)==Fraction(5013,110209645)
    count=families_intersect_one()
    assert count==30, count
    print('Exactly 30 labeled pairwise-one 7-triple families; all relabelings of Fano')
    print('VERIFY_OK')

if __name__ == '__main__':main()
