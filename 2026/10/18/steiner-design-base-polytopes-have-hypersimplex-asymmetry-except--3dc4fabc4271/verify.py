"""Exact arithmetic checks for the symmetry centers of Steiner design base polytopes.

Run: python3 verify.py. Requires only the Python standard library.
Checks finite examples; the theorem for arbitrary designs is proved separately.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def projective_plane(p):
    if p not in (2, 3, 5):
        raise ValueError('This example generator uses only prime fields 2, 3, 5.')
    def normalize(v):
        t = next(x for x in v if x % p)
        inv = pow(t, -1, p)
        return tuple((x * inv) % p for x in v)
    vectors = sorted({normalize(v) for v in product(range(p), repeat=3) if any(v)})
    lines = []
    for w in vectors:
        lines.append(frozenset(i for i, v in enumerate(vectors)
                               if sum(a * b for a, b in zip(w, v)) % p == 0))
    return len(vectors), lines


def affine_plane_three():
    points = list(product(range(3), repeat=2))
    lines = set()
    for a, b in product(range(3), repeat=2):
        if not (a or b):
            continue
        for c in range(3):
            lines.add(frozenset(i for i, (x, y) in enumerate(points)
                                 if (a*x+b*y)%3 == c))
    return 9, sorted(lines, key=lambda S: tuple(sorted(S)))


def steiner_triples_15():
    points = range(1, 16)
    return 15, sorted({frozenset((a - 1, b - 1, (a ^ b) - 1))
                       for a, b in combinations(points, 2)},
                       key=lambda S: tuple(sorted(S)))


def verify(name, n, blocks):
    blocks = list(blocks)
    k = len(blocks[0]); assert 3 <= k < n
    assert all(len(B) == k for B in blocks)
    incidences = Counter(tuple(sorted((a,b)))
                         for B in blocks for a,b in combinations(B,2))
    assert len(incidences) == n*(n-1)//2
    assert set(incidences.values()) == {1}
    replication = Counter(a for B in blocks for a in B)
    assert set(replication.values()) == {(n-1)//(k-1)}
    assert n >= k*(k-1)+1 and n-k>k
    s = Fraction(9,5) if (n,k)==(7,3) else Fraction(n-3,3)
    c = Fraction(3,n)
    ss = max(Fraction(n-3,3),Fraction(3,n-3),
             Fraction(3*k,2*n-3*k),Fraction(2*n-3*k,3*k))
    assert ss == s
    bases = [T for T in combinations(range(n),3) if not any(set(T)<=B for B in blocks)]
    assert bases
    assert all(any(i in T for T in bases) and any(i not in T for T in bases)
               for i in range(n))
    assert all(min(len(set(T)&B) for T in bases)==0 and
               max(len(set(T)&B) for T in bases)==2 for B in blocks)
    reflected = 0
    for T in bases:
        y = [((s+1)*c-(1 if i in T else 0))/s for i in range(n)]
        assert sum(y)==3
        assert min(y)>=0 and max(y)<=1
        for B in blocks:
            assert sum(y[i] for i in B)<=2
            reflected += 1
    if (n,k)==(7,3):
        assert all(sum(len(B&C) for C in blocks) == k+(len(blocks)-1)
                   for B in blocks)
        assert k==3 and len(blocks)==n
    print('PASS:',name,'points=',n,'blocks=',len(blocks),'bases=',len(bases),
          'reflected_line_checks=',reflected,'asymmetry=',s,'center=',c)
    return len(bases), reflected


if __name__ == '__main__':
    count_bases = count_reflections = 0
    for name, (n, blocks) in [
        ('Fano PG(2,2)', projective_plane(2)),
        ('Affine AG(2,3)', affine_plane_three()),
        ('Projective PG(2,3)', projective_plane(3)),
        ('Steiner triples PG(3,2)', steiner_triples_15()),
        ('Projective PG(2,5)', projective_plane(5)),
    ]:
        b, r = verify(name,n,blocks)
        count_bases += b
        count_reflections += r
    print('ALL_EXACT_CHECKS_PASS', 'total_bases=',count_bases,
          'total_reflected_line_checks=',count_reflections)
