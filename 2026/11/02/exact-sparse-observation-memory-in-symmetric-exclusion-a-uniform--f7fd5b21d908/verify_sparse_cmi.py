#!/usr/bin/env python3
"""Finite-state and spectral checks for half-filled exclusion memory."""
import itertools, math
import numpy as np
from scipy.linalg import expm
from scipy.special import i0e

checks = 0

def check(ok, msg):
    global checks
    checks += 1
    if not ok: raise AssertionError(msg)

def F(a,b):
    if not (0 <= a < 1 and 0 <= b < 1 and 1+2*a+b>0 and 1-2*a+b>0):
        raise ValueError((a,b))
    z=[(1+2*a+b,(1+a)**2), (1-2*a+b,(1-a)**2), (1-b,1-a*a)]
    return (z[0][0]*math.log(z[0][0]/z[0][1])+z[1][0]*math.log(z[1][0]/z[1][1])+2*z[2][0]*math.log(z[2][0]/z[2][1]))/4

def states(L,N=None):
    return [x for x in itertools.product((0,1),repeat=L) if N is None or sum(x)==N]

def generator(ss, edges):
    d={s:i for i,s in enumerate(ss)}; G=np.zeros((len(ss),len(ss)))
    for i,s in enumerate(ss):
        for x,y,rate in edges:
            if s[x]==s[y]:continue
            new=list(s);new[x],new[y]=new[y],new[x]
            j=d[tuple(new)];G[i,j]+=rate;G[i,i]-=rate
    return G

def three_moment_from_matrix(ss,G,t,x=0):
    P=expm(t*G);n=len(ss);wt=1/n
    triples=np.zeros((2,2,2))
    for i,s in enumerate(ss):
        for j,u in enumerate(ss):
            for k,v in enumerate(ss):
                triples[s[x],u[x],v[x]]+=wt*P[i,j]*P[j,k]
    # independence of middle sign via complement symmetry
    p=triples.sum(axis=(1,2))
    check(np.allclose(p,[.5,.5],atol=1e-11), 'halffilled marginal')
    cv=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            cv[i,j]=sum(triples[u,v,w]*[(2*u-1),(2*v-1),(2*w-1)][i]*[(2*u-1),(2*v-1),(2*w-1)][j] for u,v,w in itertools.product((0,1),repeat=3))
    a,b=cv[0,1],cv[0,2]
    info=0.0
    for u,v,w in itertools.product((0,1),repeat=3):
        p3=triples[u,v,w];p12=triples.sum(axis=2)[u,v];p23=triples.sum(axis=0)[v,w];pm=triples.sum(axis=(0,2))[v]
        if p3>0:info+=p3*math.log((p3*pm)/(p12*p23))
    return a,b,info

for L in [4,6]:
    edges=[(i,(i+1)%L,1.0) for i in range(L)]
    for n in [None,L//2]:
        ss=states(L,n);G=generator(ss,edges)
        for t in [.11, .6, 1.8]:
            a,b,I=three_moment_from_matrix(ss,G,t)
            check(abs(I-F(a,b))<2e-11,(L,n,t,I,F(a,b)))
            lap=np.zeros((L,L))
            for i,j,w in edges:lap[i,j]+=w;lap[j,i]+=w;lap[i,i]-=w;lap[j,j]-=w
            pp=expm(t*lap)[0,0];qq=expm(2*t*lap)[0,0]
            aa=pp if n is None else (L*pp-1)/(L-1)
            bb=qq if n is None else (L*qq-1)/(L-1)
            check(abs(a-aa)<1e-11 and abs(b-bb)<1e-11, (a,b,aa,bb))
            check(I>0,'ring memory strictly positive')

# Complete-graph half-filled canonical process is an exact binary Markov chain.
L=6; ss=states(L,L//2);edges=[(i,j,.7) for i in range(L) for j in range(i+1,L)]
for t in [.1,.7,2.5]:
    a,b,I=three_moment_from_matrix(ss,generator(ss,edges),t)
    check(abs(b-a*a)<1e-11 and abs(I)<1e-11,'complete graph canonical Markov')
# Uniform hub but irregular non-hub subgraph: still binary Markov.
edges=[(0,j,.9) for j in range(1,L)]+[(1,2,.3),(2,3,1.1)]
for t in [.1, .7]:
    a,b,I=three_moment_from_matrix(ss,generator(ss,edges),t)
    check(abs(b-a*a)<1e-11 and abs(I)<1e-11,'uniform hub Markov')
# Breaking one hub conductance reintroduces strictly positive memory.
edges[0]=(0,1,1.0)
for t in [.1,.7]:
    a,b,I=three_moment_from_matrix(ss,generator(ss,edges),t)
    check(b>a*a and I>1e-10,'nonuniform hub non-Markov')

# Ring continuum / finite-size scaling and grand/canonical charge crossover.
D=1.0
for L in [60,120,240,480]:
    eig=2*D*(1-np.cos(2*np.pi*np.arange(L)/L))
    for c in [.12,.4,1.2]:
        t=c*L*L
        S1=np.exp(-eig*t).sum();S2=np.exp(-eig*2*t).sum()
        aG=S1/L;bG=S2/L
        aC=(S1-1)/(L-1);bC=(S2-1)/(L-1)
        theta2=sum(math.exp(-8*math.pi**2*D*c*k*k) for k in range(-10,11))
        check(abs(L*L*F(aG,bG) - theta2*theta2/2)<.15,(L,c,'G'))
        check(abs(L*L*F(aC,bC) - (theta2-1)**2/2)<.15,(L,c,'C'))
for t in [50,100,400,1600]:
    a=i0e(2*D*t);b=i0e(4*D*t)
    check(abs((t*F(a,b))/(1/(16*math.pi*D))-1)<.15,(t,F(a,b)))

print('PASS',checks,'checks: finite-state joint laws, graph criterion, theta crossover, Bessel coefficient')
