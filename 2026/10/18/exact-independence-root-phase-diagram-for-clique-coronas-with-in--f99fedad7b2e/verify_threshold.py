"""Independent finite checks for corona independence-root phase theorem.

Run: python3 verify_threshold.py
Uses Python's standard library only. This does not replace the unrestricted proof.
"""
from fractions import Fraction
from math import comb, cos, sin, pi, isclose


def crossings(k):
    return [1.0 / (sin((4*j+3)*pi/(2*k)) * cos((4*j+3)*pi/(2*k))**(k-1))
            for j in range(k) if 4*j+3 < k]


def right_roots_routh(k, r):
    # Descending coefficients for (1+z)^k+r*z.
    coefficients = [Fraction(comb(k,j)) for j in range(k, -1, -1)]
    coefficients[-2] += r
    width = (k+2)//2
    rows = [coefficients[::2]+[Fraction(0)]*width,
            coefficients[1::2]+[Fraction(0)]*width]
    rows = [row[:width] for row in rows]
    if rows[1][0] == 0:
        return None
    for _ in range(2,k+1):
        old, above = rows[-2], rows[-1]
        if above[0] == 0:
            return None
        new = []
        for j in range(width):
            u = old[j+1] if j+1 < width else 0
            v = above[j+1] if j+1 < width else 0
            new.append((above[0]*u - old[0]*v)/above[0])
        if all(q == 0 for q in new):
            return None  # On-axis root: handled separately, not presumed stable.
        rows.append(new)
    signs = [1 if row[0]>0 else -1 if row[0]<0 else 0 for row in rows]
    if 0 in signs:
        return None
    return sum(a!=b for a,b in zip(signs,signs[1:]))


def enumeration(r,k):
    n = r*(k+1)
    adj = [0]*n
    for i in range(r):
        for j in range(r):
            if i!=j: adj[i] |= 1<<j
        for t in range(k):
            leaf = r+i*k+t
            adj[i] |= 1<<leaf
            adj[leaf] |= 1<<i
    count = [0]*(k*r+2)
    for mask in range(1<<n):
        if all(not((mask>>v)&1) or not(adj[v]&mask) for v in range(n)):
            count[mask.bit_count()]+=1
    predicted = [0]*(k*r+2)
    for a in range(k*(r-1)+1):
        for b in range(k+1):
            predicted[a+b] += comb(k*(r-1),a)*comb(k,b)
        predicted[a+1] += r*comb(k*(r-1),a)
    assert count == predicted, (r,k,count,predicted)
    return 1<<n


def main():
    total = 0
    for r in range(1,5):
        for k in range(1,5):
            if r*(k+1) > 16:
                continue
            total += enumeration(r,k)
    routh = 0
    skipped = []
    cases = ([Fraction(2*r+1,2) for r in range(0,41)] +
             [Fraction(51,1),Fraction(101,1), Fraction(201,1),Fraction(1001,1), Fraction(100000,1), Fraction(10**12,1)])
    for k in range(1,21):
        thresholds = crossings(k)
        for r in cases:
            nr = right_roots_routh(k,r)
            if nr is None:
                skipped.append((k,str(r)))
                continue
            expected = 2*sum(float(r) > u for u in thresholds)
            assert nr == expected, (k,r,nr,expected,thresholds)
            routh += 1
    assert isclose(crossings(4)[0],8+8*2**.5,rel_tol=1e-12)
    assert isclose(crossings(5)[0],16*(1+5**.5)/5,rel_tol=1e-12)
    assert isclose(crossings(6)[0],8.,rel_tol=1e-12)
    # (1+z)^6+8z=(1+z*z)*(z^4+6z^3+14z^2+14z+1).
    from_left = [1,6,15,20,15,6,1]
    from_right = [1,14,14,6,1]
    prod = [0]*7
    for j,x in enumerate(from_right):
        prod[j] += x
        prod[j+2] += x
    assert prod == [1,14,15,20,15,6,1],prod
    print(f'VERIFIED: {total} explicitly enumerated vertex subsets; {routh} exact rational Routh cases; {len(skipped)} skipped singular Routh cases')
    print('Skipped pivot-singular cases (not used as evidence):',skipped[:12])
    print('Verified three critical parameters and exact dimension-six boundary factorization.')


if __name__ == '__main__':
    main()
