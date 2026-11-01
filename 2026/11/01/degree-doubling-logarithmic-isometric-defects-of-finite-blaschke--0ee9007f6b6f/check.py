"""Independent finite consistency checks for the degree-doubling defect formula.

This script checks exact monomial projection coefficients and selected finite-
Blaschke angular means. Sampling does not establish spectral asymptotics.
Requires Python 3 standard library only.
"""
import cmath
import math

checks = 0

def check(condition, note):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(note)

# For the harmonic Bergman monomial shift, the defect of harmonicity has
# a positive squared norm and a summable inverse-square tail.
for m in range(1, 16):
    for j in range(1, 250):
        input_product_norm_sq = (j + 1) / (j + m + 1)
        if j < m:
            harmonic_component_norm_sq = (j + 1)*(m-j+1)/(m+1)**2
        else:
            harmonic_component_norm_sq = (j-m+1)/(j+1)
        gap = input_product_norm_sq-harmonic_component_norm_sq
        check(gap >= -1e-13, (m, j, 'negative gap'))
        if j >= m:
            expected = m*m/((j+1)*(j+m+1))
            check(abs(gap-expected) < 2e-13, (m,j,'tail identity'))
    # Exact bilateral monomial defect weights. Each tail has a 1/j law.
    for j in range(0, 500):
        w_plus_sq=(j+1)/(j+m+1)
        d_plus=1-w_plus_sq
        check(abs(d_plus-m/(j+m+1)) < 2e-13, ('plus',m,j))
        if j>=m:
            w_minus_sq=(j-m+1)/(j+1)
            d_minus=1-w_minus_sq
            check(abs(d_minus-m/(j+1)) < 2e-13, ('minus',m,j))

# Entire angular means of selected non-monomial finite Blaschke products.
# B(z)=(z^m-a)/(1-a*z^m) has degree m when 0<=a<1.
for m in (1, 2, 3, 5):
    for a in (0.0, 0.2, 0.6):
        for r in (0.05, 0.2, 0.6, 0.9, 0.99):
            nt=512
            avg=0.0
            for j in range(nt):
                z=r*cmath.exp(2*j*math.pi*1j/nt)
                zz=z**m
                b=(zz-a)/(1-a*zz)
                avg+=(1-abs(b)**2)/nt
            expected=(1-a*a)*(1-r**(2*m))/(1-a*a*r**(2*m))
            check(abs(avg-expected)<3e-12,(m,a,r,'mean'))
        # Numerical integration of the beta-series for diagonal Toeplitz elements.
        for n in (0,1,3,10,30,100,1000):
            val=(n+1)*(1-a*a)*sum((a*a)**k*(1/(n+m*k+1)-1/(n+m*(k+1)+1)) for k in range(200))
            check(0 < val < 1+1e-12,(m,a,n,'diagonal positivity'))
            if n>=100:
                check(abs((n+1)*val-m)< 0.13*m,(m,a,n,'limiting degree'))
        # Poisson-kernel integral: integral of |B'|/(2*pi) equals degree.
        nt=1024
        avgder=0.0
        for j in range(nt):
            t=2*math.pi*j/nt
            z=cmath.exp(1j*t)
            zz=z**m
            # Derivative of (z^m-a)/(1-a*z^m)
            derivative=m*(z**(m-1))*(1-a*a)/(1-a*zz)**2
            avgder+=abs(derivative)/nt
        check(abs(avgder-m)<1e-10,(m,a,'boundary winding'))

print(f'PASS {checks} finite consistency assertions')
