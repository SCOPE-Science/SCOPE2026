"""Independent exhaustive checks for involution commutation in UT_4(F_{2^e}).

Run: python ut4_even_involution_verify.py
No optional dependencies. Field multiplication uses binary-polynomial reduction.
"""
from itertools import product
from collections import Counter

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011}


def field_mul(x, y, degree):
    mask = (1 << degree) - 1
    modulus = IRREDUCIBLE[degree]
    result = 0
    while y:
        if y & 1:
            result ^= x
        y >>= 1
        x <<= 1
        if x & (1 << degree):
            x ^= modulus
    return result & mask


def mul(A, B, degree):
    C = [0] * 16
    for i in range(4):
        for j in range(i, 4):
            v = 0
            for k in range(i, j + 1):
                v ^= field_mul(A[4*i+k], B[4*k+j], degree)
            C[4*i+j] = v
    return tuple(C)


def identity():
    return tuple(int(i == j) for i in range(4) for j in range(4))


def involutions(degree):
    q = 1 << degree
    out = []
    E = identity()
    for a, b, c, d, e, f in product(range(q), repeat=6):
        A = list(E)
        for i, j, value in [(0,1,a),(1,2,b),(2,3,c),(0,2,d),(1,3,e),(0,3,f)]:
            A[4*i+j] = value
        A = tuple(A)
        if mul(A, A, degree) == E:
            out.append(A)
    return out


def category(A):
    a, b, c, d, e = A[1], A[6], A[11], A[2], A[7]
    if b:
        return "middle"
    if a or c:
        return "regular_quadric"
    if d or e:
        return "isotropic_axis"
    return "central"


def expected(q):
    return {
        "central": (q, 2*q**4-q**2),
        "isotropic_axis": (q**3-q, q**4+q**3-q**2),
        "regular_quadric": (q**4-q**2, 2*q**3-q**2),
        "middle": (q**4-q**3, q**4),
    }


def verify(degree, full):
    q = 1 << degree
    A = involutions(degree)
    assert len(A) == 2*q**4-q**2, (q,len(A))
    classes = Counter(map(category, A))
    prediction = expected(q)
    assert classes == Counter({name: v[0] for name,v in prediction.items()}), (q, classes)
    total_pred = q**8+2*q**7-2*q**5
    assert sum(multiplicity*centralizer for multiplicity,centralizer in prediction.values()) == total_pred
    if full:
        selected = A
    else:
        selected = []
        for name in prediction:
            selected.append(next(x for x in A if category(x)==name))
    centralizers = {}
    for x in selected:
        centralizers[x] = sum(mul(x,y,degree)==mul(y,x,degree) for y in A)
        assert centralizers[x] == prediction[category(x)][1], (q,category(x),centralizers[x])
    if full:
        assert sum(centralizers.values()) == total_pred
        hist = Counter((category(x), centralizers[x]) for x in A)
        assert hist == Counter({(name,v[1]):v[0] for name,v in prediction.items()})
    print("q=%d, involutions=%d, commuting ordered pairs=%d, checked centralizers=%d" %
          (q,len(A),total_pred,len(selected)))


if __name__ == '__main__':
    verify(1, True)
    verify(2, True)
    verify(3, False)
    print("VERIFY_OK involution commutation and centralizers in UT4 over even fields")
