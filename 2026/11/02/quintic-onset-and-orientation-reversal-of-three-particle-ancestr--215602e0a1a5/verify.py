#!/usr/bin/env python3
"""Standalone, standard-library exact-rational certificate for a local Fleming--Viot ancestral current.

Reproduces the 10 population-count equations and the 18 one-founder equations
for three particles on the unit-rate motion triangle. No external data required.
"""
from fractions import Fraction as F
from itertools import product

N=3
E=tuple(tuple(int(i==j) for i in range(3)) for j in range(3))
COUNT=tuple((i,j,3-i-j) for i in range(4) for j in range(4-i))
OTHER=tuple((i,j,2-i-j) for i in range(3) for j in range(3-i))
FOUND=tuple((i,d) for i in range(3) for d in OTHER)
COUNT_ID={s:i for i,s in enumerate(COUNT)}
FOUND_ID={s:i for i,s in enumerate(FOUND)}
ANCHOR=FOUND_ID[(0,(2,0,0))]

def changed(s,a,b):
    return tuple(s[t]-E[a][t]+E[b][t] for t in range(3))

def mat(n):return [[F(0) for _ in range(n)] for _ in range(n)]

def population(k):
    m=mat(len(COUNT))
    for row,c in enumerate(COUNT):
        for a in range(3):
            if not c[a]:continue
            for b in range(3):
                if b==a:continue
                rate=F(c[a])*(1+F(c[b])*k[a]/(N-1))
                m[row][COUNT_ID[changed(c,a,b)]]+=rate
                m[row][row]-=rate
    return m

def founder(k):
    m=mat(len(FOUND))
    for row,(i,d) in enumerate(FOUND):
        for j in range(3):
            if j==i:continue
            m[row][FOUND_ID[(j,d)]]+=1
            m[row][row]-=1
        m[row][row]-=k[i]
        for a in range(3):
            if not d[a]:continue
            for b in range(3):
                if a==b:continue
                rate=F(d[a])*(1+F(d[b])*k[a]/(N-1))
                m[row][FOUND_ID[(i,changed(d,a,b))]]+=rate
                m[row][row]-=rate
            rate=F(d[a])*k[a]/(N-1)
            m[row][FOUND_ID[(i,changed(d,a,i))]]+=2*rate
            m[row][row]-=rate
    return m

def subtract(a,b):return [[u-v for u,v in zip(x,y)] for x,y in zip(a,b)]
def transpose(a):return list(map(list,zip(*a)))
def mv(a,x):return [sum(p*q for p,q in zip(row,x)) for row in a]

def inverse(a):
    n=len(a);aug=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        piv=next(i for i in range(j,n) if aug[i][j])
        aug[piv],aug[j]=aug[j],aug[piv]
        v=aug[j][j]
        aug[j]=[x/v for x in aug[j]]
        for i in range(n):
            if i==j:continue
            v=aug[i][j]
            if v:aug[i]=[x-v*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]

def multiply(a,b):return [sum(x*y for x,y in zip(u,b)) for u in a]

def delta(pi,h):
    out=F(0)
    for c in COUNT:
        for i,j,sgn in ((0,2,1),(2,0,-1)):
            if c[i]:
                d=tuple(c[t]-E[i][t] for t in range(3))
                out+=sgn*pi[COUNT_ID[c]]*c[i]*h[FOUND_ID[(j,d)]]
    return out

def adjusted(M,j):
    m=[row[:] for row in M]
    m[j]=[F(int(i==j)) for i in range(len(M))]
    return m

def stationary_adjusted(M):
    m=[row[:] for row in M]
    m[0]=[F(1)]*len(M)
    return m

def main():
    k0=[F(1)]*3;direction=[F(-1),F(0),F(1)]
    L0=population(k0)
    L1=subtract(population(direction),population([F(0)]*3))
    T0=founder(k0)
    T1=subtract(founder(direction),founder([F(0)]*3))
    invP=inverse(stationary_adjusted(transpose(L0)))
    invH=inverse(adjusted(T0,ANCHOR))
    pis=[];hs=[];coeff=[]
    for d in range(6):
        if d==0:
            bp=[F(1)]+[F(0)]*(len(COUNT)-1)
            bh=[F(int(i==ANCHOR),3) for i in range(len(FOUND))]
        else:
            bp=[-t for t in mv(transpose(L1),pis[-1])]
            bh=[-t for t in mv(T1,hs[-1])]
            bp[0]=F(0);bh[ANCHOR]=F(0)
        pis.append(multiply(invP,bp));hs.append(multiply(invH,bh))
        assert (sum(pis[d])==F(int(d==0)))
        assert hs[d][ANCHOR]==F(int(d==0),3)
        coeff.append(sum(delta(pis[j],hs[d-j]) for j in range(d+1)))
    print('Taylor coefficients through degree five:',[str(x) for x in coeff])
    assert coeff==[F(0)]*5+[F(89,56010528)]

    # Full nonperturbative cross-check with the published exact three-particle instance.
    k=[F(1),F(2),F(4)]
    p=multiply(inverse(stationary_adjusted(transpose(population(k)))),[F(1)]+[F(0)]*(len(COUNT)-1))
    b=[F(int(i==ANCHOR),3) for i in range(len(FOUND))]
    h=multiply(inverse(adjusted(founder(k),ANCHOR)),b)
    assert delta(p,h)==F(421413160,139117744582101)
    print('Exact published benchmark:',delta(p,h))
    print('PASS: quintic coefficient and published full-system benchmark')

if __name__=='__main__':main()
