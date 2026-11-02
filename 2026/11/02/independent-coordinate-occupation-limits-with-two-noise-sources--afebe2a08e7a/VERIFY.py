#!/usr/bin/env python3
"""Reproducible finite-identity checks for coordinate-occupation limits.
Only exact finite algebra is checked; infinite limits are proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import gamma

checks = 0

def check(expr, message):
    global checks
    checks += 1
    if not expr:
        raise AssertionError(message)

# Martingale coefficient identities, including off-diagonal brackets.
for k in range(2, 9):
    for spins in product((-1, 1), repeat=k):
        vals = [[(1-k*(a==i))*spins[i] for i in range(k)] for a in range(k)]
        for i in range(k):
            check(sum(vals[a][i] for a in range(k)) == 0, 'martingale drift')
            for j in range(k):
                q = F(sum(vals[a][i]*vals[a][j] for a in range(k)), k)
                want = F(k-1) if i==j else -spins[i]*spins[j]
                check(q == want, 'predictable bracket')

# All finite realizations of the model (two coordinates) through depth six.
p = (F(2,3),F(3,5))
alpha = tuple(2*a-1 for a in p)
# state: (histories, cumulative occupations, clock correction, probability)
states = {( ((1,),(-1,)), (0,0), (0,0) ): F(1)}
for t in range(1,7):
    next_states = {}
    for (h,a,r),prob in states.items():
        for selected in range(2):
            aa = tuple(a[i]+h[i][-1] for i in range(2))
            rr = tuple(r[i]+(1-2*(selected==i))*h[i][-1] for i in range(2))
            mean = alpha[selected]*F(sum(h[selected]),len(h[selected]))
            for new_spin,pr in ((1,(1+mean)/2),(-1,(1-mean)/2)):
                hh = list(h)
                hh[selected] += (new_spin,)
                key=(tuple(hh), aa, rr)
                next_states[key]=next_states.get(key,F(0))+prob*F(1,2)*pr
    states=next_states
    check(sum(states.values()) ==1, 'total finite path mass')
    for (h,a,r),prob in states.items():
        check(0 <= prob <= 1, 'nonnegative path mass')
        for i in range(2):
            count=len(h[i])-1
            embedded=sum(h[i][:count])
            check(a[i]==2*embedded+r[i], 'pathwise clock decomposition')

# Check embedded-ERW second-moment recursion against exact path enumeration.
for pp in (F(1,5),F(1,2),F(2,3),F(3,4),F(7,8)):
    aa=2*pp-1
    distr={(1,):F(1)}
    mm=F(1)
    for m in range(1,11):
        enum=sum(prob*sum(h)**2 for h,prob in distr.items())
        check(enum==mm, 'ERW second moment exact recurrence')
        next_distr={}
        for h,prob in distr.items():
            mean=aa*F(sum(h),len(h))
            for v,q in ((1,(1+mean)/2),(-1,(1-mean)/2)):
                next_distr[h+(v,)]=prob*q
        distr=next_distr
        mm=(1+2*aa/F(m))*mm+1

# When p=1/2, each refresh is an independent symmetric bit.  Exact Markov
# enumeration for initial spin 1 checks mean and raw second occupation moment.
for k in range(2,7):
    q=F(k-1,k)
    dist={(1,0):F(1)} # (current spin, cumulative occupation)
    for n in range(1,12):
        new={}
        for (spin,acc),mass in dist.items():
            for new_spin,pr in ((spin,q),(1,F(1,2*k)),(-1,F(1,2*k))):
                key=(new_spin,acc+spin)
                new[key]=new.get(key,F(0))+mass*pr
        dist=new
        ex=sum(mass*acc for (spin,acc),mass in dist.items())
        ex2=sum(mass*acc**2 for (spin,acc),mass in dist.items())
        formula_mean=sum(q**t for t in range(n))
        formula_second=F(n)+2*sum((n-h)*q**h for h in range(1,n))
        check(ex==formula_mean, 'unbiased exact mean')
        check(ex2==formula_second, 'unbiased exact second raw moment')
        check(sum(dist.values())==1, 'unbiased path mass')

# Analytic supercritical coefficient is the large-m limit of the verified
# recurrence.  Display approximations, not fake finite certifiers.
for alpha_float in (.6,.75,.9):
    m2=1.0
    for m in range(1,100001):
        m2=(1+2*alpha_float/m)*m2+1
    estimate=m2/(100001**(2*alpha_float))
    exact=1/((2*alpha_float-1)*gamma(2*alpha_float))
    print(f'illustrative supercritical alpha={alpha_float}: finite={estimate:.8f}, limit={exact:.8f}')

print(f'PASS: {checks} exact finite assertions; no infinite theorem certified by enumeration.')
