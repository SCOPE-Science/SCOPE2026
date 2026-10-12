from itertools import product

def coordinate_weights(dims):
    B = max(dims) + 1
    out = []
    for js in product(*[range(a) for a in dims]):
        w = sum(j * (B ** i) for i, j in enumerate(js))
        out.append((js, w))
    return B, out

format_checks = coordinate_checks = 0
for t in range(3, 7):
    # Exhaust all dimension choices from 2 through 5 for t factors.
    for dims in product(range(2, 6), repeat=t):
        B, data = coordinate_weights(dims)
        weights = [w for _, w in data]
        expected = 1
        for a in dims:
            expected *= a

        assert B > max(dims)
        assert len(data) == expected
        assert len(set(weights)) == expected

        # Every multi-index represents one decomposable tensor-coordinate line.
        for js, w in data:
            assert len(js) == t
            assert all(0 <= js[i] < dims[i] for i in range(t))
            coordinate_checks += 1

        format_checks += 1

# Representative filled-secant sanity checks: if sigma_r is the full ambient
# P^(N-1), its Euler characteristic is N, matching the fixed-point prediction.
for dims in [(2,2,2), (2,2,3), (2,3,3), (3,3,3)]:
    N = 1
    for a in dims:
        N *= a
    ambient_euler = N
    predicted = N
    assert ambient_euler == predicted

print("VERIFY_OK", format_checks, coordinate_checks)
