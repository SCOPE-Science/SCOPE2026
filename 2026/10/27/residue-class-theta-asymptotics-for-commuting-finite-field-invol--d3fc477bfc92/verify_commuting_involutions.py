"""Standalone exact checks for commuting involutions over prime finite fields."""
from fractions import Fraction
from itertools import product
from math import prod, comb

def matmul(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def involution_mats(n,q):
    ident=tuple(int(i==j) for i in range(n) for j in range(n))
    return [M for M in product(range(q),repeat=n*n) if matmul(M,M,n,q)==ident]

def gl(n,q):
    return prod((q**n-q**k) for k in range(n))

def counts(n,q):
    G=[gl(k,q) for k in range(n+1)]
    INV=sum(gl(n,q)//(G[k]*G[n-k]) for k in range(n+1))
    PAIRS=0
    for a in range(n+1):
      for b in range(n-a+1):
       for c in range(n-a-b+1):
        d=n-a-b-c
        PAIRS+=gl(n,q)//(G[a]*G[b]*G[c]*G[d])
    return INV,PAIRS

def theta_constants(q,rho,K=22):
    import math
    infprod=prod(1-q**(-j) for j in range(1,150))
    # center over two-variable theta, 3-var theta
    eps=rho%2
    theta=sum(q**(-2*(k-eps/2)**2) for k in range(-K,K+1))
    psi=0.0
    for a in range(-K,K+1):
      for b in range(-K,K+1):
       for c in range(-K,K+1):
        d=rho-a-b-c
        if abs(d)>K:continue
        psi+=q**(-(sum((v-rho/4)**2 for v in (a,b,c,d))))
    return psi/(infprod*theta*theta)

def main():
    brute=0
    for q,n in ((3,1),(3,2),(3,3),(5,1),(5,2),(7,1)):
        mats=involution_mats(n,q)
        count=sum(matmul(A,B,n,q)==matmul(B,A,n,q) for A in mats for B in mats)
        expectedI,expectedP=counts(n,q)
        assert len(mats)==expectedI,(q,n,len(mats),expectedI)
        assert count==expectedP,(q,n,count,expectedP)
        brute+=len(mats)**2
        print(f'brute q={q} n={n} involutions={len(mats)} commuting_pairs={count}')
    for q in (3,5,7):
      for n in range(1,17):
        one,two=counts(n,q)
        assert 0<two<=one*one
      for rho in range(4):
        K=theta_constants(q,rho)
        ns=[rho+4*k for k in range(1,11)]
        ns=[n for n in ns if n>=4]
        errors=[]
        for n in ns:
          one,two=counts(n,q)
          # avoid float overflow rational, convert via logarithms
          import math
          scaled=math.exp(math.log(two)-2*math.log(one)+(n*n/4)*math.log(q))
          errors.append(abs(scaled/K-1))
        assert errors[-1]<0.0005,(q,rho,errors)
        print(f'asymptotic q={q} residue={rho} K={K:.12g} final_rel_error={errors[-1]:.4g}')
    print(f'ALL_COMMUTING_INVOLUTIONS_CHECKS_PASSED brute_ordered_pairs={brute} exact_count_cases=48 asymptotic_sequences=12')
if __name__=='__main__':main()
