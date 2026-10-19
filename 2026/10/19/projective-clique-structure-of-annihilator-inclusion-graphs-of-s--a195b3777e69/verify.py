"""Exact finite-ring checks for annihilator-inclusion graph decompositions.

The test algebras are commutative local algebras K ⊕ V ⊕ Ks,
with V V products prescribed by a symmetric bilinear form.
All computations use integer arithmetic modulo prime p.
"""
from itertools import product
from collections import Counter


def dot(v, u, b, p):
    return sum(v[i] * b[i][j] * u[j]
               for i in range(len(v)) for j in range(len(v))) % p


def mul(x, y, b, p):
    a, v, w = x
    c, u, z = y
    return ((a*c) % p,
            tuple((a*u[i]+c*v[i]) % p for i in range(len(v))),
            (a*z+c*w+dot(v,u,b,p)) % p)


def canon(form, p):
    first = next(z for z in form if z)
    inv = pow(first, -1, p)
    return tuple(z*inv % p for z in form)


def check(p, b, label):
    d = len(b)
    zero = (0, (0,)*d, 0)
    elements = [(a, v, w) for a in range(p)
                for v in product(range(p), repeat=d)
                for w in range(p)]
    vertices = [x for x in elements if x[0] == 0 and x != zero]
    forms = {x: tuple(sum(x[1][i]*b[i][j] for i in range(d)) % p
                     for j in range(d)) for x in vertices}
    soc = {x for x in vertices if all(z == 0 for z in forms[x])}
    r = 0
    n = len(soc) + 1
    while n > 1:
        assert n % p == 0
        n //= p
        r += 1
    r -= 1
    t = d-r
    assert t >= 1
    c = p**(r+1)-1
    h = p**(r+1)*(p-1)
    clusters = (p**t-1)//(p-1)
    assert len(soc) == c
    classes = Counter(canon(forms[x],p) for x in vertices if x not in soc)
    assert len(classes) == clusters and set(classes.values()) == {h}
    anns = {x: frozenset(y for y in elements if mul(x,y,b,p) == zero)
            for x in vertices}
    for i,x in enumerate(vertices):
        for y in vertices[i+1:]:
            observed = anns[x] <= anns[y] or anns[y] <= anns[x]
            expected = x in soc or y in soc or canon(forms[x],p)==canon(forms[y],p)
            assert observed == expected, (label,x,y)
    # Degree profile tests: all vertices in the same predicted class have the same degree.
    degree = Counter()
    for x in vertices:
        degree[len(vertices)-1 if x in soc else c+h-1] += 1
    if clusters == 1:
        assert degree == Counter({len(vertices)-1:len(vertices)})
    else:
        assert degree[c+h-1] == clusters*h
        assert degree[len(vertices)-1] == c
    print(f'PASS {label}: p={p} d={d} radical={r} rank={t}; '
          f'graph=K_{c} join ({clusters} K_{h}); |V|={len(vertices)}; '
          f'annihilators and all adjacencies checked')


def check_external(elements, zero, multiply, expected, label):
    vertices = [x for x in elements if x != zero and x[0] % 2 == 0]
    ann = {x:frozenset(y for y in elements if multiply(x,y)==zero) for x in vertices}
    adjacency_degrees=Counter()
    for x in vertices:
        deg=sum(ann[x] <= ann[y] or ann[y] <= ann[x] for y in vertices if y!=x)
        adjacency_degrees[deg]+=1
    assert dict(adjacency_degrees)==expected, (label,adjacency_degrees,expected)
    print(f'PASS {label}: mixed-characteristic, degrees {dict(adjacency_degrees)}')


def check_mixed_characteristic():
    # Z/8Z, with vertex representatives 2,4,6.
    elems=[(i,) for i in range(8)]
    check_external(elems,(0,),lambda x,y:((x[0]*y[0])%8,), {2:3}, 'Z8')
    # Z/4Z[x,y]/(x^2-2,2x,2y,xy,y^2); x,y are F_2 coefficients.
    elems=[(a,b,c) for a in range(4) for b in range(2) for c in range(2)]
    def mult(x,y):
        a,b,c=x;d,e,f=y
        return ((a*d+2*b*e)%4, ((a%2)*e+(d%2)*b)%2,
                ((a%2)*f+(d%2)*c)%2)
    check_external(elems,(0,0,0),mult,{6:7}, 'Z4_two_generators')


if __name__ == '__main__':
    check(2, [[1,0],[0,1]], 'binary_nondegenerate_2')
    check(2, [[1,0,0],[0,1,0],[0,0,0]], 'binary_radical_1')
    check(2, [[1,0,0],[0,0,0],[0,0,0]], 'binary_rank_1_complete')
    check(3, [[0,1],[1,0]], 'ternary_hyperbolic')
    check(3, [[1,0],[0,1]], 'ternary_anisotropic')
    check(3, [[1,0,0],[0,1,0],[0,0,0]], 'ternary_radical_1')
    check(3, [[1,0,0],[0,1,0],[0,0,1]], 'ternary_nondegenerate_3')
    check(5, [[1,0],[0,0]], 'quinary_radical_1_complete')
    check(5, [[1,0],[0,1]], 'quinary_nondegenerate_2')
    check_mixed_characteristic()
    print('ALL_TESTS_PASS: 11 exact ring configurations')
