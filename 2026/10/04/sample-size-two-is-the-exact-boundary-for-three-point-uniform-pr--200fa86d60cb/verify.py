from fractions import Fraction
from itertools import product

def rho_parts(n,s):
    A=(1-s)**n; B=s**n; C=(1-2*s)**n
    mu=1-A-B
    var=1-A+B-mu*mu
    cov=-1+2*A+2*B-C+mu*mu
    return cov,var

def D(k):
    return (4*Fraction(8,3)**k + 20*Fraction(4,3)**k + 11*Fraction(2,3)**k
            + Fraction(1,3)**k - 9*(2**k) - 27)

assert D(1)==0
assert D(2)==6
assert D(3)==Fraction(248,9)
for k in range(2,25):
    assert D(k)>0

# Exact enumeration check for selected n and rational s.
for n in range(2,8):
    for s in (Fraction(1,4),Fraction(1,3),Fraction(2,5)):
        p={-1:s,0:1-2*s,1:s}
        probs=[]
        for xs in product((-1,0,1), repeat=n):
            pr=Fraction(1)
            for x in xs: pr*=p[x]
            probs.append((pr,min(xs),max(xs)))
        EL=sum(pr*l for pr,l,u in probs); EU=sum(pr*u for pr,l,u in probs)
        ELU=sum(pr*l*u for pr,l,u in probs); EU2=sum(pr*u*u for pr,l,u in probs)
        cov=ELU-EL*EU; var=EU2-EU*EU
        c2,v2=rho_parts(n,s)
        assert cov==c2 and var==v2
print('VERIFY_OK')
