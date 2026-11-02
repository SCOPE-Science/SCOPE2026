"""Finite consistency tests for Jacobi origin asymptotics and derivative identities.
No finite test is used as an infinite proof.
Requires numpy and scipy; run: python CHECK.py
"""
import math
from scipy.special import eval_jacobi, gammaln
CASES = [(0.0, 0.0), (0.25, -0.2), (-0.3, 1.1), (-0.9, -0.9), (0.5, 0.5), (0.5, 1.0), (0.5, 2.5)]
checks = 0
for a,b in CASES:
    delta = math.pi*(b-a)/4
    amp = 2**((a+b+1)/2)/math.sqrt(math.pi)
    for n in (49,50,51,52,101,102,103,104,401,402,403,404):
        p0 = float(eval_jacobi(n,a,b,0.0))
        d = (n+a+b+1)/2*float(eval_jacobi(n-1,a+1,b+1,0.0))
        p1 = float(math.exp(gammaln(n+a+1)-gammaln(n+1)-gammaln(a+1)))
        d_alt = (float(eval_jacobi(n,a,b,1e-5))-float(eval_jacobi(n,a,b,-1e-5)))/(2e-5)
        assert abs(d-d_alt) <= 3e-5*max(1,abs(d)), (a,b,n,d,d_alt)
        checks += 1
        approx_d = amp*math.sqrt(n)*math.sin(n*math.pi/2+delta)
        assert abs(d-approx_d) <= 6.5/math.sqrt(n), (a,b,n,d,approx_d)
        checks += 1
        approx_p0 = amp*math.cos(n*math.pi/2+delta)/math.sqrt(n)
        assert abs(p0-approx_p0) <= 4.0/n**1.5, (a,b,n,p0,approx_p0)
        checks += 1
        e = p1-p0-d
        if a<.5 and n>=401 and math.sin(n*math.pi/2+delta)>0.5:
            assert e<0, (a,b,n,e)
            checks += 1
assert 2**((2.5-.5)/2)/math.sqrt(2)>1
checks += 1
print(f'JACOBI_ORIGIN_CHECKS_OK {checks}')
