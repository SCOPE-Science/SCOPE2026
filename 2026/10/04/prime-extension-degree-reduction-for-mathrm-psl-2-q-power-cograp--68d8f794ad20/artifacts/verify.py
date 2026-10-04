def factorint(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def is_prime(n):
    if n < 2:
        return False
    f = factorint(n)
    return len(f) == 1 and next(iter(f.values())) == 1

def admissible(n):
    f = factorint(n)
    return len(f) == 1 or (len(f) == 2 and all(e == 1 for e in f.values()))

def prime_or_distinct_semiprime(n):
    f = factorint(n)
    return (len(f) == 1 and next(iter(f.values())) == 1) or (
        len(f) == 2 and all(e == 1 for e in f.values())
    )

def prime_int(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def source_criterion(p, f):
    q = p**f
    if p == 2:
        return admissible(q-1) and admissible(q+1)
    return admissible((q-1)//2) and admissible((q+1)//2)

def reduced_criterion(p, f):
    if p == 2:
        if f in (2, 4):
            return True
        if f % 2 == 0 or not prime_int(f):
            return False
        return is_prime((2**f+1)//3) and prime_or_distinct_semiprime(2**f-1)

    if f % 2 == 0:
        return p == 3 and f == 2

    if not prime_int(f):
        return False

    if p == 3:
        return admissible((3**f-1)//2) and is_prime((3**f+1)//4)

    if p == 5:
        return is_prime((5**f-1)//4) and is_prime((5**f+1)//6)

    return False

passing_2 = []
for f in range(2, 32):
    a = source_criterion(2, f)
    b = reduced_criterion(2, f)
    assert a == b, (2, f, a, b)
    if a:
        passing_2.append(f)

assert passing_2 == [2,3,4,5,7,11,13,17,19,23,31]

passing_odd = []
for p in (3,5,7,11):
    for f in range(2, 10):
        a = source_criterion(p, f)
        b = reduced_criterion(p, f)
        assert a == b, (p, f, a, b)
        if a:
            passing_odd.append((p, f))

assert passing_odd == [(3,2),(3,3),(3,5),(3,7)]

print("VERIFY_OK")
