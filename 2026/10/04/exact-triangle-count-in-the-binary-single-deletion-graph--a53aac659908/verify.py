#!/usr/bin/env python3
from collections import deque
from itertools import product, combinations
import sympy as sp
S="S"; A="A"
def nfa_step(st,x,y):
    out=set()
    if st==S:
        if x==y: out.add(S)
        out.add(A); out.add("X"+str(y)); out.add("Y"+str(x))
    elif st==A:
        if x==y: out.add(A)
    elif st[0]=="X":
        c=int(st[1])
        if x==c: out.add("X"+str(y)); out.add(A)
    elif st[0]=="Y":
        c=int(st[1])
        if y==c: out.add("Y"+str(x)); out.add(A)
    return out
def dstep(sub,x,y):
    out=set()
    for st in sub: out |= nfa_step(st,x,y)
    return frozenset(out)
start=frozenset([S])
Q={start}; dq=deque([start])
while dq:
    q=dq.popleft()
    for x,y in product(range(2),repeat=2):
        r=dstep(q,x,y)
        if r not in Q: Q.add(r); dq.append(r)
assert len(Q)==11
pl=list(Q); pi={q:i for i,q in enumerate(pl)}; P=len(pl)
MP=sp.zeros(P,P)
for q in pl:
    for x,y in product(range(2),repeat=2): MP[pi[q],pi[dstep(q,x,y)]] += 1
fp=sp.zeros(P,1)
for i,q in enumerate(pl):
    if S in q or A in q: fp[i]=1
p0=sp.zeros(1,P); p0[0,pi[start]]=1
# Product DFA for the three unordered pair conditions.
start3=(start,start,start); Q3={start3}; dq=deque([start3]); tr={}
while dq:
    q=dq.popleft()
    for abc in product(range(2),repeat=3):
        a,b,c=abc
        r=(dstep(q[0],a,b),dstep(q[1],b,c),dstep(q[2],c,a))
        tr[(q,abc)]=r
        if r not in Q3: Q3.add(r); dq.append(r)
assert len(Q3)==287
ql=list(Q3); qi={q:i for i,q in enumerate(ql)}; N=len(ql)
M=sp.zeros(N,N)
for q in ql:
    for abc in product(range(2),repeat=3): M[qi[q],qi[tr[(q,abc)]]] += 1
f=sp.zeros(N,1)
for i,q in enumerate(ql):
    if all(S in sub or A in sub for sub in q): f[i]=1
u=sp.zeros(1,N); u[0,qi[start3]]=1

def krylov_basis(row,mat,max_steps=40):
    basis=[]; rank=0; r=row*mat
    for _ in range(max_steps):
        nr=sp.Matrix.vstack(*(basis+[r])).rank() if basis else (0 if r.is_zero_matrix else 1)
        if nr>rank: basis.append(r); rank=nr
        r=r*mat
    return basis

def cert(row,mat,col,coeff,expected_rank):
    basis=krylov_basis(row,mat)
    assert len(basis)==expected_rank
    B=sp.Matrix.vstack(*basis)
    assert all(sp.Matrix.vstack(B,b*mat).rank()==expected_rank for b in basis)
    pows=[col]
    for _ in range(len(coeff)-1): pows.append(mat*pows[-1])
    g=sp.zeros(mat.rows,1)
    for c,v in zip(coeff,pows): g += c*v
    assert all((b*g)[0]==0 for b in basis)
# (t-2)^3(t-1)=t^4-7t^3+18t^2-20t+8
cert(p0,MP,fp,[8,-20,18,-7,1],5)
# (t-2)^4(t-1)^3=t^7-11t^6+51t^5-129t^4+192t^3-168t^2+80t-16
cert(u,M,f,[-16,80,-168,192,-129,51,-11,1],14)

def P_formula(n): return 2**(n-1)*(n*n-n+6)-2
def A_formula(n): return (2**n*(3*n**3+9*n*n-24*n-56)+48*n*n+48*n+72)//4
def T_formula(n): return (2**n*(n**3+n*n-6*n-28)+16*(n*n+n+2))//8
# Enough initial values for the certified recurrences.
r=p0; s=u
for n in range(1,16):
    r=r*MP; s=s*M
    assert int((r*fp)[0])==P_formula(n)
    assert int((s*f)[0])==A_formula(n)
    assert (A_formula(n)-3*P_formula(n)+2**(n+1))//6==T_formula(n)
# Independent literal graph enumeration for n<=8.
def dels(w): return {w[:i]+w[i+1:] for i in range(len(w))}
checked=0
for n in range(1,9):
    words=[format(i,'0%db'%n) for i in range(2**n)]
    ds={w:dels(w) for w in words}
    adj={w:set() for w in words}
    for i,x in enumerate(words):
        for y in words[i+1:]:
            if ds[x] & ds[y]: adj[x].add(y); adj[y].add(x)
    tri=0
    for i,x in enumerate(words):
        for y in [v for v in adj[x] if v>x]:
            tri += sum(1 for z in adj[x]&adj[y] if z>y)
    assert tri==T_formula(n),(n,tri,T_formula(n))
    checked += len(words)
print(f"VERIFY_OK direct_words={checked} n<=8 pair_states={P} triple_states={N} pair_rank=5 triple_rank=14")
