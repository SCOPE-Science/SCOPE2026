#!/usr/bin/env python3
"""Exact rational checks for the second-order point-mass Cesaro spectral limit.

This checks finite algebra and a certified first-root bracket; the analytic
convergence and differential boundary theorem require their written proof.
"""
from fractions import Fraction as Q
from math import factorial

checks = 0

def verify(flag, detail):
    global checks
    assert flag, detail
    checks += 1

# Characteristic coefficients, computed without any floating-point arithmetic.
# F(w)=sum a_n w^n, G(w)=sum b_n w^n, Delta=F^2-2w(FG'-F'G).
N = 16
a = [Q(1, factorial(n)**4) for n in range(N)]
harm = [sum((Q(1, k) for k in range(1, n + 1)), Q(0)) for n in range(N)]
b = [2 * harm[n] * a[n] for n in range(N)]
co = []
for k in range(N):
    p = sum((a[j] * a[k - j] for j in range(k + 1)), Q(0))
    d = sum(((k - 2*j) * a[j] * b[k-j] for j in range(k + 1)), Q(0))
    co.append(p - 2*d)
for k, known in enumerate([Q(1), Q(-2), Q(3,8), Q(-5,324),
                           Q(35,165888), Q(-7,5760000)]):
    verify(co[k] == known, ('Delta coefficient',k))
verify(co[1] == -16 * Q(1,8), 'first trace normalization')
verify(co[2] == Q(16**2,2) * (Q(1,8)**2-Q(13,1024)),
       'second trace normalization')

# A global bound on the coefficient tail for |w| <= 1:
# |[w^k] Delta| <= (1+4k^2)*16^k/(k!)^4.
# For k >= 16 the ratio of consecutive upper bounds is below 1/2,
# so the sum of absolute tail terms is at most twice the first bound.
T = N
bound = 2 * Q((1 + 4*T*T) * 16**T, factorial(T)**4)
verify(bound < Q(1,10**20), 'tail error')

def polynomial(w):
    return sum((c * w**k for k,c in enumerate(co)), Q(0))

lo, hi = Q(5568,10000), Q(5569,10000)
verify(polynomial(lo) > bound, 'positive first-root bracket endpoint')
verify(polynomial(hi) < -bound, 'negative first-root bracket endpoint')
# Derivative is strictly negative throughout 0<=w<=1, as even its
# maximum obtained by omitting negative terms is strictly below zero.
positive_derivative_bound = Q(-2) + Q(3,4) + sum(
    (k*co[k] for k in range(3,N) if co[k]>0), Q(0)) + Q(2*T)*bound
verify(positive_derivative_bound < 0, 'uniqueness on [0,1]')

# Two independent polynomial trace representations at each rational q.
for r in (Q(1,2), Q(2,3), Q(3,4), Q(5,6)):
    q = r*r
    A = (1+q)/(1-q)**3
    B = 1/(1-q)**2
    hs = (1+q)/(1-q)**4
    fourth1 = (q**6 + 4*q**5 + 13*q**4 + 16*q**3 +
               13*q**2 + 4*q + 1)/((1-q)**8*(1+q)**4)
    fourth2 = (A*A*(1+q*q)/(1-q*q) + 4*A*B*q*q/(1-q*q)**2 +
               2*B*B*q*q*(1+q*q)/(1-q*q)**3)/(1-q*q)
    verify(fourth1 == fourth2, ('fourth Schatten moment',r))
    verify(A/(1-q) == hs, ('Hilbert-Schmidt trace',r))
    for i in range(9):
        for j in range(9):
            # WW* is a finite sum in each pair of rows.
            finite = sum((r**(i+j)*(i-k+1)*(j-k+1)
                          for k in range(min(i,j)+1)), Q(0))
            m,M = min(i,j),max(i,j)
            closed = r**(i+j)*Q((m+1)*(m+2)*(3*M-m+3),6)
            verify(finite==closed, ('row Gram',r,i,j))
            # W*W sum in the infinite tail: explicitly split after L terms.
            d = abs(i-j)
            L = 9
            partial = sum((q**s*(s+1)*(s+d+1) for s in range(L)), Q(0))
            # Reindex the remainder s=L+t and use three geometric moments.
            tail = q**L * (
                Q((L+1)*(L+d+1),1)/(1-q) +
                Q(2*L+d+2,1)*q/(1-q)**2 +
                q*(1+q)/(1-q)**3)
            gram = q**max(i,j)*(partial+tail)
            expected = q**max(i,j)*(A+B*d)
            verify(gram==expected, ('column Gram',r,i,j))

# Limiting continuous Gram moments, independently integrated:
# trace Q=integral e^{-2x} x^3/3 dx=1/8,
# trace Q^2=1/8 integral e^{-4x} ((1+x)^3-1)/3 dx=13/1024.
cont_hs = Q(factorial(3),3*2**4)
cont_fourth = Q(1,24)*(Q(3,4**2)+Q(6,4**3)+Q(6,4**4))
verify(cont_hs==Q(1,8), 'continuous Hilbert-Schmidt moment')
verify(cont_fourth==Q(13,1024), 'continuous fourth moment')
print('CESARO2_HYPERGEOMETRIC_CHECK_OK', checks, 'exact rational assertions')
