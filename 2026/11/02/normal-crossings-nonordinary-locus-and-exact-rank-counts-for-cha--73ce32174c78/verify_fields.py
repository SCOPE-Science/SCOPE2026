#!/usr/bin/env python3
"""Independent finite-field enumeration for characteristic-three Ciani quartics.

Fields are represented by polynomials over F3, with irreducible moduli
x+0 (degree one), x^2+1 (degree two), x^3-x-1 (degree three).
The count uses only the smoothness discriminant and three scalar Hasse tests,
not symbolic computer algebra or precomputed strata.
"""
from collections import Counter
from itertools import product

def field(n):
    q=3**n
    mod={1:(0,1),2:(1,0,1),3:(2,2,0,1)}[n]
    coeff=[tuple((v//(3**j))%3 for j in range(n)) for v in range(q)]
    def pack(c):return sum((x%3)*3**j for j,x in enumerate(c))
    add=[[pack([(coeff[a][j]+coeff[b][j])%3 for j in range(n)]) for b in range(q)] for a in range(q)]
    neg=[pack([-coeff[a][j] for j in range(n)]) for a in range(q)]
    mul=[]
    for a in range(q):
        row=[]
        for b in range(q):
            pol=[0]*(2*n-1)
            for i,u in enumerate(coeff[a]):
                for j,v in enumerate(coeff[b]):pol[i+j]=(pol[i+j]+u*v)%3
            for k in range(2*n-2,n-1,-1):
                c=pol[k]
                for j in range(n):pol[k-n+j]=(pol[k-n+j]-c*mod[j])%3
            row.append(pack(pol[:n]))
        mul.append(row)
    one=1; minus=neg[one]
    return q,add,neg,mul,one,minus

def census(n):
    q,add,neg,mul,one,minus=field(n)
    plus=lambda a,b:add[a][b]
    prod=lambda a,b:mul[a][b]
    sub=lambda a,b:add[a][neg[b]]
    square=[prod(a,a) for a in range(q)]
    smooth=Counter(); singular=0
    for r,s,t in product(range(q),repeat=3):
        D=sub(plus(plus(square[r],square[s]),square[t]),plus(prod(prod(r,s),t),one))
        if r in (one,minus) or s in (one,minus) or t in (one,minus) or D==0:
            singular+=1;continue
        hx=plus(s,prod(r,t));hy=plus(t,prod(r,s));hz=plus(r,prod(s,t))
        rank=int(hx!=0)+int(hy!=0)+int(hz!=0)
        smooth[rank]+=1
    expected={0:1,1:3*(q-3),2:3*(q-3)*(q-5),3:(q-3)*(q*q-7*q+18)}
    assert all(smooth[i]==expected[i] for i in range(4)),(n,smooth,expected)
    assert sum(smooth.values())==(q-2)**3-(q-3)**2
    assert singular+sum(smooth.values())==q**3
    print('q=%d smooth=%d singular=%d ranks=%s'%(q,sum(smooth.values()),singular,tuple(smooth[i] for i in range(4))))
for n in (1,2,3):census(n)
print('CHAR3_CIANI_INDEPENDENT_GF3_GF9_GF27_CENSUS_OK')
