#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import json, os

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def coeff(f,v): return [f[i]*v[j] for i in range(4) for j in range(4)]
base=[(1,0,0,0),(-1,1,0,0),(0,-1,1,0),(0,0,-1,1),(0,0,0,1)]
V=base+[tuple(-x for x in v) for v in base]
F=[]
for z in range(5):
    rest=[i for i in range(5) if i!=z]
    for pos in combinations(rest,2):
        d=[-1]*5; d[z]=0
        for i in pos: d[i]=1
        F.append((d[0],d[0]+d[1],d[0]+d[1]+d[2],d[0]+d[1]+d[2]+d[3]))
assert len(V)==10 and len(F)==30 and len(set(F))==30
inc=[(i,j) for i,v in enumerate(V) for j,f in enumerate(F) if dot(f,v)==1]
assert len(inc)==120
A=[]; b=[]
for v in V:
    for f in F:
        A.append(coeff(f,v)+[0]); b.append(1)
for i,j in inc:
    c=coeff(F[j],V[i]); A.append(c+[-1]); b.append(0); A.append([-x for x in c]+[-1]); b.append(0)
assert len(A)==540
path=os.path.join(os.path.dirname(__file__),'dual_certificates.json')
with open(path,encoding='utf-8') as fh: data=json.load(fh)
assert data['schema_version']==1 and len(data['certificates'])==300
assert [tuple(x) for x in data['V']]==V and [tuple(x) for x in data['F']]==F
for cert in data['certificates']:
    vi=int(cert['active_v']); fj=int(cert['active_f'])
    h=coeff(F[fj],V[vi])+[0]
    y={int(r):Fraction(q) for r,q in cert['y']}
    assert all(0<=r<len(A) and q<=0 for r,q in y.items())
    mu=Fraction(cert['mu'])
    for k in range(17):
        lhs=sum(q*A[r][k] for r,q in y.items())+mu*h[k]
        assert lhs==Fraction(1 if k==16 else 0)
    value=sum(q*b[r] for r,q in y.items())+mu
    assert value==Fraction(cert['value']) and value>=Fraction(3,4)
# explicit attaining operator, row-major in the delta_1,...,delta_4 basis
T=[[Fraction(-1,4),0,0,0],[0,Fraction(1,4),0,0],[0,0,0,0],[0,Fraction(-1,2),0,0]]
def apply(v): return [sum(T[i][j]*v[j] for j in range(4)) for i in range(4)]
def evalf(f,x): return sum(Fraction(f[i])*x[i] for i in range(4))
op=max(evalf(f,apply(v)) for v in V for f in F)
num=max(abs(evalf(F[j],apply(V[i]))) for i,j in inc)
assert op==1 and num==Fraction(3,4)
print('VERIFY_OK cases=300 incidence=120 operator_norm=1 numerical_radius=3/4')
