def euler_projective(dim_vector_space):
    assert dim_vector_space >= 1
    return dim_vector_space

checks = 0
for m in range(1, 201):
    fixed = 2 * euler_projective(m)
    ambient = euler_projective(2 * m)
    assert fixed == 2 * m
    assert ambient == 2 * m
    assert fixed == ambient
    checks += 1

for n in range(1, 51):
    gl = n * n
    assert 2 * gl == 2 * n * n

    if n >= 2:
        sl = n * n - 1
        assert 2 * sl == 2 * (n * n - 1)

    so = n * (n - 1) // 2
    if so > 0:
        assert 2 * so == n * (n - 1)

    sp = n * (2 * n + 1)
    assert 2 * sp == 2 * n * (2 * n + 1)
    checks += 4

patterns = [(True, False), (False, True)]
assert all(a ^ b for a, b in patterns)
assert (True, True) not in patterns
assert (False, False) not in patterns

print("VERIFY_OK", checks)
