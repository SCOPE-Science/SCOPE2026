#!/usr/bin/env python3
from itertools import product, combinations, permutations
from collections import Counter
from fractions import Fraction
import hashlib

Q=3; N=5; T=2
WORDS=list(product(range(Q), repeat=N))
INDEX={w:i for i,w in enumerate(WORDS)}

def dshadow(w,t=T):
    return {tuple(w[i] for i in range(len(w)) if i not in S)
            for S in combinations(range(len(w)),t)}

def lcs(a,b):
    m=len(b)
    dp=[0]*(m+1)
    for x in a:
        nd=[0]*(m+1)
        for j,y in enumerate(b,1):
            nd[j]=dp[j-1]+1 if x==y else max(dp[j],nd[j-1])
        dp=nd
    return dp[m]

SH=[dshadow(w) for w in WORDS]
V=len(WORDS)
ADJ=[0]*V
pair_checks=0
for i in range(V):
    for j in range(i+1,V):
        via_shadow=SH[i].isdisjoint(SH[j])
        via_lcs=lcs(WORDS[i],WORDS[j]) <= N-T-1
        assert via_shadow == via_lcs
        pair_checks += 1
        if via_shadow:
            ADJ[i] |= 1<<j
            ADJ[j] |= 1<<i

# Complete maximum-clique search with greedy-color upper bounds.
def greedy_coloring(P):
    verts=[]; colors=[]; U=P; c=0
    while U:
        c+=1; Qm=U
        while Qm:
            b=Qm & -Qm; v=b.bit_length()-1
            verts.append(v); colors.append(c)
            U &= ~b; Qm &= ~b; Qm &= ~ADJ[v]
    return verts, colors

best=[]
def expand(R,P):
    global best
    if not P:
        if len(R)>len(best): best=R[:]
        return
    vs,cs=greedy_coloring(P)
    for k in range(len(vs)-1,-1,-1):
        v=vs[k]
        if len(R)+cs[k] <= len(best):
            return
        if (P>>v)&1:
            expand(R+[v], P & ADJ[v])
            P &= ~(1<<v)
expand([], (1<<V)-1)
maximum=len(best)

# Independent ordered target-size recursion; this directly counts k-cliques.
def collect_k(k, store=False):
    total=0; out=[]
    def rec(prefix,cand,need):
        nonlocal total
        if need==0:
            total+=1
            if store: out.append(frozenset(prefix))
            return
        if cand.bit_count()<need: return
        while cand:
            if cand.bit_count()<need: return
            b=cand & -cand; v=b.bit_length()-1
            cand ^= b
            rec(prefix+[v], cand & ADJ[v], need-1)
    rec([], (1<<V)-1, k)
    return total,out

k6, MAXIMA = collect_k(6, True)
k7, _ = collect_k(7, False)
assert maximum==6 and k6==478 and k7==0 and len(MAXIMA)==478
MAXSET=set(MAXIMA)
canon='\n'.join(','.join(''.join(map(str,WORDS[i])) for i in sorted(C)) for C in sorted(MAXIMA, key=lambda C: tuple(sorted(C))))+'\n'
maxima_sha256=hashlib.sha256(canon.encode()).hexdigest()

# Natural symmetry group: all alphabet permutations and coordinate reversal.
SYMS=[(p,r) for p in permutations(range(Q)) for r in (False,True)]
def tw(w,g):
    p,r=g
    z=tuple(p[x] for x in w)
    return z[::-1] if r else z

def tc(C,g):
    return frozenset(INDEX[tw(WORDS[i],g)] for i in C)

unseen=set(MAXIMA); orbit_sizes=[]
while unseen:
    C=next(iter(unseen))
    orb={tc(C,g) for g in SYMS}
    assert orb <= MAXSET
    orbit_sizes.append(len(orb)); unseen -= orb
orbit_hist=Counter(orbit_sizes)
assert orbit_hist==Counter({12:35,6:8,4:2,2:1})
assert len(orbit_sizes)==46

fixed=[]
for g in SYMS:
    fixed.append(sum(1 for C in MAXIMA if tc(C,g)==C))
assert sum(fixed)==46*len(SYMS)

coverage=Counter(sum(len(SH[i]) for i in C) for C in MAXIMA)
assert coverage==Counter({22:144,21:100,23:96,20:54,24:52,25:18,19:12,18:2})
assert max(coverage)==25 < Q**(N-T)

# Exact maxima for fixed two deletions at n=2,3,4,5 (same finite procedure).
def small_max(n):
    ws=list(product(range(Q), repeat=n))
    ss=[{tuple(w[i] for i in range(n) if i not in S) for S in combinations(range(n),T)} for w in ws]
    m=len(ws); ad=[0]*m
    for i in range(m):
        for j in range(i+1,m):
            if ss[i].isdisjoint(ss[j]):
                ad[i]|=1<<j; ad[j]|=1<<i
    bestn=0
    def color(P):
        verts=[]; cols=[]; U=P; c=0
        while U:
            c+=1; Qm=U
            while Qm:
                b=Qm&-Qm; v=b.bit_length()-1
                verts.append(v); cols.append(c)
                U&=~b; Qm&=~b; Qm&=~ad[v]
        return verts,cols
    def ex(r,P):
        nonlocal bestn
        if not P:
            bestn=max(bestn,r); return
        vs,cs=color(P)
        for k in range(len(vs)-1,-1,-1):
            v=vs[k]
            if r+cs[k] <= bestn: return
            if (P>>v)&1:
                ex(r+1,P&ad[v]); P&=~(1<<v)
    ex(0,(1<<m)-1)
    return bestn
small=[small_max(n) for n in range(2,6)]
assert small==[1,3,3,6]

# Kulkarni--Kiyavash Theorem IV.1 specialized to q=3,s=2,n=5:
# sum over length-3 strings of reciprocal sizes of their 2-deletion sets.
bound=Fraction(0,1)
for x in product(range(Q), repeat=N-T):
    bound += Fraction(1,len(dshadow(x,T)))
assert bound==14

print('VERIFY_OK',
      f'vertices={V}',
      f'pair_checks={pair_checks}',
      f'maximum={maximum}',
      f'labeled_maxima={k6}',
      f'maxima_sha256={maxima_sha256}',
      f'k7={k7}',
      'small_max=1,3,3,6',
      'published_bound=14',
      f'orbits={len(orbit_sizes)}',
      'orbit_sizes=2x1,4x2,6x8,12x35',
      'coverage=18x2,19x12,20x54,21x100,22x144,23x96,24x52,25x18',
      'perfect_maxima=0')
