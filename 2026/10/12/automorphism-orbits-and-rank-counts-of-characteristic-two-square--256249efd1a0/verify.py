"""Finite-field checks for algebra retractions of truncated squarefree power algebras."""
from collections import Counter
from itertools import product


def gl(k, q):
    ans = 1
    for j in range(k):
        ans *= q ** k - q ** j
    return ans


def expected(n, q):
    full = gl(n, q) * q ** (n * (2 ** n - 1 - n))
    counts = {}
    for r in range(n + 1):
        s = n - r
        central = gl(r, q) * gl(s, q) * q ** (
            r * (2 ** r - 1 - r) + s * (2 ** n - 2 ** r - s)
        )
        assert full % central == 0
        counts[2 ** r] = full // central
    return counts


def brute_binary(n):
    nmono = 1 << n
    polys = 1 << nmono
    radical = list(range(0, polys, 2))
    def mult(a, b):
        result = 0
        while a:
            lo = a & -a
            i = lo.bit_length() - 1
            a ^= lo
            z = b
            while z:
                low = z & -z
                j = low.bit_length() - 1
                z ^= low
                if i & j == 0:
                    result ^= 1 << (i | j)
        return result
    products = {a: {} for a in radical}
    for a in radical:
        for b in radical:
            if b > a:
                continue
            p = mult(a, b)
            products[a][b] = p
            products[b][a] = p
    def multiply(a, b):
        if a in products and b in products[a]:
            return products[a][b]
        return mult(a,b)
    inds = [tuple(i for i in range(nmono) if p & (1 << i)) for p in range(polys)]
    def mapped(p, images):
        v = 0
        for i in inds[p]:
            v ^= images[i]
        return v
    def rank(vecs):
        pivots = {}
        for v in vecs:
            while v:
                j = v.bit_length() - 1
                if j not in pivots:
                    pivots[j] = v
                    break
                v ^= pivots[j]
        return len(pivots)
    counts = Counter()
    for generators in product(radical, repeat=n):
        images = [1] * nmono
        for mask in range(1, nmono):
            lo = mask & -mask
            index = lo.bit_length() - 1
            images[mask] = multiply(images[mask ^ lo], generators[index])
        if all(mapped(generators[i], images) == generators[i] for i in range(n)):
            counts[rank(images)] += 1
    return dict(counts)


def multiply_f4(a, b):
    out = 0
    for i in range(2):
        if b & (1 << i):
            out ^= a << i
    if out & 8:
        out ^= 0b1100
    if out & 4:
        out ^= 0b0111
    return out


def brute_f4_two_variables():
    field = range(4)
    radical = list(product(field, repeat=3))
    def plus(a,b): return tuple(x ^ y for x,y in zip(a,b))
    def scale(c,a): return tuple(multiply_f4(c,x) for x in a)
    def mult(a,b):
        return (0,0,multiply_f4(a[0],b[1]) ^ multiply_f4(a[1],b[0]))
    counts = Counter()
    for a in radical:
        for b in radical:
            ab = mult(a,b)
            f_a = plus(plus(scale(a[0],a),scale(a[1],b)),scale(a[2],ab))
            if f_a != a:
                continue
            f_b = plus(plus(scale(b[0],a),scale(b[1],b)),scale(b[2],ab))
            if f_b != b:
                continue
            linear_columns = ((a[0],a[1]),(b[0],b[1]))
            if all(v == (0,0) for v in linear_columns):
                r=0
            elif multiply_f4(a[0],b[1]) ^ multiply_f4(b[0],a[1]):
                r=2
            else:
                r=1
            counts[2**r] += 1
    return dict(counts)


def run():
    for n in (1,2,3):
        got, want = brute_binary(n), expected(n,2)
        assert got == want,(n,got,want)
        print('F2',n,got)
    got, want=brute_f4_two_variables(),expected(2,4)
    assert got==want,(got,want)
    print('F4',2,got)
    for q in (2,4,8):
        for n in (1,2,3,4):
            out=expected(n,q)
            assert out[1]==out[2**n]==1
            assert all(x>0 for x in out.values())
    print('VERIFY_OK')

if __name__=='__main__':
    run()
