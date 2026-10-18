"""Finite semantic stress tests for three propositional team conditionals.

The test computes satisfaction directly from the published clauses, independently
of the normal form construction. Python 3, standard library only.
"""
from itertools import combinations
from random import Random


def subteams(T):
    s=T
    while True:
        yield s
        if s==0: break
        s=(s-1)&T


def valuation_teams(k):
    # The point domain is {0,...,k-1}; a team is a k-bit integer.
    return range(1<<k)


def union_closed(P,k):
    ts=[t for t in valuation_teams(k) if t in P]
    return 0 in P and all((x|y) in P for x in ts for y in ts)


def flat(A,k):
    return {T for T in valuation_teams(k) if T & ~A == 0}


def conj(P,Q): return P&Q


def tensor(P,Q,k):
    return {T for T in valuation_teams(k)
            if any(S in P and (T ^ S) in Q for S in subteams(T))}
    # Exact partitions suffice when P,Q union-closed, since lax splits
    # may overlap; see tensor_lax below for the independent direct clause.


def tensor_lax(P,Q,k):
    return {T for T in valuation_teams(k)
            if any((S in P) and (U in Q) and (S|U)==T
                   for S in subteams(T) for U in subteams(T))}


def must_all(P,T):return all(S in P for S in subteams(T))


def indicative(P,Q,k):
    return {T for T in valuation_teams(k) if not must_all(P,T) or T in Q}


def epistemic(P,Q,k):
    return {T for T in valuation_teams(k)
            if not must_all(P,T) or must_all(Q,T)}


def counterfactual(P,Q,k):
    return {T for T in valuation_teams(k)
            if all(not must_all(P,S) or S in Q for S in subteams(T))}


def characteristic(S,k,arrow):
    # Flat bound \alpha_S means T subseteq S. For every v in S, the
    # arrow (\alpha_{V\{v}} > bot) means T empty or v belongs to T.
    full=(1<<k)-1
    bot={0}
    out=flat(S,k)
    for v in range(k):
        if (S>>v)&1:
            exc_v=flat(full^(1<<v),k)
            out=conj(out,arrow(exc_v,bot,k))
    return out


def generate_union_closed_families(k):
    teams=list(valuation_teams(k))
    for bits in range(1<<(len(teams)-1)):
        P={0}|{j+1 for j in range(len(teams)-1) if bits>>j&1}
        if union_closed(P,k): yield P


def check():
    # Independently test the split connective's lax and disjoint readings
    # whenever inputs are downward closed. For general union-closed input
    # only the lax semantics is used in the normal-form stress tests.
    k=4
    flats=[flat(A,k) for A in valuation_teams(k)]
    for P in flats:
        for Q in flats:
            assert tensor(P,Q,k)==tensor_lax(P,Q,k)
    print('FLAT_SPLIT_PAIRS_OK',len(flats)**2)
    rng=Random(260302136)
    total=0
    for k,expected in [(1,2),(2,7),(3,61),(4,2480)]:
        families=list(generate_union_closed_families(k))
        assert len(families)==expected
        for arrow in (indicative,epistemic):
            clauses={S:characteristic(S,k,arrow) for S in range(1,1<<k)}
            for S,sem in clauses.items():
                assert sem=={0,S}, ('characteristic',k,S,arrow.__name__)
            for P in families:
                # Independent lax-split convolution of exact generators.
                result={0}
                for S in sorted(P-{0}):
                    result=tensor_lax(result,clauses[S],k)
                assert result==P, ('normal_form',k,arrow.__name__,P,result)
                total+=1
            # Random pairwise semantic union-closure tests for both arrows.
            for _ in range(300):
                A,B=rng.choice(families),rng.choice(families)
                out=arrow(A,B,k)
                assert union_closed(out,k),('union_closure',k,arrow.__name__,A,B)
        print('ALL_UNION_CLOSED_NORMAL_FORMS_OK',k,expected)
    print('NORMAL_FORM_FAMILIES_CHECKED',total)
    # Counterfactual maps flat predicates to flat predicates, exactly the
    # classical material implication truth set at every team.
    tests=0
    for k in range(1,5):
        for A in valuation_teams(k):
            for B in valuation_teams(k):
                result=counterfactual(flat(A,k),flat(B,k),k)
                assert result==flat((~A|B)&((1<<k)-1),k)
                tests+=1
    print('COUNTERFACTUAL_FLAT_PAIR_TESTS',tests)
    # A non-flat property has conditional depth exactly one for k>=2.
    for k in (2,3,4):
        S=3
        nonflat={0,S}
        assert all(nonflat!=flat(A,k) for A in valuation_teams(k))
        assert characteristic(S,k,indicative)==nonflat
        assert characteristic(S,k,epistemic)==nonflat
    print('SHARP_DEPTH_SEPARATIONS_OK')
    print('VERIFY_OK')

if __name__=='__main__':check()
