import math

rho = 1.0 + math.sqrt(2.0)
p = math.log(rho, 2.0)

def join_rate(a, b):
    return 2.0*a*b / (a+b+math.sqrt(a*a+6.0*a*b+b*b))

def join_step(a, b):
    return 1.0 + (math.sqrt(a*a+6.0*a*b+b*b)-(a+b))/(2.0*a*b)

cache = {1: ([], 1.0)}
def schedule(N):
    if N in cache:
        return cache[N]
    m = N//2
    r = N-m
    left, a = schedule(m)
    right, b = schedule(r)
    h = left + [join_step(a,b)] + right
    eta = join_rate(a,b)
    cache[N] = (h, eta)
    return cache[N]

for N in range(2, 257):
    h, eta = schedule(N)
    assert len(h) == N-1
    assert all(x > 1.0 for x in h)
    assert min(h) < 2.0
    H = sum(h)
    prod = 1.0
    for x in h:
        prod *= x-1.0
    assert abs(eta - 1.0/(1.0+H)) < 2e-10
    assert abs(eta - prod) < 2e-9
    U = 1.0/eta
    M = sum(x for x in h if x > 2.0)
    O = sum(max(x-2.0, 0.0) for x in h)
    lower = 1.0 - 2.0*(N-1)/H
    assert M/H + 2e-12 >= lower
    assert O/H + 2e-12 >= lower
    assert max(h) + 1e-12 >= H/(N-1)
    # Balanced phase value reconstructed from the exact scalar.
    phase = U/(N**p)
    assert phase > 0.98 and phase <= 1.0000000001

# Along dyadic horizons the exact recursion scales by rho.
for k in range(1, 9):
    N = 2**k
    h, eta = schedule(N)
    U = 1.0/eta
    assert abs(U - rho**k) < 2e-8

print("VERIFY_OK")
