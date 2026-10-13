from math import factorial

checks = 0
for n in range(1, 201):
    volume = (n + 1) ** (n - 1)
    degree = factorial(n) * volume
    euler = factorial(n + 1)

    assert degree * (n + 1) == euler * (n + 1) ** (n - 1)

    if n == 1:
        assert (degree, euler) == (1, 2)
    elif n == 2:
        assert degree == euler == 6
    else:
        assert degree > euler

    checks += 1

print("VERIFY_OK", checks)
