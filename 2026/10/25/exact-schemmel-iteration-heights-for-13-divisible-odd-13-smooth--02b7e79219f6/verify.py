"""Exact independent arithmetic checks for a 13-smooth Schemmel iteration theorem."""
from itertools import product

PRIMES = (3, 5, 7, 11, 13)


def schemmel_two(n):
    if n <= 1:
        return n
    x = n
    result = 1
    for p in PRIMES:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e:
            result *= (p - 2) * p ** (e - 1)
    assert x == 1, 'Input is not 13-smooth'
    return result


def direct_height(a,b,c,d,e):
    n = 3**a * 5**b * 7**c * 11**d * 13**e
    t = 0
    while n > 1:
        z = schemmel_two(n)
        assert 1 <= z < n
        n = z
        t += 1
    return t


def predicted_height(a,b,c,d,e):
    assert e >= 1
    w = a + b + c + 2*d + 2*e
    if d:
        return w + int(a == 0)
    return w + int(a == 0) + int(a <= 1 and b == 0)


def exponent_height(a,b,c,d,e):
    t=0
    while a or b or c or d or e:
        A, B, C, D, E = (a,b,c,d,e)
        a = max(A-1,0) + int(B>0) + 2*int(D>0)
        b = max(B-1,0) + int(C>0)
        c = max(C-1,0)
        d = max(D-1,0) + int(E>0)
        e = max(E-1,0)
        t += 1
    return t


def run():
    direct_count=0
    for a,b,c,d,e in product(range(6),range(6),range(6),range(6),range(1,6)):
        expected = predicted_height(a,b,c,d,e)
        assert direct_height(a,b,c,d,e) == expected, (a,b,c,d,e)
        direct_count+=1
    grid_count=0
    for a,b,c,d,e in product(range(9),range(9),range(9),range(9),range(1,9)):
        assert exponent_height(a,b,c,d,e) == predicted_height(a,b,c,d,e), (a,b,c,d,e)
        grid_count+=1
    for a,b,c,d,e in [
        (0,0,0,0,50),(1,0,0,0,50),(2,0,0,0,50),
        (0,0,100,0,1),(0,100,0,0,1),(0,0,0,100,1),
        (100,0,0,0,1),(0,0,0,0,100),(0,0,100,100,1)
    ]:
        assert exponent_height(a,b,c,d,e) == predicted_height(a,b,c,d,e)
    print(f'VERIFY_OK: {direct_count} independent exact-integer iterates; {grid_count} exponent-state iterates; 9 large-boundary cases')

if __name__ == '__main__':
    run()
