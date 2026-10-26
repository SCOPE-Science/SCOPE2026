"""Numerical reproducibility checks for critical two-time memory under Poisson resetting.

Runs with mpmath (version-independent standard functions) and verifies direct
stationary-age quadrature against independently evaluated analytic formulas.
"""
import mpmath as mp
mp.mp.dps = 45


def flow(sigma, coupling, initial, t):
    alpha = sigma - coupling / 2
    beta = coupling / 2
    if alpha > 0:
        return initial * mp.exp(-alpha*t) / mp.sqrt(1 + beta*initial**2/alpha * (-mp.expm1(-2*alpha*t)))
    if alpha < 0:
        equilibrium = mp.sqrt(-alpha / beta)
        return equilibrium / mp.sqrt(1 + (equilibrium**2/initial**2 - 1)*mp.exp(2*alpha*t))
    return initial / mp.sqrt(1 + 2*beta*initial**2*t)


def stationary_integral(reset_rate, F):
    return mp.quad(lambda a: reset_rate*mp.exp(-reset_rate*a)*F(a), [0, 1, 4, 16, mp.inf])


def reduced_covariance(sigma, coupling, initial, reset_rate, lag):
    F = lambda a: flow(sigma, coupling, initial, a)
    m = stationary_integral(reset_rate, F)
    # Center both factors before integration to avoid subtracting close terms.
    return stationary_integral(reset_rate, lambda a: (F(a)-m)*F(a+lag))


def asymptotic_coefficient(sigma, coupling, initial, reset_rate):
    a = sigma-coupling/2
    F = lambda x: flow(sigma, coupling, initial, x)
    if a > 0:
        k = a
        B = initial/mp.sqrt(1 + coupling*initial**2/(2*a))
    elif a < 0:
        k = -2*a
        q = mp.sqrt(-2*a/coupling)
        B = q*(1-q*q/initial**2)/2
    else:
        z = reset_rate/(2*sigma*initial**2)
        return mp.exp(z)*((z+1)*mp.gammainc(mp.mpf('0.5'), z) - mp.gammainc(mp.mpf('1.5'), z))/(4*sigma*mp.sqrt(reset_rate)), mp.mpf('0')
    m = stationary_integral(reset_rate,F)
    cov_e = stationary_integral(reset_rate, lambda x: (F(x)-m)*mp.exp(-k*x))
    return B*cov_e, k


def close(a,b,tolerance):
    assert abs(a-b) < tolerance * max(abs(a),abs(b),mp.mpf('1e-30')), (a,b)


def run():
    checks=0
    for sigma,coupling,initial,r in [(1,0,.8,.9), (1,1,.8,.9), (1,3,.8,.7), (1,3,.3,.7), (1,2,.8,.7)]:
        sigma,coupling,initial,r=map(mp.mpf, (str(sigma),str(coupling),str(initial),str(r)))
        F=lambda x:flow(sigma,coupling,initial,x)
        close(F(0),initial,mp.mpf('1e-38')); checks+=1
        for t in [mp.mpf('0.25'),mp.mpf('2'),mp.mpf('5')]:
            close(mp.diff(F,t), -(sigma-coupling/2)*F(t) - coupling/2*F(t)**3,mp.mpf('1e-35')); checks+=1
        coef,k=asymptotic_coefficient(sigma,coupling,initial,r)
        assert coef>0; checks+=1
        if coupling==2*sigma:
            m=stationary_integral(r,F)
            cov_a=stationary_integral(r,lambda x:(F(x)-m)*x)
            other=-cov_a/(2*mp.sqrt(2*sigma))
            close(coef,other,mp.mpf('1e-35')); checks+=1
            for lag, eps in [(30,.14),(100,.045),(300,.016)]:
                ratio=reduced_covariance(sigma,coupling,initial,r,mp.mpf(lag)) * mp.power(lag,mp.mpf('1.5'))/coef
                print('critical',lag,mp.nstr(ratio,12))
                assert abs(ratio-1)<eps;checks+=1
        else:
            for lag,eps in [(10,.008),(25,.0001)]:
                ratio=reduced_covariance(sigma,coupling,initial,r,mp.mpf(lag))*mp.exp(k*lag)/coef
                print('offcritical',mp.nstr(coupling,2), mp.nstr(initial,2),lag,mp.nstr(ratio,12))
                assert abs(ratio-1)<eps;checks+=1
    print('PASSED',checks,'deterministic independent checks')

if __name__=='__main__':run()
