"""Exact checks for singular components of symmetric arrowhead determinants.

Run: python3 checker.py; standard library only.
The finite checks supplement, and do not replace, the general proof.
"""
from itertools import product, combinations
from math import comb


def mul(values):
    result = 1
    for value in values:
        result *= value
    return result


def minor_product(a, excluded):
    return mul(a[i] for i in range(len(a)) if i not in excluded)


def det_arrowhead(a, b, t):
    return t * mul(a) - sum(b[i]**2 * minor_product(a, {i}) for i in range(len(a)))


def gradient(a, b, t):
    m = len(a)
    dt = mul(a)
    da = [t * minor_product(a, {i}) - sum(
        b[j]**2 * minor_product(a, {i, j})
        for j in range(m) if j != i) for i in range(m)]
    db = [-2*b[i]*minor_product(a, {i}) for i in range(m)]
    return [dt] + da + db


def expected_components(a, b, t):
    m = len(a)
    triples = [c for c in combinations(range(m), 3) if all(a[i] == 0 for i in c)]
    nonlinear = []
    for i in range(m):
        rest = [j for j in range(m) if j != i]
        remaining_det = det_arrowhead([a[j] for j in rest], [b[j] for j in rest], t)
        if a[i] == b[i] == 0 and remaining_det == 0:
            nonlinear.append(i)
    return nonlinear, triples


def exact_enumeration(m, values):
    checks = 0
    zeros = 0
    for v in product(values, repeat=2*m+1):
        t = v[0]; a = v[1:m+1]; b = v[m+1:]
        grad = gradient(a,b,t)
        predicted = any(expected_components(a,b,t))
        observed = all(z == 0 for z in grad)
        assert observed == predicted, (m,values,v,grad)
        if observed:
            zeros += 1
            assert det_arrowhead(a,b,t) == 0
        checks += 1
    return checks, zeros


def generic_points(m):
    # On Y_0 all other diagonal entries equal one.
    a = [0]+[1]*(m-1)
    b = [0]+[1]*(m-1)
    t = m-1
    assert det_arrowhead(a,b,t) == 0 and not any(gradient(a,b,t))
    nonlinear, triples=expected_components(a,b,t)
    assert nonlinear == [0] and triples == []
    # On L_{0,1,2}: three zero leaf diagonals, all leaf spokes nonzero.
    a = [0,0,0]+[1]*(m-3)
    b = [1]*m
    t = m+1
    assert det_arrowhead(a,b,t) == 0 and not any(gradient(a,b,t))
    nonlinear, triples=expected_components(a,b,t)
    assert nonlinear == [] and triples == [(0,1,2)]
    return (m + comb(m,3),m*m+comb(m,3))


def main():
    for m, alphabet in [(3,(0,1)),(4,(0,1)),(5,(0,1)),(6,(0,1)),
                        (3,(-1,0,1)),(4,(-1,0,1))]:
        checked, singular=exact_enumeration(m,alphabet)
        print(f"ENUM m={m} values={alphabet}: {checked} points, {singular} singular; all classified")
    for m in range(3,9):
        components,degree=generic_points(m)
        print(f"GENERIC m={m}: components={components}, reduced-support degree={degree}; witnesses verified")
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':
    main()
