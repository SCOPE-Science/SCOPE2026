import mpmath as mp
mp.mp.dps=60

def const(alpha,theta,lamb):
    return alpha*2**(alpha-1)/(2**alpha-1)*lamb**theta

def surv(x,alpha,theta,lamb):
    v=(lamb/(lamb+x))**theta
    return (2**alpha-(2-v)**alpha)/(2**alpha-1)

def dens(x,alpha,theta,lamb):
    v=(lamb/(lamb+x))**theta
    return alpha*theta*lamb**theta/(2**alpha-1)*(2-v)**(alpha-1)*(lamb+x)**(-theta-1)

def hazard(x,a,th,la):
    return dens(x,a,th,la)/surv(x,a,th,la)

for aa,tt,ll in [('0.4','0.8','0.5'),('2.3','1.7','0.9'),('8.0','3.2','2.0')]:
    a,th,la=mp.mpf(aa),mp.mpf(tt),mp.mpf(ll)
    C=const(a,th,la)
    x=mp.mpf('1e8')
    tail=x**th*surv(x,a,th,la)
    assert abs(tail/C-1) < mp.mpf('2e-4'), (a,th,la,tail,C)
    assert abs(x*hazard(x,a,th,la)-th) < mp.mpf('2e-4')*max(1,th)

# Critical truncated moment has theta*C*log R leading growth.
a,th,la=mp.mpf('2.3'),mp.mpf('1.7'),mp.mpf('0.9')
C=const(a,th,la)
def trunc_moment(q,R):
    # stable tail identity; integrate in logarithmic blocks
    f=lambda x: q*x**(q-1)*surv(x,a,th,la)
    cuts=[mp.mpf('0'),mp.mpf('1'),mp.mpf('10'),mp.mpf('100'),mp.mpf('1000'),R]
    cuts=sorted(set(c for c in cuts if c<R))+[R]
    integ=mp.mpf('0')
    for lo,hi in zip(cuts[:-1],cuts[1:]):
        integ += mp.quad(f,[lo,hi])
    return integ-R**q*surv(R,a,th,la)

R1=mp.mpf('1e4'); R2=mp.mpf('1e6')
m1=trunc_moment(th,R1); m2=trunc_moment(th,R2)
slope=(m2-m1)/mp.log(R2/R1)
assert abs(slope/(th*C)-1) < mp.mpf('0.02')

# Positive exponential truncations are rapidly increasing.
t=mp.mpf('0.02')
def exp_trunc(R):
    return mp.quad(lambda x: mp.e**(t*x)*dens(x,a,th,la), [0,1,10,R])
e1=exp_trunc(mp.mpf('100'))
e2=exp_trunc(mp.mpf('300'))
assert e2 > e1

print('VERIFY_OK')
