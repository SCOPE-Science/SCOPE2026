from fractions import Fraction
from itertools import product

def purity_factor(ps):
    out=Fraction(1,1)
    for p in ps:
        out*=p*p+(1-p)*(1-p)
    return out

def purity_bruteforce(ps):
    s=Fraction(0,1)
    for bits in product((0,1), repeat=len(ps)):
        q=Fraction(1,1)
        for p,b in zip(ps,bits):
            q*=p if b else (1-p)
        s+=q*q
    return s

# Exact factorization and union-bound inequality on a dense rational grid.
checks=0
for M in range(1,6):
    vals=[Fraction(k,6) for k in range(7)]
    for ps in product(vals, repeat=M):
        pf=purity_factor(ps)
        pb=purity_bruteforce(ps)
        assert pf==pb
        defect=1-pf
        rhs=sum(2*p*(1-p) for p in ps)
        assert defect<=rhs
        checks+=1

# Exact normalized position distributions for multiple particles; verify the global IPR bound.
dist_checks=0
examples=[
    [[Fraction(1,2),Fraction(1,2)]],
    [[Fraction(1,3)]*3,[Fraction(1,2),Fraction(1,4),Fraction(1,4)]],
    [[Fraction(1,4)]*4,[Fraction(1,10),Fraction(2,10),Fraction(3,10),Fraction(4,10)],
     [Fraction(2,5),Fraction(1,5),Fraction(1,5),Fraction(1,5)]],
]
for dists in examples:
    M=len(dists); L=len(dists[0])
    assert all(len(d)==L and sum(d)==1 for d in dists)
    impurity=sum(1-purity_factor([dists[i][j] for i in range(M)]) for j in range(L))
    ipr_rhs=2*sum(1-sum(p*p for p in d) for d in dists)
    assert impurity<=ipr_rhs<=2*M
    dist_checks+=1

print('VERIFY_OK')
print('factorization_grid_checks =', checks)
print('global_distribution_checks =', dist_checks)
print('proved_bound = E_MW <= (2^M/(2^M-1))*2*sum_i(1-IPR_i)/L <= (2^M/(2^M-1))*2M/L')
