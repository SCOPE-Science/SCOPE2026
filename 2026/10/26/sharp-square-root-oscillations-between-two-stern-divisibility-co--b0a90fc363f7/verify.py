#!/usr/bin/env python3
"""Exact finite-state arithmetic certificate for dyadic Stern divisibility."""
from math import gcd

def multiply(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def product(*factors):
    p=[1]
    for f in factors:p=multiply(p,f)
    return p

def step(m, states, idx, units, vec):
    def canonical(a,b):
        return min((u*a%m,u*b%m) for u in units)
    out=[0]*len(states)
    for j,(a,b) in enumerate(states):
        out[idx[canonical(a,a+b)]]+=vec[j]
        out[idx[canonical(a+b,b)]]+=vec[j]
    return out

def make_sequence(m, recurrence, first_n):
    units=[u for u in range(m) if gcd(u,m)==1]
    def canon(a,b):return min((u*a%m,u*b%m) for u in units)
    states=sorted({canon(a,b) for a in range(m) for b in range(m)
                   if gcd(gcd(a,b),m)==1})
    assert len(states)==12
    index={q:i for i,q in enumerate(states)}
    vec=[0]*len(states);vec[index[canon(1,1)]]=1
    certificate=[0]*len(states)
    values=[]
    for n in range(max(len(recurrence),first_n)):
        values.append(vec[index[canon(0,1)]])
        if n<len(recurrence):
            for j,v in enumerate(vec):certificate[j]+=recurrence[n]*v
        vec=step(m,states,index,units,vec)
    assert certificate==[0]*len(states),('nonzero polynomial action',m,certificate)
    return values

poly6=product([-2,1],[1,1],[2,-2,1],[2,1,1])
poly8=product([-2,1],[1,1],[2,-1,1],[4,0,-1,0,1])
seq6=make_sequence(6,poly6,32)
seq8=make_sequence(8,poly8,32)
assert len(poly6)==7 and len(poly8)==9

def numerator(sequence, p):
    Q=list(reversed(p));d=len(p)-1
    return [sum(Q[j]*sequence[i-j] for j in range(i+1)) for i in range(d)]

assert numerator(seq6,poly6)==[0,0,0,0,0,4]
assert numerator(seq8,poly8)==[0,0,0,0,2,-2,0,8]
N6=[0,0,0,0,0,4]
N8=[0,0,0,0,2,-2,0,8]
Q6=list(reversed(poly6));Q8=list(reversed(poly8))
L=product([1,1],[1,-2,2],[1,-1,2],[1,1,2],[1,0,-1,0,4])
E=[0,0,0,0,2,-4,2]
lhs=multiply([a-b for a,b in zip(multiply(N8,Q6)+[0]*2, multiply(N6,Q8)+[0]*2)],L)
rhs=multiply(E,multiply(Q6,Q8))
assert lhs[:len(rhs)]==rhs and all(v==0 for v in lhs[len(rhs):]),('rational identity',lhs,rhs)
assert [x-y for x,y in zip(seq8[:15],seq6[:15])]==[0,0,0,0,2,-2,-4,0,-2,10,16,4,-14,-34,4]
# Independently compute original Stern values, checking modulus and shell correspondence.
s=[0,1]
for k in range(2,1<<15):
    s.append(s[k//2] if k%2==0 else s[k//2]+s[k//2+1])
for r in range(14):
    assert sum(s[k]%6==0 for k in range(1<<r,1<<(r+1)))==seq6[r]
    assert sum(s[k]%8==0 for k in range(1<<r,1<<(r+1)))==seq8[r]
print('VERIFY_OK: two 12-state polynomial-action identities, rational function, and 14 original Stern shells')
