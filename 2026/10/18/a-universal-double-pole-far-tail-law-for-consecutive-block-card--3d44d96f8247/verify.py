#!/usr/bin/env python3
"""Exact-rational finite checks for the consecutive-block merger tail theorem.
Run: python3 verify.py. Requires only Python standard library.
Checks complement, but do not replace, the proof for arbitrary starting size.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial

def coefficients(N):
    a=[0]*(N+1); a[0]=a[1]=1
    for j in range(2,N+1):
        a[j]=j*a[j-1]+(j-1)*a[j-2]
    p={}
    for n in range(2,N+1):
        p[n]={k:F(comb(n-1,k-1)*a[k-1],factorial(n)) for k in range(1,n+1)}
        assert sum(p[n].values())==1
    return p

def asymptotic_coefficients(p):
    nmax=max(p); aa={2:F(0),3:F(2,3)}; bb={2:F(1),3:F(1)}
    for n in range(4,nmax+1):
        q=p[n][n]; assert q<F(1,2)
        aa[n]=2*sum(p[n][k]*aa[k] for k in range(2,n))/(1-2*q)
        bb[n]=(2*sum(p[n][k]*(bb[k]-aa[k]) for k in range(2,n))-2*q*aa[n])/(1-2*q)
    return aa,bb

def survival(p,n,T):
    # Independent finite-state Markov propagation, without using the asymptotic formula.
    mass={n:F(1)}; out=[]
    for t in range(T+1):
        out.append(sum(v for k,v in mass.items() if k>=2))
        nxt={}
        for k,v in mass.items():
            if k==1: nxt[1]=nxt.get(1,F(0))+v
            else:
                for j,z in p[k].items(): nxt[j]=nxt.get(j,F(0))+v*z
        mass=nxt
        assert sum(mass.values())==1
    return out

def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def annihilated(seq,roots):
    poly=[F(1)]
    for r in roots: poly=multiply(poly,[-r,F(1)])
    for t in range(len(seq)-len(poly)+1):
        assert sum(poly[j]*seq[t+j] for j in range(len(poly)))==0,(t,roots)
    return len(seq)-len(poly)+1

def main():
    P=coefficients(11); aa,bb=asymptotic_coefficients(P)
    c=0
    for n in range(2,8):
        hist={j:0 for j in range(1,n+1)}
        for perm in permutations(range(1,n+1)):
            j=n-sum(perm[i+1]==perm[i]+1 for i in range(n-1))
            hist[j]+=1
        for j in range(1,n+1):
            assert F(hist[j],factorial(n))==P[n][j]
            c+=1
    assert P[3][2]==F(1,3) and P[2][2]==P[3][3]==F(1,2)
    assert P[4][4]==F(11,24)
    assert (aa[4],bb[4])==(F(6),F(-60))
    assert (aa[5],bb[5])==(F(276,7),F(-34886,49))
    for n in range(2,11):
        s=survival(P,n,50)
        assert s[0]==1
        assert all(s[t]>=s[t+1] for t in range(50))
        for t in range(51):
            if n==2: assert s[t]==F(1,2)**t
            if n==3: assert s[t]==(1+F(2,3)*t)*F(1,2)**t
            if n==4: assert s[t]==(6*t-60)*F(1,2)**t+61*F(11,24)**t
            c+=1
        residual=[s[t]-(aa[n]*t+bb[n])*F(1,2)**t for t in range(51)]
        roots=[P[j][j] for j in range(4,n+1)]
        if n>=4:
            c+=annihilated(residual,roots)
            assert aa[n]>0
        else: assert not any(residual)
        roots_all=[F(1,2)]*(1 if n==2 else 2)+roots
        c+=annihilated(s,roots_all)
    for n in range(4,12):
        assert F(0)<P[n][n]<=F(11,24)<F(1,2)
        if n>=5: assert P[n][n]<P[n-1][n-1]
        c+=1
    print('VERIFICATION_OK', c,'exact checks')
    print('n q_n alpha_n beta_n')
    for n in range(2,7): print(n,str(P[n][n]),str(aa[n]),str(bb[n]))

if __name__=='__main__': main()
