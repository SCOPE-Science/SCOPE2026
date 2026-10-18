#!/usr/bin/env python3
"""Exact independent-pattern-count polynomial comparison, plus overlap witness."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb


def cross_bifix_free(code):
    if not code: return False
    L = len(code[0]); assert all(len(w)==L for w in code)
    return all(u[-h:]!=v[:h] for u in code for v in code for h in range(1,L))


def multiply(A,B):
    out=[F(0)]*(len(A)+len(B)-1)
    for j,a in enumerate(A):
        for k,b in enumerate(B):out[j+k]+=a*b
    return out


def add(A,B):
    out=[F(0)]*max(len(A),len(B))
    for i,x in enumerate(A):out[i]+=x
    for i,x in enumerate(B):out[i]+=x
    return out


def distribution(alphabet, row_probs, code):
    n=len(row_probs); L=len(code[0]); out=[F(0)]*(n-L+2)
    for s in product(range(len(alphabet)),repeat=n):
        pr=F(1)
        for i,c in enumerate(s): pr*=row_probs[i][c]
        t=tuple(alphabet[c] for c in s)
        count=sum(t[i:i+L] in code for i in range(n-L+1))
        out[count]+=pr
    return out


def via_nonoverlap(alphabet,row_probs,code):
    n=len(row_probs);L=len(code[0]); r=n-L+1
    a=[]
    for i in range(r):
        q=F(0)
        for w in code:
            t=F(1)
            for j,c in enumerate(w):t*=row_probs[i+j][alphabet.index(c)]
            q+=t
        a.append(q)
    # coefficients E binom(N,k)
    W=[F(0)]*(r+1)
    for k in range(r+1):
        for starts in combinations(range(r),k):
            if any(v-u<L for u,v in zip(starts,starts[1:])):continue
            s=F(1)
            for i in starts:s*=a[i]
            W[k]+=s
    out=[F(0)]*(r+1)
    for k,v in enumerate(W):
        for j in range(k+1):out[j]+=v*comb(k,j)*(-1)**(k-j)
    return out


def test():
    cases=0
    for code in [(('0','0','1'),),(('0','1'),),(('0','0','1'),('0','2','1')),(('0','1'),('0','2'))]:
        A=('0','1') if all('2' not in w for w in code) else ('0','1','2')
        assert cross_bifix_free(code)
        L=len(code[0]); base=[F(1,2)]*2 if len(A)==2 else [F(1,6),F(1,3),F(1,2)]
        for n in range(L,min(L+5,9)):
            for choice in range(5):
                row=[]
                for i in range(n):
                    if len(A)==2:
                        p=F((i*3+choice*5)%9+1,11)
                        row.append((p,1-p))
                    else:
                        x=F((i+choice)%3+1,12)
                        y=F((2*i+choice)%4+1,12)
                        row.append((x,y,1-x-y))
                actual=distribution(A,row,tuple(tuple(w) for w in code))
                pred=via_nonoverlap(A,row,tuple(tuple(w) for w in code))
                assert actual==pred[:len(actual)],(code,n,choice,actual,pred)
                assert all(v>=0 for v in pred)
                assert sum(pred)==1
                cases+=1
    for L in range(2,13):
        for p in (F(1,5),F(1,2),F(4,5)):
            em=2*p**L
            ebinom=p**(L+1)
            assert em**2-4*ebinom<0
    # stationary closed form check for pattern 001 with n in 3..15
    for L in (2,3,4,5):
        for n in range(L,25):
            c=F(1,2)**L
            for k in range(n//L+1):
                assert sum(1 for s in combinations(range(n-L+1),k) if all(v-u>=L for u,v in zip(s,s[1:])))==comb(n-(L-1)*k,k)
    print('PASS',cases,'exact enumerative comparisons;',11*3,'overlap impossibility cases; stationary formula placement counts')

if __name__=='__main__':test()

def min_period(w):
    L=len(w)
    return next((s for s in range(1,L) if w[:-s]==w[s:]),None)

def check_border_thresholds():
    trials=0
    for L in range(2,7):
      for w in product(('0','1'),repeat=L):
       s=min_period(w)
       if s is None: continue
       n=L+s
       for p in (F(1,4),F(1,2),F(3,4)):
        law=[(1-p,p)]*n
        dist=distribution(('0','1'),law,(w,))
        q=F(1)
        for c in w:q*=p if c=='1' else 1-p
        pref=F(1)
        for c in w[:L-s]: pref*=p if c=='1' else 1-p
        assert all(u==0 for u in dist[3:])
        assert sum(k*x for k,x in enumerate(dist)) == (s+1)*q
        assert dist[2]==q*q/pref
        discriminant=dist[1]**2-4*dist[0]*dist[2]
        assert (discriminant>=0)==(pref*(s+1)**2>=4)
        trials+=1
    print('PASS',trials,'exact borderline word/discriminant and all-support tests')

if __name__=='__main__': check_border_thresholds()
