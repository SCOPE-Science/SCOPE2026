def two_part(n):
    p = 1
    while n % (2*p) == 0:
        p *= 2
    return p

def delta_closed(n):
    if n % 2:
        return (n + 1)//2
    return (3*n + two_part(n))//4

for n in range(1, 4097):
    d = delta_closed(n)
    assert d >= 1 and d <= n
    if n % 2:
        assert d == (n + 1)//2
    else:
        p = two_part(n)
        q = n // p
        assert q % 2 == 1
        k = (q - 1)//2
        a = p.bit_length() - 1
        alpha = (2**(a-1)) * (3*k + 2)
        assert d == alpha
        if q == 1:
            assert d == n
        if a == 1:
            assert d == (3*q + 1)//2
print("VERIFY_OK")
