#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

class Q6:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q6) else Q6(o); return Q6(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q6(-self.a,-self.b)
    def __sub__(self,o): return self+(-o if isinstance(o,Q6) else -Q6(o))
    def __rsub__(self,o): return Q6(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q6) else Q6(o)
        return Q6(self.a*o.a+6*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,Q6): return Q6(self.a/F(o),self.b/F(o))
        den=o.a*o.a-6*o.b*o.b
        return Q6((self.a*o.a-6*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=o if isinstance(o,Q6) else Q6(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f'Q6({self.a},{self.b})'
    def positive(self):
        if self.b==0: return self.a>0
        if self.b>0:
            if self.a>=0: return True
            return 6*self.b*self.b > self.a*self.a
        if self.a<=0: return False
        return self.a*self.a > 6*self.b*self.b

def parse_weight(s):
    # Fixed package grammar: (A+B*sqrt(6))/D or (A-B*sqrt(6))/D.
    t=s.replace(' ','').replace('(','').replace(')','')
    num,den=t.split('/')
    den=F(int(den))
    pos=num.find('+',1); neg=num.find('-',1)
    k=pos if pos!=-1 else neg
    A=int(num[:k]); term=num[k:]
    sign=1 if term[0]=='+' else -1
    coeff=int(term[1:].split('*')[0])
    return Q6(F(A,1)/den,F(sign*coeff,1)/den)

def bits4(n): return [(n>>3)&1,(n>>2)&1,(n>>1)&1,n&1]
def dot(a,b): return sum(x*y for x,y in zip(a,b))&1

def rank(rows):
    A=[r[:] for r in rows]; rr=0
    for c in range(4):
        p=next((i for i in range(rr,len(A)) if A[i][c]),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        for i in range(len(A)):
            if i!=rr and A[i][c]: A[i]=[x^y for x,y in zip(A[i],A[rr])]
        rr+=1
    return rr

def affine_constraints(S):
    us=[bits4(x) for x in S]; u0=us[0]
    diffs=[[a^b for a,b in zip(u,u0)] for u in us[1:]]
    candidates=[]
    for m in range(1,16):
        c=bits4(m)
        if all(dot(c,d)==0 for d in diffs): candidates.append(c)
    basis=[]
    for c in candidates:
        if rank(basis+[c])>rank(basis): basis.append(c)
    assert len(S)==2**(4-len(basis))
    # Verify exact affine reconstruction.
    rhs=[dot(c,u0) for c in basis]
    got={n for n in range(16) if all(dot(c,bits4(n))==t for c,t in zip(basis,rhs))}
    assert got==set(S)
    return basis,rhs

# e = M u over F2; M is self-inverse.
M=[[0,0,0,1],[1,0,1,0],[0,1,0,1],[1,0,0,0]]
def row_times_M(c): return [sum(c[k]*M[k][j] for k in range(4))&1 for j in range(4)]

# G0=IXIX, G1=IZZZ, G2=XIXX, G3=ZIZI in A1,A2,B1,B2 order.
G=['IXIX','IZZZ','XIXX','ZIZI']
def pbits(ch): return (1,0) if ch=='X' else (0,1) if ch=='Z' else (1,1) if ch=='Y' else (0,0)
def product_bits(d):
    x=[0]*4; z=[0]*4
    for k,bit in enumerate(d):
        if bit:
            for j,ch in enumerate(G[k]):
                xx,zz=pbits(ch); x[j]^=xx; z[j]^=zz
    return x,z
def symp(p,q,inds):
    x,z=p; X,Z=q
    return sum(x[i]*Z[i]+z[i]*X[i] for i in inds)&1
CUTS={'A1B1|A2B2':[0,2], 'A1B2|A2B1':[0,3], 'A1A2|B1B2':[0,1]}

data=json.loads((Path(__file__).with_name('decomposition.json')).read_text())
comps=data['components']

sqrt6=Q6(0,1)
p=(Q6(8)-2*sqrt6)/5
assert 5*p*p-16*p+8==Q6(0)
assert p.positive() and (Q6(1)-p).positive()
a=Q6(1)-Q6(F(3,4))*p
b=p/4

weights=[parse_weight(c['weight']) for c in comps]
assert all(w.positive() for w in weights)
assert sum(weights,Q6(0))==Q6(1)

# Exact target probabilities in output-Pauli basis.
target=[]
for u in range(16):
    x1,z1,x2,z2=bits4(u)
    w1=a if (x1,z1)==(0,0) else b
    w2=a if (x2,z2)==(0,0) else b
    target.append(w1*w2)

mix=[Q6(0) for _ in range(16)]
certs=0
for c,w in zip(comps,weights):
    S=c['support']; share=w/len(S)
    for u in S: mix[u]=mix[u]+share
    basis,rhs=affine_constraints(S)
    ops=[]
    for parity in basis:
        # parity c.u is d.e with d=c M^{-1}=c M (M is self-inverse in the stated column-vector convention).
        d=row_times_M(parity)
        # Validate d.e(u)=c.u on all labels using e=M u.
        for u in range(16):
            ub=bits4(u)
            e=[sum(M[i][j]*ub[j] for j in range(4))&1 for i in range(4)]
            assert dot(d,e)==dot(parity,ub)
        ops.append(product_bits(d))
    inds=CUTS[c['cut']]
    for i in range(len(ops)):
        for j in range(i):
            assert symp(ops[i],ops[j],inds)==0
            certs+=1

assert mix==target
print('VERIFY_OK')
print('p_star_exact = (8-2*sqrt(6))/5')
print('components =',len(comps))
print('choi_probability_checks =',len(target))
print('local_commutation_pair_checks =',certs)
print('weights_sum_exact = 1')
