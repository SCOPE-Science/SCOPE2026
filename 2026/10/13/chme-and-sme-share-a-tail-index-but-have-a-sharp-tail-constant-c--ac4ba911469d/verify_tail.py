import mpmath as mp
mp.mp.dps=60

def R(q):
    q=mp.mpf(q)
    return 2**(-q)*mp.gamma(2*q)/(q*mp.gamma(q)**2)

def KC(beta,q):
    return (q+1)*2**(-q)*beta**q*mp.gamma(2*q)/mp.gamma(q)

def KS(beta,q):
    return beta**q*mp.gamma(q+2)

def S_chme(x,beta,q):
    # Stable transformed beta-mixture integral.
    L=2*x/beta
    pref=(beta/(2*x))**q/mp.beta(q,q)
    f=lambda t: t**(q-1)*(1-t/L)**(q-1)*(1+t)*mp.e**(-t)
    return pref*mp.quad(f,[0,1,L])

def S_sme(x,beta,q):
    L=x/beta
    pref=q*(beta/x)**q
    f=lambda t: t**(q-1)*(1+t)*mp.e**(-t)
    return pref*mp.quad(f,[0,1,L])

def f_chme(x,beta,q):
    L=2*x/beta
    pref=(beta/(2*x))**(q+1) * (2*x/beta**2) * 2 / mp.beta(q,q)
    # Equivalent stable transform of 4x/(beta^2 B) int z^(q+1)(1-z)^(q-1)e^-Lz dz.
    # Directly recompute with the exact Jacobian below for clarity.
    return (4*x/(beta**2*mp.beta(q,q))) * (1/L)**(q+2) * mp.quad(lambda t:t**(q+1)*(1-t/L)**(q-1)*mp.e**(-t), [0,1,L])

def f_sme(x,beta,q):
    return q*beta**q*x**(-q-1)*mp.gammainc(q+2,0,x/beta)

assert abs(R(1)-mp.mpf('0.5'))<mp.mpf('1e-50')
assert abs(R(2)-mp.mpf('0.75'))<mp.mpf('1e-50')
assert abs(R(3)-mp.mpf('1.25'))<mp.mpf('1e-50')
root=mp.findroot(lambda z:R(z)-1,(2,3))
assert abs(root-mp.mpf('2.578543315125812028114435005317918565533301907694649'))<mp.mpf('1e-47')

# Analytic derivative lower bound is positive on q>=1.
for q in (1,1.5,2,3,5,10):
    d=mp.log(2)+mp.digamma(q+mp.mpf('0.5'))-mp.digamma(q)-1/q
    assert d>0
    assert d >= mp.log(2)-1/(2*q)-mp.mpf('1e-50')

beta=mp.mpf('1.3')
for q,x,tol in [(mp.mpf('1'),mp.mpf('500'),mp.mpf('0.02')),
                (mp.mpf('2'),mp.mpf('300'),mp.mpf('0.03')),
                (mp.mpf('3'),mp.mpf('150'),mp.mpf('0.05'))]:
    sc=S_chme(x,beta,q); ss=S_sme(x,beta,q)
    assert abs(sc/(KC(beta,q)*x**(-q))-1)<tol
    assert abs(ss/(KS(beta,q)*x**(-q))-1)<tol
    assert abs((sc/ss)/R(q)-1)<2*tol
    hc=f_chme(x,beta,q)/sc
    hs=f_sme(x,beta,q)/ss
    assert abs(x*hc/q-1)<2*tol
    assert abs(x*hs/q-1)<2*tol

print('VERIFY_OK')
print('q_star',mp.nstr(root,40))
print('R1_R2_R3',mp.nstr(R(1),20),mp.nstr(R(2),20),mp.nstr(R(3),20))
