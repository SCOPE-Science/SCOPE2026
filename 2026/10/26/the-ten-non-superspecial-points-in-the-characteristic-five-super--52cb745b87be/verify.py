#!/usr/bin/env python3
"""Exact characteristic-five checks for the marked j=0 Howe family.

Runs with the Python standard library only. Field elements are represented by
polynomials in a fixed root of an irreducible monic polynomial over F_5.
The symbolic proof and the scope of the tests are in RESULT.md.
"""

P = 5


def trim(a):
    a = [int(x) % P for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def sub(a, b):
    return trim([(a[i] if i < len(a) else 0) -
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] = (c[i+j] + ai * bj) % P
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b
    q = [0] * max(0, (len(a) - len(b) + 1))
    inv = pow(b[-1], -1, P)
    while a and len(a) >= len(b):
        k = len(a) - len(b)
        t = a[-1] * inv % P
        q[k] = t
        a = sub(a, [0] * k + [(t * z) % P for z in b])
    return trim(q), a


def mod(a, b):
    return divrem(a, b)[1]


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, mod(a, b)
    if not a:
        return []
    return trim([(x * pow(a[-1], -1, P)) % P for x in a])


def powmod(a, e, m):
    r = [1]
    while e:
        if e & 1:
            r = mod(mul(r, a), m)
        a = mod(mul(a, a), m)
        e //= 2
    return r


def irreducible(f):
    n = len(trim(f)) - 1
    if n <= 0:
        return False
    if n == 1:
        return True
    x = [0, 1]
    # Irreducibility test based on gcd(f, x^(5^(n/l))-x).
    for ell in range(2, n + 1):
        if n % ell == 0 and all(ell % d for d in range(2, int(ell**0.5)+1)):
            if gcd(f, sub(powmod(x, 5**(n // ell), f), x)) != [1]:
                return False
    return sub(powmod(x, 5**n, f), x) == []


class Field:
    def __init__(self, modulus):
        self.pol = trim(modulus)
        self.n = len(self.pol) - 1
        self.q = 5**self.n
        assert self.pol[-1] == 1 and irreducible(self.pol)
        self.digits = [self._digits(i) for i in range(self.q)]
        self.zero, self.one = 0, 1

    def _digits(self, a):
        digits = []
        for _ in range(self.n):
            digits.append(a % 5)
            a //= 5
        return digits

    def _encode(self, v):
        z, power = 0, 1
        for t in v:
            z += int(t) % 5 * power
            power *= 5
        return z

    def add(self, a, b):
        return self._encode([(x+y) % 5 for x, y in zip(self.digits[a], self.digits[b])])

    def neg(self, a):
        return self._encode([-x % 5 for x in self.digits[a]])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if a == 0 or b == 0:
            return 0
        return self._encode(mod(mul(self.digits[a], self.digits[b]), self.pol))

    def power(self, a, n):
        r = 1
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n >>= 1
        return r

    def integer(self, v):
        return int(v) % 5


def polyprod_field(a, b, K):
    z = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            z[i+j] = K.add(z[i+j], K.mul(ai, bj))
    return z


def direct_cartier(A, B, L, K):
    """Independently expand (x^3+A)*((x-L)^3+B), then square."""
    two = K.integer(2)
    three = K.integer(3)
    # Characteristic-five cube: x^3 - 3 L x^2 + 3 L^2 x - L^3.
    c1 = [A, 0, 0, 1]
    c2 = [K.sub(B, K.power(L, 3)), K.mul(three, K.power(L, 2)),
          K.neg(K.mul(three, L)), 1]
    f = polyprod_field(c1, c2, K)
    f2 = polyprod_field(f, f, K)
    return [[f2[4], f2[9]], [f2[3], f2[8]]]


def is_super(M, K):
    Mf = [[K.power(M[i][j], 5) for j in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            acc = K.add(K.mul(M[i][0], Mf[0][j]),
                        K.mul(M[i][1], Mf[1][j]))
            if acc != 0:
                return False
    return True


def formulas(A, B, L, K):
    mulf, addf = K.mul, K.add
    three, two, four = K.integer(3), K.integer(2), K.integer(4)
    a = mulf(mulf(A, K.power(L, 2)), addf(mulf(three, K.power(L, 3)), mulf(two, B)))
    b = mulf(two, addf(A, B))
    c = mulf(A, addf(addf(mulf(two, K.power(L, 6)), mulf(B, K.power(L, 3))),
                   addf(mulf(two, mulf(A, B)), mulf(two, mulf(B, B)))))
    d = mulf(L, addf(mulf(three, A), mulf(four, B)))
    return [[a, b], [c, d]]


def resultant_nonzero(A, B, L, K):
    # Equal cubic roots iff f_1 and f_2 have a common factor; use Euclidean
    # arithmetic for monic polynomials over an extension field.
    def divrem_field(a, b):
        aa = list(a)
        assert b[-1] == 1
        while len(aa) >= len(b):
            z = aa[-1]
            j = len(aa)-len(b)
            for k,v in enumerate(b):
                aa[j+k] = K.sub(aa[j+k], K.mul(z, v))
            while aa and aa[-1] == 0:
                aa.pop()
        return aa
    three = K.integer(3)
    f1=[A, 0, 0, 1]
    f2=[K.sub(B, K.power(L,3)), K.mul(three,K.power(L,2)),K.neg(K.mul(three,L)),1]
    # Subtract monic cubics; if the difference is zero they coincide.
    g=[K.sub(x,y) for x,y in zip(f1,f2)]
    while g and g[-1]==0:
        g.pop()
    if not g:
        return False
    # For root sharing, calculate gcd via Euclid with normalization.
    # These small fields admit inversion by q-2.
    a, b = f1, g
    while b:
        inv=K.power(b[-1], K.q-2)
        b=[K.mul(inv,z) for z in b]
        rem=divrem_field(a,b)
        a,b=b,rem
    return len(a)==1


def eval_poly(coeffs, x, K):
    z=0
    for c in reversed(coeffs):
        z=K.add(K.mul(z,x),K.integer(c))
    return z


def checks():
    # Characteristic-five elimination of the rank-one Cartier locus.
    h=[1,0,0,0,0,0,4,0,2,0,2]
    u=[2,0,1,1]
    v=[3,0,4,1]
    w=[3,0,2,0,1]
    assert mul([2],mul(mul(u,v),w))==h
    for f in (u,v,w):
        assert irreducible(f)
    # A(S)=3S^2+3S-1, B(S)=2S^2+3S+1 and resultant condition.
    af=[4,3,3]
    bf=[1,3,2]
    rf=[3,0,2,0,1,0,4]   # -S^6+S^4+2S^2-2
    assert gcd(h,af)==gcd(h,bf)==gcd(h,rf)==gcd(h,[0,1])==[1]
    counts=[]
    for n, pol in ((1,[0,1]),(2,[2,0,1]),(3,[1,1,0,1]),(4,[2,0,1,0,1])):
        K=Field(pol)
        root_s=[s for s in range(K.q) if eval_poly(h,s,K)==0]
        expected=6*(n%3==0)+4*(n%4==0)
        assert len(root_s)==expected, (n,len(root_s),expected)
        # Check each root is smooth and Cartier-nilpotent by direct expansion.
        for s in root_s:
            A=eval_poly(af,s,K)
            B=eval_poly(bf,s,K)
            assert A!=0 and B!=0
            assert resultant_nonzero(A,B,1,K)
            M=direct_cartier(A,B,1,K)
            assert M==formulas(A,B,1,K)
            assert is_super(M,K) and M!=[[0,0],[0,0]]
        counts.append((K.q,len(root_s)))
        if n in (1,2):
            count=0
            for L in range(K.q):
                for A in range(1,K.q):
                    for B in range(1,K.q):
                        if not resultant_nonzero(A,B,L,K):
                            continue
                        M=direct_cartier(A,B,L,K)
                        assert M==formulas(A,B,L,K)
                        if is_super(M,K):
                            count+=1
            assert count==(K.q-1)*(1+expected),(n,count)
            print('full_coefficient_census F_%d=%d'%(K.q,count))
    assert counts==[(5,0),(25,0),(125,6),(625,4)]
    print('normalized_nonzero_shift_roots', counts)
    print('factorization_and_smoothness OK')
    print('VERIFY_OK')

if __name__=='__main__':
    checks()
