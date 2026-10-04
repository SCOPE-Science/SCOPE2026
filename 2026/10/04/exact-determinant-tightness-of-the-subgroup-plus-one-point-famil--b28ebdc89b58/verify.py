import cmath
import math

def det_complex(A):
    A = [list(map(complex, row)) for row in A]
    n = len(A)
    d = 1+0j
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(A[i][j]))
        if abs(A[pivot][j]) < 1e-12:
            return 0j
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            d = -d
        p = A[j][j]
        d *= p
        for i in range(j+1, n):
            f = A[i][j] / p
            if f == 0:
                continue
            for c in range(j+1, n):
                A[i][c] -= f * A[j][c]
    return d

def matrix(m, k):
    z = cmath.exp(2j*math.pi/m)
    E = [(x,0) for x in range(m)] + [(0,1)]
    B = [(a,0) for a in range(m)] + [(0,k)]
    return [[z**((a*x+b*y) % m) for (a,b) in B] for (x,y) in E]

def target(m, k):
    z = cmath.exp(2j*math.pi/m)
    return (m**(m/2.0))*abs(1-z**k)

for m in range(2, 25):
    vals = []
    for k in range(1, m):
        d = abs(det_complex(matrix(m,k)))
        t = target(m,k)
        assert abs(d-t) <= 5e-8*max(1.0,t), (m,k,d,t)
        vals.append(d)
    got = max(vals)
    if m % 2 == 0:
        want = 2*m**(m/2.0)
    else:
        want = 2*m**(m/2.0)*math.cos(math.pi/(2*m))
    assert abs(got-want) <= 5e-8*max(1.0,want), (m,got,want)

def log_tilde_D(m):
    s = 1.0 if m % 2 == 0 else math.cos(math.pi/(2*m))
    logD = math.log(2*s) + 0.5*m*math.log(m)
    return 0.5*math.log(m+1) - logD/(m+1)

for m in [10, 100, 1000, 10000]:
    assert log_tilde_D(m) > 0
assert log_tilde_D(10000) < log_tilde_D(1000) < log_tilde_D(100) < log_tilde_D(10)
assert math.exp(log_tilde_D(10000)) < 1.001

print("VERIFY_OK")
