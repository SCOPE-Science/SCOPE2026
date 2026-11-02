#!/usr/bin/env python3
"""Exhaustive rational-idempotent distribution for uniform invertible 2x2 matrices."""
from collections import Counter
from fractions import Fraction
from itertools import product

def field(p,m,mod):
    q=p**m
    def digits(x):
        z=[]
        for _ in range(m): z.append(x%p);x//=p
        return z
    P=[digits(i) for i in range(q)]
    def encode(v): return sum((t%p)*p**i for i,t in enumerate(v))
    plus=[[encode([ (P[a][i]+P[b][i])%p for i in range(m)]) for b in range(q)] for a in range(q)]
    neg=[encode([-v for v in P[a]]) for a in range(q)]
    mul=[[None]*q for _ in range(q)]
    for a in range(q):
      for b in range(q):
        poly=[0]*(2*m-1)
        for i,x in enumerate(P[a]):
          for j,y in enumerate(P[b]): poly[i+j]=(poly[i+j]+x*y)%p
        for k in range(2*m-2,m-1,-1):
          co=poly[k]
          for j in range(m): poly[k-m+j]=(poly[k-m+j]-co*mod[j])%p
          poly[k]=0
        mul[a][b]=encode(poly[:m])
    if m==1: assert mod==[0,1]
    for a in range(1,q): assert len(set(mul[a]))==q
    return q,plus,mul,neg

def predicted(q,even):
    if even: return {0:Fraction(1,3),1:Fraction(1,2),2:Fraction(0),3:Fraction(1,6)}
    den=q*(q+1)
    return {0:Fraction(1,3),1:Fraction(q*q+1,2*den),2:Fraction(q-1,den),3:Fraction(q*q-2*q+3,6*den)}

cases=[(2,1,[0,1]),(3,1,[0,1]),(2,2,[1,1,1]),(5,1,[0,1]),(2,3,[1,1,0,1]),(7,1,[0,1]),(3,2,[1,0,1])]
for p,m,mod in cases:
    q,add,mult,neg=field(p,m,mod)
    square=[mult[a][a] for a in range(q)]
    # All nonzero vectors in projective space have unique normalized rep either (1,t) or (0,1).
    rays=[(1,t) for t in range(q)]+[(0,1)]
    histogram=Counter(); invertible=0
    for a,b,c,d in product(range(q),repeat=4):
        det=add[mult[a][d]][neg[mult[b][c]]]
        if det==0: continue
        invertible+=1; count=0
        for x,y in rays:
            X=add[mult[a][square[x]]][mult[b][square[y]]]
            Y=add[mult[c][square[x]]][mult[d][square[y]]]
            # direction [X:Y]=[x:y] iff determinant zero. M invertible ensures nonzero.
            if add[mult[X][y]][neg[mult[Y][x]]]==0:count+=1
        histogram[count]+=1
    assert invertible==q*(q-1)**2*(q+1),(q,invertible)
    expected=predicted(q,p==2)
    for k in range(4):
        assert Fraction(histogram[k],invertible)==expected[k],(q,k,histogram[k],invertible,expected[k])
    assert sum(histogram.values())==invertible
    print(f'q={q} GL2={invertible} counts='+str([histogram[k] for k in range(4)])+' probabilities='+str([str(expected[k]) for k in range(4)]))
print('VERIFY_OK')
