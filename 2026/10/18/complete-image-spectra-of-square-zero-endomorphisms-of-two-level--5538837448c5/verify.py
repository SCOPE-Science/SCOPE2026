"""Independent exhaustive checks of square-zero endomorphism image types.
Run: python3 verify.py.  Python standard library only.
"""
from collections import Counter

def order_p_element(x, mod, p):
    order = 1
    while (order * x) % mod:
        order *= p
    return order

def image_type(a, b, c, d, p, n):
    p2, pn = p * p, p ** n
    u = (a, (p ** (n - 2)) * c)
    v = (b, d)
    uord = max(order_p_element(u[0], p2, p), order_p_element(u[1], pn, p))
    vord = max(order_p_element(v[0], p2, p), order_p_element(v[1], pn, p))
    H = {((i * u[0] + j * v[0]) % p2,
          (i * u[1] + j * v[1]) % pn)
         for i in range(uord) for j in range(vord)}
    size, exponent = len(H), max(uord, vord)
    k = j = 0
    while p ** k < exponent:
        k += 1
    while p ** j < size:
        j += 1
    assert p ** k == exponent and p ** j == size
    return (j - k, k)

def predicted(p, n):
    spectrum = Counter({(0, 0): 1, (0, 1): (p+1)*(p*p-1),
                        (1, 1): p*(p-1)*(p*p-1)})
    spectrum[(0, 2)] = (p*p*(p*p-1) if n == 2 else
                        2*p**3*(p-1) if n == 3 else 3*p**3*(p-1))
    for j in range(3, n+1):
        if 2*j <= n:
            x = (p-1)*(3*p-2)*p**j
        elif 2*j == n+1:
            x = 2*(p-1)**2*p**j
        elif 2*j == n+2:
            x = (p-1)**2*p**j
        else:
            x = 0
        if x:
            spectrum[(0,j)] = x
    for j in range(2, n//2+1):
        spectrum[(1,j)] = (p-1)**2*p**(j+1)
    return spectrum

def brute(p, n):
    p2, pn, z = p*p, p**n, Counter()
    for a in range(p2):
        for b in range(p2):
            for c in range(p2):
                if (a*a+p**(n-2)*b*c) % p2:
                    continue
                for d in range(pn):
                    if ((a+d)*b) % p2 or ((a+d)*c) % p2:
                        continue
                    if (d*d+p**(n-2)*b*c) % pn:
                        continue
                    z[image_type(a,b,c,d,p,n)] += 1
    return z

def main():
    cases = [(2,n) for n in range(2,11)] + [(3,n) for n in range(2,8)] + [(5,n) for n in (2,3,4)]
    for p, n in cases:
        actual, expected = brute(p, n), predicted(p, n)
        assert actual == expected, (p, n, actual, expected)
        total = sum(actual.values())
        closed = ((2*p*p-1)*p**(n//2+1) if n % 2 == 0 else
                  (3*p-2)*p**((n+3)//2))
        assert total == closed, (p, n, total, closed)
        print('OK',p,n,total,sorted(actual.items()))
    print('VERIFY_OK',len(cases),'cases')
if __name__ == '__main__':
    main()
