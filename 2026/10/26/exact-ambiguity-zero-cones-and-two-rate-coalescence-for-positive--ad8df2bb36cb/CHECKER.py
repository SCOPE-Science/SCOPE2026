"""Numerical checks for the Gaussian-width ambiguity-zero cone theorem.

Requires mpmath. The analytic proof, not this finite computation,
establishes all quantified statements.
"""
import mpmath as mp

mp.mp.dps = 55


def params(p, q, c):
    assert 0 < p < q and c > 0
    h = (q-p)/(4*(p+q))
    kappa = 2*h
    a = mp.sqrt((p+q)/(8*p))/c
    b = c*mp.sqrt((p+q)/(8*q))
    return h, kappa, a, b


def exact_ambiguity(p, q, c, T, w):
    d1 = mp.sqrt(mp.pi/p)*mp.exp(-p*T*T/4-w*w/(4*p))
    d2 = c*c*mp.sqrt(mp.pi/q)*mp.exp(-q*T*T/4-w*w/(4*q))
    cross = 2*c*mp.sqrt(2*mp.pi/(p+q))*mp.exp(-p*q*T*T/(2*(p+q))-w*w/(2*(p+q)))
    return d1+d2+cross*mp.cos((q-p)*T*w/(2*(p+q)))


def factored(p, q, c, T, w):
    h, kappa, a, b = params(p, q, c)
    base = 2*c*mp.sqrt(2*mp.pi/(p+q))*mp.exp(-p*q*T*T/(2*(p+q))-w*w/(2*(p+q)))
    ratio = a*mp.exp(h*(p*T*T-w*w/p))+b*mp.exp(h*(-q*T*T+w*w/q))
    return base*(mp.cos(kappa*T*w)+ratio)


def first_zero_balanced(p, q, c):
    h, kappa, a, b = params(p, q, c)
    beta = kappa*mp.sqrt(p*q)
    delta = (q-p)**2/(4*(p+q))
    B = a+b
    tstart = mp.log(B)/delta
    # The first cosine minimum at or after the necessary amplitude threshold.
    k = int(mp.ceil((beta*tstart/mp.pi-1)/2))
    k = max(k, 0)
    tmin = (2*k+1)*mp.pi/beta
    if tmin < tstart:
        tmin += 2*mp.pi/beta
    fun = lambda t: mp.cos(beta*t)+B*mp.exp(-delta*t)
    assert fun(tstart) >= -mp.mpf('1e-45')
    assert fun(tmin) < 0
    # The first root can be earlier in the same cycle, but lies in this interval.
    root = mp.findroot(fun, (tstart, tmin), solver='anderson', verify=False)
    return root, tstart, 2*mp.pi/beta


def main():
    for p, q, c, T, w in [(mp.mpf('1'), mp.mpf('4'), mp.mpf('.3'), mp.mpf('1.1'), mp.mpf('2.2')),
                           (mp.mpf('2'), mp.mpf('5'), mp.mpf('1.7'), mp.mpf('.6'), mp.mpf('3.1')),
                           (mp.mpf('.7'), mp.mpf('1.8'), mp.mpf('.8'), mp.mpf('1.9'), mp.mpf('.6'))]:
        g = lambda t: mp.exp(-p*t*t/2)+c*mp.exp(-q*t*t/2)
        integrand = lambda t: g(t+T/2)*g(t-T/2)*mp.cos(w*t)
        direct = mp.quad(integrand, [-mp.inf, 0, mp.inf])
        form = exact_ambiguity(p, q, c, T, w)
        fact = factored(p, q, c, T, w)
        assert abs(direct-form) < mp.mpf('1e-45')
        assert abs(fact-form) < mp.mpf('1e-45')
    print('PASS: three independent ambiguity-integral checks')

    p=mp.mpf('1');q=mp.mpf('4');c=mp.mpf('.25');r=mp.mpf('2')
    h,kappa,a,b=params(p,q,c)
    beta=kappa*r
    d1=h*(r*r-p*p)/p
    d2=h*(q*q-r*r)/q
    for k in [3,5,8,12]:
        t0=(k+mp.mpf('.5'))*mp.pi/beta
        R=lambda t:a*mp.exp(-d1*t)+b*mp.exp(-d2*t)
        f=lambda t:mp.cos(beta*t)+R(t)
        t=mp.findroot(f,(t0-mp.mpf('.1'),t0+mp.mpf('.1')))
        assert abs(f(t))<mp.mpf('1e-45')
        predicted=(-1)**k*R(t0)
        error=abs(beta*(t-t0)-predicted)
        assert error < 100*R(t0)**2
        assert abs(exact_ambiguity(p,q,c,mp.sqrt(t),r*mp.sqrt(t))) < mp.mpf('1e-35')
    print('PASS: four simple-ray roots and exponentially precise phase corrections')

    # Endpoint-ray coefficient thresholds are exact identities.
    for c in map(mp.mpf,['.25','1','4']):
        _,_,a,b=params(p,q,c)
        assert (a<1)==(c>mp.sqrt((p+q)/(8*p)))
        assert (b<1)==(c<mp.sqrt(8*q/(p+q)))
    print('PASS: both sharp endpoint-ray weight inequalities')

    # Coalescing-width singular-perturbation limits. A root is bracketed
    # analytically by tstart and the next oscillatory minimum.
    for c in [mp.mpf('1'),mp.mpf('2')]:
        eps=mp.mpf('.005');q=p+eps
        root,start,width=first_zero_balanced(p,q,c)
        assert root >= start- mp.mpf('1e-20')
        assert root <= start+width+mp.mpf('1e-20')
        if c==1:
            quantity=eps*root
            assert abs(quantity-4*mp.pi) < mp.mpf('1')
            print('equal-amplitude: epsilon*T_first^2 =',mp.nstr(quantity,16),'limit',mp.nstr(4*mp.pi,16))
        else:
            quantity=eps**2*root
            target=8*p*mp.log((c+1/c)/2)
            assert abs(quantity-target)<mp.mpf('.15')
            print('unequal-amplitude: epsilon^2*T_first^2 =',mp.nstr(quantity,16),'limit',mp.nstr(target,16))
    print('PASS: all finite numerical checks')

if __name__=='__main__':
    main()
