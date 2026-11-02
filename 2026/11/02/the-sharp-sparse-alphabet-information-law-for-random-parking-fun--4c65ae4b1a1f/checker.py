"""Finite exact checks for boundary-alphabet observation of uniform parking preferences.

This program tests finite identities and data processing, not infinite-limit theorems.
"""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter
from math import factorial, lgamma, log, exp, pi

checks = 0

def check(pred, detail):
    global checks
    assert pred, detail
    checks += 1

def marginal_bias(n):
    g = [Fraction(n-1,n+1)]
    for i in range(1,n):
        delta = Fraction((i**(i-1))*((n+1-i)**(n-i))*factorial(n+1),
                         factorial(i)*factorial(n+1-i)*((n+1)**n))
        g.append(g[-1]-delta)
    return g

def is_parking(x):
    return all(y <= i for i,y in enumerate(sorted(x),1))

def tv_counts(a,b):
    A=sum(a.values()); B=sum(b.values())
    return sum(abs(Fraction(a.get(x,0),A)-Fraction(b.get(x,0),B)) for x in a.keys()|b.keys())/2

def mask(x,E):
    return tuple(v if v in E else 0 for v in x)

for n in range(2,7):
    allpref=list(product(range(1,n+1),repeat=n))
    parking=[x for x in allpref if is_parking(x)]
    check(len(parking)==(n+1)**(n-1),('count',n))
    g=marginal_bias(n)
    check(sum(g)==0,('zero sum',n))
    check(all(1+t>0 for t in g),('positivity',n))
    check(all(g[i]>g[i+1] for i in range(n-1)),('monotone',n))
    for j in range(n):
        count=sum(x[0]==j+1 for x in parking)
        check(Fraction(count,len(parking))==Fraction(1+g[j],n),('marginal',n,j))
    for j in range(1,n-1):
        check(g[j]+g[n-j]==Fraction(-2,n+1),('mirror',n,j))
    if n<=5:
        for k in (1,2):
            pa=Counter(x[:k] for x in parking)
            un=Counter(x[:k] for x in allpref)
            full=tv_counts(pa,un)
            for size in range(0,min(3,n)+1):
                for E in combinations(range(1,n+1),size):
                    p_mask=Counter({} if False else mask(x,E) for x in pa.elements())
                    q_mask=Counter(mask(x,E) for x in un.elements())
                    check(tv_counts(p_mask,q_mask)<=full,('data processing',n,k,E))
                    if k==1:
                        S=sum(g[v-1] for v in E)
                        score=sum(g[v-1]**2 for v in E)
                        star=Fraction(S*S,n-len(E)) if len(E)<n else 0
                        # χ² of the coarsened marginal under the coarsened uniform law
                        chi=(score+star)/n
                        chi_by_dist=sum((Fraction(p_mask[x],sum(p_mask.values()))-Fraction(q_mask[x],sum(q_mask.values())))**2/Fraction(q_mask[x],sum(q_mask.values())) for x in q_mask)
                        check(chi==chi_by_dist,('information identity',n,E))
print('finite_assertions',checks)

# Supplementary numerical only: compare logarithmic boundary-information growth.
def bias_float(n):
    g=[(n-1)/(n+1)]
    for i in range(1,n):
        j=n+1-i
        z=lgamma(n+2)+(i-1)*log(i)+(j-1)*log(j)-n*log(n+1)-lgamma(i+1)-lgamma(j+1)
        g.append(g[-1]-exp(z))
    return g
for n in (1000,5000,20000):
    m=int(n**.65)
    g=bias_float(n)
    e=sum(x*x for x in g[:m//2]+g[-(m-m//2):])
    print('diagnostic_n_m_energy_ratio',n,m,round(e/log(m),8),'target',round(4/pi,8))
print('all_finite_checks_passed')
