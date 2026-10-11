"""Reproduce collision and sharp sixth-moment identities for three parabolic modes.

All convolution multiplicity tests are exact in finite-field arithmetic.
Fourier evaluations are independent complex numerical cross-checks;
finite cases are corroboration, not a proof of the universal statement.
"""
from collections import defaultdict
from itertools import combinations, product
from random import Random
import cmath

class Field:
    def __init__(self, p, kappa=None):
        self.p,self.kappa=p,kappa
        self.el=list(range(p)) if kappa is None else list(product(range(p),repeat=2))
        self.q=len(self.el)
    def add(self,x,y):
        p=self.p
        if self.kappa is None: return (x+y)%p
        return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def mul(self,x,y):
        p=self.p
        if self.kappa is None: return x*y%p
        return ((x[0]*y[0]+self.kappa*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def trace(self,x):
        return x if self.kappa is None else (2*x[0])%self.p
    def char(self,x):
        return cmath.exp(2j*cmath.pi*self.trace(x)/self.p)


def gamma(F,t): return (t,F.mul(t,t))

def sum3(F,terms):
    x=F.add(F.add(terms[0][0],terms[1][0]),terms[2][0])
    y=F.add(F.add(terms[0][1],terms[1][1]),terms[2][1])
    return x,y

def bins(F,ts,fs):
    pts=[gamma(F,t) for t in ts]
    bucket=defaultdict(complex)
    size=defaultdict(int)
    for inds in product(range(3),repeat=3):
        v=sum3(F,[pts[i] for i in inds])
        term=fs[inds[0]]*fs[inds[1]]*fs[inds[2]]
        bucket[v]+=term
        size[v]+=1
    return bucket,size

def exact_formula(p,fs):
    a=[abs(x)**2 for x in fs]
    pair=9*sum(a[i]**2*a[j] for i in range(3) for j in range(3) if i!=j)
    distinct=36*a[0]*a[1]*a[2]
    diagonal=(abs(sum(z**3 for z in fs))**2 if p==3 else sum(v**3 for v in a))
    return diagonal+pair+distinct

def direct_sixth(F,ts,fs):
    tot=0.0
    pts=[gamma(F,t) for t in ts]
    for x,y in product(F.el,repeat=2):
        z=sum(fs[i]*F.char(F.add(F.mul(x,pts[i][0]),F.mul(y,pts[i][1]))) for i in range(3))
        tot+=abs(z)**6
    return tot

def close(a,b): return abs(a-b)<=max(1.0,abs(a),abs(b))*2e-10

def sample(F,ts,fs):
    bucket,mult=bins(F,ts,fs)
    pattern=sorted(mult.values())
    expect=(sorted([3]*7+[6]) if F.p==3 else sorted([1]*3+[3]*6+[6]))
    assert pattern==expect,(F.p,F.q,ts,pattern)
    energy=sum(abs(z)**2 for z in bucket.values())
    formula=exact_formula(F.p,fs)
    direct=direct_sixth(F,ts,fs)
    assert close(energy,formula),(F.q,energy,formula)
    assert close(direct,F.q**2*formula),(F.q,direct,F.q**2*formula)
    S=sum(abs(z)**2 for z in fs)
    K=(11/3 if F.p==3 else 31/9)
    assert formula<=K*S**3+2e-9*max(1,S**3)
    return close(formula,K*S**3) and S>0

rng=Random(282021)
fields=[Field(3),Field(5),Field(7),Field(11),Field(3,2),Field(5,2)]
checks=0
for F in fields:
    triples=list(combinations(F.el,3))
    test_ts=triples if F.q<=9 else [triples[i] for i in range(0,len(triples),max(1,len(triples)//30))]
    for ts in test_ts:
        sample(F,ts,(1+0j,1+0j,1+0j));checks+=1
        fs=tuple(complex(rng.randint(-2,2),rng.randint(-2,2)) for _ in range(3))
        sample(F,ts,fs);checks+=1
    for j in range(12):
        ts=triples[rng.randrange(len(triples))]
        # All equal-modulus phase vectors extremize in nonternary characteristic.
        if F.p==3:
            w=cmath.exp(2j*cmath.pi/3)
            fs=(1.0,w**(j%3),w**(j//3%3))
        else:
            fs=(1.0,cmath.exp(1j*j/10),cmath.exp(1j*j*j/13))
        assert sample(F,ts,fs)
        checks+=1
# In F_3 every 3-point support is the whole parabola.
assert len(list(combinations(Field(3).el,3)))==1
print('PASS',checks,'independent field/phase/Fourier checks; fields: 3, 5, 7, 11, 9, 25')
