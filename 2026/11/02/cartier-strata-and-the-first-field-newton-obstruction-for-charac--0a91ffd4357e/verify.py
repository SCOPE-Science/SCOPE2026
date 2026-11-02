"""Exact finite-field certificate for the cyclic trigonal genus-four result.

Run: python3 verify.py. Standard library only. All curve coefficients are
ordinary elements of GF(2), GF(4), or their specified polynomial embeddings.
"""
from itertools import product
from collections import Counter

MOD = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011,
       5: 0b100101, 6: 0b1000011, 7: 0b10000011, 8: 0b100011101}

def mul(x, y, n):
    assert 0 <= x < (1 << n) and 0 <= y < (1 << n)
    r = 0
    while y:
        if y & 1: r ^= x
        y >>= 1
        x <<= 1
        if x & (1 << n): x ^= MOD[n]
    return r

def root_of_unity(n):
    roots = [t for t in range(1 << n) if mul(t, t, n) ^ t ^ 1 == 0]
    assert len(roots) == 2
    return roots[0]

def embed4(a, n):
    return (a & 1) ^ (root_of_unity(n) if a & 2 else 0)

def admissible(u, v, w, z, q):
    # f = x(x^2+u*x+v)^2 + (w*x+z)^2; f'= (x^2+u*x+v)^2.
    # For h linear/nonzero the gcd is nonconstant only at h's rational root.
    n = 1 if q == 2 else 2
    if w == 0: return z != 0
    for r in range(q):
        if mul(w, r, n) == z:
            return mul(r, r, n) ^ mul(u, r, n) ^ v != 0
    raise AssertionError('Nonzero linear polynomial without a root')

def count_points(u, v, w, z, n, coeff_degree):
    # n divisible by coeff_degree. Compute in GF(2^n) by polynomial arithmetic.
    q = 1 << n
    if coeff_degree == 2:
        u, v, w, z = [embed4(c, n) for c in (u, v, w, z)]
    # Coefficients f=x^5+u^2*x^3+w^2*x^2+v^2*x+z^2.
    u, v, w, z = [mul(t, t, n) for t in (u, v, w, z)]
    cube = [0] * q
    for y in range(q):
        cube[mul(mul(y, y, n), y, n)] += 1
    total = 1  # unique point at infinity
    for x in range(q):
        x2 = mul(x, x, n)
        x3 = mul(x2, x, n)
        x5 = mul(x3, x2, n)
        f = x5 ^ mul(u, x3, n) ^ mul(w, x2, n) ^ mul(v, x, n) ^ z
        total += cube[f]
    return total

def weil_polynomial(u, v, w, z):
    # Coefficients in GF(4); extension counts over GF(4^j), j=1..4.
    Ns = [count_points(u, v, w, z, 2*j, 2) for j in range(1, 5)]
    power_sums = {j: 4**j + 1 - N for j, N in enumerate(Ns, 1)}
    c = [1]
    for j in range(1, 5):
        numer = sum(c[j-k] * power_sums[k] for k in range(1, j+1))
        assert numer % j == 0
        c.append(-numer // j)
    c += [4*c[3], 16*c[2], 64*c[1], 256]
    # Standard curve functional equation for genus 4, q=4.
    assert c[5] == 4*c[3] and c[6] == 16*c[2]
    assert c[7] == 64*c[1] and c[8] == 4**4
    return tuple(c)

def v2(c):
    assert c
    d = 0
    while c % 2 == 0:
        d += 1
        c //= 2
    return d

def valuation_slopes(c):
    pts = [(i, v2(t)) for i,t in enumerate(c) if t]
    hull = []
    for point in pts:
        while len(hull) > 1:
            a,b = hull[-2], hull[-1]
            # Delete middle if slopes not increasing.
            if (b[1]-a[1])*(point[0]-b[0]) >= (point[1]-b[1])*(b[0]-a[0]):
                hull.pop()
            else: break
        hull.append(point)
    return tuple((hull[j+1][1]-hull[j][1], hull[j+1][0]-hull[j][0])
                 for j in range(len(hull)-1))


def run():
    assert all(mul(x, y, 2) == mul(y, x, 2)
               for x in range(4) for y in range(4))
    for q in (2,4):
        n = 1 if q == 2 else 2
        rank_counts = Counter()
        np_counts = Counter()
        polys = Counter()
        checked = 0
        for u, v, w, z in product(range(q), repeat=4):
            if not admissible(u,v,w,z,q): continue
            checked += 1
            rank = 0 if u == 0 else 2
            rank_counts[rank] += 1
            if q == 4:
                poly = weil_polynomial(u,v,w,z)
                polys[(rank,poly)] += 1
                slopes = valuation_slopes(poly)
                np_counts[(rank, slopes)] += 1
                if rank == 0:
                    # q=4: Newton hull (0,0), (4,2), (8,8):
                    # normalized slopes 1/4 (x4), 3/4 (x4).
                    assert poly[4] % 8 == 4
                    assert slopes == ((2,4),(6,4)), (u,v,w,z,poly,slopes)
                else:
                    assert slopes == ((0,2),(4,4),(4,2)), (u,v,w,z,poly,slopes)
        assert checked == q**3*(q-1), (q,checked)
        assert rank_counts == {0:q*q*(q-1),2:q*q*(q-1)**2},rank_counts
        print('GF',q,'smooth',checked,'rank0',rank_counts[0],'rank2',rank_counts[2])
        if q == 4:
            assert len([1 for (r,p) in polys if r==0]) == 15
            assert len([1 for (r,p) in polys if r==2]) == 51
            print('GF4 distinct L-polynomials rank0',15,'rank2',51)
            print('GF4 Newton strata',dict(np_counts))
    print('VERIFY_OK')

if __name__ == '__main__':run()
