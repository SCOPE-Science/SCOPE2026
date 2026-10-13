import mpmath as mp
mp.mp.dps = 80

def cdf_loglr(x, alpha, beta, lam):
    FR = 1-mp.e**(-x*x/(2*lam*lam))
    return (beta/(beta-mp.log(FR)))**alpha

def x_of_t(t, lam):
    return lam*mp.sqrt(-2*mp.log(1-mp.e**(-t)))

def logJ(t, lam):
    L = -mp.log1p(-mp.e**(-t))
    return mp.log(lam) - mp.log(mp.expm1(t)) - mp.mpf('0.5')*mp.log(2*L)

def ft(t, alpha, beta):
    return alpha*beta**alpha/(beta+t)**(alpha+1)

# Exact transform identity at separated parameter choices.
for alpha,beta,lam in [(mp.mpf('0.8'),mp.mpf('0.5'),mp.mpf('2.0')),
                       (mp.mpf('1.7'),mp.mpf('1.2'),mp.mpf('0.7'))]:
    for t in [mp.mpf('0.02'),mp.mpf('0.3'),mp.mpf('2'),mp.mpf('20')]:
        x=x_of_t(t,lam)
        lhs=cdf_loglr(x,alpha,beta,lam)
        rhs=(beta/(beta+t))**alpha
        assert abs(lhs-rhs) < mp.mpf('1e-45')

# Tail slope of the log-Jacobian.
for t in [mp.mpf('40'), mp.mpf('80'), mp.mpf('120')]:
    assert abs(logJ(t, mp.mpf('1.3'))/t + mp.mpf('0.5')) < mp.mpf('0.02')

# Finite-regime exact expectations.
alpha=mp.mpf('1.7'); beta=mp.mpf('0.8')
ET=mp.quad(lambda t: t*ft(t,alpha,beta), [0,1, mp.inf])
EL=mp.quad(lambda t: mp.log(beta+t)*ft(t,alpha,beta), [0,1, mp.inf])
assert abs(ET-beta/(alpha-1)) < mp.mpf('1e-35')
assert abs(EL-(mp.log(beta)+1/alpha)) < mp.mpf('1e-35')

# Truncated log-Jacobian expectations move downward in the divergent regimes.
def trunc(alpha,beta,R):
    return mp.quad(lambda t: logJ(t,1)*ft(t,alpha,beta), [0,1,R])
for alpha in [mp.mpf('0.8'), mp.mpf('1.0')]:
    a=trunc(alpha,1,20)
    b=trunc(alpha,1,100)
    c=trunc(alpha,1,500)
    assert c < b < a

print('VERIFY_OK')
