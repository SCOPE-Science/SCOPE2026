"""Reproducibility checks for the affine-focus left flight-time law.

Requires SymPy; finite samples only supplement the analytic sign proof.
Run: python check_flight_time.py
"""
import math
import sympy as sp

z, d = sp.symbols('z d', real=True)
q = 1 + d*d
N = 1 - sp.exp(-d*z) * (sp.cos(z) + d*sp.sin(z))
M = sp.diff(N,z)*sp.sin(z) - 2*N*sp.cos(z)
K = 2*N - d*q*sp.exp(-d*z)*sp.sin(z)
assert sp.simplify(sp.diff(N,z) - q*sp.exp(-d*z)*sp.sin(z)) == 0
assert sp.simplify(sp.diff(M,z) - sp.sin(z)*K) == 0
assert sp.simplify(sp.diff(K,z) - q*sp.exp(-d*z)*((2+d*d)*sp.sin(z)-d*sp.cos(z))) == 0
assert sp.simplify(sp.limit(M/z**3,z,0) + d*(1+d*d)/3) == 0
assert sp.simplify(M.subs(z,sp.pi)-2*(1+sp.exp(-d*sp.pi))) == 0

for dd in (-3.0,-0.3,0.0,0.01,0.5,3.0,15.0):
    def n(t):return 1-math.exp(-dd*t)*(math.cos(t)+dd*math.sin(t))
    def mm(t):return (1+dd*dd)*math.exp(-dd*t)*math.sin(t)**2-2*n(t)*math.cos(t)
    vals=[mm(math.pi*j/1000) for j in range(1,1000)]
    if dd<=0:assert min(vals)>-1e-12,(dd,min(vals))
    else:
        assert vals[0]<0 and vals[-1]>0,dd
        s=[1 if v>0 else -1 for v in vals]
        assert sum(s[i]!=s[i-1] for i in range(1,len(s)))==1,dd
print('CHECK_OK')
