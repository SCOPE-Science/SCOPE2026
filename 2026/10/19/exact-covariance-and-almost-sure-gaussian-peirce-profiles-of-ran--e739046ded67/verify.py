from itertools import combinations
from math import comb
from fractions import Fraction
import random

def stats(m, bits):
    triples=list(combinations(range(m),3)); fours=list(combinations(range(m),4))
    ti={t:i for i,t in enumerate(triples)}
    kappa={f:sum((bits>>ti[t])&1 for t in combinations(f,3))%2 for f in fours}
    d={b:sum(kappa[tuple(sorted(b+(x,)))] for x in range(m) if x not in b) for b in triples}
    return triples,d

def validate_cov(m):
    triples=list(combinations(range(m),3)); N=len(triples); n=m-3
    vals=[]
    for bits in range(1<<N):
      _, d=stats(m,bits)
      vals.append([sum(x==k for x in d.values()) for k in range(n+1)])
    c=len(vals)
    E=[Fraction(sum(row[k] for row in vals),c) for k in range(n+1)]
    p=[Fraction(comb(n,k),2**n) for k in range(n+1)]
    a=[Fraction(comb(n-1,k),2**(n-1)) if 0<=k<=n-1 else Fraction(0) for k in range(n+1)]
    b=[Fraction(comb(n-1,k-1),2**(n-1)) if 0<=k-1<=n-1 else Fraction(0) for k in range(n+1)]
    assert E==[N*x for x in p]
    for k in range(n+1):
      for ell in range(n+1):
        cov=Fraction(sum(row[k]*row[ell] for row in vals),c)-E[k]*E[ell]
        target=N*((1 if k==ell else 0)*p[k]-p[k]*p[ell])+Fraction(N*3*n,4)*(a[k]-b[k])*(a[ell]-b[ell])
        assert cov==target, (m,k,ell,cov,target)
    print(f'COV_OK m={m} decorations={c} profile_mean='+str(E))

validate_cov(4)
validate_cov(5)

def validate_random(m, n_trials=10000):
  rng=random.Random(20261017)
  triples=list(combinations(range(m),3))
  n=m-3
  rows=[]
  for _ in range(n_trials):
    _,d=stats(m,rng.getrandbits(len(triples)))
    rows.append([sum(x==k for x in d.values()) for k in range(n+1)])
  N=len(triples)
  theo=[N*comb(n,k)/2**n for k in range(n+1)]
  obs=[sum(row[k] for row in rows)/n_trials for k in range(n+1)]
  assert max(abs(x-y) for x,y in zip(obs,theo))<.15, (obs,theo)
  print('MONTE_CARLO_OK',m,n_trials,'observed',obs,'theory',theo)
validate_random(6)

# Direct Peirce multiplication operators, rather than relying on Pasch indicators.
from itertools import product
import sympy as sp

def direct_peirce_check(m, bitstrings):
    pairs=list(combinations(range(m),2)); triples=list(combinations(range(m),3))
    index={p:i for i,p in enumerate(pairs)}; tindex={t:i for i,t in enumerate(triples)}
    x=sp.Symbol('x')
    for bits in bitstrings:
        sign={t: 1-2*((bits>>tindex[t])&1) for t in triples}
        _,degrees=stats(m,bits)
        for B in triples:
            subpairs=list(combinations(B,2)); L=sp.zeros(len(pairs))
            for col,P in enumerate(pairs):
                for Q in subpairs:
                    if len(set(P)&set(Q))!=1: continue
                    T=tuple(sorted(set(P)|set(Q)))
                    R=tuple(sorted(set(P)^set(Q)))
                    L[index[R],col]+=sp.Rational(sign[B]*sign[T],2)
            k=degrees[B]; n=m-3
            predicted=(x**comb(n,2)*(x-1)**(n+1-k)*(x+1)**k
                       *(x+sp.Rational(1,2))**(2*(n+1-k))
                       *(x-sp.Rational(1,2))**(2*k))
            assert sp.factor(L.charpoly(x).as_expr()-predicted)==0,(m,bits,B,k)
    print('PEIRCE_MATRIX_OK',m,len(bitstrings),'decorations')

direct_peirce_check(4,range(16))
direct_peirce_check(5,[0,1,37,229,511,730,1023])
print('VERIFY_OK')
