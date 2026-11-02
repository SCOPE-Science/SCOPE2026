"""Standalone algebraic and numerical checks for six-block SEIR contact scheduling.
Run: python verify.py (requires sympy, numpy, scipy).
"""
from itertools import permutations
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import brentq

# Derive trace identities for generic 2-by-2 matrices over a polynomial ring.
a,b,c,d,e,f,g,h=sp.symbols('a b c d e f g h')
A=sp.Matrix([[a,b],[c,d]])
B=sp.Matrix([[e,f],[g,h]])
def product(word, left=A, right=B):
    M=sp.eye(2)
    for letter in word:
        M=M*(left if letter=='H' else right)
    return M
K=-sp.det(A*B-B*A)
T0=sp.trace(product('HHHLLL'))
T1=sp.trace(product('HHLHLL'))
T2=sp.trace(product('HLHLHL'))
assert sp.expand(T1-T0-sp.trace(A)*sp.trace(B)*K)==0
assert sp.expand(T2-T1-sp.trace(A*B)*K)==0
for word in set(''.join(w) for w in permutations('HHHLLL')):
    value=sp.trace(product(word))
    assert any(sp.expand(value-v)==0 for v in (T0,T1,T2))
assert sp.expand(sp.trace(product('HHLLHL'))-T1)==0
print('Symbolic identities and exhaustive twenty-calendar reduction: PASS')

# Independently check the commutator factorization, without exponentiating.
sigma,gamma,x,y=sp.symbols('sigma gamma x y',positive=True)
GH=sp.Matrix([[-sigma,x],[sigma,-gamma]])
GL=sp.Matrix([[-sigma,y],[sigma,-gamma]])
assert sp.factor(sp.det(GH*GL-GL*GH)) == -sigma**2*(x-y)**2
print('SEIR-generator commutator determinant: PASS')

# Perturb parameters, including unequal latent/recovery rates and distinct durations.
words=('HHHLLL','HHLHLL','HLHLHL')
rng=np.random.default_rng(20261025)
for j in range(96):
    ss,gg=np.exp(rng.uniform(-1.5,1.5,2))
    lo,hi=np.sort(np.exp(rng.uniform(-1.5,1.2,2)))
    times=np.exp(rng.uniform(-1.0,0.4,2))
    H=expm(times[0]*np.array([[-ss,hi],[ss,-gg]]))
    L=expm(times[1]*np.array([[-ss,lo],[ss,-gg]]))
    mats=[]
    for w in words:
        P=np.eye(2)
        for z in w: P=P@(H if z=='H' else L)
        mats.append(P)
    spectra=[max(np.linalg.eigvals(M).real) for M in mats]
    assert spectra[0]<spectra[1]<spectra[2],(j,spectra)
    KK=-np.linalg.det(H@L-L@H)
    assert KK>0
    gap1=np.trace(mats[1])-np.trace(mats[0])
    gap2=np.trace(mats[2])-np.trace(mats[1])
    assert np.isclose(gap1,np.trace(H)*np.trace(L)*KK,rtol=5e-6,atol=1e-12)
    assert np.isclose(gap2,np.trace(H@L)*KK,rtol=5e-6,atol=1e-12)
print('Ninety-six numerical matrix-exponential scheduling checks: PASS')

# Numerical invasion-boundary witness (not used as an analytic proof).
ss=gg=tt=1.0
lo=.2
def multiplier(w,hi):
    H=expm(tt*np.array([[-ss,hi],[ss,-gg]]))
    L=expm(tt*np.array([[-ss,lo],[ss,-gg]]))
    P=np.eye(2)
    for z in w: P=P@(H if z=='H' else L)
    return max(np.linalg.eigvals(P).real)
thresholds=[]
for w in words:
    root=brentq(lambda high:multiplier(w,high)-1,lo,4.0,xtol=1e-13)
    assert abs(multiplier(w,root)-1)<5e-12
    thresholds.append(root)
assert thresholds[2]<thresholds[1]<thresholds[0]
assert multiplier(words[2],1.9)>1>multiplier(words[1],1.9)>multiplier(words[0],1.9)
assert multiplier(words[2],2.0)>multiplier(words[1],2.0)>1>multiplier(words[0],2.0)
for w,root in zip(words,thresholds):print(w,format(root,'.14f'))
print('Two distinct schedule-dependent invasion flips: PASS')
