#!/usr/bin/env python3
"""Standalone exact finite-field checks for a genus-five complete intersection."""

MODULI = {
    1: (0, 1),
    2: (1, 0, 1),
    3: (1, 2, 0, 1),
    4: (2, 1, 0, 0, 1),
}


def arithmetic(n):
    """Finite-field arithmetic, polynomial basis modulo a monic polynomial."""
    p = 3
    m = MODULI[n]
    size = p**n

    def unpack(z):
        return tuple(z // p**j % p for j in range(n))

    def pack(a):
        return sum((v % p) * p**j for j, v in enumerate(a))

    def add(x, y):
        return pack([u + v for u, v in zip(unpack(x), unpack(y))])

    def neg(x):
        return pack([-u for u in unpack(x)])

    def mul(x, y):
        z = [0] * (2*n-1)
        for i, u in enumerate(unpack(x)):
            for j, v in enumerate(unpack(y)):
                z[i+j] = (z[i+j] + u*v) % p
        for j in range(2*n-2, n-1, -1):
            if z[j]:
                for k in range(n):
                    z[j-n+k] = (z[j-n+k] - z[j]*m[k]) % p
        return pack(z[:n])

    def power(x, e):
        y = 1
        while e:
            if e % 2:
                y = mul(y, x)
            x = mul(x, x)
            e //= 2
        return y

    # Directly tests that the specified quotient ring is a field.
    assert all(mul(x, power(x, size-2)) == 1 for x in range(1, size))

    squares = [0]*size
    for x in range(size):
        squares[mul(x,x)] += 1

    def value(q1, q2, q3, mask):
        v = 1
        for index, a in enumerate((q1,q2,q3)):
            if mask & (1 << index):
                v = mul(v, a)
        return v

    count = [0]*8
    total = 0
    # Projective base P^1(F_q): q finite charts and one infinity.
    for u, v in [(t,1) for t in range(size)] + [(1,0)]:
        q1 = neg(add(mul(u,u), mul(v,v)))
        q2 = add(neg(mul(u,u)),mul(v,v))
        q3 = neg(mul(u,v))
        s = tuple(squares[a] for a in (q1,q2,q3))
        total += s[0] * s[1] * s[2]
        for mask in range(8):
            count[mask] += squares[value(q1,q2,q3,mask)]
    return size, count, total



def projective_direct(n):
    """Direct brute-force independent enumeration in projective four-space."""
    from itertools import product
    p = 3
    mod = MODULI[n]
    q = p**n
    def coeffs(z):
        return tuple(z // p**j % p for j in range(n))
    def enc(c):
        return sum((v%p)*p**j for j, v in enumerate(c))
    def add(x,y):
        return enc([u+v for u,v in zip(coeffs(x),coeffs(y))])
    def sub(x,y):
        return enc([u-v for u,v in zip(coeffs(x),coeffs(y))])
    def mul(x,y):
        z = [0]*(2*n-1)
        for i,a in enumerate(coeffs(x)):
            for j,b in enumerate(coeffs(y)):
                z[i+j] = (z[i+j]+a*b)%p
        for j in range(2*n-2,n-1,-1):
            for k in range(n):
                z[j-n+k] = (z[j-n+k]-z[j]*mod[k])%p
        return enc(z[:n])
    ct=0
    for i in range(5):
        # First nonzero homogeneous coordinate normalized to one.
        for tail in product(range(q), repeat=4-i):
            x=(0,)*i + (1,) + tail
            x0,x1,x2,x3,x4=x
            if add(mul(x0,x0),add(mul(x3,x3),mul(x4,x4)))!=0:
                continue
            if add(mul(x1,x1),sub(mul(x3,x3),mul(x4,x4)))!=0:
                continue
            if add(mul(x2,x2),mul(x3,x4))!=0:
                continue
            ct+=1
    return ct


def verify():
    # Different defining polynomials make these four point counts independent.
    expected = {3:4,9:24,27:28,81:56}
    for n in (1,2,3,4):
        q, subcover, actual = arithmetic(n)
        assert actual == expected[q], (q, actual, expected[q])
        if n in (1,2):
            direct=projective_direct(n)
            assert direct == actual,(q, direct, actual)
        assert actual == q+1+sum(subcover[i]-(q+1) for i in range(1,8))
        if q == 3:
            assert [subcover[i] for i in (1,2,4)] == [4]*3
            assert [subcover[i] for i in (3,5,6)] == [4]*3
            assert subcover[7] == 4
        if q == 9:
            assert [subcover[i] for i in (3,5,6)] == [16]*3
            assert subcover[7] == 6
        print('field_order=', q, 'curve_points=',actual,
              'elliptic_quotients=',tuple(subcover[i] for i in (3,5,6)),
              'genus_two_quotient=',subcover[7])
    # #E(F_3)=4 yields trace 0 and L_E(T)=1+3T^2.
    # #H(F_3)=4 and #H(F_9)=6 yield L_H(T)=1-2T^2+9T^4.
    # Algebraic derivation (not exhaustive code testing) gives all higher counts.
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
