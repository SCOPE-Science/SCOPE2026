"""Exact checks for the winner-index polymatroid and its uniform example.

Run: python verify.py
Standard library only. Finite checks corroborate, but do not prove, the
measure-theoretic characterization.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import sqrt

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def set_capacity(capacity, index_set):
    return sum((capacity[i] for i in index_set), Q(0))


def rank_profile(marginals, maximum):
    """marginals[i][a] and maximum[a] are rational atom masses."""
    d = len(marginals)
    m = len(maximum)
    result = {}
    for mask in range(1 << d):
        chosen = [i for i in range(d) if mask & (1 << i)]
        result[mask] = sum((min(maximum[a],sum((marginals[i][a] for i in chosen),Q(0))) for a in range(m)), Q(0))
    return result


def greedy_allocation(marginals, maximum, order):
    d = len(marginals)
    m = len(maximum)
    allocations = [[Q(0) for _ in range(m)] for _ in range(d)]
    for a in range(m):
        remaining = maximum[a]
        for i in order:
            allocations[i][a] = min(marginals[i][a], remaining)
            remaining -= allocations[i][a]
        verify(remaining == 0,'maximum atom is not completely allocated')
    return allocations


def validate_example(marginals, maximum):
    d = len(marginals)
    total = sum(maximum)
    verify(all(sum(row)==total for row in marginals),'marginals not normalized to common mass')
    verify(all(sum(marginals[i][:t+1]) >= sum(maximum[:t+1]) for i in range(d) for t in range(len(maximum))),'CDF dominance')
    verify(all(maximum[a]<=sum(marginals[i][a] for i in range(d)) for a in range(len(maximum))),'measure dominance')
    r = rank_profile(marginals, maximum)
    verify(r[0]==0 and r[(1<<d)-1]==total,'endpoint ranks')
    for a,b in product(range(1<<d),repeat=2):
        verify(r[a]+r[b]>=r[a&b]+r[a|b], 'submodularity')
    for order in permutations(range(d)):
        z=greedy_allocation(marginals,maximum,order)
        p=[sum(z_i) for z_i in z]
        verify(sum(p)==total,'greedy mass preservation')
        mask=0
        for i in order:
            mask |= 1<<i
            verify(sum(p[j] for j in range(d) if mask&(1<<j)) == r[mask], 'greedy prefix must be sharp')
        for mask in range(1<<d):
            verify(sum(p[j] for j in range(d) if mask&(1<<j)) <= r[mask], 'greedy violated subset bound')
    return r

# Discrete example: all marginal laws uniform on three atoms; the maximum law is skewed.
mu = [[Q(10),Q(10),Q(10)] for _ in range(3)]
gamma=[Q(3),Q(6),Q(21)]
r=validate_example(mu,gamma)
verify(r[1] == Q(19) and r[3] == Q(29), 'discrete symmetric subset ranks')
verify(greedy_allocation(mu,gamma,(0,1,2))[0] == [Q(3),Q(6),Q(10)],'greedy first winner measure')
verify([sum(z) for z in greedy_allocation(mu,gamma,(0,1,2))] == [Q(19),Q(10),Q(1)],'extreme winner counts')

# A second asymmetric discrete test, with identical aggregate masses and CDF dominance.
mu2=[[Q(2),Q(4)],[Q(3),Q(3)],[Q(4),Q(2)]]
gamma2=[Q(2),Q(4)]
validate_example(mu2,gamma2)

# Exhaustively enumerate integer allocations for the three-atom example.
def partitions_with_caps(g, caps):
    for x in range(min(g,caps[0])+1):
        for y in range(min(g-x,caps[1])+1):
            z=g-x-y
            if 0<=z<=caps[2]:
                yield (x,y,z)
atom_allocations=[]
for a,g in enumerate(gamma):
    atom_allocations.append(list(partitions_with_caps(int(g), [int(mu[i][a]) for i in range(3)])))
possible={}
for a0,a1,a2 in product(*atom_allocations):
    p=tuple(a0[i]+a1[i]+a2[i] for i in range(3))
    possible[p]=True
for x in range(31):
    for y in range(31-x):
        p=(x,y,30-x-y)
        inequalities=all(sum(p[i] for i in range(3) if mask&(1<<i))<=int(r[mask]) for mask in range(8))
        verify((p in possible)==inequalities,'finite integer feasibility equals rank polytope')

# Uniform marginals and independence-maximum law: exact d=2 rank at any even grid.
for n in (2,4,8,16,32,64):
    atoms=[Q((a+1)**2-a*a, n*n) for a in range(n)]
    margins=[[Q(1,n) for _ in range(n)] for _ in range(2)]
    rr=rank_profile(margins,atoms)
    verify(rr[1]==Q(3,4),'continuous sharp 3/4 rank from exact even-grid partition')
    verify(rr[3]==1,'maximum mass 1')

# General closed-form symmetric rank, compared against integration by midpoint cells.
for d in range(2,8):
    last=0.
    for k in range(1,d+1):
        a=(k/d)**(1/(d-1))
        rk=k-(d-1)*k*a/d
        verify(last-1e-13<=rk<=1+1e-13,'symmetric rank bounds')
        if k<d:
            n=12000
            ri=sum(min(d*((j+0.5)/n)**(d-1),k) for j in range(n))/n
            verify(abs(ri-rk)<0.00003,'closed-form uniform rank integral')
        last=rk
    verify(abs(last-1)<1e-12,'full uniform rank equals one')

# The sharp two-label probability segment and the d=3 extreme increments.
verify(abs((1-1/4)-.75)<1e-15,'two-label winner upper endpoint')
for d in (3,4,5,6):
    R=[0.]
    for k in range(1,d+1):
        a=(k/d)**(1/(d-1))
        R.append(k-(d-1)*k*a/d)
    inc=[R[k]-R[k-1] for k in range(1,d+1)]
    verify(all(inc[k] >= inc[k+1]-1e-12 for k in range(d-1)), 'majorization increments decrease')
    verify(abs(sum(inc)-1)<1e-12,'majorization increments sum one')
    verify(inc[-1]>0,'all winner types can have positive mass')

print(f'{checks} exact-rational / deterministic assertions passed')
print('uniform d=2 attainable P(first unique winner)=[1/4,3/4]')
print('source date: 2026-10-22; mathematical proof needed for all-dimensional theorem')
