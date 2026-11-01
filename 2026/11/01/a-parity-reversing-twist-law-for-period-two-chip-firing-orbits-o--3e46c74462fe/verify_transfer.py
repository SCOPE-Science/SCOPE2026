#!/usr/bin/env python3
"""Exact transfer-matrix verification for primitive period-two chip-firing on cyclic ladders."""
import sympy as s

COLS = [(0,0),(0,1),(1,0),(1,1)]
STATES = [(p,q) for p in range(4) for q in range(4)]
M = s.zeros(16)
P = s.zeros(16)
for i,(p,q) in enumerate(STATES):
    a0,b0=COLS[p]
    a,b=COLS[q]
    for r in range(4):
        a1,b1=COLS[r]
        ca=(a!=a0)+(a!=a1)+(a!=b)
        cb=(b!=b0)+(b!=b1)+(b!=a)
        j=STATES.index((q,r))
        M[i,j]=int(ca)*int(cb)
    def sw(k):return COLS.index(tuple(reversed(COLS[k])))
    P[i,STATES.index((sw(p),sw(q)))]=1
assert P*P==s.eye(16)
assert M*P==P*M
orbits=[];seen=set()
for i in range(16):
    if i in seen:continue
    js=[j for j in range(16) if P[i,j]==1]
    assert len(js)==1
    j=js[0]
    seen.add(i);seen.add(j)
    orbits.append((i,j))
plus=[];minus=[]
for i,j in orbits:
    v=s.zeros(16,1);v[i]=1;v[j]=1;plus.append(v)
    if i!=j:
        w=s.zeros(16,1);w[i]=1;w[j]=-1;minus.append(w)
assert len(plus)==10 and len(minus)==6
B=s.Matrix.hstack(*(plus+minus))
assert B.det()!=0
D=B.inv()*M*B
assert D[:10,10:]==s.zeros(10,6) and D[10:,:10]==s.zeros(6,10)
z=s.Symbol('z')
cplus=s.factor(D[:10,:10].charpoly(z).as_expr())
cminus=s.factor(D[10:,10:].charpoly(z).as_expr())
wantplus=(z-1)**3*(z+1)*(z*z-12*z+1)*(z*z+2*z-1)**2
wantminus=(z-1)*(z+1)*(z*z+4*z-1)**2
assert s.expand(cplus-wantplus)==0
assert s.expand(cminus-wantminus)==0
print('matrix_dimension=16, symmetric_dimension=10, antisymmetric_dimension=6')
print('plus_charpoly:',cplus)
print('minus_charpoly:',cminus)
U=[2,12]; V=[2,-2]; W=[2,-4]
for n in range(2,12):
    U.append(12*U[-1]-U[-2]); V.append(-2*V[-1]+V[-2]); W.append(-4*W[-1]+W[-2])
for n in range(3,11):
    t=M**n
    p=s.trace(t)//2
    mob=s.trace(t*P)//2
    fp=(4+2*(-1)**n+U[n]+2*V[n]+2*W[n])//2
    fm=(2+U[n]+2*V[n]-2*W[n])//2
    assert p==fp and mob==fm
    assert p-mob==1+(-1)**n+2*W[n]
    print(f'n={n} prism_orbits={p} mobius_orbits={mob} difference={p-mob}')
print('ALL_TRANSFER_TESTS_PASS')
