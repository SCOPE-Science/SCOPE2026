"""Independent finite checks for a natural-conjugacy enumeration theorem.

Run: python3 verification/check.py.  Only Python standard library is required.
This checks small cases, not the general algebraic or formal-series proof.
"""
import itertools
import collections
from math import comb

DEG = 10

def multiply_polys(a, b, n=DEG):
    return [sum(a[j] * b[k-j] for j in range(k+1)) for k in range(n+1)]

def euler_transform_tree(n=DEG):
    t = [0]*(n+1)
    e = [0]*(n+1)
    e[0] = 1
    for k in range(1, n+1):
        t[k] = e[k-1] - (k == 1) + (k == 2)
        def derivative_sum(j):
            return sum(d*t[d] for d in range(1,j+1) if j % d == 0)
        dividend = sum(derivative_sum(j)*e[k-j] for j in range(1,k+1))
        assert dividend % k == 0
        e[k] = dividend//k
    return t, [0] + e[:n]

def class_numbers(c, n=DEG):
    _, a = euler_transform_tree(n)
    out = [1] + [0]*n
    for d in range(1,n+1):
        term = [0]*(n+1)
        for k in range(1,n//d+1):
            term[k*d] = a[k]
        pow_term = [1] + [0]*n
        block = [0]*(n+1)
        for k in range(n//d+1):
            weight = comb(c+k-1,k)
            block = [block[j]+weight*pow_term[j] for j in range(n+1)]
            pow_term = multiply_polys(pow_term,term,n)
        out = multiply_polys(out,block,n)
    return [sum(out[1:k+1]) for k in range(n+1)]

def count_unlabeled_image_maps(n):
    canonical = set()
    for f in itertools.product(range(n),repeat=n):
        image = sorted(set(f))
        index = {x:j for j,x in enumerate(image)}
        induced = tuple(index[f[i]] for i in image)
        r = len(image)
        normalized = []
        for p in itertools.permutations(range(r)):
            inv = {p[j]:j for j in range(r)}
            normalized.append(tuple(p[induced[inv[j]]] for j in range(r)))
        canonical.add((r,min(normalized)))
    return len(canonical)

# Compute full natural-conjugacy relation in the nonabelian example G=S_3, m=2,
# directly from the four defining monoid identities, with no use of the classification.
permutations = list(itertools.permutations(range(3)))
pos = {p:i for i,p in enumerate(permutations)}
comp = [[pos[tuple(permutations[i][permutations[j][k]] for k in range(3))]
         for j in range(6)] for i in range(6)]
endomorphisms = [ (f,w) for f in itertools.product(range(2),repeat=2)
                 for w in itertools.product(range(6),repeat=2) ]
lookup = {v:i for i,v in enumerate(endomorphisms)}
order = len(endomorphisms)
mult = [[0]*order for _ in range(order)]
for ia,(fa,wa) in enumerate(endomorphisms):
    for ib,(fb,wb) in enumerate(endomorphisms):
        # Composition: ia after ib.
        result = (tuple(fa[fb[i]] for i in range(2)),
                  tuple(comp[wb[i]][wa[fb[i]]] for i in range(2)))
        mult[ia][ib] = lookup[result]

parent = list(range(order))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def image_isomorphism(a,b):
    fa,wa=endomorphisms[a]; fb,wb=endomorphisms[b]
    ia=sorted(set(fa)); ib=sorted(set(fb))
    if len(ia)!=len(ib): return False
    for permutation in itertools.permutations(ib):
        sigma=dict(zip(ia,permutation))
        if any(sigma[fa[i]]!=fb[sigma[i]] for i in ia):continue
        for twists in itertools.product(range(6),repeat=len(ia)):
            t=dict(zip(ia,twists))
            if all(comp[wa[i]][t[fa[i]]] == comp[t[i]][wb[sigma[i]]] for i in ia):
                return True
    return False

for a in range(order):
    for b in range(a):
        gs = [g for g in range(order) if mult[a][g] == mult[g][b]]
        hs = [h for h in range(order) if mult[b][h] == mult[h][a]]
        definition = any(mult[mult[h][a]][g] == b and
                         mult[mult[g][b]][h] == a for g in gs for h in hs)
        image = image_isomorphism(a,b)
        if definition != image:
            raise AssertionError(('conjugacy image mismatch',a,b,definition,image))
        if definition:
            parent[find(a)]=find(b)
classes = collections.Counter(find(a) for a in range(order))
expected = class_numbers(3)[2]
assert order == 144
assert len(classes) == expected == 12
assert sorted(classes.values()) == [1,4,4,6,6,9,12,12,12,18,24,36]
print('S3 acting on two free orbits: direct four-witness test, 10,296 pairs, 12 classes: PASS')
for n in range(1,6):
    actual = count_unlabeled_image_maps(n)
    expected = class_numbers(1)[n]
    assert actual == expected,(n,actual,expected)
print('Trivial group, ranks 1..5: direct orbit enumeration and series agree: PASS')
assert class_numbers(1)[:7] == [0,1,3,7,15,30,61]
assert class_numbers(3)[:7] == [0,3,12,37,103,268,675]
print('Formal series integer coefficient tests: PASS')
