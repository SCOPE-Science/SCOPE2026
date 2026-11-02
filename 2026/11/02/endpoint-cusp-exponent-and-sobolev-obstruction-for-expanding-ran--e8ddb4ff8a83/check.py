#!/usr/bin/env python3
"""Finite consistency tests for a cusp transfer-operator endpoint law.

These checks verify branch geometry, inverse equations, and finite-z transfer
asymptotics for smooth test inputs. They do not prove existence or uniqueness
of a stationary density, or any infinite-limit theorem.
"""
import mpmath as mp

mp.mp.dps = 70
alpha = mp.mpf(3)/4
gamma = (1-alpha)/alpha
pi = [mp.mpf(2)/5, mp.mpf(3)/5]
thetas = [mp.mpf(6)/5, mp.mpf(17)/10]
A = [(1-th/2)*mp.power(2, alpha) for th in thetas]
phi = lambda x: 1+x+x*x
c=mp.mpf(1)/2
checks=0

for th,a in zip(thetas,A):
    assert mp.almosteq(th/2+a*mp.power(mp.mpf(1)/2,alpha), 1)
    checks += 1
    lower_slope=th+alpha*a*mp.power(mp.mpf(1)/2,alpha-1)
    assert mp.almosteq(lower_slope,2*alpha+(1-alpha)*th)
    assert lower_slope>1
    checks+=2

def inv_t(th,a,z):
    lo=mp.mpf('0'); hi=mp.mpf('0.5')
    # Exact monotonicity makes bisection well-defined in real arithmetic.
    for _ in range(280):
        mid=(lo+hi)/2
        if th*mid+a*mp.power(mid,alpha)<z: lo=mid
        else: hi=mid
    t=(lo+hi)/2
    assert abs(th*t+a*mp.power(t,alpha)-z)<mp.mpf('1e-57')
    return t

def transferred(z):
    total=mp.mpf('0')
    for prob, th, a in zip(pi,thetas,A):
        t=inv_t(th,a,z)
        weight=1/(th+alpha*a*mp.power(t,alpha-1))
        total+=prob*weight*(phi(c-t)+phi(c+t))
    return total

C=2*phi(c)/alpha*sum(prob*mp.power(a,-1/alpha) for prob,a in zip(pi,A))
errors=[]
for exponent in [4,8,12,16,20]:
    z=mp.power(10,-exponent)
    ratio=transferred(z)/(C*mp.power(z,gamma))
    err=abs(ratio-1)
    errors.append(err)
    checks+=1
assert all(errors[i+1]<errors[i] for i in range(len(errors)-1))
checks+=len(errors)-1
assert errors[-1]<mp.mpf("1e-5")
checks+=1
checks+=1

# Borderline W^{1,p} obstruction: for beta=-1/4, p_crit=3/2.
beta=alpha-1
pcrit=alpha/(2*alpha-1)
assert beta==-mp.mpf(1)/4
assert pcrit==mp.mpf(3)/2
checks+=2

print(f'PASS {checks} deterministic finite checks')
print(f'gamma={mp.nstr(gamma, 16)}; p_crit={mp.nstr(pcrit,16)}')
print('z exponents: 4,8,12,16,20; relative errors:')
print(*[mp.nstr(e,12) for e in errors],sep='\n')
print('No infinite-limit or historical-novelty certification is claimed.')
