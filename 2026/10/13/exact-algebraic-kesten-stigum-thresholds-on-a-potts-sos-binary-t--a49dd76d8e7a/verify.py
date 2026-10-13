#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import permutations
from decimal import Decimal, getcontext

# Integer polynomials in t, ascending coefficients.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)
def neg(a): return tuple(-v for v in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,k): return trim([k*v for v in a])
Z=(0,); O=(1,); T=(0,1)

# F=y^3-t*y^2+2*t*y-2 and K=2*y^2(t-y)^2-(2t+y^2)^2.
Fc=[O,neg(T),scale(T,2),(-2,)]
Kc=[O,scale(T,-4),add(scale(mul(T,T),2),scale(T,-4)),Z,scale(mul(T,T),-4)]
S=[[Z for _ in range(7)] for __ in range(7)]
for i in range(4):
    for j,c in enumerate(Fc): S[i][i+j]=c
for i in range(3):
    for j,c in enumerate(Kc): S[4+i][i+j]=c

def parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv&1 else 1
D=Z
for p in permutations(range(7)):
    term=O
    for i,j in enumerate(p): term=mul(term,S[i][j])
    D=add(D,term if parity(p)>0 else neg(term))
P=(1,0,-24,-70,-18,40,-1,-10,1)
assert D==scale(P,16), (D,scale(P,16))

# Rational polynomial arithmetic for Sturm counting.
def qtrim(a):
    a=[Q(x) for x in a]
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def qder(a): return qtrim([Q(i)*a[i] for i in range(1,len(a))]) if len(a)>1 else [Q(0)]
def qdivmod(a,b):
    a=qtrim(a); b=qtrim(b)
    if b==[0]: raise ZeroDivisionError
    q=[Q(0)]*max(1,len(a)-len(b)+1)
    r=a[:]
    while len(r)>=len(b) and r!=[0]:
        c=r[-1]/b[-1]; k=len(r)-len(b); q[k]+=c
        for j,v in enumerate(b): r[j+k]-=c*v
        r=qtrim(r)
    return qtrim(q),qtrim(r)
def sturm(a):
    seq=[qtrim(a),qder(qtrim(a))]
    while seq[-1]!=[0]:
        _,r=qdivmod(seq[-2],seq[-1])
        if r==[0]: break
        seq.append(qtrim([-x for x in r]))
    return seq
def evalq(a,x):
    s=Q(0)
    for c in reversed(a): s=s*x+c
    return s
def variations(vals):
    sig=[1 if v>0 else -1 for v in vals if v]
    return sum(sig[i]!=sig[i-1] for i in range(1,len(sig)))
def var_at(seq,x): return variations([evalq(p,x) for p in seq])
def sign_inf(p,pos=True):
    s=1 if p[-1]>0 else -1
    if not pos and (len(p)-1)%2: s=-s
    return s
def var_inf(seq,pos=True): return variations([sign_inf(p,pos) for p in seq])
seq=sturm([Q(x) for x in P])
assert var_at(seq,Q(0))-var_inf(seq,True)==2
assert var_at(seq,Q(1666993,10_000_000))-var_at(seq,Q(1666994,10_000_000))==1
assert var_at(seq,Q(9706301,1_000_000))-var_at(seq,Q(9706302,1_000_000))==1

# Direct exact check of the eigenvalue constant coefficient at r=t^2.
# 2t^4-t^4 r-2t^2 r+r^3 = 0 after r=t^2.
assert add(add((0,0,0,0,2), neg((0,0,0,0,0,0,1))), add(neg((0,0,0,0,2)), (0,0,0,0,0,0,1))) == Z

# Readability-only high precision root refinement by bisection on P.
getcontext().prec=70
def pdec(x):
    cs=[Decimal(v) for v in P]
    s=Decimal(0)
    for c in reversed(cs): s=s*x+c
    return s
def bis(a,b,n=240):
    a=Decimal(a); b=Decimal(b); fa=pdec(a)
    for _ in range(n):
        m=(a+b)/2; fm=pdec(m)
        if fm==0: return m
        if (fa<0) != (fm<0): b=m
        else: a=m; fa=fm
    return (a+b)/2
lo=bis('0.1666993','0.1666994')
hi=bis('9.706301','9.706302')
print('VERIFY_OK positive_roots=2')
print('theta_minus='+str(lo))
print('theta_plus='+str(hi))
