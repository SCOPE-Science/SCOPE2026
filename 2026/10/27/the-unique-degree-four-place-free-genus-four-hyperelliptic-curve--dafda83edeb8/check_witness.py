"""An independent exact test of the genus-four witness over F_3."""
# Base-three vectors represent F_81 = F_3[u]/(u^4+u+2).
def mul(a, b):
    da = [(a // 3**i) % 3 for i in range(4)]
    db = [(b // 3**i) % 3 for i in range(4)]
    out = [0] * 7
    for i in range(4):
        for j in range(4):
            out[i+j] += da[i] * db[j]
    for k in range(6, 3, -1):
        v = out[k] % 3
        out[k-4] -= 2*v
        out[k-3] -= v
    return sum((out[i] % 3) * (3**i) for i in range(4))

def sub(a, b):
    return sum((((a//3**i) % 3 - (b//3**i) % 3) % 3) * 3**i for i in range(4))

def power(a, n):
    z = 1
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n >>= 1
    return z

assert all(power(a, 81) == a for a in range(81))
assert all(power(a, 80) == 1 for a in range(1,81))
roots9 = [a for a in range(81) if power(a, 9) == a]
assert len(roots9) == 9
point_count81 = 1
for x in range(81):
    rhs = sub(power(x, 9), x)
    assert (rhs == 0) == (x in roots9)
    if rhs:
        assert power(rhs, 40) == 2
    point_count81 += int(rhs == 0)
assert point_count81 == 10
print('WITNESS_VERIFY_OK N2=10 N4=10 B4=0')
