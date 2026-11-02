"""Checks for the homothetic-frustum difference-body profile. Python 3 stdlib."""
from fractions import Fraction as Q
from math import comb, exp, log, isclose


def ratio(m,t, v):
    if t == 1:
        return Q(2)*sum(Q(comb(m,j))*v[j] for j in range(m+1))
    num=sum(Q(comb(m,j))*v[j]*(1-t**(j+1))/Q(j+1) for j in range(m+1))
    return Q(2*(m+1))*num/(1-t**(m+1))


def lower(m,t):
    if t == 1:
        return Q(2**(m+1))
    return Q(2)*(2**(m+1)-(1+t)**(m+1))/(1-t**(m+1))


def upper(m,t):
    return ratio(m,t,[Q(comb(m,j)) for j in range(m+1)])


for m in range(1,19):
    sym=[Q(1)]*(m+1)
    tri=[Q(comb(m,j)) for j in range(m+1)]
    for t in [Q(0),Q(1,7),Q(1,3),Q(5,7),Q(1)]:
        assert ratio(m,t,sym)==lower(m,t)
        assert ratio(m,t,tri)==upper(m,t)
        assert lower(m,t)<=upper(m,t)
    assert upper(m,Q(0))==comb(2*m+2,m+1)
    assert lower(m,Q(0))==2*(2**(m+1)-1)
    assert upper(m,Q(1))==2*comb(2*m,m)
    for v in [sym,tri]:
        ts=[Q(0),Q(1,10),Q(2,5),Q(4,5),Q(1)]
        rs=[ratio(m,t,v) for t in ts]
        assert all(rs[i]>rs[i+1] for i in range(4))
print('EXACT_ALL_DIMENSIONAL_ENDPOINT_AND_MONOTONICITY_CHECKS_PASSED',18)

for c in [Q(1),Q(9,8),Q(3,2),Q(2)]:
    v=[Q(1),c,Q(1)]
    for t in [Q(0),Q(1,4),Q(2,3),Q(1)]:
        pred=2+Q(6)*(1+c*(1+t))/(1+t+t*t)
        assert ratio(2,t,v)==pred
        c_again=((pred-2)*(1+t+t*t)/6-1)/(1+t)
        assert c_again==c
print('EXACT_THREE_DIMENSIONAL_RECONSTRUCTION_PASSED')

# Binomial reweighting concentration, exact finite extremal families.
for m in range(1,250):
    for v in [[Q(1)]*(m+1),[Q(comb(m,j)) for j in range(m+1)]]:
        den=sum(comb(m,j)*v[j] for j in range(m+1))
        second=sum(Q(comb(m,j))*v[j]*Q((2*j-m)**2,4) for j in range(m+1))/den
        assert second<=Q(m,4)
print('EXACT_ALEKSANDROV_FENCHEL_CONCENTRATION_MODELS_PASSED',249)


def limit_ratio(m,tau,model):
    # Exact shape models used only via weights; normalized weights avoid overflow.
    if model=='symmetric':
        w=[comb(m,j) for j in range(m+1)]
    elif model=='simplex':
        w=[comb(m,j)**2 for j in range(m+1)]
    else:
        w=[comb(m,j)*exp(-3.0*(j-m/2)**2/m) for j in range(m+1)]
    ws=sum(w)
    probs=[x/ws for x in w]
    def simpson(fun,n=100):
        h=tau/n
        return h/3*(fun(0)+fun(tau)+4*sum(fun(h*j) for j in range(1,n,2))+2*sum(fun(h*j) for j in range(2,n-1,2)))
    numerator=simpson(lambda u: sum(p*(1-u/m)**j for j,p in enumerate(probs)))
    denominator=simpson(lambda u: (1-u/m)**m)
    return numerator/denominator

for model in ['symmetric','simplex','middle']:
    for tau in [.4,1.,3.]:
        target=2/(1+exp(-tau/2))
        errors=[]
        for m in [32,64,128,256]:
            r=limit_ratio(m,tau,model)
            errors.append(abs(r-target))
        assert errors[-1]<.035,(model,tau,errors)
        assert errors[-1]<errors[0],(model,tau,errors)
print('SHAPE_UNIFORM_LOGISTIC_TRANSITION_DIAGNOSTICS_PASSED')
print('ALL_CHECKS_PASSED')
