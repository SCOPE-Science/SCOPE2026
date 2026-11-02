"""Exact finite spot checks for the sharp graph-spread theorem on clique bouquets.

This script checks illustrative configurations, using integer arithmetic. The
universal proof is in RESULT.md; finite checks do not certify the infinite family.
"""
from itertools import product, combinations_with_replacement


def closed_formula(sizes):
    sizes = tuple(sizes)
    assert len(sizes) >= 2 and all(x >= 1 for x in sizes)
    total = sum(sizes)
    count = total + 1
    discrepancy = min(abs(sum(s*x for s, x in zip(signs, sizes)))
                      for signs in product((-1, 1), repeat=len(sizes)))
    full = count * total - discrepancy**2
    largest = max(sizes)
    rest = total - largest
    if largest >= 3*rest + 2:
        dominant = 2*count*rest + (count**2)//4
        assert dominant >= full
        return dominant, ('tie' if dominant == full else 'partial')
    return full, 'full'


def combinatorial_optimization(sizes):
    count = 1 + sum(sizes)
    best = -1
    for counts in product(*(range(1, a+1) for a in sizes)):
        for signs in product((-1,1), repeat=len(sizes)):
            charge = sum(e*k for e,k in zip(signs, counts))
            score = count*sum(counts)-charge*charge
            if score > best:
                best = score
    return best


def independent_labelled_optimization(sizes):
    """Enumerate every integral anchored graph-Lipschitz assignment directly."""
    count = sum(sizes)+1
    best = -1
    good = 0
    for assignments in product((-1,0,1),repeat=count-1):
        st = 0
        valid = True
        for a in sizes:
            vals = assignments[st:st+a]
            st += a
            if max(vals)-min(vals)>1:
                valid=False
                break
        if valid:
            good+=1
            score=count*sum(v*v for v in assignments)-sum(assignments)**2
            best=max(best,score)
    return best,good


def test_formula():
    checks=0
    for t in (2,3,4):
        for sizes in combinations_with_replacement(range(1,7),t):
            val,reg=closed_formula(sizes)
            assert val==combinatorial_optimization(sizes),(sizes,val,reg)
            checks+=1
    print('EXACT_ALL_SIGNED_ACTIVE_COUNT_STATES_OK',checks)


def test_labelled():
    checks=0;seen=0
    for t in (2,3,4):
        for sizes in combinations_with_replacement(range(1,6),t):
            if sum(sizes)>8: continue
            expected,_=closed_formula(sizes)
            brute, admissible=independent_labelled_optimization(sizes)
            assert brute==expected,(sizes,expected,brute)
            checks+=1;seen+=admissible
    print('DIRECT_LABELLED_INTEGER_LIPSCHITZ_POTENTIALS_OK',checks,seen)


def test_boundaries():
    for q in range(1,25):
        for gap in (-2,-1,0,1,2,3,11):
            a=3*q+2+gap
            if a<1:continue
            sizes=(a,q)
            value,reg=closed_formula(sizes)
            count=a+q+1
            full=count*(a+q)-(a-q)**2
            if gap==0:
                assert value==full and reg=='tie'
            elif gap>=1:
                assert value>full and reg=='partial'
                assert value-full==((a-3*q-1)**2)//4
            else:
                assert value==full and reg=='full'
            # Directly recover vertex-label optimum from its active-count search near transition.
            if q<=5 and a<=28:
                assert combinatorial_optimization(sizes)==value
    print('EXACT_DOMINANT_PHASE_AND_SQUARE_LAW_OK',24*7)


def test_symmetry_and_limits():
    for blades in range(2,10):
        for a in range(1,12):
            v,_=closed_formula((a,)*blades)
            count=blades*a+1
            target=count*blades*a-(a*a if blades%2 else 0)
            assert v==target
    for q in (1,3,7):
        for a in (4*q+10, 11*q+12, 40*q+20):
            v,_=closed_formula((a,q))
            N=a+q+1
            assert v==2*N*q+N*N//4
    print('EQUAL_PETAL_PARITY_AND_GIANT_CLIQUE_LIMIT_CHECKS_OK')

if __name__=='__main__':
    test_formula()
    test_labelled()
    test_boundaries()
    test_symmetry_and_limits()
    print('ALL_CLIQUE_BOUQUET_SPREAD_CHECKS_OK')
