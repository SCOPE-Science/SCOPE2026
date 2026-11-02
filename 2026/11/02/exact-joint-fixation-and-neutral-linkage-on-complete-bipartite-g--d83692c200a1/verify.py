#!/usr/bin/env python3
"""Independent reproducibility for the neutral, shared-neighbor two-trait model.

Requires only Python standard library, numpy, scipy. Tests full forward absorption
chains, without using the ancestral reduction in constructing forward transitions.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def weights(a,b):
    d=4*a*b+a+b
    return [F(a+3*b,2*d), F(b*(a-1),d), F(3*a+b,2*d),F(a*(b-1),d),F(a*b,d),F(a*b,d)]


def pair_distribution(a,b):
    # Coordinate order is strategy's initial source index and game's initial source index.
    n=a+b; W=weights(a,b)
    out=np.zeros((n,n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i<a and j<a:
                out[i,j]=float(W[0])/a if i==j else float(W[1])/(a*(a-1))
            elif i>=a and j>=a:
                out[i,j]=float(W[2])/b if i==j else float(W[3])/(b*(b-1))
            else:
                out[i,j]=float(W[4] if i<a else W[5])/(a*b)
    assert abs(out.sum()-1)<1e-12
    return out


def forward_all(a,b):
    n=a+b
    assert n<=4
    z=4**n
    Q=lil_matrix((z,z),dtype=float)
    absorbing={}
    for state in range(z):
        vals=[(state//(4**i))%4 for i in range(n)]
        sa=[v%2 for v in vals]; ga=[v//2 for v in vals]
        if len(set(sa))==len(set(ga))==1:
            absorbing[state]=(sa[0],ga[0]); continue
        Q[state,state]=1
        for focal in range(n):
            neighbors=range(a,n) if focal<a else range(a)
            for model in neighbors:
                for cs,cg in product((0,1),repeat=2):
                    new=vals.copy()
                    new[focal]=(sa[model] if cs else sa[focal])+2*(ga[model] if cg else ga[focal])
                    target=sum(v*(4**i) for i,v in enumerate(new))
                    p=1/(n*len(neighbors)*4)
                    Q[state,target]-=p
    transient=[i for i in range(z) if i not in absorbing]
    idx={x:i for i,x in enumerate(transient)}
    # reconstruct from forward chain; compute probability of each (strategy,game) final outcome
    A=Q.tocsr()[transient,:][:,transient]
    results={}
    for s,g in product((0,1),repeat=2):
        rhs=np.array([-sum(Q[i,j] for j in absorbing if absorbing[j]==(s,g)) for i in transient], dtype=float)
        vals=spsolve(A,rhs)
        for i,v in zip(transient,vals):
            results[(i,s,g)]=v
        for i,xy in absorbing.items():
            results[(i,s,g)]=float(xy==(s,g))
    return results


def main():
    exhaustive_cases=0
    for a,b in [(1,1),(1,2),(2,1),(1,3),(2,2),(3,1)]:
        n=a+b; U=pair_distribution(a,b)
        forward=forward_all(a,b)
        for st in range(4**n):
            vals=[(st//(4**i))%4 for i in range(n)]
            s=np.array([v%2 for v in vals]);g=np.array([v//2 for v in vals])
            for ss,gg in product((0,1),repeat=2):
                expected=sum(U[i,j] for i in range(n) for j in range(n) if s[i]==ss and g[j]==gg)
                diff=abs(expected-forward[st,ss,gg])
                assert diff<3e-10,(a,b,st,ss,gg,expected,forward[st,ss,gg],diff)
                exhaustive_cases+=1
    for a in range(1,15):
        for b in range(1,15):
            w=weights(a,b)
            assert sum(w)==1
            assert w[4]==w[5]
            assert 3*w[0]==w[2]+4*w[4]/a
            assert 3*w[2]==w[0]+4*w[4]/b
            assert w[1]==w[4]*(a-1)/a
            assert w[3]==w[4]*(b-1)/b
            assert w[0]+w[2]==F(2*(a+b),4*a*b+a+b)
    print('VERIFIED full-forward-exhaustive comparisons',exhaustive_cases)
    print('VERIFIED exact lumped-stationarity and normalization',14*14)

if __name__=='__main__':main()
