import math

def rho(a,h):
    return (h-a)*(1-h) if h <= (1+a)/2 else (1-a)**2/4

def F(T,a,h,lam,beta,tau):
    r=rho(a,h)
    return r*T-(lam/beta)*math.log((h+tau)/(h+tau*math.exp(-beta*T)))

def root(a,h,p,lam,beta,tau):
    r=rho(a,h); L=-math.log(1-p)
    assert r >= lam*tau/(h+tau)
    lo,hi=0.0,1.0
    while F(hi,a,h,lam,beta,tau) <= L:
        hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if F(mid,a,h,lam,beta,tau) <= L: lo=mid
        else: hi=mid
    return (lo+hi)/2

r1=root(0.1,0.61,0.27,0.5,0.55,0.18)
r2=root(0.1,0.46,0.0878,0.5,0.55,0.0737)
assert abs(r1-2.3686218444908107)<1e-12
assert abs(r2-0.6782308509533814)<1e-12
assert abs((-math.log(0.73))/rho(0.1,0.61)-1.5541271350108652)<1e-12
assert abs((-math.log(1-0.0878))/rho(0.1,0.46)-0.4727161250233383)<1e-12
print('VERIFY_OK')
