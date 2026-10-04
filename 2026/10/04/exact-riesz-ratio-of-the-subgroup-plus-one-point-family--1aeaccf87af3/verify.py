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
            if abs(f) < 1e-18:
                continue
            for c in range(j+1, n):
                A[i][c] -= f*A[j][c]
    return d


def fourier_matrix(m, k):
    w = cmath.exp(2j*math.pi/m)
    E = [(x,0) for x in range(m)] + [(0,1)]
    B = [(a,0) for a in range(m)] + [(0,k)]
    return [[w**((a*x+b*y) % m) for (a,b) in B] for (x,y) in E]


def gram(T):
    n = len(T)
    return [[sum(T[r][i].conjugate()*T[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def det_lambda_I_minus_G(G, lam):
    n = len(G)
    A = [[(lam if i == j else 0)-G[i][j] for j in range(n)] for i in range(n)]
    return det_complex(A)


def poly(m, t, lam):
    return lam**3-(4*m+1)*lam**2+(4*m*m+m*t)*lam-m*m*t


def bisect_root(m, t, a, b, steps=100):
    fa = poly(m,t,a)
    fb = poly(m,t,b)
    assert fa == 0 or fb == 0 or fa*fb < 0, (m,t,a,b,fa,fb)
    if fa == 0:
        return a
    if fb == 0:
        return b
    for _ in range(steps):
        c = (a+b)/2
        fc = poly(m,t,c)
        if fa*fc <= 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a+b)/2


def roots3(m, t):
    if abs(t-4.0) < 1e-12:
        return (1.0, 2.0*m, 2.0*m)
    r1 = bisect_root(m,t,0.0,float(m))
    r2 = bisect_root(m,t,float(m),2.0*m)
    r3 = bisect_root(m,t,2.0*m,4.0*m+1.0)
    return (r1,r2,r3)

# Directly test the full Fourier Gram characteristic factorization.
for m in range(2, 11):
    for k in range(1, m):
        T = fourier_matrix(m,k)
        G = gram(T)
        t = abs(1-cmath.exp(2j*math.pi*k/m))**2
        for lam in (0.37*m, 1.31*m, 2.73*m, 4.11*m):
            lhs = det_lambda_I_minus_G(G, lam)
            rhs = ((lam-m)**(m-2))*poly(m,t,lam)
            err = abs(lhs-rhs)
            scale = max(1.0,abs(lhs),abs(rhs))
            assert err <= 2e-7*scale, (m,k,lam,lhs,rhs)

# Check the root intervals and that maximal chord minimizes the ratio.
for m in range(2, 101):
    data = []
    for k in range(1,m):
        t = 4*math.sin(math.pi*k/m)**2
        r1,r2,r3 = roots3(m,t)
        assert r1 > 0 and r1 < m+1e-9
        assert r2 > m-1e-9 and r2 <= 2*m+1e-8
        assert r3 >= 2*m-1e-8
        data.append((t,r3/r1,r1,r3,k))
    best = min(data, key=lambda x:x[1])
    max_t = max(x[0] for x in data)
    assert abs(best[0]-max_t) < 1e-10
    if m % 2 == 0:
        assert abs(best[2]-1.0) < 1e-8
        assert abs(best[3]-2*m) < 1e-8
        assert abs(best[1]-2*m) < 2e-7
    else:
        want_t = 4*math.cos(math.pi/(2*m))**2
        assert abs(best[0]-want_t) < 1e-10

# Odd-modulus asymptotic check.
for m in (101, 301, 1001, 3001):
    t = 4*math.cos(math.pi/(2*m))**2
    r1,_,r3 = roots3(m,t)
    rho = r3/r1
    approx = 2*m + math.pi/math.sqrt(2*m)
    # The theorem claims an O(1/m) remainder.
    assert abs(rho-approx)*m < 7.0

print('VERIFY_OK')
