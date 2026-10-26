"""Standard-library checks for planar power-residual Kaczmarz edge laws.

The infinite-horizon assertions are proved in RESULT.md, not by this finite checker.
Run: python VERIFY.py
"""
from fractions import Fraction as F
from math import log, exp, sqrt, isclose
from random import Random

A=((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13)))
m=len(A)
E=[]
for i in range(m):
    assert sum(v*v for v in A[i])==1
    for j in range(i+1,m):
        c=abs(sum(A[i][k]*A[j][k] for k in range(2)))
        s=abs(A[i][0]*A[j][1]-A[i][1]*A[j][0])
        assert 0<c<1 and 0<s<1 and c*c+s*s==1
        E.append((i,j,c,s))
assert [(c,s) for _,_,c,s in E]==[(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(63,65),F(16,65))]

def theory(p):
    weights=[float(s)**p for _,_,c,s in E]
    return sum(w*log(float(c)) for w,(_,_,c,s) in zip(weights,E))/sum(weights)

def kernel(p):
    W=[[F(0) for _ in range(m)] for _ in range(m)]
    for i,j,c,s in E:
        W[i][j]=W[j][i]=s**p
    d=[sum(row) for row in W]
    pi=[v/sum(d) for v in d]
    P=[[W[i][j]/d[i] for j in range(m)] for i in range(m)]
    assert all(sum(P[i])==1 and P[i][i]==0 for i in range(m))
    assert sum(pi)==1
    for i in range(m):
        for j in range(m):
            assert pi[i]*P[i][j]==pi[j]*P[j][i]
    return pi,P

for power in (1,2,3,5,7):
    pi,P=kernel(power)
    row_rate=sum(float(pi[i]*P[i][j])*log(abs(float(sum(A[i][k]*A[j][k] for k in range(2))))) for i in range(m) for j in range(m) if i!=j)
    assert abs(row_rate-theory(power))<1e-13

assert theory(1)>theory(2)>theory(3)>theory(5)>theory(7)
assert isclose(theory(1e-8), sum(log(float(c)) for _,_,c,s in E)/len(E), rel_tol=1e-7,abs_tol=1e-7)
lam_uniform=2*sum(log(float(c)) for _,_,c,s in E)/m**2
lam_zero_plus=sum(log(float(c)) for _,_,c,s in E)/len(E)
assert abs(lam_zero_plus/lam_uniform-m/(m-1))<1e-12
assert isclose(theory(70), log(float(F(5,13))), rel_tol=2e-5,abs_tol=2e-5)

# Direct projection and residual-selection identities, in rational arithmetic.
for i in range(m):
    n_i=(-A[i][1],A[i][0])
    for j in range(m):
        n_j=(-A[j][1],A[j][0])
        residual=sum(A[j][k]*n_i[k] for k in range(2))
        proj=tuple(n_i[k]-residual*A[j][k] for k in range(2))
        dot=sum(A[i][k]*A[j][k] for k in range(2))
        assert proj==tuple(dot*n_j[k] for k in range(2))
        assert residual*residual+dot*dot==1

# A Markov path models the successive normalized projection directions.
def mc_rate(p,N,seed,uniform=False):
    rng=Random(seed)
    state=0
    v=0.0
    for _ in range(N):
        if uniform:
            nxt=rng.randrange(m)
        else:
            scores=[abs(float(A[j][0]*A[state][1]-A[j][1]*A[state][0]))**p for j in range(m)]
            t=rng.random()*sum(scores)
            q=0.0
            nxt=m-1
            for j,s in enumerate(scores):
                q+=s
                if t<q:
                    nxt=j
                    break
        c=abs(float(sum(A[state][k]*A[nxt][k] for k in range(2))))
        v+=log(c)
        state=nxt
    return v/N

for power in (0.02,1,2,5):
    observed=mc_rate(power,150000,100+int(100*power))
    assert abs(observed-theory(power))<0.025, (power,observed,theory(power))
assert abs(mc_rate(0,150000,293,True)-lam_uniform)<0.025
print('VERIFY_OK: exact kernels, detailed balance, projection identities, endpoint limits, and 750000 simulated transitions')
print('rates',{'uniform':lam_uniform,'zero_plus':lam_zero_plus,'p2':theory(2),'greedy_limit':log(float(F(5,13)))})
