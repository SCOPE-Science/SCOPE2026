"""Reproducible numerical consistency checks for concentrated radial Bergman mass.
The theorem is proved analytically; these finite checks are not a root census.
Run: python checker.py (requires mpmath and sympy).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
u,v,A,B,C = sp.symbols('u v A B C')
k = sp.Rational(1,3) + A*u + B*u**2 + C*v
F = sp.Rational(1,4) - k/(1+k) + 4*k*u - 8*k*k*u*u - 9*k*v
sol = sp.solve([sp.diff(F,u).subs({u:0,v:0}),sp.diff(F,u,2).subs({u:0,v:0}),sp.diff(F,v).subs({u:0,v:0})],[A,B,C], dict=True)[0]
expected = {A:sp.Rational(64,27), B:sp.Rational(4736,243), C:-sp.Rational(16,3)}
assert sol == expected, (sol, expected)
print('symbolic_moment_coefficients',str(sol))


def moments(eps,profile,n):
    if n==0: return mp.mpf(1)
    if profile=='disk': return eps**n/(n+1)
    if profile=='radius_squared_density': return 2*eps**n/(n+2)
    if profile=='circle': return eps**n
    raise ValueError(profile)


def kernel(z,k,eps,profile,N=100):
    """Evaluate pi*K as classical rational term + absolutely convergent correction."""
    z=mp.mpc(z)
    out=(1-z)**(-2)-k/(1+k)
    for n in range(1,N+1):
        m=moments(eps,profile,n)
        h=k*(n+1)*m
        out-= (n+1)*h/(1+h)*z**n
    return out


def threshold(eps,profile):
    f=lambda k:mp.re(kernel(-1,k,eps,profile))
    k=mp.findroot(f,(mp.mpf('.3'),mp.mpf('.7')))
    assert abs(f(k))<mp.mpf('1e-45')
    return k

for profile in ['disk','radius_squared_density','circle']:
    for epsstring in ['0.010','0.005','0.0025']:
        eps=mp.mpf(epsstring)
        m1=moments(eps,profile,1)
        m2=moments(eps,profile,2)
        predicted=mp.mpf(1)/3+mp.mpf(64)/27*m1+mp.mpf(4736)/243*m1**2-mp.mpf(16)/3*m2
        critical=threshold(eps,profile)
        deviation=critical-predicted
        assert abs(deviation)<mp.mpf('200')*eps**3
        kval=critical+mp.mpf('0.008')
        root=mp.findroot(lambda t:mp.re(kernel(t,kval,eps,profile)),(-mp.mpf('.999'),-mp.mpf('.95')))
        assert -1<root<0 and abs(kernel(root,kval,eps,profile))<mp.mpf('1e-38')
        print('profile',profile,'eps',epsstring,
              'critical',mp.nstr(critical,20),
              'second_order_prediction',mp.nstr(predicted,20),
              'scaled_third_order_remainder',mp.nstr(deviation/eps**3,10),
              'supercritical_negative_root',mp.nstr(root,20))

# An independent integral check of radial moments for the piecewise constant bump.
eps=mp.mpf('0.02'); k=mp.mpf('0.45')
for n in range(5):
    radial_norm=2*mp.pi*(mp.quad(lambda r: r**(2*n+1)*(1+k/eps), [0,mp.sqrt(eps)])
                         +mp.quad(lambda r: r**(2*n+1),[mp.sqrt(eps),1]))
    predicted_norm=mp.pi/(n+1)*(1+k*eps**n)
    assert mp.almosteq(radial_norm,predicted_norm,rel_eps=mp.mpf('1e-50'))
print('direct_radial_norm_checks',5,'PASS')
print('all_checks_passed')
