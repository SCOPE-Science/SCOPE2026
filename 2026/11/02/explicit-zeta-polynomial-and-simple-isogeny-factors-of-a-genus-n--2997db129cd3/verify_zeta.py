"""Exact rational-point and zeta computation for an explicit genus-nine curve.

Curve (smooth projective normalization over F_2):
    (x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1.

Run: python3 verify_zeta.py
The central check uses only Python's standard library.
"""

POLYS = {
    1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011,
    5: 0b100101, 6: 0b1000011, 7: 0b10000011,
    8: 0b100011101, 9: 0b1000010001,
    10: 0b10000001001, 11: 0b100000000101,
    12: 0b1000001010011,
}
EXPECTED = (4, 8, 4, 24, 44, 8, 116, 312, 508, 808, 2116, 4056)
EXPECTED_COEFFS = (1, 1, 2, 0, 2, 2, -4, -8, -11, 5, -22, -32,
                   -32, 32, 64, 0, 256, 256, 512)

class GF2N:
    def __init__(self, n):
        self.n, self.size, self.mod = n, 1 << n, POLYS[n]
        self.inverse = [0] * self.size
        for a in range(1, self.size):
            inverse = self.power(a, self.size - 2)
            assert self.mul(a, inverse) == 1, (n, a)
            self.inverse[a] = inverse
        self.as_roots = {}
        self.qas_roots = {}
        for a in range(self.size):
            a2 = self.mul(a, a)
            self.as_roots.setdefault(a2 ^ a, []).append(a)
            self.qas_roots.setdefault(self.mul(a2, a2) ^ a, []).append(a)
        assert all(len(v) == 2 for v in self.as_roots.values())
        assert all(len(v) == (2 if n % 2 else 4) for v in self.qas_roots.values())

    def mul(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            b >>= 1
            a <<= 1
            if a & self.size:
                a ^= self.mod
        return result

    def power(self, a, n):
        result = 1
        while n:
            if n & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            n >>= 1
        return result

    def trace2(self, a):
        trace = 0
        for _ in range(self.n):
            trace ^= a
            a = self.mul(a, a)
        assert trace in (0, 1)
        return trace


def count_via_plane(n):
    K = GF2N(n)
    # The exceptional fibers in the normalization are the ramified
    # points above infinity, x=0 and the two elliptic points for each
    # root x of x^3+1.  All are rational whenever x is rational.
    total = 2
    for x in range(1, K.size):
        x2 = K.mul(x, x)
        x3 = K.mul(x2, x)
        if x3 == 1:
            total += 2
            continue
        x4 = K.mul(x2, x2)
        x6 = K.mul(x3, x3)
        x7 = K.mul(x6, x)
        x8 = K.mul(x4, x4)
        d = x7 ^ x
        assert d != 0
        b = K.mul(x8 ^ x6 ^ x4 ^ x2 ^ 1, K.inverse[d])
        total += len(K.qas_roots.get(b, []))
    return total


def count_via_elliptic_cover(n):
    K = GF2N(n)
    # Elliptic curve y^2 + xy = x^3 + 1,
    # and z^2+z=y/x+(x^4+x^3+1)/(x^4+x).
    # The 8 simple poles are the geometric E[8], including infinity.
    total = 2  # one ramified point above O, one above (x,y)=(0,1)
    for x in range(1, K.size):
        x2 = K.mul(x, x)
        x3 = K.mul(x2, x)
        if x3 == 1:
            total += 2
            continue
        x4 = K.mul(x2, x2)
        d = x4 ^ x
        t_rhs = x ^ K.inverse[x2]
        for t in K.as_roots.get(t_rhs, []):
            f = t ^ K.mul(x4 ^ x3 ^ 1, K.inverse[d])
            total += 2 if K.trace2(f) == 0 else 0
    return total


def multiply_Z(polys):
    result = [1]
    for pol in polys:
        out = [0] * (len(result) + len(pol) - 1)
        for i, u in enumerate(result):
            for j, v in enumerate(pol):
                out[i+j] += u*v
        result = out
    return result


def recover_weil_polynomial(counts):
    g = 9
    powers = [0] + [2**n + 1 - counts[n-1] for n in range(1, g+1)]
    coeffs = [1]
    for k in range(1, g+1):
        v = -sum(coeffs[k-j]*powers[j] for j in range(1, k+1))
        assert v % k == 0
        coeffs.append(v // k)
    coeffs += [0] * g
    for k in range(g):
        coeffs[2*g-k] = 2**(g-k)*coeffs[k]
    assert len(coeffs) == 2*g+1
    return coeffs, powers


def gf2_poly_mul(a,b):
    out=0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def main():
    H = (1<<3)|1
    N = (1<<4)|(1<<3)|1
    F = (1<<8)|(1<<6)|(1<<4)|(1<<2)|1
    left = gf2_poly_mul(gf2_poly_mul(H,H),H) ^ gf2_poly_mul(N,N) ^ (gf2_poly_mul(gf2_poly_mul(2,N),H))
    assert left == gf2_poly_mul(2,F), 'elimination identity'
    assert gf2_poly_mul(2, gf2_poly_mul(H,H)) == ((1<<7)|2)

    a = [count_via_plane(n) for n in POLYS]
    b = [count_via_elliptic_cover(n) for n in POLYS]
    assert a == b == list(EXPECTED), (a,b)
    coeffs, power_sums = recover_weil_polynomial(a)
    assert tuple(coeffs) == EXPECTED_COEFFS, coeffs
    factors = [[1,-1,2], [1,1,2], [1,1,2],
               [1,0,-1,0,4], [1,0,-2,0,1,0,-8,0,16]]
    assert multiply_Z(factors) == coeffs
    assert sum(coeffs) == 1024
    assert coeffs[9] % 2 == 1

    for n in range(10,13):
        pred = -sum(coeffs[j]*power_sums[n-j] for j in range(1,n)) - n*coeffs[n]
        assert 2**n + 1 - a[n-1] == pred
        power_sums.append(pred)
    print('POINT_COUNTS',a)
    print('L_COEFFICIENTS',coeffs)
    print('JACOBIAN_F2_ORDER',sum(coeffs))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
