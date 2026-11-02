"""Exact finite diagnostics for the uniform-vertex spread of two-end double brooms.

The analytic proof for all sizes is in RESULT.md. Python 3 standard library only.
"""
from fractions import Fraction
from itertools import product


def sharp(m, n):
    assert m >= 2 and n >= 2
    H, L = max(m, n), min(m, n)
    N, S = m+n+3, m+n
    num = 16*m*n+14*S+6 if H <= 3*L+3 else N*(H+9*L+5)-int(S % 2 == 0)
    return Fraction(num, N*N)


def candidate(m, n, a, b, straight):
    # Hubs are 0,1,2 (straight) or 0,1,0 (folded).
    # a,b give signed leaf-edge steps at their adjacent end hubs.
    c = 2 if straight else 0
    f = (0,1,c,*a,*(c+x for x in b))
    N = len(f)
    return Fraction(N*sum(x*x for x in f)-sum(f)**2,N*N)


def analytic_profiles(m,n):
    N=m+n+3; S=m+n
    scores={(k,l):Fraction(N*(S+5+8*l)-(3-m+n+2*(k+l))**2,N*N)
            for k in range(m+1) for l in range(n+1)}
    best=max(scores.values())
    return best,{x for x,y in scores.items() if y==best}

count=0
for m in range(2,7):
    for n in range(2,7):
        hi=-1;fold=-1
        for aa in product((-1,1),repeat=m):
            for bb in product((-1,1),repeat=n):
                hi=max(hi,candidate(m,n,aa,bb,True))
                fold=max(fold,candidate(m,n,aa,bb,False))
        pred,profiles=analytic_profiles(m,n)
        assert hi==pred==sharp(m,n),(m,n,hi,pred)
        assert hi>fold,(m,n,hi,fold)
        count+=1
print('EXACT_FULL_EDGE_CUBE_AND_REFLECTION_DOMINANCE_OK',count)

count=0
for m in range(2,30):
    for n in range(2,30):
        H,L=max(m,n),min(m,n)
        _,p=analytic_profiles(m,n)
        if H<=3*L+3: expected={(0,n)}
        elif n>3*m+3:
            z=Fraction(3*m+n+3,2)
            expected={(0,k) for k in {z.numerator//z.denominator,-(-z.numerator//z.denominator)}}
        else:
            z=Fraction(m-n-3,2)
            expected={(k-n,n) for k in {z.numerator//z.denominator,-(-z.numerator//z.denominator)}}
        assert p==expected,(m,n,p,expected)
        count+=1
print('EXACT_ALL_OPTIMIZER_MULTIPLICITIES_AND_PARITY_OK',count)

count=0
for leaves in range(4,151):
    a=[sharp(k,leaves-k) for k in range(2,leaves//2+1)]
    assert all(x<y for x,y in zip(a,a[1:])),leaves
    count+=1
print('STRICT_FIXED_LEAF_BUDGET_BALANCING_OK',count)

assert sharp(2,2)==Fraction(18,7)
assert analytic_profiles(2,9)[1]=={(0,9)}
assert analytic_profiles(2,10)[1]=={(0,9),(0,10)}
assert analytic_profiles(2,11)[1]=={(0,10)}
for r in (1,Fraction(3,2),2,3,4,7):
    L=6000;H=int(r*L)
    limit=16*Fraction(r)/(1+Fraction(r))**2 if r<=3 else (Fraction(r)+9)/(1+Fraction(r))
    assert abs(float(sharp(L,H)-limit))<0.001
print('EXACT_FIRST_PHASE_TIES_AND_LIMIT_DIAGNOSTICS_OK')
print('ALL_DOUBLE_BROOM_SPREAD_CHECKS_OK')
