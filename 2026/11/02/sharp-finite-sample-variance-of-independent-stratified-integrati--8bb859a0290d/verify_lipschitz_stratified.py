"""Exact rational diagnostics for a stratified-integration variance theorem.

Run: python verify_lipschitz_stratified.py
The continuum proof is in RESULT.md; finite tests are diagnostic only.
"""
from fractions import Fraction as Q
from itertools import product

checks = 0

def check(ok, message):
    global checks
    checks += 1
    assert ok, message


def h(t):
    return t*t*(3-2*t)/12


def sharp_variance(n, L):
    """Exact maximum on nondecreasing [0,1]-valued L-Lipschitz integrands."""
    L = Q(L)
    s = Q(n) * min(L, Q(1)) / L
    low = (s.numerator + s.denominator - 1) // s.denominator
    best = max((Q(L*L, n**4)*k*h(s/Q(k)), k) for k in range(max(1,low), n+1))
    return best


def cell_variance_of_ramp(n, L, delta):
    """Rational integration of a centered saturating ramp in a cell of length 1/n."""
    H = Q(1, n)
    w = delta / L
    assert 0 <= w <= H
    a = (H-w)/2
    # left plateau value 0, middle line from 0 to delta, right plateau delta
    mean = (w * delta/2 + a * delta) / H
    second = (w * delta*delta/3 + a * delta*delta) / H
    return second-mean*mean


def piecewise_variance(n, samples_per_cell, values):
    """Exact variance of one-per-cell estimator for a polygonal function."""
    m = samples_per_cell
    assert len(values) == n*m+1
    total = Q(0)
    for i in range(n):
        x = values[i*m:(i+1)*m+1]
        mu = sum((x[j]+x[j+1])/2 for j in range(m))/m
        mu2 = sum((x[j]**2+x[j]*x[j+1]+x[j+1]**2)/3 for j in range(m))/m
        total += (mu2-mu**2)/n**2
    return total


def optimize_integer_grid(n, L, m, increments):
    """Exhaust small polygonal monotone Lipschitz subclasses."""
    step = Q(L, n*m*increments)
    bound = Q(1)
    cap = int(bound / step)
    count = 0
    for diff in product(range(increments+1), repeat=n*m):
        if sum(diff) > cap:
            continue
        vals=[Q(0)]
        for v in diff:
            vals.append(vals[-1] + step*v)
        var=piecewise_variance(n, m, vals)
        check(var <= sharp_variance(n, L)[0], 'grid variance bound')
        count += 1
    return count


def main():
    # Algebraic two-coordinate exchange, exact with rational coefficients.
    for den in range(1,11):
        for i,j in product(range(den+1), repeat=2):
            a,b = Q(i,den),Q(j,den)
            v = h(a)+h(b)
            exchange = h(a+b) + (a+b-1)*a*b/2
            check(v == exchange, 'pairwise exchange identity')
            if a+b <= 1:
                check(v <= h(a+b), 'merge inequality')
            if a+b >= 1:
                check(v <= 2*h((a+b)/2), 'equalization inequality')
    # Cell-level equality of exact integrated ramp and variance envelope.
    for n in range(1,11):
        for L in (Q(1,2),Q(1),Q(4,3),Q(2),Q(5),Q(20)):
            for j in range(1,21):
                t=Q(j,20)
                delta = (L/n)*t
                got=cell_variance_of_ramp(n,L,delta)
                want=delta*delta*(Q(1,4)-t/6)
                check(got==want,'centered ramp equality')
    # Exact optimizer and its constructor across different regimes.
    for n in range(1,21):
        for L in (Q(1,3), Q(1), Q(11,10), Q(4,3), Q(3,2), Q(2), Q(7), Q(20), Q(100)):
            value,k=sharp_variance(n,L)
            delta=min(Q(1),L)/k
            t = delta*n/L
            check(t<=1, 'ramp feasible')
            check(value == Q(L*L,n**4)*k*h(t), 'constructor exact')
            check(k>=1 and k<=n,'active cell budget')
            if L<=1:
                check(k==n and value==L*L/(12*n**3),'linear low-L branch')
            if Q(1)<=L<=Q(4,3):
                check(k==n and value==(Q(1,4)-Q(1,6)/L)/n**3,'full active branch')
    # Exhaust a nontrivial finite-dimensional subclass of piecewise linear competitors.
    cases = [(2,Q(2),2,2),(3,Q(2),2,2),(3,Q(3,2),2,2),
             (3,Q(1),2,2),(4,Q(5,2),1,2)]
    for n,L,m,M in cases:
        num=optimize_integer_grid(n,L,m,M)
        check(num>0,'nonempty comparison class')
    print('PASS: %d exact-rational assertions' % checks)

if __name__=='__main__':
    main()
