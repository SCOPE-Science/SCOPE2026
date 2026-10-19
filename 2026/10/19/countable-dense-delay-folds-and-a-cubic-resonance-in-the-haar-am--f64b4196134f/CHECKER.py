"""Reproducible high-precision checks for an exact Haar ambiguity zero theorem.

Run: python3 CHECKER.py  (requires mpmath)
Numerical checks corroborate, but do not replace, the analytic proof.
"""
from mpmath import mp
mp.dps = 70

def A_piecewise(delay, nu):
    t=abs(mp.mpf(delay)); v=mp.mpf(nu)
    if t>=2: return mp.mpf(0)
    if abs(v)<mp.mpf('1e-50'):
        return (2-3*t) if t<=1 else -(2-t)
    if t<=1:
        return (mp.sin(mp.pi*v*(2-t))-2*mp.sin(mp.pi*v*t))/(mp.pi*v)
    return -mp.sin(mp.pi*v*(2-t))/(mp.pi*v)

def integrate_segments(delay, nu):
    t=abs(mp.mpf(delay)); v=mp.mpf(nu)
    if t>=2: return mp.mpf(0)
    def integral(a,b):
        if a>=b: return mp.mpf(0)
        if v == 0: return b-a
        return (mp.exp(-2*mp.pi*1j*v*a)-mp.exp(-2*mp.pi*1j*v*b))/(2*mp.pi*1j*v)
    left=-1+t/2; right=1-t/2
    if t>=1: return -integral(left,right)
    return integral(left,-t/2)-integral(-t/2,t/2)+integral(t/2,right)

samples=[('0.21','0.19'),('0.43','1.7'),('0.666666666666666666','3'),('0.91','2.6'),('1.33','1.8'),('1.77','5.1'),('0.666666666666666666','0')]
for tau,nu in samples:
    diff=abs(A_piecewise(tau,nu)-integrate_segments(tau,nu))
    assert diff<mp.mpf('1e-55'), (tau,nu,diff)
print('Direct piecewise Fourier integrals: passed',len(samples))

def f(r,T): return mp.sin(r*T)-2*mp.sin(T)
def ft(r,T): return r*mp.cos(r*T)-2*mp.cos(T)
def ftt(r,T): return -r*r*mp.sin(r*T)+2*mp.sin(T)
def fr(r,T): return T*mp.cos(r*T)

seeds=[('2.913253','3.53905'),('2.326348','9.71154'),('3.0','6.5'),('4.0','5.5')]
found=[]
for a,b in seeds:
    try:
        r,T=mp.findroot((f,ft), (mp.mpf(a),mp.mpf(b)), solver='mdnewton', tol=mp.mpf('1e-60'), maxsteps=60)
    except (ValueError,ZeroDivisionError):
        continue
    if r>2 and T>0 and abs(f(r,T))<mp.mpf('1e-55') and abs(ft(r,T))<mp.mpf('1e-55'):
        assert abs(ftt(r,T))>mp.mpf('1e-15')
        assert abs(fr(r,T))>mp.mpf('1e-15')
        if all(abs(r-x[0])>mp.mpf('1e-15') for x in found): found.append((r,T))
assert len(found)>=2, found
for r,T in found:
    tau=2/(r+1)
    nu=T/(mp.pi*tau)
    assert 0<tau<mp.mpf(2)/3
    assert abs(A_piecewise(tau,nu))<mp.mpf('1e-50')
print('Distinct nondegenerate double-zero folds:',len(found))
for r,T in found: print('r=',mp.nstr(r,22),'T=',mp.nstr(T,22),'delay=',mp.nstr(2/(r+1),22),'freq=',mp.nstr(T/(mp.pi*(2/(r+1))),22))

# At delay 2/3, the cubic vanishing at nonzero nu=3*k is exact by
# the factorization 2*sin(T)*(cos(T)-1), T=2*pi*nu/3.
t=mp.mpf(2)/3
for k in [1,2,3,4,6]:
    nu=3*k
    assert abs(A_piecewise(t,nu))<mp.mpf('1e-65')
    # The sine numerator F(T) has vanishing derivatives 0,1,2;
    # its third derivative at T=2*pi*k is -6.
    T=2*mp.pi*k
    assert abs(f(2,T))<mp.mpf('1e-60')
    assert abs(ft(2,T))<mp.mpf('1e-60')
    assert abs(ftt(2,T))<mp.mpf('1e-60')
    third=-(2**3)*mp.cos(2*T)+2*mp.cos(T)
    assert abs(third+6)<mp.mpf('1e-60')
print('Exact-factor cubic resonance checks: passed 5')
print('All checks passed.')
