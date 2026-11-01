"""Exact finite checks for two-layer permuted regular-graph vacancy fluctuations.
Run with Python 3, standard library only.
"""
from fractions import Fraction
from math import comb
from itertools import combinations

checks = 0

def require(condition, note):
    global checks
    assert condition, note
    checks += 1

def choose(n,k):
    return comb(n,k) if n >= 0 and 0 <= k <= n else 0

def blocks(d, base):
    return [frozenset((j+a)%d for a in base) for j in range(d)]

def switch(B):
    C=[set(s) for s in B]
    d=len(C)
    for j in range(d):
        for k in range(j+1,d):
            for a in sorted(C[j]-C[k]):
                for b in sorted(C[k]-C[j]):
                    C[j].remove(a); C[j].add(b)
                    C[k].remove(b); C[k].add(a)
                    if tuple(frozenset(s) for s in C)!=tuple(B):
                        return [frozenset(s) for s in C]
    raise AssertionError('switch unavailable')

def var_formula(B):
    d=len(B); r=len(B[0]); den=choose(d,r)
    u=Fraction(choose(d-r,r),den)
    moment2=d*u + sum(Fraction(choose(d-2*r+len(B[j]&B[k]),r),den) for j in range(d) for k in range(d) if j!=k)
    variance=moment2-(d*u)**2
    return variance

def enumerate_var(B):
    d=len(B); r=len(B[0]); den=choose(d,r)
    Z=[sum(not (set(S) & Bj) for Bj in B) for S in combinations(range(d),r)]
    return Fraction(sum(x*x for x in Z),den)-Fraction(sum(Z),den)**2

def gap_motifs(B):
    d=len(B); r=len(B[0]); D=d-2*r; den=choose(d,r)
    gap=Fraction(0)
    for j in range(d):
        for k in range(d):
            if j==k: continue
            t=len(B[j]&B[k])
            gap+=sum(Fraction(choose(D,h)*choose(t,r-h),den) for h in range(r+1)) if False else Fraction(0)
            gap+=sum(Fraction(choose(D,r-v)*choose(t,v),den) for v in range(2,r+1))
    return gap

def target(d,r):
    den=choose(d,r)
    u=Fraction(choose(d-r,r),den)
    f1=Fraction(choose(d-2*r+1,r),den)
    return d*u*(1-u)+d*(d-1)*(f1-u*u)

for d,base in [(7,(0,1,3)),(13,(0,1,3,9))]:
    r=len(base)
    B=blocks(d,base)
    require(all(len(s)==r for s in B),f'column degrees {d}')
    require(all(sum(i in s for s in B)==r for i in range(d)),f'row degrees {d}')
    require(all(len(B[j]&B[k])==1 for j in range(d) for k in range(j+1,d)),f'plane {d}')
    v=var_formula(B)
    require(v==enumerate_var(B),f'exact enumeration {d}')
    require(v==target(d,r),f'bound attained {d}')
    require(gap_motifs(B)==0,f'zero 4-cycles {d}')
    C=switch(B)
    require(all(len(s)==r for s in C),f'column preserved {d}')
    require(all(sum(i in s for s in C)==r for i in range(d)),f'row preserved {d}')
    require(var_formula(C)==enumerate_var(C),f'switched enumeration {d}')
    require(var_formula(C)-v==gap_motifs(C),f'exact motif identity {d}')
    require(var_formula(C)>v,f'positive defect {d}')
    print('d',d,'r',r,'minimal_variance',str(v),'switched_variance',str(var_formula(C)),'strict_gap',str(var_formula(C)-v))

# A non-design admissible example also checks the universal covariance formula.
B=blocks(9,(0,1,4))
require(all(sum(i in s for s in B)==3 for i in range(9)),'nine-vertex regularity')
require(var_formula(B)==enumerate_var(B),'nine-vertex exact variance')

# Independently test combinatorial Vandermonde identity for the full overlap range.
for r in (3,4,5):
    d=r*r-r+1
    D=d-2*r
    for t in range(r+1):
        require(choose(D+t,r)==sum(choose(t,k)*choose(D,r-k) for k in range(r+1)),f'Vandermonde {r} {t}')
print('PASS',checks,'exact assertions')
