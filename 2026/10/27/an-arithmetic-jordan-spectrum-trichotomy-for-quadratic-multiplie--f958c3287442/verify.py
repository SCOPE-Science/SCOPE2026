#!/usr/bin/env python3
"""Independent finite-field tests for the stated degree-two Jordan spectrum.
No external dependencies. The formulas are theorem statements, not certificates for
arbitrary fields; the proof is supplied separately.
"""
from collections import Counter
from itertools import product
import random

EDGE=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def rank_matrix(M, plus, times, inv, minus, zero=0, one=1):
    A=[list(row) for row in M]
    if not A: return 0
    rows,cols=len(A),len(A[0]); r=0
    for j in range(cols):
        ix=next((i for i in range(r,rows) if A[i][j]!=zero),None)
        if ix is None: continue
        A[r],A[ix]=A[ix],A[r]
        scale=inv(A[r][j]); A[r]=[times(scale,z) for z in A[r]]
        for i in range(r+1,rows):
            a=A[i][j]
            if a!=zero:
                A[i]=[plus(v,minus(times(a,u))) for v,u in zip(A[i],A[r])]
        r+=1
        if r==rows: break
    return r

def prime_field(p):
    return (lambda a,b:(a+b)%p,lambda a,b:a*b%p,
            lambda a:pow(a,-1,p),lambda a:(-a)%p)

def pair_field9():
    # F3[t]/(t^2+1); represent a+bt by a+3b.
    def dec(a):return a%3,a//3
    def add(a,b):
        x,y=dec(a);u,v=dec(b)
        return (x+u)%3+3*((y+v)%3)
    def mul(a,b):
        x,y=dec(a);u,v=dec(b)
        return (x*u+2*y*v)%3+3*((x*v+y*u)%3)
    invtab={a:next(b for b in range(1,9) if mul(a,b)==1) for a in range(1,9)}
    def inv(a):return invtab[a]
    def minus(a):return add(0,mul(2,a))
    return add,mul,inv,minus

def predicted(q):
    r=q-1;w=2*q-1
    t=1 if q%3==0 else (2 if q%3==1 else 0)
    R20=6*r+12*r*r+4*r**3
    R21=3*r**3
    D=w**3+3*r*w*r**2+r*(q-2)*r**3
    DH=w**3+t*r**4
    H0=q**5+(q-1)*q**2
    ans={(0,True):1, (2,True):R20, (2,False):R21,
         (3,True):DH-1-R20, (3,False):D-DH-R21,
         (4,True):H0-DH, (4,False):q**6-H0-D+DH}
    assert all(v>0 for v in ans.values()) and sum(ans.values())==q**6
    return ans

def spectrum_from_coefs(coefs,add,mul,inv,minus):
    # coefs follow pairs 01,02,03,12,13,23, independent of B labeling.
    M=[[0]*4 for _ in range(4)]
    for (i,j),a in zip(EDGE,coefs):
        comp=[v for v in range(4) if v not in (i,j)]
        M[comp[0]][comp[1]]=M[comp[1]][comp[0]]=a
    rank=rank_matrix(M,add,mul,inv,minus)
    H=add(add(mul(coefs[0],coefs[5]),mul(coefs[1],coefs[4])),mul(coefs[2],coefs[3]))
    return rank,H==0

def full_multiplication_ranks(coefs,add,mul,inv,minus):
    # Literal squarefree multiplication in the 16-dimensional algebra.
    A=[[0]*16 for _ in range(16)]
    for m in range(16):
        for (i,j),a in zip(EDGE,coefs):
            bit=(1<<i)|(1<<j)
            if not (m&bit): A[m|bit][m]=add(A[m|bit][m],a)
    A2=[[0]*16 for _ in range(16)]
    for i in range(16):
        for k in range(16):
            if A[i][k]:
                for j in range(16):
                    if A[k][j]:A2[i][j]=add(A2[i][j],mul(A[i][k],A[k][j]))
    r1=rank_matrix(A,add,mul,inv,minus)
    r2=rank_matrix(A2,add,mul,inv,minus)
    return r1,r2

def do_field(q,field,complete=False):
    add,mul,inv,minus=field
    seq=product(range(q),repeat=6) if complete else (tuple(random.Random(q*133+i).randrange(q) for i in range(6)) for _ in [])
    if not complete:
        rng=random.Random(12345+q)
        seq=[tuple(rng.randrange(q) for _ in range(6)) for _ in range(2400)]
    count=Counter()
    actual_check=0
    for ix,coef in enumerate(seq):
        r,zero=spectrum_from_coefs(coef,add,mul,inv,minus)
        count[(r,zero)]+=1
        if (q==3 and complete) or (ix%7==0 and actual_check<360):
            r1,r2=full_multiplication_ranks(coef,add,mul,inv,minus)
            assert (r1,r2)==((r+2 if r else 0),int(not zero)),(q,coef,r,zero,r1,r2)
            actual_check+=1
    if complete: assert count==predicted(q),(q,count,predicted(q))
    print('field',q,'complete',complete,'tuples',sum(count.values()),'literal_multiplication_checks',actual_check,'distribution',dict(sorted(count.items())))

def check_f9_weighted():
    add,mul,inv,minus=pair_field9();q=9
    vals=[]
    for x,y,z in product(range(q),repeat=3):
        D=add(add(mul(x,x),mul(y,y)),mul(z,z))
        xy=add(add(mul(x,y),mul(x,z)),mul(y,z))
        D=add(D,minus(mul(2,xy)))
        h=add(add(x,y),z)
        w=(lambda a:(2*q-1 if a==0 else q-1))
        wt=w(x)*w(y)*w(z)
        vals.append((D==0,h==0,wt))
    D=sum(w for d,h,w in vals if d)
    DH=sum(w for d,h,w in vals if d and h)
    HH=sum(w for d,h,w in vals if h)
    r=q-1;w=2*q-1
    assert D==w**3+3*r*w*r**2+r*(q-2)*r**3
    assert DH==w**3+r**4  # characteristic three
    assert HH==q**5+(q-1)*q**2
    print('F9_weighted_D_DH_H',D,DH,HH)

if __name__=='__main__':
    for q in (3,5,7): do_field(q,prime_field(q),True)
    do_field(9,pair_field9(),False)
    check_f9_weighted()
    print('VERIFY_OK_DEGREE_TWO_SQUAREFREE_JORDAN')
