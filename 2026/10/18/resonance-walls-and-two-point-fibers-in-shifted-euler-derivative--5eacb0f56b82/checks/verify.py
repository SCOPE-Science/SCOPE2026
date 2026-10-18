"""Exact algebraic and floating-point checks for angular Euler-filter phase retrieval.

Run with Python 3 and NumPy: python angular_filter_phase_verifier.py
Numerical tests corroborate, but do not prove, the general theorem.
"""
from fractions import Fraction as F
from collections import defaultdict
import numpy as np

class Q:
    def __init__(self,re=0,im=0): self.re,self.im=F(re),F(im)
    @staticmethod
    def of(x): return x if isinstance(x,Q) else Q(x)
    def __add__(self,x):
        x=Q.of(x);return Q(self.re+x.re,self.im+x.im)
    __radd__=__add__
    def __neg__(self):return Q(-self.re,-self.im)
    def __sub__(self,x):return self+-Q.of(x)
    def __rsub__(self,x):return Q.of(x)+-self
    def __mul__(self,x):
        x=Q.of(x);return Q(self.re*x.re-self.im*x.im,self.re*x.im+self.im*x.re)
    __rmul__=__mul__
    def conj(self):return Q(self.re,-self.im)
    def __truediv__(self,x):
        x=Q.of(x);den=x.re*x.re+x.im*x.im
        return Q((self.re*x.re+self.im*x.im)/den,(self.im*x.re-self.re*x.im)/den)
    def __eq__(self,x):
        x=Q.of(x);return self.re==x.re and self.im==x.im
    def __repr__(self):return f'({self.re}+{self.im}i)'
I=Q(0,1)

def correl(a):
    out=defaultdict(Q)
    for j,p in enumerate(a):
        for k,r in enumerate(a): out[j-k]+=p*r.conj()
    return dict(out)

def add(a,b):
    out=defaultdict(Q)
    for k,v in a.items():out[k]+=v
    for k,v in b.items():out[k]+=v
    return dict(out)

def scale(a,c):return {k:v*c for k,v in a.items()}

def multiply(a,b):
    out=defaultdict(Q)
    for k,v in a.items():
        for j,w in b.items():out[k+j]+=v*w
    return dict(out)

def equal(a,b):return all(a.get(k,Q())==b.get(k,Q()) for k in set(a)|set(b))

def measurements(a,alpha):
    v=[(Q(j)-alpha)*p for j,p in enumerate(a)]
    return correl(a),correl(v)

def flip(a,k,d):return [a[k-j].conj() if 0<=k-j<len(a) else Q() for j in range(d+1)]

def square_test(a,alpha):
    A,S=measurements(a,alpha)
    u,v=alpha.re,alpha.im
    C=defaultdict(Q)
    for j,p in enumerate(a):
        for k,r in enumerate(a):C[j-k]+=Q(j)*p*r.conj()
    T={m:(C.get(m,Q())+C.get(-m,Q()).conj())/2 for m in range(-len(a)+1,len(a))}
    R=add(T,scale(A,-u))
    J={m:(-I*Q(m)/2-Q(v))*x for m,x in A.items()}
    assert equal(add(multiply(R,R),multiply(J,J)),multiply(A,S))

exact=0
for d in range(1,9):
    a=[Q(j+1,j*j-3) for j in range(d+1)]
    for alpha in [Q(F(2,5),F(3,7)),Q(F(d,2)),Q(0),Q(F(3,2),F(1,3))]:
        square_test(a,alpha);exact+=1
    for k in range(1,2*d):
        a=[Q() for _ in range(d+1)]
        for j in range(max(0,k-d),min(d,k)+1):a[j]=Q(j+2,j-1)
        q=flip(a,k,d)
        alpha=Q(F(k,2),F(3,7))
        A,S=measurements(a,alpha)
        B,T=measurements(q,alpha)
        assert equal(A,B) and equal(S,T)
        exact+=1

# Detuning the real part breaks a genuinely nontrivial reflected solution.
a=[Q(1,2),Q(2,-1),Q(3,1),Q(4,-3),Q()]
q=flip(a,3,4)
A,S=measurements(a,Q(F(7,5),F(2,7)))
B,T=measurements(q,Q(F(7,5),F(2,7)))
assert equal(A,B) and not equal(S,T)
exact+=1

for d in range(1,9):
    a=[Q(j+2,j+1) for j in range(d+1)]
    alpha=Q(F(7,4),F(5,3))
    A,S=measurements(a,alpha)
    assert S[d]==-alpha.conj()*(Q(d)-alpha)*A[d]
    exact+=1

rng=np.random.default_rng(148)
max_err=0.0
sample_checks=0
for d in range(1,9):
    for trial in range(6):
        a=rng.normal(size=d+1)+1j*rng.normal(size=d+1)
        alpha=1.23+0.43j
        q=np.array([(j-alpha)*a[j] for j in range(d+1)])
        aa=np.array([sum(a[j+m]*np.conj(a[j]) for j in range(d+1-m)) for m in range(d+1)])
        ss=np.array([sum(q[j+m]*np.conj(q[j]) for j in range(d+1-m)) for m in range(d+1)])
        t1=(np.arange(2*d+1)+0.17*np.sin(np.arange(2*d+1)*1.4))*2*np.pi/(2*d+1)
        t2=(np.arange(2*d-1)+0.11*np.cos(np.arange(2*d-1)*1.8))*2*np.pi/(2*d-1)
        def trig(c,t):return c[0].real+sum(2*np.real(c[m]*np.exp(1j*m*t)) for m in range(1,len(c)))
        def interp(values,t,n):
            V=np.column_stack([np.ones(len(t))]+[f(m*t) for m in range(1,n+1) for f in (np.cos,np.sin)])
            v=np.linalg.solve(V,values)
            return np.array([v[0]]+[v[2*m-1]/2-1j*v[2*m]/2 for m in range(1,n+1)])
        Arec=interp(trig(aa,t1),t1,d)
        top=-np.conj(alpha)*(d-alpha)*Arec[d]
        Slow=trig(ss,t2)-2*np.real(top*np.exp(1j*d*t2))
        Srec=np.r_[interp(Slow,t2,d-1),top]
        err=max(np.max(np.abs(aa-Arec)),np.max(np.abs(ss-Srec)))
        max_err=max(max_err,float(err))
        assert err<1e-8,(d,trial,err)
        sample_checks+=1

print('exact symbolic identity and resonance checks:',exact)
print('nonuniform finite-sampling reconstructions:',sample_checks)
print('maximum Fourier interpolation coefficient error: %.5g'%max_err)
print('PASS')
