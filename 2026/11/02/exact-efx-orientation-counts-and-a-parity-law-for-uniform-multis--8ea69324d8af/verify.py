"""Exact EFX-orientation enumerator for unit-valued uniform multistars."""
from itertools import product
from math import comb


def efx_direct(b, q, orientation):
    # Edges indexed by (leaf_index, parallel_edge_index).
    owners = [(0 if orientation[i*q+j] else i+1) for i in range(b) for j in range(q)]
    incidence = [(0,i+1) for i in range(b) for _ in range(q)]
    bundles = [[k for k, owner in enumerate(owners) if owner == a] for a in range(b+1)]
    utility = lambda a, item: int(a in incidence[item])
    for a in range(b+1):
        own_value = sum(utility(a, e) for e in bundles[a])
        for other in range(b+1):
            if other == a:
                continue
            for removed in bundles[other]:
                other_value = sum(utility(a,e) for e in bundles[other] if e != removed)
                if own_value < other_value:
                    return False
    return True


def exact_formula(b,q):
    s = q//2
    result = 0
    for ys in product(range(s+1),repeat=b):
        if sum(ys)+min(ys) >= q-1:
            ways = 1
            for y in ys:
                ways *= comb(q,y)
            result += ways
    if q == 3:
        result += 3*b
    return result


def polynomial_count(b,q):
    if b < max(2,q-1):
        raise ValueError('stable range only')
    s=q//2
    poly=[1]+[0]*(q-2)
    for _ in range(b):
        out=[0]*(q-1)
        for t,v in enumerate(poly):
            for y in range(min(s,q-2-t)+1):
                out[t+y] += v*comb(q,y)
        poly=out
    A=sum(comb(q,y) for y in range(s+1))
    return A**b-sum(poly)+(3*b if q==3 else 0)


def run():
    tests=0
    for b,q in [(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3),(2,4),(3,4),(4,4),(2,5),(3,5),(2,6)]:
        direct=sum(efx_direct(b,q,p) for p in product((0,1),repeat=b*q))
        exact=exact_formula(b,q)
        assert direct==exact,(b,q,direct,exact)
        if b >= max(2,q-1):
            assert direct==polynomial_count(b,q)
        tests+=1
    for b in range(2,9):
        for q in range(2,10):
            v=exact_formula(b,q)
            if b>=max(2,q-1):
                assert v==polynomial_count(b,q),(b,q,v,polynomial_count(b,q))
            assert 0<v<2**(b*q)
    assert exact_formula(2,2)==8
    assert all(exact_formula(b,2)==3**b-1 for b in range(2,9))
    assert all(exact_formula(b,3)==4**b-1 for b in range(2,9))
    assert all(exact_formula(b,4)==11**b-1-10*b-16*comb(b,2) for b in range(3,9))
    print('VERIFY_OK exact_labeled_orientation_cases=',tests,'binomial_profiles=',7*8)

if __name__=='__main__':
    run()
