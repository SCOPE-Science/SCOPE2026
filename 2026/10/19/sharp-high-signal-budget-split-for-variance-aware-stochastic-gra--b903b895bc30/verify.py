"""Numerical cross-checks for exact two-stage oracle-gradient minibatch risk.

Requires mpmath (tested with 1.3.0). These tests supplement, not replace,
the analytic proof in RESULT.md. Execute with: python verify.py
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 55
count = 0

def check(cond, message):
    global count
    if not cond:
        raise AssertionError(message)
    count += 1

def f(batch, s, v):
    return v * s / (v + batch * s)

# Exact composition at a variety of rational parameters.
for b in range(1, 15):
    for c in range(1, 12):
        for numer in (1, 2, 5, 17):
            s, v = Fraction(numer, 7), Fraction(11, 3)
            check(f(b, f(c, s, v), v) == f(b + c, s, v),
                  'exact one-step risk map composition')

# Deterministic evaluation of the chi-square spectral-risk integral.
def ratio(d, t):
    a = mp.mpf(d) / 2
    t = mp.mpf(t)
    norm = a**a / mp.gamma(a)
    density = lambda q: norm * q**(a-1) * mp.exp(-a*q)
    return (1+t) * mp.quad(lambda q: q/(q+t) * density(q),
                            [0, 1, mp.inf])

def tilted(d, t):
    a = mp.mpf(d) / 2
    t = mp.mpf(t)
    density = lambda q: a**a / mp.gamma(a) * q**(a-1) * mp.exp(-a*q)
    z = mp.quad(lambda q: q / (q+t)**2 * density(q), [0, 1, mp.inf])
    m = mp.quad(lambda q: q*q / (q+t)**2 * density(q), [0, 1, mp.inf])
    return m/z

k = lambda t: mp.sqrt(mp.pi/(2*t)) * mp.exp(t/2) * mp.erfc(mp.sqrt(t/2))
explicit_ratio = lambda t: (1+t)*(1-t*k(t))
root = mp.findroot(lambda t: (t+3) - (t*t+4*t+1)*k(t), (.5, .8))
check(abs(root-mp.mpf('0.604867542154887602248340196450407322274728952022582')) < mp.mpf('1e-43'), 'sharp batch ratio')
check(abs(explicit_ratio(root)-mp.mpf('0.680415310037752291779444651416338069499722050371128')) < mp.mpf('1e-43'), 'sharp normalized risk')
for t in ('0.1','0.35','0.6048675421548876','1','3','10'):
    t = mp.mpf(t)
    check(abs(ratio(1,t)-explicit_ratio(t)) < mp.mpf('1e-42'), 'chi-square/erfc equivalence')
    dr = ((t+3)-(t*t+4*t+1)*k(t))/2
    numdr = mp.diff(explicit_ratio, t)
    check(abs(dr-numdr) < mp.mpf('1e-42'), 'derivative identity')
for d in range(1, 8):
    for t in (mp.mpf('0.2'),mp.mpf('0.6'),mp.mpf('1'),mp.mpf('3')):
        rd=ratio(d,t)
        check(0 < rd < 1, 'strict Gaussian adaptation benefit')
        if d>1:
            check(rd>ratio(d-1,t), 'dimension monotonicity')
for d in (1,2,3,5):
    check(tilted(d, mp.mpf('0.000001')) < 1, 'low allocation derivative')
    check(tilted(d, mp.mpf('1000000')) > 1, 'high allocation derivative')
for d in (1,2,3,5,10):
    ratios = [ratio(d, mp.mpf(t)) for t in ('0.2','0.6','1','3')]
    check(min(ratios)<1,'finite strict optimal split')

# Exact two-stage Gaussian integration in 1D; check strict finite-signal
# advantage over combining both independent gradients into a single block.
normal = lambda z: mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
for b1,b2 in ((1,1),(1,2),(2,1)):
    for s in (mp.mpf('0.1'),mp.mpf('1'),mp.mpf('20')):
        alpha = b1*s/(b1*s+1)
        f2 = lambda z: f(b2, ((1-alpha)*mp.sqrt(s)-alpha*z/mp.sqrt(b1))**2, mp.mpf(1))
        twostep = mp.quad(lambda z: f2(z)*normal(z),[-mp.inf,0,mp.inf])
        pooled = f(b1+b2,s,mp.mpf(1))
        check(twostep<pooled, 'two blocks strictly improve fixed-budget MSE')

print('PASS:',count,'deterministic checks')
print('optimal dimension-one first/second sample ratio:',mp.nstr(root,28))
print('sharp high-signal two-stage/pooled MSE ratio:',mp.nstr(explicit_ratio(root),28))
print('maximum relative high-signal gain:',mp.nstr(1-explicit_ratio(root),28))
