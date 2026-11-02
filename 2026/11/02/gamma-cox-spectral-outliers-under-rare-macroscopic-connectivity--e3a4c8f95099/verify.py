"""Finite exact checks for the Gamma-Cox rare-gap theorem on Pólya threshold graphs.

Run: python verify.py
Only finite identities are checked computationally; the limit theorem needs the proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, gamma, lgamma, exp, log, isclose
import numpy as np

checks = 0

def test(ok, msg):
    global checks
    assert ok, msg
    checks += 1

def rising(x,n):
    o=Fraction(1)
    for j in range(n): o*=x+j
    return o

def beta_seq_prob(a,b,z):
    return rising(a,sum(z))*rising(b,len(z)-sum(z))/rising(a+b,len(z))

def graph_eigens(z):
    n=len(z)
    L=np.zeros((n,n),dtype=float)
    for i in range(n):
        for j in range(i+1,n):
            if z[j]:
                L[i,j]=L[j,i]=-1.0
                L[i,i]+=1.0;L[j,j]+=1.0
    return np.linalg.eigvalsh(L)

def claimed_eigens(z):
    n=len(z)
    return sorted([0]+[j*z[j-1]+sum(z[j:]) for j in range(2,n+1)])

def gap_by_bits(z):
    n=len(z)
    if not z[-1]:return 0
    zeros=[j for j in range(2,n) if not z[j-1]]
    return n-max(zeros) if zeros else n

# Brute-force finite spectral theorem and rare-gap event equivalence, independent of Beta weights.
for n in range(3,11):
    for bits in product((0,1),repeat=n-1):
        z=(0,)+bits   # the first creation draw does not affect the ordinary Laplacian
        computed=graph_eigens(z)
        expected=claimed_eigens(z)
        test(np.max(np.abs(computed-np.array(expected)))<2e-8,
             f'spectrum n={n}, z={z}: {computed} versus {expected}')
        gap=gap_by_bits(z)
        test(abs(computed[1]-gap)<2e-8,f'gap n={n}, z={z}')
        for k in range(1,n):
            event=(gap>=k)
            suffix=all(z[-j] for j in range(1,k+1))
            test(event==suffix,f'rare event n={n}, k={k}, z={z}')

# Exact finite Beta-mixture conditional laws, checked by independent path enumeration.
for a,b in ((1,1),(2,3),(3,1),(1,4)):
    a,b=Fraction(a),Fraction(b)
    for n in range(3,10):
        pairs=[]
        for bits in product((0,1),repeat=n-1):
            z=(0,)+bits
            w=beta_seq_prob(a,b,bits)
            pairs.append((z,w,gap_by_bits(z)))
        test(sum(w for _,w,_ in pairs)==1,f'probabilities n={n}')
        for k in range(1,n):
            selected=[(z,w,gap) for z,w,gap in pairs if gap>=k]
            PE=sum(w for _,w,_ in selected)
            test(PE==rising(a,k)/rising(a+b,k),f'event mass n={n}, k={k}')
            N=n-k-1
            for m in range(N+1):
                direct=sum(w for z,w,g in selected if sum(1-z[j-1] for j in range(2,n-k+1))==m)/PE
                theoretical=Fraction(comb(N,m))*rising(b,m)*rising(a+k,N-m)/rising(a+b+k,N)
                test(direct==theoretical,f'Beta-binomial n={n}, k={k}, m={m}')
            for t in range(k,n):
                mass=sum(w for z,w,g in selected if g>=t)/PE
                theoretical=rising(a+k,t-k)/rising(a+b+k,t-k)
                test(mass==theoretical,f'gap survival n={n}, k={k}, t={t}')
            p_complete=sum(w for z,w,g in selected if g==n)/PE
            test(p_complete==rising(a+k,N)/rising(a+b+k,N),f'complete-graph mass n={n}, k={k}')

# Quantitative approach to Gamma-Poisson and the macroscopic-gap limit from exact formulas.
a,b,theta=2.0,3.0,0.4
for n in (500,3000,12000):
    k=round(theta*n)
    N=n-k-1
    # Probability of no defects converges to theta**b, independent of a.
    logp = sum(log(a+k+j)-log(a+b+k+j) for j in range(N))
    test(abs(exp(logp)-theta**b)<0.017, f'complete atom asymptotic n={n}')
    for s in (0.51,0.7,0.91):
        t=round(s*n)
        q=exp(sum(log(a+k+j)-log(a+b+k+j) for j in range(t-k)))
        test(abs(q-(theta/s)**b)<0.021,f'gap tail asymptotic n={n},s={s}')
    # First factorial moment of number of zeros, compared with the NB limit.
    expectedM=N*b/(a+b+k)
    test(abs(expectedM-b*(1-theta)/theta)<150/n,f'count mean n={n}')

print(f'PASS {checks} deterministic finite and asymptotic sanity assertions')
