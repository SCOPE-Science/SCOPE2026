"""Finite support checks and exact counterexample for sparse approval elections.

Run with Python 3: python verify.py
Only the Python standard library is required.
Exhaustive finite tests do not replace the general mathematical proof.
"""
from fractions import Fraction
from itertools import combinations, product


def dominates(new, old):
    return all(a >= b for a, b in zip(new, old)) and any(
        a > b for a, b in zip(new, old)
    )


def utility(ballots, weights):
    return tuple(sum(weights[c] for c in ballot) for ballot in ballots)


def committees(m, k):
    return [tuple(int(i in S) for i in range(m))
            for S in combinations(range(m), k)]


def witness():
    # Candidates 0:a, 1:b, 2:c, 3:d, 4:e.
    ballots = [(0,2,3), (0,2,4), (0,3,4),
               (1,2), (1,3), (1,4), (2,3)]
    W = (1,1,0,0,0)
    fractional = (Fraction(0),Fraction(1,2),Fraction(1,2),
                  Fraction(1,2),Fraction(1,2))
    assert sum(W) == sum(fractional) == 2
    initial = utility(ballots,W)
    assert initial == (1,1,1,1,1,1,0)
    assert utility(ballots,fractional) == (1,1,1,1,1,1,1)
    assert dominates(utility(ballots,fractional),initial)
    for C in committees(5,2):
        assert not dominates(utility(ballots,C),initial)
    return len(committees(5,2))


def non_single_dominance_example():
    # Degree-two ballots, two-seat committee W={a,b}, full Pareto
    # dominator {c,d}, but none of the four single swaps dominates W.
    ballots = [(0,2),(0,3),(1,2),(1,3),(2,3)]
    W=(1,1,0,0)
    alternative=(0,0,1,1)
    baseline=utility(ballots,W)
    assert dominates(utility(ballots,alternative),baseline)
    for c in (0,1):
        for d in (2,3):
            changed=list(W)
            changed[c]=0
            changed[d]=1
            assert not dominates(utility(ballots,changed),baseline)
    return 4


def exhaustive_small():
    # Every subset of distinct approval types of cardinality 1 or 2 on 4 candidates.
    m=4
    types = [a for s in (1,2) for a in combinations(range(m),s)]
    checked_profiles=0
    checked_PO=0
    checked_fractional=0
    X={}
    for k in range(1,m):
        X[k] = []
        for q in (2,3):
            for vec in product(range(q+1), repeat=m):
                if sum(vec)==k*q:
                    X[k].append(tuple(Fraction(v,q) for v in vec))
    for mask in range(1<<len(types)):
        ballots=[types[i] for i in range(len(types)) if mask&(1<<i)]
        checked_profiles += 1
        for k in range(1,m):
            CW=committees(m,k)
            vals=[utility(ballots,W) for W in CW]
            for W, val in zip(CW,vals):
                if any(dominates(v,val) for v in vals):
                    continue
                checked_PO+=1
                for x in X[k]:
                    checked_fractional+=1
                    assert not dominates(utility(ballots,x),val), (
                        'Sparse-election counterexample', ballots,k,W,x)
    return checked_profiles,checked_PO,checked_fractional

if __name__=='__main__':
    assert witness()==10
    assert non_single_dominance_example()==4
    p,o,f=exhaustive_small()
    assert p==1024
    print('Five-candidate three-approval witness: 10 committees checked; PASS')
    print('Two-approval non-single-dominance witness: 4 swaps checked; PASS')
    print(f'Four-candidate approval-support profiles: {p}; Pareto committees: {o}; fractional tests: {f}; PASS')
    print('Checks are finite only; the arbitrary-size theorem is proved analytically.')
