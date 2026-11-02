"""Independent finite-case and matrix-identity checks for marked wheel percolation.

Run: python3 wheel_checker.py. All finite configuration checks use exact fractions.
These checks are diagnostics; the infinite-limit proof is mathematical.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, sqrt, factorial, isclose

CHECKS = 0

def verify(condition, message="test"):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(f"{message} at assertion {CHECKS}")


def finite_mean_formula(n, delta, q):
    connected = (1-delta)**n + n*delta*(1-delta)**(n-1)
    no_spoke = connected*(1-q)**n
    no_spoke += sum(l*delta**2*(1-delta)**(l-1)*(1-q)**l
                    for l in range(1, n))
    return 1-no_spoke


def enumerate_hub(n, delta, q):
    """Enumerate 2n independent rim/spoke edge states by exact probability."""
    total_h = F(0)
    p0 = F(0)
    p1 = F(0)
    total_prob = F(0)
    for edges in product((0, 1), repeat=2*n):
        rim, spoke = edges[:n], edges[n:]
        weight = F(1)
        for x in rim:
            weight *= (1-delta) if x else delta
        for x in spoke:
            weight *= q if x else (1-q)
        seen = {n}
        stack = [n]
        while stack:
            v = stack.pop()
            if v == n:
                nbrs = [i for i in range(n) if spoke[i]]
            else:
                nbrs = []
                if spoke[v]:
                    nbrs.append(n)
                if rim[v]:
                    nbrs.append((v+1) % n)
                if rim[(v-1) % n]:
                    nbrs.append((v-1) % n)
            for u in nbrs:
                if u not in seen:
                    seen.add(u)
                    stack.append(u)
        count = len(seen) - 1
        total_h += F(count, n)*weight
        p0 += weight if count == 0 else 0
        p1 += weight if count == n else 0
        total_prob += weight
    return total_h, p0, p1, total_prob


def tr_power(M, steps):
    A = ((F(1), F(0)), (F(0), F(1)))
    for _ in range(steps):
        A = tuple(tuple(sum(A[i][k]*M[k][j] for k in (0,1))
                        for j in (0,1)) for i in (0,1))
    return A[0][0]+A[1][1]


def circular_words(m, a, b):
    """Exact weight of color strings (S,C) with at least one S and no CC."""
    ans = F(0)
    for bits in product((0,1), repeat=m):
        if not any(bits):
            continue
        # 0 cut, 1 spoke. For m=1, a single cut is not allowed.
        if any(bits[j]==0 and bits[(j+1)%m]==0 for j in range(m)):
            continue
        ans += a**bits.count(0)*b**bits.count(1)
    return ans


def mean_limit(a,b):
    t=a+b
    return 1-(1+a)*exp(-t) - a*a/(t*t)*(1-(1+t)*exp(-t))


def full_limit(a,b):
    s=sqrt(b*b+4*a*b)
    return exp(-(a+b))*(exp((b+s)/2)+exp((b-s)/2)-2)


def main():
    for n in range(3,8):
        for delta,q in ((F(1,3),F(1,4)),(F(2,5),F(3,7))):
            mean,p0,p1,total=enumerate_hub(n,delta,q)
            verify(total==1,"normalization")
            verify(mean==finite_mean_formula(n,delta,q),"finite mean")
            verify(p0==(1-q)**n,"zero atom")
            verify(F(0)<p1<F(1),"finite all connected probability")
            verify(F(0)<=mean<=F(1),"finite mean range")
    for a,b in ((F(1,2),F(3,5)),(F(2),F(3)),(F(3,2),F(5,4))):
        M=((b,a),(b,F(0)))
        for m in range(1,12):
            verify(tr_power(M,m)==circular_words(m,a,b),"cycle transfer identity")
        approx=sum(float(tr_power(M,m))/factorial(m) for m in range(1,35))
        verify(abs(exp(-(float(a)+float(b)))*approx-full_limit(float(a),float(b)))<1e-12,
               "limit transfer exponential")
    for a,b in ((.2,.5),(.5,4.),(1.,1.),(3.,2.),(5.,.1)):
        assert 0<full_limit(a,b)<1-exp(-b)
        assert 0<mean_limit(a,b)<1
        # E e^{-bL} = atom at L=1 plus continuous size-biased gap density.
        steps=40000
        dx=1/steps
        density_integral=sum(a*a*(j+.5)*dx*exp(-(a+b)*(j+.5)*dx)
                             for j in range(steps))*dx
        no_spoke=(1+a)*exp(-(a+b))+density_integral
        verify(abs(1-no_spoke-mean_limit(a,b))<1e-9,"size-biased gap integral")
    print(f"PASS: {CHECKS} exact identities and numerical diagnostics")

if __name__ == '__main__':
    main()
