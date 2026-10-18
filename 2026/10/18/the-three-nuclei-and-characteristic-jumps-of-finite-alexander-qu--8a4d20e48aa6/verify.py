"""Direct finite-field associator checks for finite Alexander quandle algebras.

No symbolic group-ring nuclearity equations are assumed in the computation:
the verifier forms the original quandle multiplication table, constructs each
associator matrix and takes its nullity by modular Gaussian elimination.
"""
from itertools import product
from math import gcd


def rank_mod(rows, prime):
    rows = [list(row) for row in rows if any(x % prime for x in row)]
    if not rows:
        return 0
    length = len(rows[0]); pivot_row = 0
    for col in range(length):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col] % prime), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        unit = pow(rows[pivot_row][col] % prime, -1, prime)
        rows[pivot_row] = [(x * unit) % prime for x in rows[pivot_row]]
        for k in range(pivot_row + 1, len(rows)):
            coefficient = rows[k][col] % prime
            if coefficient:
                rows[k] = [(rows[k][j] - coefficient * rows[pivot_row][j]) % prime
                           for j in range(length)]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def test_case(orders, matrix, field_prime):
    elements = list(product(*(range(n) for n in orders)))
    count = len(elements)
    pos = {g: i for i, g in enumerate(elements)}
    def add(x, y):
        return tuple((a + b) % m for a, b, m in zip(x, y, orders))
    def subtract(x, y):
        return tuple((a - b) % m for a, b, m in zip(x, y, orders))
    def phi(x):
        return tuple(sum(matrix[i][j]*x[j] for j in range(len(orders))) % orders[i]
                     for i in range(len(orders)))
    assert len({phi(g) for g in elements}) == count
    beta = lambda x: subtract(x, phi(x))
    H = {beta(g) for g in elements}
    HH = {beta(g) for g in H}
    h = len(H); b = h // len(HH); a = count // h
    left = a
    middle = count - h + 1
    right = count - h + (1 if HH == H else 0)
    full = a if (HH == H or b % field_prime == 0) else a - b
    expected = (left, middle, right, full)
    table = [[pos[add(phi(x), beta(y))] for y in elements] for x in elements]
    associative = {}
    for x in range(count):
        for y in range(count):
            for z in range(count):
                associative[x,y,z] = (table[table[x][y]][z], table[x][table[y][z]])
    rows = [[], [], []]
    for slot in range(3):
        for fixed_first in range(count):
            for fixed_second in range(count):
                for out in range(count):
                    row = []
                    for variable in range(count):
                        triple = [fixed_first, fixed_second]
                        triple.insert(slot, variable)
                        plus, minus = associative[tuple(triple)]
                        row.append(((plus == out) - (minus == out)) % field_prime)
                    rows[slot].append(row)
    observed = tuple(count - rank_mod(mat, field_prime) for mat in
                     rows + [rows[0] + rows[1] + rows[2]])
    assert observed == expected, (orders,matrix,field_prime,expected,observed)
    return expected


def main():
    cases = 0
    for n in range(1,13):
        for multiplier in range(n):
            if gcd(multiplier, n) != 1:
                continue
            for coefficient_prime in (2,3,5,7):
                dimensions = test_case((n,), ((multiplier,),), coefficient_prime)
                cases += 1
                if n in (4,6) and multiplier == n-1 and coefficient_prime in (2,3):
                    print('CYCLIC',n,'multiplier',multiplier,'char',coefficient_prime,
                          'L,M,R,N',dimensions)
    cyclic_cases=cases
    for p in (2,3):
        for entries in product(range(p), repeat=4):
            a,b,c,d = entries
            if (a*d-b*c) % p == 0:
                continue
            for coefficient_prime in (2,3,5):
                dimensions = test_case((p,p), ((a,b),(c,d)), coefficient_prime)
                cases += 1
                if a==1 and b==1 and c==0 and d==1 and coefficient_prime in (2,3):
                    print('UNIPOTENT',p,'char',coefficient_prime,'L,M,R,N',dimensions)
    print('DIRECT_ASSOCIATOR_LINEAR_SYSTEMS',cases,'PASS')
    print('CYCLIC_CASES',cyclic_cases,'NONCYCLIC_CASES',cases-cyclic_cases)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
