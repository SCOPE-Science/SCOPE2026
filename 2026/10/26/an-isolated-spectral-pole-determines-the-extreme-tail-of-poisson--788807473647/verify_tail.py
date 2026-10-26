"""Independent numerical checks of rate-refresh Brownian-reset spectral law.
Uses the singularity equation, Stieltjes inversion, and direct Fourier transform.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import exp1, expi


def F(s,b):
    return math.exp(s/b)*exp1(s/b)/b


def params(mu,b,D):
    root=brentq(lambda s:mu*F(s,b)-1,1.e-12*min(1,mu,b),mu,xtol=1e-14)
    m2=1/(b*root)-F(root,b)/b # derivative: F'(s)= F(s)/b - 1/(b*s) ; -F'=1/(b*s)-F/b
    t=mu-root
    B=1/(mu*mu*m2)
    C=B*math.sqrt(t)/(2*math.sqrt(D))
    return root,t,B,C

def dens(a,mu,b):
    if a<=0: return 0.0
    u=a/b
    g=math.exp(-u)/b
    pv=-math.exp(-u)*expi(u)/b
    return g/((1-mu*pv)**2+(math.pi*mu*g)**2)

def integral(func,mu,b):
    return quad(lambda a:func(a)*dens(a,mu,b),0, min(80*b,400), epsabs=2e-11,epsrel=1e-10,limit=450,points=[1e-4*b,1e-2*b,b,10*b])[0]

def test(mu,b=1.,D=1.):
    s,t,B,C=params(mu,b,D)
    mass=B+integral(lambda a:1,mu,b)
    F0=F(mu,b)
    var_exact=2*D*F0/(1-mu*F0)
    var_spec=2*D*(B/t+integral(lambda a:1/(mu+a),mu,b))
    out=[]
    for k in [0.2,0.9,2.]:
        z=D*k*k
        direct=(1-(mu+z)*F(mu+z,b))/(1-mu*F(mu+z,b))
        spectrum=B*t/(t+z)+integral(lambda a:(mu+a)/(mu+a+z),mu,b)
        out.append((k,direct,spectrum))
        assert abs(direct-spectrum)<4e-8,(mu,k,direct,spectrum)
    assert abs(mass-1)<4e-8,(mu,mass)
    assert abs(var_exact-var_spec)<3e-8,(mu,var_exact,var_spec)
    # For x moderately large the strictly subleading continuum is negligible.
    vals=[]
    for x in [15.,30.,60.,120.]:
        tail=C*math.exp(-math.sqrt(t/D)*x)
        cont=integral(lambda a:math.sqrt(mu+a)/(2*math.sqrt(D))*math.exp(-math.sqrt((mu+a)/D)*x),mu,b)
        vals.append((x,cont/tail))
    assert vals[-1][1] < vals[0][1]
    print(f'mu={mu:.3g} b={b:.3g} D={D:.3g} s0={s:.12g} alpha={t:.12g} B={B:.12g} C={C:.12g} mass={mass:.12g} variance={var_exact:.12g}')
    print(' Fourier:',out,' continuum/pole:',vals)

if __name__=='__main__':
    for mu in [0.5,1.,3.]: test(mu)
    import mpmath as mp
    mp.mp.dps=80
    for m in ['0.5','0.3','0.2','0.1']:
        mu=mp.mpf(m);b=mp.mpf(1)
        f=lambda s:mu*mp.e**(s/b)*mp.e1(s/b)/b-1
        lo=b*mp.e**(-mp.euler-b/mu-1);hi=b*mp.e**(-mp.euler-b/mu+1)
        for _ in range(200):
            mid=(lo+hi)/2
            if f(mid)>0:lo=mid
            else:hi=mid
        s0=(lo+hi)/2
        appr=b*mp.e**(-mp.euler-b/mu)
        print('slow-refresh',m,'s0=',mp.nstr(s0,15),'asymptotic_ratio=',mp.nstr(s0/appr,13), 'true_tail_rate/tail_scale=',mp.nstr((mu-s0)/mu,13))
