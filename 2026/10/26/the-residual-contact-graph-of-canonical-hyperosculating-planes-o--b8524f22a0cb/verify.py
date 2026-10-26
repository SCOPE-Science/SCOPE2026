#!/usr/bin/env python3
"""Exact arithmetic checks for the canonical Hasse-Wronskian on a genus-four curve.
All polynomial arithmetic uses integers modulo 3; no third-party dependencies.
"""
from itertools import product
from math import comb
from collections import Counter

P = 3

def laurent_add(a, b, sign=1):
    c = dict(a)
    for k, v in b.items():
        c[k] = (c.get(k, 0) + sign*v) % P
    return {k:v for k,v in c.items() if v}

def laurent_mul(a,b):
    c = {}
    for i,v in a.items():
        for j,w in b.items():
            c[i+j] = (c.get(i+j,0)+v*w)%P
    return {k:v for k,v in c.items() if v}

def laurent_cube(a):
    return {3*k:v for k,v in a.items()}  # Frobenius in characteristic three

# Expand (U-t+t^3)^(-1) up to t^3 and solve Y(t)^3-Y(t)=that inverse.
f = [{-1:1},{-2:1},{-3:1},{-4:1,-2:2}]
y1 = {k:-v%3 for k,v in f[1].items()}
y2 = {k:-v%3 for k,v in f[2].items()}
y3 = laurent_add(laurent_cube(y1),f[3],-1)
W = laurent_add(laurent_mul(y2,y2),laurent_mul(y1,y3),-1)
assert W == {-4:1,-8:2}, (y1,y2,y3,W)

# At x=infinity, v=y-a satisfies v^3-v=t^3/(1-t^2).
# Coefficients to order t^12 give the local Wronskian order (exactly four).
N = 14
rhs = {k:1 for k in range(3,N,2)}
# v = -rhs - rhs^3 - rhs^9 ... in characteristic three.
v = {}
for k in rhs:
    for h,coeff in ((k,2),(3*k,2),(9*k,2)):
        if h<N:
            v[h]=(v.get(h,0)+coeff)%3
v={k:c for k,c in v.items() if c}
def deriv(k):
    return {i-k:(c*comb(i,k))%3 for i,c in v.items() if i>=k and (c*comb(i,k))%3}
Wloc=laurent_add(laurent_mul(deriv(2),deriv(2)),laurent_mul(deriv(1),deriv(3)),-1)
assert min(Wloc)==4 and Wloc[4]==1,Wloc

class F:
    def __init__(self, mod):
        self.mod=mod; self.n=len(mod)-1
        self.els=list(product(range(3),repeat=self.n))
        self.zero=(0,)*self.n
        self.one=(1,)+(0,)*(self.n-1)
    def add(self,a,b):return tuple((x+y)%3 for x,y in zip(a,b))
    def neg(self,a):return tuple(-x%3 for x in a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        n=self.n; c=[0]*(2*n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%3
        for k in range(2*n-2,n-1,-1):
            h=c[k]
            if h:
                for j in range(n):c[k-n+j]=(c[k-n+j]-h*self.mod[j])%3
        return tuple(c[:n])
    def power(self,a,e):
        b=self.one
        while e:
            if e&1:b=self.mul(b,a)
            a=self.mul(a,a); e//=2
        return b
    def compute(self):
        H=Counter(self.sub(self.power(a,3),a) for a in self.els)
        total=0
        for u,nx in H.items():
            if u!=self.zero and self.power(u,4)==self.one:
                v=self.power(u,3**self.n-2)
                total+=nx*H.get(v,0)
        return total

assert F((0,1)).compute()==0
assert F((1,0,1)).compute()==18
assert F((2,2,0,1)).compute()==18
# The distinct affine ramification points are the 4*3*3 zeros U^4=1.
# Six boundary points carry weight four each: 36+6*4=60=10(2g-2).
assert 4*3*3+6*4==60
print('VERIFY_OK: W=(U^4-1)/U^8; boundary order four; support F3/F9/F27 = 6/24/24')

# Hyperosculating canonical hyperplane H_P at U=A (A^4=1) is
# z+A^{-2}s-A^{-1}sz=0, where s=x-x(P), z=y-y(P).
# Its intersection polynomial is -A*s^4*(A*s^2-s+A).
K=F((1,0,1))
for A in K.els:
    if K.power(A,4)!=K.one: continue
    Ai=K.power(A,3)
    for s in K.els:
        d=K.sub(K.one,K.mul(Ai,s)); nn=K.neg(K.mul(K.power(A,2),s))
        U=K.sub(K.add(A,K.power(s,3)),s)
        d3=K.power(d,3)
        zpart=K.sub(K.add(K.mul(Ai,d3),K.power(nn,3)),K.mul(nn,K.power(d,2)))
        lhs=K.sub(K.mul(U,zpart),d3)
        rhs=K.neg(K.mul(K.mul(A,K.power(s,4)),K.sub(K.add(K.mul(A,K.power(s,2)),A),s)))
        assert lhs==rhs,(A,s,lhs,rhs)
# Fixed A=+/-1: 18 points over F_27 and six directed 3-cycles
K3=F((2,2,0,1))
vals={x:K3.sub(K3.power(x,3),x) for x in K3.els}
P_pm={(x,y) for x in K3.els for y in K3.els if vals[x] in (K3.one,K3.neg(K3.one)) and K3.mul(vals[x],vals[y])==K3.one}
assert len(P_pm)==18
adj={}
for x,y in P_pm:
    A=vals[x]; target=(K3.sub(x,A),K3.sub(y,A))
    assert target in P_pm and target!=(x,y)
    adj[x,y]=target
seen=set(); lengths=[]
for P0 in adj:
    if P0 in seen: continue
    cur=P0; length=0
    while cur not in seen:
        seen.add(cur); length+=1; cur=adj[cur]
    assert cur==P0
    lengths.append(length)
assert sorted(lengths)==[3]*6
# Nonreal fourth-root strata over F_9 form a degree-two residual graph of 3 hexagons.
negone=K.neg(K.one)
P_i={(x,y) for x in K.els for y in K.els if K.power(vals_K:=K.sub(K.power(x,3),x),2)==negone and K.mul(vals_K,K.sub(K.power(y,3),y))==K.one}
assert len(P_i)==18
edges={}
for x,y in P_i:
    A=K.sub(K.power(x,3),x)
    targets=set()
    for eps in (K.one,K.neg(K.one)):
        x2=K.add(K.add(x,A),eps)
        y2=K.add(K.sub(y,A),eps)
        assert (x2,y2) in P_i
        targets.add((x2,y2))
    assert len(targets)==2
    edges[x,y]=targets
for p,ns in edges.items():
    for q in ns: assert p in edges[q]
seen=set(); sizes=[]
for p in edges:
    if p in seen:continue
    stack=[p]; comp=set()
    while stack:
        v=stack.pop()
        if v in comp:continue
        comp.add(v);stack.extend(edges[v])
    seen.update(comp);sizes.append(len(comp))
assert sorted(sizes)==[6]*3
print('VERIFY_OK: osculating section 4P+2Q in six directed 3-cycles; 4P+Q+R in three 6-cycles')
