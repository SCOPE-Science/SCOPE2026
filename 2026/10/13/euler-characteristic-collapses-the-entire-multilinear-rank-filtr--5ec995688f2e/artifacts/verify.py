from itertools import product
from math import prod

def weights(dims):
    B = max(dims)
    vals = []
    for js in product(*[range(a) for a in dims]):
        vals.append(sum(j * (B ** i) for i, j in enumerate(js)))
    return vals

format_checks = bound_checks = exact_checks = 0

for t in range(3, 6):
    for dims in product(range(2, 5), repeat=t):
        N = prod(dims)
        ws = weights(dims)
        assert len(ws) == N
        assert len(set(ws)) == N

        exact = {}
        for bounds in product(*[range(1, a+1) for a in dims]):
            subtotal = 0
            for s, value in exact.items():
                if all(s[i] <= bounds[i] for i in range(t)):
                    subtotal += value
            value = N - subtotal
            exact[bounds] = value

            if all(x == 1 for x in bounds):
                assert value == N
            else:
                assert value == 0
            bound_checks += 1

        assert sum(1 for v in exact.values() if v != 0) == 1
        exact_checks += len(exact)
        format_checks += 1

print("VERIFY_OK", format_checks, bound_checks, exact_checks)
