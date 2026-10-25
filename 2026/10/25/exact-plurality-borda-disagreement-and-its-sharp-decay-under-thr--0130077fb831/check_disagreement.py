"""Reproduce the exact strict plurality/Borda mismatch counts and asymptotic inputs.
Only the scientific four-ballot model is needed; Python 3 standard library suffices.
"""
from itertools import product
from math import factorial, sqrt, pi, log, exp, lgamma, isclose

BALLOTS = ('ABC', 'BAC', 'BCA', 'CBA')

def scores(seq):
    plu = {z:0 for z in 'ABC'}
    bor = {z:0 for z in 'ABC'}
    for ranking in seq:
        plu[ranking[0]] += 1
        for j,z in enumerate(ranking):
            bor[z] += 2-j
    return plu,bor

def unique_argmax(d):
    big=max(d.values())
    w=[k for k in d if d[k]==big]
    return w[0] if len(w)==1 else None

def direct(n):
    count=0
    for words in product(BALLOTS,repeat=n):
        p,b=scores(words)
        x,y=unique_argmax(p),unique_argmax(b)
        count+=(x is not None and y is not None and x!=y)
    return count

def multinomial_count(n):
    f=[factorial(j) for j in range(n+1)]
    q=0
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                if a>max(b+c,d) and a<d+b+2*c:
                    q+=f[n]//(f[a]*f[b]*f[c]*f[d])
    return 2*q

# Independent direct sequence enumeration versus compressed anonymous counts.
for n in range(1,9):
    d=direct(n)
    m=multinomial_count(n)
    assert d==m, (n,d,m)
    print('exact words',n,d,'/',4**n)

# The first strict disagreement is at n=4; its exact probability is 3/32.
assert [multinomial_count(n) for n in range(1,5)]==[0,0,0,24]
for n in range(9,15):
    print('count',n,multinomial_count(n),'/',4**n)

# Verify the saddle point with an independent centered-tilt calculation.
t=log(2)/2
rho=(exp(t)+2*exp(-t)+1)/4
Z=1+2*sqrt(2)
qA,qB,qC,qD=sqrt(2)/Z,1/(sqrt(2)*Z),1/(sqrt(2)*Z),1/Z
assert abs(qA-qB-qC)<1e-14
sigma2=qA+qB+qC
assert qA>qD and qD+qB+2*qC>qA
assert isclose(rho,Z/4,rel_tol=1e-14)
pref=2/(exp(t)-1)/sqrt(2*pi*sigma2)
print('rho',format(rho,'.15f'),'rate',format(-log(rho),'.15f'))
print('sigma2',format(sigma2,'.15f'),'prefactor',format(pref,'.15f'))

# All strict-discordance frequencies can be calculated using nonnegative
# multinomial probabilities. These figures are numerical corroborations of
# the analytic asymptotic theorem, not a proof of its infinite limit.
for n in (20,40,80,120):
    lf=[lgamma(j+1) for j in range(n+1)]
    p=0.
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                if a>max(b+c,d) and a<d+b+2*c:
                    p+=exp(lf[n]-lf[a]-lf[b]-lf[c]-lf[d]-n*log(4))
    p*=2
    ap=pref*rho**n/sqrt(n)
    print('n',n,'exact',format(p,'.12g'),'leading',format(ap,'.12g'),'ratio',format(p/ap,'.10g'))
print('ALL EXACT COMBINATORIAL CHECKS PASSED')
