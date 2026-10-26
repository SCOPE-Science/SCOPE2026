"""Independent finite-state checks of reservoir-driven bipartite exclusion formulas.
Only Python standard library is required. Run: python verify_reservoir_bipartite.py
"""
from fractions import Fraction as F
from math import sqrt


def solve(A, b):
    """Exact rational Gauss-Jordan solution."""
    n = len(b)
    R = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        pivot = next((i for i in range(c, n) if R[i][c]), None)
        assert pivot is not None
        R[c], R[pivot] = R[pivot], R[c]
        v = R[c][c]
        R[c] = [a / v for a in R[c]]
        for i in range(n):
            if i != c and R[i][c]:
                f = R[i][c]
                R[i] = [a - f * v for a, v in zip(R[i], R[c])]
    return [R[i][n] for i in range(n)]


def exact_moments(m, n, alpha, beta):
    """Independently calculate stationary law of lumped occupancy-count CTMC."""
    states = [(i, j) for i in range(m + 1) for j in range(n + 1)]
    lookup = {v: k for k, v in enumerate(states)}
    Q = [[F(0) for _ in states] for _ in states]
    for k, (i, j) in enumerate(states):
        transitions = [((i + 1, j), alpha * (m - i)),
                       ((i, j - 1), beta * j),
                       ((i - 1, j + 1), i * (n - j)),
                       ((i + 1, j - 1), (m - i) * j)]
        for state, rate in transitions:
            if rate:
                ell = lookup[state]
                Q[k][ell] += rate
                Q[k][k] -= rate
    size = len(states)
    A = [[Q[j][i] for j in range(size)] for i in range(size)]
    A[-1] = [F(1)] * size
    rhs = [F(0)] * (size - 1) + [F(1)]
    pi = solve(A, rhs)
    assert sum(pi) == 1 and min(pi) > 0
    mean_i = sum(p * i for p, (i, j) in zip(pi, states))
    mean_j = sum(p * j for p, (i, j) in zip(pi, states))
    second_i = sum(p * i * (i - 1) for p, (i, j) in zip(pi, states))
    second_j = sum(p * j * (j - 1) for p, (i, j) in zip(pi, states))
    cross = sum(p * i * j for p, (i, j) in zip(pi, states))
    x, y = mean_i/m, mean_j/n
    return (x, y, second_i/(m*(m-1)) - x*x,
            second_j/(n*(n-1)) - y*y, cross/(m*n) - x*y)


def formulas(m, n, alpha, beta):
    d = 1/(1 + F(n)/alpha + F(m)/beta)
    x, y = 1 - n*d/alpha, m*d/beta
    D = alpha + beta + F(n-1)*beta/(m+beta) + F(m-1)*alpha/(n+alpha)
    w = -d*d/D
    u, v = F(n)*w/(n+alpha), F(m)*w/(m+beta)
    return x, y, u, v, w


def score(t, m, n, a, b):
    return -formulas(m, n, a*t, b*t)[-1]


def root_bisection(m, n, a, b):
    C = F(n)/a + F(m)/b
    p, q = F(m)/b, F(n)/a
    A, B = n-1, m-1
    def num(t):
        return ((C-t)*(a+b)
                + A*(t*(2*C-p)+C*p)/(t+p)**2
                + B*(t*(2*C-q)+C*q)/(t+q)**2)
    left = C
    right = 2*C
    while num(right) > 0:
        right *= 2
    for _ in range(80):
        t = (left+right)/2
        if num(t)>0: left=t
        else: right=t
    return float((left+right)/2)


def main():
    checks=0
    pairs = [(m,n,a,b) for m in range(2,5) for n in range(2,5)
             for a,b in ((F(1),F(1)),(F(2,3),F(3,2)),(F(5,2),F(7,3)))]
    for m,n,a,b in pairs:
        expected=formulas(m,n,a,b)
        actual=exact_moments(m,n,a,b)
        assert expected==actual, (m,n,a,b,expected,actual)
        checks += 5
    for m,n,a,b in ((2,3,F(1),F(1)),(3,5,F(2),F(3)),(6,2,F(3,2),F(5,3))):
        tstar = root_bisection(m,n,a,b)
        C = float(F(n)/a+F(m)/b)
        assert tstar>C
        central=float(score(F(tstar),m,n,a,b))
        for ratio in (.01,.1,.5,.99,1.01,1.5,3,10,100):
            assert central>float(score(F(tstar*ratio),m,n,a,b))
            checks+=1
    tau=(1+sqrt(3))/2
    height=sqrt(3)/18
    for N in (100, 400, 1600):
        k=N//2
        tstar=root_bisection(k,k,F(1),F(1))
        assert abs(tstar/N-tau) < 30/N
        assert abs(float(score(F(tstar),k,k,F(1),F(1)))*N-height)<30/N
        checks+=2
    print(f'PASS: {checks} independent exact-rational, optimization, and asymptotic checks')

if __name__ == '__main__': main()
