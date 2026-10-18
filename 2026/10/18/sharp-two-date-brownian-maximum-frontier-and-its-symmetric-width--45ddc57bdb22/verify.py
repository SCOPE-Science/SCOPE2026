"""Numerical cross-checks for a two-date Brownian-maximum stopping frontier.

Uses mpmath. The analytic argument is in RESULT.md; these finite
checks are not substitutes for proofs of statements over all parameters.
"""
import mpmath as mp
mp.mp.dps = 48
checks = 0

def near(a,b,tol=mp.mpf('1e-30')):
    global checks
    assert abs(a-b) <= tol*(1+abs(a)+abs(b)), (a,b)
    checks += 1

def core(a,b):
    h=b-a
    ca=mp.sqrt(2*a/mp.pi)
    cb=mp.sqrt(2*b/mp.pi)
    f=lambda d:mp.sqrt(2/(mp.pi*a))*mp.exp(-d*d/(2*a))
    G=lambda d: mp.sqrt(2*h/mp.pi)*mp.exp(-d*d/(2*h))-d*mp.erfc(d/mp.sqrt(2*h))
    H=lambda z: cb*mp.erf(z*mp.sqrt(b/(2*a*h))) + ca*mp.exp(-z*z/(2*a))*mp.erfc(z/mp.sqrt(2*h))
    F=lambda d:mp.erf(d/mp.sqrt(2*a))
    Q=lambda p:mp.sqrt(2*a)*mp.erfinv(p)
    near(H(0),ca)
    for z in [mp.mpf('0.05'),mp.mpf('0.3'),mp.mpf('1.0'),mp.mpf('2.7')]:
        near(H(z)-ca, mp.quad(lambda x:f(x)*G(x),[0,z]))
        near(mp.diff(H,z),f(z)*G(z))
        near(F(z),mp.quad(f,[0,z]))
        checks_approx = G(z)
        assert 0 < checks_approx < mp.sqrt(2*h/mp.pi)
    for q in [mp.mpf('.01'),mp.mpf('.1'),mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),mp.mpf('.9'),mp.mpf('.99')]:
        u=Q(1-q)
        v=Q(q)
        upper=H(u)
        lower=ca+cb-H(v)
        near(upper,ca+mp.quad(lambda x:f(x)*G(x),[0,u]))
        near(lower,ca+mp.quad(lambda x:f(x)*G(x),[v, mp.inf]),mp.mpf('1e-25'))
        near(F(u),1-q)
        near(F(v),q)
        assert ca<lower<upper<cb
        linear=q*ca+(1-q)*cb
        assert lower<linear<upper
        near(upper+H(v), ca+cb+(upper-lower))
    return H,ca,cb

for aa,bb in [('1','2'),('1','4'),('.3','.8'),('3','5'),('.2','10')]:
    core(mp.mpf(aa),mp.mpf(bb))

a=mp.mpf(1); b=mp.mpf(2)
H,ca,cb=core(a,b)
q=mp.mpf('.5');u=mp.sqrt(2*a)*mp.erfinv(1-q);v=mp.sqrt(2*a)*mp.erfinv(q)
upper=H(u);lower=ca+cb-H(v)
near(upper,mp.mpf('1.0623396438887271'), mp.mpf('1e-16'))
near(lower,mp.mpf('0.8639240840096509'), mp.mpf('1e-16'))
near(upper-lower,mp.mpf('0.19841555987907644'), mp.mpf('1e-16'))
print('PASS:',checks,'high-precision identity checks; strict inequalities across 42 cases; reference case:',mp.nstr(upper,18),mp.nstr(lower,18))
