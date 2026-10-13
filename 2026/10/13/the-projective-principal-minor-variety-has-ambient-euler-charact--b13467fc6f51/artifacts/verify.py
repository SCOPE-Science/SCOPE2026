from itertools import combinations

weight_cases = 0
for n in range(1, 17):
    weights = []
    for mask in range(1 << n):
        w = sum((1 << i) for i in range(n) if (mask >> i) & 1)
        weights.append(w)
    assert len(set(weights)) == (1 << n)
    weight_cases += len(weights)

coordinate_cases = 0
coordinate_evaluations = 0
for n in range(1, 11):
    for target in range(1 << n):
        a = [1 if (target >> i) & 1 else 0 for i in range(n)]
        b = [0 if (target >> i) & 1 else 1 for i in range(n)]
        nonzero = []
        for mask in range(1 << n):
            z = 1
            for i in range(n):
                z *= a[i] if ((mask >> i) & 1) else b[i]
            coordinate_evaluations += 1
            if z:
                nonzero.append((mask, z))
        assert nonzero == [(target, 1)], (n, target, nonzero)
        coordinate_cases += 1

assert weight_cases == (1 << 17) - 2
assert coordinate_cases == (1 << 11) - 2
print('VERIFY_OK', weight_cases, coordinate_cases, coordinate_evaluations)
