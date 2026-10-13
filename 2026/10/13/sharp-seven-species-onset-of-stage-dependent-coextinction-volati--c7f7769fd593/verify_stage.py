"""Exact enumeration for the sharp first stage-dependent coextinction-volatility split.
Standard-library-only Python 3.10+; run: python verify_stage.py.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb


def moment_direct(neighborhoods, m, t):
    # A uniform t-subset of the m primary species survives.
    n = len(neighborhoods)
    xs = []
    for survivors in combinations(range(m), t):
        live = set(survivors)
        xs.append(sum(not (live & s) for s in neighborhoods))
    den = len(xs)
    mean = Fraction(sum(xs), den)
    return mean, Fraction(sum(x*x for x in xs), den) - mean*mean


def moment_pairs(neighborhoods, m, t):
    # Independent inclusion-exclusion by singleton/ordered-pair union sizes.
    den = comb(m, t)
    p = lambda r: Fraction(comb(m-r, t) if 0 <= t <= m-r else 0, den)
    mu = sum((p(len(s)) for s in neighborhoods), Fraction(0))
    ex2 = sum((p(len(s|q)) for s in neighborhoods for q in neighborhoods), Fraction(0))
    return mu, ex2 - mu*mu


def choices(m, d):
    return [frozenset(c) for c in combinations(range(m), d)]


def feasible(m, ds):
    for Ns in product(*(choices(m,d) for d in ds)):
        if len(set().union(*Ns)) == m:
            yield Ns


def verify_profile(m, ds):
    allnets = list(feasible(m, ds))
    assert allnets, (m,ds)
    best = [max(moment_direct(Ns,m,t)[1] for Ns in allnets) for t in range(m+1)]
    maxes = [Ns for Ns in allnets if all(moment_direct(Ns,m,t)[1]==best[t] for t in range(m+1))]
    for Ns in allnets:
        for t in range(m+1):
            assert moment_direct(Ns,m,t) == moment_pairs(Ns,m,t)
    return len(allnets), best, maxes


def classify_4x3(Ns):
    c = Counter(Ns)
    if max(c.values()) == 2:
        assert sorted(c.values()) == [1,2]
        singleton, repeat = next(e for e in c if c[e]==1), next(e for e in c if c[e]==2)
        assert not (singleton & repeat)
        return 'double_edge_plus_disjoint_edge'
    assert max(c.values()) == 1
    degrees = sorted([sum(v in e for e in Ns) for v in range(4)], reverse=True)
    if degrees == [3,1,1,1]: return 'star'
    assert degrees == [2,2,1,1]
    return 'path'


def main():
    groups = matrices = profiles = 0
    all_failure = []
    table33 = []
    for total in range(2,8):
        for m in range(1,total):
            n = total - m
            for ds in combinations_with_replacement(range(1,m+1), n):
                if sum(ds)<m: continue
                k, vs, maxnets=verify_profile(m, ds)
                matrices+=k;profiles+=1
                if not maxnets:
                    all_failure.append((m,n,ds,vs))
                if (m,n)==(3,3):
                    table33.append((ds,tuple(vs[t] for t in (1,2)),maxnets[0]))
        groups+=1
    assert len(all_failure)==1, all_failure
    assert all_failure[0][:3]==(4,3,(2,2,2)),all_failure
    c = Counter()
    cases = {}
    for Ns in feasible(4,(2,2,2)):
        typ=classify_4x3(Ns)
        vals=tuple(moment_direct(Ns,4,t)[1] for t in (1,2,3))
        if typ in cases: assert cases[typ] == vals
        cases[typ]=vals
        c[typ]+=1
        assert [moment_direct(Ns,4,t)[0] for t in (1,2,3)]==[Fraction(3,2),Fraction(1,2),Fraction(0)]
    assert c == {'star':24,'path':72,'double_edge_plus_disjoint_edge':18},c
    assert cases == {
        'star':(Fraction(3,4), Fraction(1,4), Fraction(0)),
        'path':(Fraction(1,4), Fraction(1,4), Fraction(0)),
        'double_edge_plus_disjoint_edge':(Fraction(1,4), Fraction(7,12), Fraction(0))},cases
    assert len(table33)==10
    print(f'All non-isolated m+n<=7: {profiles} degree multiset classes, {matrices} labeled matrices checked')
    print('Unique degree-multiset without a common variance maximizer: (m,n,degrees)=(4,3,(2,2,2))')
    print('3x3 degree-multiset table:')
    for ds, vals, Ns in table33:
        print(ds, 'max V1,V2=',vals,'common witness=',tuple(''.join(str(i+1) for i in sorted(s)) for s in Ns))
    print('4x3 motif counts:',dict(c),'exact stage variances:',cases)
    print('VERIFY_OK')

if __name__=='__main__':main()
