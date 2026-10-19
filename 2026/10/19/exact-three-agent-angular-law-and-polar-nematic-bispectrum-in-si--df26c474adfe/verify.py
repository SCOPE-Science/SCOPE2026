"""Reproduce exact three-site Fourier identities with a finite-state Markov chain.

Run: python verify.py .  Dependencies: numpy and scipy.
Finite-state computations illustrate the identities; the proof in RESULT.md is analytical.
"""
from itertools import product
from fractions import Fraction
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def pair(N, a, c, p, k):
    parity_factor = (2*p-1) if k % 2 else 1
    return c*parity_factor/(N*(a+c*(1-parity_factor))+c*parity_factor)


def triple(N, a, c, p, h):
    assert len(h) == 3 and sum(h) == 0 and all(x != 0 for x in h)
    gamma = [2*p-1 if x % 2 else 1 for x in h]
    vals = [pair(N, a, c, p, x) for x in h]
    top = (c/N)*sum(gamma[i]*(vals[(i+1)%3]+vals[(i+2)%3]) for i in range(3))
    bot = 3*(a+c)-c*(N-2)*sum(gamma)/N
    return top/bot


def two_values(N, a, c, p):
    q=2*p-1
    omega=a+c*(1-q)
    C=c*q/(N*omega+c*q)
    F=c/(N*a+c)
    T=(2*c/N)*(q*F+(q+1)*C)/(3*a+2*c*(1-q)+2*c*(2*q+1)/N)
    E=2*c*c/((N*a+c)*(N*a+2*c))
    return C, F, T, E


def discrete_chain(N, a, c, p, K):
    # An even K-root alphabet permits exact inversion by pi.
    assert K % 2 == 0
    all_states=list(product(range(K), repeat=N))
    index={state:i for i,state in enumerate(all_states)}
    size=len(all_states)
    generator=lil_matrix((size,size),dtype=float)
    for u, state in enumerate(all_states):
        def transition(i, new_symbol, rate):
            new_state=list(state)
            new_state[i]=new_symbol
            v=index[tuple(new_state)]
            if v != u:
                generator[u,v]+=rate
                generator[u,u]-=rate
        for i in range(N):
            for symbol in range(K):
                transition(i,symbol,a/K)
            for j in range(N):
                transition(i,state[j],c*p/N)
                transition(i,(state[j]+K//2)%K,c*(1-p)/N)
    mat=generator.T.tolil()
    mat[-1,:]=np.ones(size)
    rhs=np.zeros(size)
    rhs[-1]=1.0
    stationary=spsolve(mat.tocsc(),rhs)
    assert np.min(stationary)>-1e-11 and abs(stationary.sum()-1)<1e-10
    roots=np.exp(2j*np.pi*np.arange(K)/K)
    return all_states, stationary, roots


def measure(states, weights, roots, exponents):
    return sum(w * np.prod([roots[s[i]]**exponents[i] for i in range(len(exponents))])
               for s,w in zip(states, weights))


def run():
    checked=0
    for N,K in ((3,8),(4,4)):
        for a,c,p in ((.4,1.3,0),(.4,1.3,.3),(.4,1.3,.5),(.4,1.3,1)):
            states,stationary,roots=discrete_chain(N,a,c,p,K)
            triples=((1,1,-2),(1,2,-3),(2,2,-4),(1,3,-4))
            for exps in triples:
                if any(abs(k)>=K for k in exps):
                    continue  # Avoid roots-of-unity aliasing of nonzero circle harmonics.
                value=measure(states,stationary,roots,exps+(0,)*(N-3))
                predicted=triple(N,a,c,p,exps)
                assert abs(value-predicted)<2e-10,(N,a,c,p,exps,value,predicted)
                checked+=1
            for k in (1,2):
                exps=(k,-k)+(0,)*(N-2)
                observed=measure(states,stationary,roots,exps)
                assert abs(observed-pair(N,a,c,p,k))<2e-10
                checked+=1
    for N in (3,4,5,9,101):
        for a,c in ((Fraction(2,5),Fraction(13,10)),(Fraction(21,10),Fraction(7,10))):
            for p in (Fraction(0),Fraction(1,10),Fraction(2,5),Fraction(1,2),Fraction(3,4),Fraction(1)):
                C,F,T,E=two_values(N,a,c,p)
                assert C==pair(N,a,c,p,1)
                assert F==pair(N,a,c,p,2)
                assert T==triple(N,a,c,p,(1,1,-2))
                assert T==triple(N,a,c,p,(1,2,-3))
                assert E==triple(N,a,c,p,(2,2,-4))
                q=2*p-1
                assert (T<0 if q<0 else (T>0 if q>0 else T==0))
                checked+=6
    print(f'PASS: {checked} comparisons, including independent stationary generators and exact rational identities')

if __name__=='__main__':
    run()
