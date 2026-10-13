#!/usr/bin/env python3
"""Finite independent test of a generalized sum-rank MacWilliams transform.

Uses GF(4), two rank-support blocks, an arbitrary 2-dimensional code and
its independently computed Euclidean dual. Enumerates subcodes and all
25 pairs of base-field support spaces; exact integer arithmetic only.
"""
from itertools import product, combinations
from collections import Counter, defaultdict
from math import prod

Q=4

def mul(a,b):
    c=0
    for i in range(2):
        if b&(1<<i): c^=a<<i
    if c&4: c^=7  # polynomial t^2+t+1
    return c

def sc(a,u):return tuple(mul(a,x) for x in u)
def plus(u,v):return tuple(x^y for x,y in zip(u,v))
def dot(u,v):
    r=0
    for x,y in zip(u,v):r^=mul(x,y)
    return r

def span(gs):
    w={tuple(0 for _ in gs[0])}
    for g in gs:
        w={plus(x,sc(a,g)) for x in w for a in range(4)}
    return frozenset(w)

def gaussian(a,b,z):
    if b<0 or a<0 or b>a:return 0
    t=prod(z**(a-j)-1 for j in range(b))
    u=prod(z**(b-j)-1 for j in range(b))
    assert t%u==0
    return t//u

def dim2_space(U):
    return len(U).bit_length()-1

def binary_spaces_2():
    return [frozenset({(0,0)}),frozenset({(0,0),(1,0)}),
            frozenset({(0,0),(0,1)}),frozenset({(0,0),(1,1)}),
            frozenset(product(range(2),repeat=2))]

def binary_rank(rows):
    base={}
    for x in rows:
        while x:
            pivot=x.bit_length()-1
            if pivot in base:x^=base[pivot]
            else:base[pivot]=x;break
    return len(base)

def profile(code):
    ans=[]
    for i in (0,2):
        rows=[sum(((v[i+j]>>b)&1)<<j for j in range(2))
              for v in code for b in range(2)]
        ans.append(binary_rank(rows))
    return tuple(ans)

def contained(word,L):
    for block in range(2):
        a,b=word[2*block:2*block+2]
        if (a&1,b&1) not in L[block] or ((a>>1)&1,(b>>1)&1) not in L[block]:
            return False
    return True

def subcode_spectra(C):
    Z=frozenset({(0,0,0,0)})
    line_set={span([w]) for w in C if w!=(0,0,0,0)}
    assert len(line_set)==5
    two_set={frozenset(C)}
    return {0:Counter({(0,0):1}),
            1:Counter(profile(s) for s in line_set),
            2:Counter(profile(s) for s in two_set)}

def binom_moments(C):
    B=defaultdict(lambda:[0]*3)
    for L in product(binary_spaces_2(),repeat=2):
        s=tuple(dim2_space(U) for U in L)
        x=sum(contained(w,L) for w in C)
        assert x in (1,4,16)
        a={1:0,4:1,16:2}[x]
        for r in range(3): B[s][r]+=gaussian(a,r,Q)
    return dict(B)

def psi(B,s):
    return [Q**(r*(r-1)//2)*v for r,v in enumerate(B[s])]

def mulpoly(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans

def P(delta):
    p=[1]
    for j in range(delta):p=mulpoly(p,[1,Q**j])
    return p

def verify(C):
    M=binom_moments(C)
    exact=subcode_spectra(C)
    for r in range(3):
        for s in product(range(3),repeat=2):
            rhs=sum(v*prod(gaussian(2-t,s_i-t,2) for t,s_i in zip(tup,s))
                    for tup,v in exact[r].items() if all(t<=si for t,si in zip(tup,s)))
            assert M[s][r]==rhs,(s,r,M[s][r],rhs)
    return M

def check():
    gens=[(1,0,2,1),(0,2,1,1)]
    C=span(gens)
    dual=frozenset(w for w in product(range(4),repeat=4) if all(dot(w,g)==0 for g in gens))
    assert len(C)==len(dual)==16 and all(dot(w,v)==0 for w in C for v in dual)
    A=verify(C)
    B=verify(dual)
    for s in product(range(3),repeat=2):
        delta=2+sum(s)-4
        other=tuple(2-i for i in s)
        if delta>=0:
            lhs=psi(A,s)
            rhs=mulpoly(P(delta),[x*Q**(j*delta) for j,x in enumerate(psi(B,other))])
        else:
            lhs=psi(B,other)
            rhs=mulpoly(P(-delta),[x*Q**(j*(-delta)) for j,x in enumerate(psi(A,s))])
        M=max(len(lhs),len(rhs))
        assert lhs+[0]*(M-len(lhs))==rhs+[0]*(M-len(rhs)),(s,delta,lhs,rhs)
    # Includes positive, zero, negative delta and every rank 0,1,2.
    print('block profiles: 9; base-field support-space pairs: 25')
    print('all duality shifts: -2,-1,0,1,2')
    print('exact subcode-to-moment transforms checked at ranks 0,1,2')
    print('VERIFY_OK')
if __name__=='__main__':check()
