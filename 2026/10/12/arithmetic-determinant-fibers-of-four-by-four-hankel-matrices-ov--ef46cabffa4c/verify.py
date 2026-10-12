"""Direct finite-field determinant-fiber enumeration for 4-by-4 Hankel matrices.

Usage: python verify.py; only the Python standard library is needed.
"""
from itertools import product


def finite_field(q):
    if q == 4:
        def mul(a, b):
            r = 0
            while b:
                if b & 1:
                    r ^= a
                b >>= 1
                a <<= 1
                if a & 4:
                    a ^= 7  # alpha^2+alpha+1=0
            return r
        add = lambda a, b: a ^ b
        neg = lambda a: a
    else:
        add = lambda a, b: (a+b) % q
        neg = lambda a: (-a) % q
        mul = lambda a, b: (a*b) % q
    mult = [[mul(a, b) for b in range(q)] for a in range(q)]
    plus = [[add(a, b) for b in range(q)] for a in range(q)]
    minus = [[plus[a][neg(b)] for b in range(q)] for a in range(q)]
    inv = [0]*q
    for a in range(1, q):
        inv[a] = next(b for b in range(1, q) if mult[a][b] == 1)
    return mult, minus, inv


def count(q):
    mult, sub, inv = finite_field(q)
    fibers = [0] * q
    for values in product(range(q), repeat=7):
        rows = [[values[i+j] for j in range(4)] for i in range(4)]
        det = 1
        for i in range(4):
            pivot = next((j for j in range(i, 4) if rows[j][i]), None)
            if pivot is None:
                det = 0
                break
            if pivot != i:
                rows[i], rows[pivot] = rows[pivot], rows[i]
                det = sub[0][det]
            a = rows[i][i]
            det = mult[det][a]
            for j in range(i+1, 4):
                factor = mult[rows[j][i]][inv[a]]
                for k in range(i+1, 4):
                    rows[j][k] = sub[rows[j][k]][mult[factor][rows[i][k]]]
        fibers[det] += 1
    expected = []
    for target in range(q):
        roots2 = sum(1 for a in range(q) if mult[a][a] == target)
        roots4 = sum(1 for a in range(q) if mult[mult[a][a]][mult[a][a]] == target)
        expected.append(q**6+q**3*((roots4-1)+(q-1)*(roots2-1)))
    assert fibers == expected, (q, fibers, expected)
    assert sum(fibers) == q**7
    return fibers


if __name__ == '__main__':
    for q in (2,3,4,5,7):
        print('q=%d fibers=%s' % (q, count(q)))
    print('VERIFY_OK')
