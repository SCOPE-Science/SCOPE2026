"""Supplementary finite tests for logarithmic Volterra singular-value formula.
Scientific mathematics only; no claim of computer proof of the infinite-dimensional limit.
Run: python volterra_log_checker.py
Requires: Python >=3.9, numpy >=1.20
"""
import cmath
import json
import math
import random
import numpy as np

RNG = random.Random(2061026)
checks=0

def close(a,b,atol=1e-10):
    global checks
    assert abs(a-b)<=atol*(1+max(abs(a),abs(b))), (a,b)
    checks+=1

def direct_T(vec,coeff):
    out={}
    for n,x in vec.items():
        for k,b in coeff.items():
            t=n*k
            out[t]=out.get(t,0)+x*b*math.log(k)/math.log(t)
    return out

def factor_T(vec,coeff):
    h={k:b*math.log(k) for k,b in coeff.items()}
    out={}
    for n,x in vec.items():
        for k,c in h.items():
            t=n*k
            out[t]=out.get(t,0)+x*c/math.log(t)
    return out

def norm2(v):
    return sum(abs(x)**2 for x in v.values())

# Exact coefficient recurrence/direct-integral versus diagonal-times-convolution.
for trial in range(125):
    ks=RNG.sample([2,3,4,5,6,8,9,10,12],RNG.randrange(1,6))
    sym={k:complex(RNG.uniform(-1,1),RNG.uniform(-1,1)) for k in ks}
    vec={n:complex(RNG.uniform(-1,1),RNG.uniform(-1,1)) for n in RNG.sample(range(1,35),10)}
    a=direct_T(vec,sym); b=factor_T(vec,sym)
    assert a.keys()==b.keys(); checks+=1
    for k in a:close(a[k],b[k])

# Monomial exact singular values: columns orthogonal and decreasing with n.
for k in (2,3,7,12):
    for N in (4,7,12,24):
        M=np.zeros((N*k+1,N),dtype=np.float64)
        for n in range(1,N+1):
            M[n*k,n-1]=math.log(k)/math.log(n*k)
        sv=np.linalg.svd(M,compute_uv=False)
        for j in range(N):
            close(sv[j],math.log(k)/math.log(k*(j+1)))

# A genuinely interacting three-term Dirichlet symbol.
coeff={2:1.0,4:1.0,8:-1.0}
log2=math.log(2)
theta=math.acos(-1/3)
K=8*log2/math.sqrt(3)
for j in range(4096):
    z=cmath.exp(2.0*math.pi*1j*j/4096)
    val=log2*(z+2*z*z-3*z*z*z)
    assert abs(val)<=K+2e-6, (val,K)
    checks+=1
z=cmath.exp(1j*theta)
close(abs(log2*(z+2*z*z-3*z*z*z)),K)

# Explicit near-maximal Hardy polynomials and the orthogonality of odd fibers.
prev=0
for L in (4,8,16,32,64,128):
    psi={2**j:cmath.exp(-1j*j*theta)/math.sqrt(L+1) for j in range(L+1)}
    norm=math.sqrt(norm2(psi))
    close(norm,1)
    hpsi={}
    for n,v in psi.items():
        for k,b in coeff.items():
            t=n*k
            hpsi[t]=hpsi.get(t,0)+v*b*math.log(k)
    ratio=math.sqrt(norm2(hpsi))
    assert ratio<=K+1e-10;checks+=1
    assert ratio>prev;checks+=1
    prev=ratio
    for m in (101,103,107,109):
        w={m*n:v for n,v in psi.items()}
        vals=direct_T(w,coeff)
        estimated=ratio/math.log(m*8*(2**L))
        assert math.sqrt(norm2(vals))+1e-12>=estimated;checks+=1
    # Check disjoint supports for different odd bases even after multiplying by powers of 2.
    for m1,m2 in ((101,103),(103,107),(101,109)):
        w1={m1*n:v for n,v in psi.items()}
        w2={m2*n:v for n,v in psi.items()}
        s1=set(direct_T(w1,coeff));s2=set(direct_T(w2,coeff))
        assert not s1.intersection(s2);checks+=1

# Analytic maximizing geometry: the squared modulus has vertex c=-1/3.
for j in range(2001):
    c=-1+j/1000
    sq=20-8*c-12*c*c
    assert sq<=64/3+1e-10;checks+=1
close(K*K,(64/3)*log2*log2)
print(json.dumps({'status':'PASS','finite_assertions':checks,'example_constant':K,'normalized_polynomial_approximation':prev,'statement':'Finite consistency checks only; infinite-dimensional limit proved analytically.'}))
