"""Numerical diagnostics for Fourier transforms of Beta densities.
Run: python checker.py. Requires mpmath >=1.2.
"""
import mpmath as mp
mp.mp.dps=55

def H(t,p,q):
    return mp.exp(-1j*t)*mp.hyp1f1(p,p+q,2j*t)

def Hp(t,p,q):
    m=p+q
    return 1j*mp.exp(-1j*t)*(2*p/m*mp.hyp1f1(p+1,m+1,2j*t)-mp.hyp1f1(p,m,2j*t))

def check_wronskian(p,q,t):
    p,q,t=map(mp.mpf,(p,q,t));m=p+q;delta=p-q
    h=H(t,p,q); dh=Hp(t,p,q)
    actual=mp.im(dh*mp.conj(h))
    integral=mp.quad(lambda s:s**(m-1)*abs(H(s,p,q))**2,[0,t])
    expected=delta*t**(-m)*integral
    assert mp.almosteq(actual,expected,rel_eps=mp.mpf('1e-35')), (actual,expected)
    return abs(h), actual, expected

def check_displacement(mu,k,eps=mp.mpf('0.0002')):
    mu=mp.mpf(mu);eps=mp.mpf(eps);m=2*mu
    nu=mu-mp.mpf('0.5')
    j=mp.besseljzero(nu,k)
    h0=lambda t:H(t,mu,mu)
    hp0=Hp(j,mu,mu)
    I=mp.quad(lambda s:s**(m-1)*h0(s)**2,[0,j])
    C=mp.re(I/(j**m*hp0**2))
    assert C>0
    sol=mp.findroot(lambda z:H(z,mu+eps/2,mu-eps/2),j+1j*eps*C, tol=mp.mpf('1e-47'))
    drift=mp.im(sol)/eps
    assert abs(drift/C-1)<mp.mpf('0.002'),(drift,C)
    assert abs(mp.re(sol)-j)<mp.mpf('0.002')
    assert abs(H(sol,mu+eps/2,mu-eps/2))<mp.mpf('1e-40')
    return j,C,drift

if __name__=='__main__':
    print('Wronskian identity:')
    for p,q,t in [(1,2,2),(1.5,3,7),(0.7,2.4,11),(3,1,15),(2.5,2.5,8)]:
       mag,act,exp=check_wronskian(p,q,t)
       print(' p,q,t = ',p,q,t,' |H| = ',mp.nstr(mag,14),' Im(Hp conj H) = ',mp.nstr(act,14))
    print('Complex-zero displacement as asymmetry vanishes:')
    for mu,k in [(1,1),(1,3),(2,2),(0.65,2)]:
       j,C,drift=check_displacement(mu,k)
       print(' symmetric p = ',mu,' zero index=',k,' j=',mp.nstr(j,13),' slope=',mp.nstr(C,13),' observed=',mp.nstr(drift,13))
    print('All diagnostics passed.')
