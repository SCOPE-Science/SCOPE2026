"""Alternative checks for joint Shannon--quadratic concentration Dirichlet covariance.
Uses raw gamma mixed-moment differentiation, independent quadrature (K=2),
and finite perturbation curvature. These are finite checks, not proof.
"""
from math import isfinite
import itertools
import mpmath as mp
mp.mp.dps = 55

def closed(alpha):
    a = [mp.mpf(x) for x in alpha]
    A=sum(a); k=len(a)
    w=[z/A for z in a]
    m=sum(wi*ai for wi,ai in zip(w,a))
    pm=sum(wi*mp.digamma(ai+1) for wi,ai in zip(w,a))
    weighted_cov=sum(wi*(ai-m)*(mp.digamma(ai+1)-pm) for wi,ai in zip(w,a))
    return -(A*A-sum(x*x for x in a))/(A*(A+1)**2*(A+2))-2*weighted_cov/((A+1)*(A+2))

def raw_moments(alpha):
    a=[mp.mpf(x) for x in alpha]; A=sum(a); k=len(a)
    E_Q=sum(x*(x+1) for x in a)/(A*(A+1))
    E_H=mp.digamma(A+1)-sum(x*mp.digamma(x+1) for x in a)/A
    cross=mp.mpf('0')
    for i in range(k):
        for j in range(k):
            if i==j:
                v=a[i]*(a[i]+1)*(a[i]+2)/(A*(A+1)*(A+2))
                q=mp.digamma(a[j]+3)-mp.digamma(A+3)
            else:
                v=a[i]*(a[i]+1)*a[j]/(A*(A+1)*(A+2))
                q=mp.digamma(a[j]+1)-mp.digamma(A+3)
            cross -=v*q
    return cross-E_H*E_Q

def integral2(alpha):
    a,b=map(mp.mpf,alpha)
    norm=mp.beta(a,b)
    def f(x):
        y=1-x
        H=-x*mp.log(x)-y*mp.log(y)
        Q=x*x+y*y
        return H,Q,H*Q
    terms=[]
    for j in range(3):
        terms.append(mp.quad(lambda x: x**(a-1)*(1-x)**(b-1)*f(x)[j],
                             [mp.mpf('0'),mp.mpf('.13'),mp.mpf('.37'),mp.mpf('.7'),mp.mpf('1')])/norm)
    return terms[2]-terms[0]*terms[1]

checks=0
for alpha in ([1,1],[2,3],[mp.mpf('.4'),mp.mpf('1.7')],
              [mp.mpf('.17'),mp.mpf('.21'),mp.mpf('.29')],
              [1,1,1], [2,3,5], [mp.mpf('.4'),mp.mpf('3.4'),mp.mpf('2.2')],
              [mp.mpf('.1'),mp.mpf('.2'),mp.mpf('.3'),mp.mpf('.4')], [2,3,5,7]):
    x=closed(alpha); y=raw_moments(alpha)
    assert mp.almosteq(x,y,rel_eps=mp.mpf('1e-48'),abs_eps=mp.mpf('1e-48')),(alpha,x,y)
    assert x<0
    checks+=1
    if len(alpha)==2:
        z=integral2(alpha)
        assert abs(z-x)<mp.mpf('1e-20'),(alpha,z,x)
        checks+=1

for k in (2,3,5,10):
    f=lambda a:2*a*(k*a+1)*mp.polygamma(1,a+1)-1
    a_star=mp.findroot(f,(mp.mpf('.01'),mp.mpf('.8')))
    assert a_star>0
    for mult in (mp.mpf('.5'),mp.mpf('2')):
        a=a_star*mult;A=k*a
        v=[mp.mpf(1),mp.mpf(-1)]+[mp.mpf(0)]*(k-2)
        eps=mp.mpf('1e-8')*min(1,a)
        baseline=-closed([a]*k)
        valplus=-closed([a+eps*z for z in v]); valminus=-closed([a-eps*z for z in v])
        quadratic=(valplus+valminus-2*baseline)/(2*eps**2)
        coeff=(2*a*(A+1)*mp.polygamma(1,a+1)-1)/(A*(A+1)**2*(A+2))*sum(t*t for t in v)
        assert abs((quadratic-coeff)/coeff)<mp.mpf('1e-10'),(k,a,quadratic,coeff)
        checks+=1
    print('critical total concentration',k,mp.nstr(k*a_star,18))
print('PASS',checks,'raw-moment / quadrature / local-curvature checks')
