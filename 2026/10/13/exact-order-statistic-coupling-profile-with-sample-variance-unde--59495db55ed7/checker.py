from fractions import Fraction
from math import factorial
from itertools import product

def beta_moment(n, k, r):
    out = Fraction(1)
    for j in range(r):
        out *= Fraction(k+j, n+1+j)
    return out

def closed_cov(n, k):
    return Fraction(
        k*(n+1-k)*(2*k-n-1),
        6*n*(n-1)*(n+1)*(n+3),
    )

def var_order(n, k):
    return Fraction(k*(n+1-k), (n+1)**2*(n+2))

def var_s2(n):
    return Fraction(2*n+3, 360*n*(n-1))

def conditional_coeffs(n, k):
    # E[S^2 | X_(k)=x] = c0 + c1 x + c2 x^2
    # Derived independently from conditional lower/upper uniforms.
    m = k-1
    r = n-k

    # E Q = q0 + q1 x + q2 x^2
    q0 = Fraction(r, 3)
    q1 = Fraction(r, 3)
    q2 = Fraction(n+2, 3)

    # E T = a + b x
    a = Fraction(r, 2)
    b = Fraction(n+1, 2)

    # Var T = [m x^2 + r(1-x)^2]/12
    v0 = Fraction(r, 12)
    v1 = Fraction(-2*r, 12)
    v2 = Fraction(m+r, 12)

    # E T^2 coefficients.
    t0 = v0 + a*a
    t1 = v1 + 2*a*b
    t2 = v2 + b*b

    return (
        (q0 - t0/Fraction(n))/(n-1),
        (q1 - t1/Fraction(n))/(n-1),
        (q2 - t2/Fraction(n))/(n-1),
    )

def conditional_cov(n, k):
    c0, c1, c2 = conditional_coeffs(n, k)
    e1 = beta_moment(n, k, 1)
    e2 = beta_moment(n, k, 2)
    e3 = beta_moment(n, k, 3)
    exs2 = c0*e1 + c1*e2 + c2*e3
    return exs2 - e1*Fraction(1,12)

def edir(counts):
    m = len(counts)
    r = sum(counts)
    num = 1
    for c in counts:
        num *= factorial(c)
    den = 1
    for j in range(r):
        den *= m+j
    return Fraction(num, den)

def eprod_linear(vectors):
    m = len(vectors[0])
    total = Fraction(0)
    for js in product(range(m), repeat=len(vectors)):
        coeff = 1
        counts = [0]*m
        for v,j in zip(vectors, js):
            coeff *= v[j]
            if coeff == 0:
                break
            counts[j] += 1
        if coeff:
            total += coeff*edir(counts)
    return total

def dirichlet_cov(n, k):
    # n order statistics from n+1 uniform spacings.
    m = n+1
    vecs = []
    for i in range(1, n+1):
        v = [0]*m
        for j in range(i):
            v[j] = 1
        vecs.append(v)
    uk = vecs[k-1]

    eq = sum((eprod_linear([v,v]) for v in vecs), Fraction(0))
    et2 = sum((eprod_linear([v,w]) for v in vecs for w in vecs), Fraction(0))
    es2 = (eq - et2/Fraction(n))/(n-1)

    euq = sum((eprod_linear([uk,v,v]) for v in vecs), Fraction(0))
    eut2 = sum((eprod_linear([uk,v,w]) for v in vecs for w in vecs), Fraction(0))
    eus2 = (euq - eut2/Fraction(n))/(n-1)

    eu = Fraction(k, n+1)
    return eus2 - eu*es2

def run():
    dirichlet_checks = 0
    conditional_checks = 0
    variance_checks = 0
    correlation_checks = 0
    symmetry_checks = 0
    median_checks = 0

    for n in range(2, 13):
        for k in range(1, n+1):
            assert dirichlet_cov(n, k) == closed_cov(n, k)
            dirichlet_checks += 1

    for n in range(2, 1001):
        for k in range(1, n+1):
            cov = closed_cov(n, k)
            assert conditional_cov(n, k) == cov
            conditional_checks += 1

            vo = var_order(n, k)
            vs = var_s2(n)
            assert vo > 0 and vs > 0
            variance_checks += 2

            corr2 = cov*cov/(vo*vs)
            target = Fraction(
                10*k*(n+1-k)*(n+2)*(2*k-n-1)**2,
                n*(n-1)*(n+3)**2*(2*n+3),
            )
            assert corr2 == target
            correlation_checks += 1

            assert closed_cov(n, n+1-k) == -cov
            symmetry_checks += 1

        if n % 2 == 1:
            assert closed_cov(n, (n+1)//2) == 0
            median_checks += 1

    print("VERIFY_OK")
    print(f"dirichlet_checks={dirichlet_checks}")
    print(f"conditional_checks={conditional_checks}")
    print(f"variance_checks={variance_checks}")
    print(f"correlation_checks={correlation_checks}")
    print(f"symmetry_checks={symmetry_checks}")
    print(f"median_checks={median_checks}")
    print("max_n=1000")

if __name__ == "__main__":
    run()
