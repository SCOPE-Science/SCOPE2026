"""Finite cross-checks for parity-language square-root state complexity.
Only exact arithmetic over GF(2) is used.
"""
from collections import deque


def matrix_product(x, y, n):
    z = 0
    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(n):
                v ^= ((x >> (i*n+k)) & 1) & ((y >> (k*n+j)) & 1)
            z |= v << (i*n+j)
    return z


def rank_bitrows(rows):
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length()-1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def rank_universal(n, final):
    count = 1 << (n*n)
    products = [[matrix_product(x,y,n) for y in range(count)] for x in range(count)]
    # Square is computed from the matrix before evaluating its (0,final) entry.
    value = [((matrix_product(x,x,n) >> final) & 1) for x in range(count)]
    return rank_bitrows([sum(value[products[x][y]] << y for y in range(count)) for x in range(count)])


def identity(n):
    return sum(1 << (i*n+i) for i in range(n))


def closure(n, generators):
    reached = {identity(n)}
    queue = deque(reached)
    while queue:
        x = queue.popleft()
        for g in generators:
            y = matrix_product(x,g,n)
            if y not in reached:
                reached.add(y)
                queue.append(y)
    return reached


def ternary_generators(n):
    # Cyclic shift, I+E_{0,1}, corank-one projection
    C = sum(1 << (((i+1)%n)*n+i) for i in range(n))
    T = identity(n) ^ (1 << 1)
    D = identity(n) ^ (1 << (n*n-1))
    return (C,T,D)


def symbolic_rank(n,m):
    """Expand (XY)^2[0,m] in Boolean square-free monomials.
    The feature monomials are labeled by sets of input matrix entries.
    Equal monomials cancel in characteristic two.
    """
    R = {}
    C = {}
    terms = []
    for q in range(n):
        for p in range(n):
            for r in range(n):
                left = frozenset((p,r+n*q)) if q else frozenset((p,r))
                # X[0,p] is entry p; X[q,r] is entry q*n+r
                left = frozenset((p,q*n+r))
                right = frozenset((p*n+q,r*n+m))
                ii = R.setdefault(left,len(R))
                jj = C.setdefault(right,len(C))
                terms.append((ii,jj))
    rows = [0]*len(R)
    for i,j in terms: rows[i] ^= 1<<j
    return rank_bitrows(rows)


for n in range(1,9):
    target = n*n*n - n*n + n
    for m in range(min(n,2)):
        got = symbolic_rank(n,m)
        assert got == target,(n,m,got,target)
    print(f'SYMBOLIC n={n} rank={target} confirmed')

for n in (2,3):
    for m in (0,1):
        r = rank_universal(n,m)
        expected = n*n*n - n*n + n
        assert r == expected,(n,m,r,expected)
        print(f'INDEPENDENT FULL MATRIX HANKEL n={n} final={m} rank={r}')
    gen = ternary_generators(n)
    reached = closure(n,gen)
    assert len(reached) == 1 << (n*n)
    print(f'TERNARY SEMIGROUP n={n} reaches={len(reached)} of {1<<(n*n)} matrices')

# Two-letter n=2 witness: bit-coded row-major transition matrices 1 and 7.
A = 1
B = 7
n = 2
initial = 0
final = 1
row_words = ['', 'a', 'b', 'ab', 'bb', 'abb']
col_words = ['', 'b', 'ab', 'bb', 'abb', 'babb']

def word_matrix(w):
    x = identity(2)
    for c in w:
        x = matrix_product(x,A if c=='a' else B,2)
    return x

minor = []
for u in row_words:
    rr = 0
    for j,v in enumerate(col_words):
        x = word_matrix(u+v)
        sq = matrix_product(x,x,2)
        rr |= ((sq >> (initial*2+final)) & 1) <<j
    minor.append(rr)
assert rank_bitrows(minor)==6
print('BINARY WITNESS HANKEL MINOR GF2 RANK=6')
for rr in minor:
    print(' '.join(str((rr>>j)&1) for j in range(6)))
print('ALL CHECKS PASS')
