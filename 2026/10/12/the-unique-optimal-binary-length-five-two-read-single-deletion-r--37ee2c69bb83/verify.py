#!/usr/bin/env python3
from itertools import product, combinations
from functools import lru_cache

N=5
WORDS=[''.join(p) for p in product('01', repeat=N)]
INDEX={w:i for i,w in enumerate(WORDS)}
ALL=(1<<len(WORDS))-1

def deletion_ball(w):
    return frozenset(w[:i]+w[i+1:] for i in range(len(w)))

BALL=[deletion_ball(w) for w in WORDS]

# Construction A: direct pairwise intersection of distinct-output deletion balls.
conf_a=[0]*len(WORDS)
for i,j in combinations(range(len(WORDS)),2):
    if len(BALL[i] & BALL[j]) >= 2:
        conf_a[i] |= 1<<j
        conf_a[j] |= 1<<i

# Construction B: independently reconstruct every forbidden pair from an unordered
# pair of shared length-four traces. Two parents conflict iff some trace pair is
# contained in both deletion balls.
trace_pairs={}
for i,b in enumerate(BALL):
    for u,v in combinations(sorted(b),2):
        trace_pairs.setdefault((u,v),[]).append(i)
conf_b=[0]*len(WORDS)
for parents in trace_pairs.values():
    for i,j in combinations(parents,2):
        conf_b[i] |= 1<<j
        conf_b[j] |= 1<<i
assert conf_a == conf_b
CONF=conf_a

# Engine 1: exact maximum independent set with memoized include/exclude recursion.
# A maximum-degree pivot tends to make both branches shrink sharply.
@lru_cache(maxsize=None)
def mis(mask):
    if not mask:
        return (0,1,0)  # size, number of maxima, lexicographically least witness mask
    verts=[i for i in range(len(WORDS)) if (mask>>i)&1]
    v=max(verts,key=lambda x:(CONF[x]&mask).bit_count())
    m0=mask & ~(1<<v)
    a=mis(m0)
    m1=mask & ~(1<<v) & ~CONF[v]
    b0=mis(m1)
    b=(b0[0]+1,b0[1],b0[2]|(1<<v))
    if a[0]>b[0]: return a
    if b[0]>a[0]: return b
    return (a[0],a[1]+b[1],min(a[2],b[2]))

best1,count1,wit1=mis(ALL)

# Engine 2: Bron-Kerbosch enumeration of maximal cliques in the compatibility graph.
COMP=[0]*len(WORDS)
for i in range(len(WORDS)):
    COMP[i]=(ALL & ~(1<<i) & ~CONF[i])

best2=0
count2=0
witnesses=[]
def bronk(R,P,X):
    global best2,count2,witnesses
    if P==0 and X==0:
        s=R.bit_count()
        if s>best2:
            best2=s; count2=1; witnesses=[R]
        elif s==best2:
            count2+=1; witnesses.append(R)
        return
    # Bound: even taking all P cannot improve the current record.
    if R.bit_count()+P.bit_count() < best2:
        return
    ux=P|X
    if ux:
        u=max((i for i in range(len(WORDS)) if (ux>>i)&1),
              key=lambda x:(P&COMP[x]).bit_count())
        cand=P & ~COMP[u]
    else:
        cand=P
    while cand:
        lb=cand & -cand
        v=lb.bit_length()-1
        bronk(R|lb, P&COMP[v], X&COMP[v])
        P &= ~lb
        X |= lb
        cand &= ~lb
        if R.bit_count()+P.bit_count() < best2:
            break

bronk(0,ALL,0)
assert best1==best2==20
assert count1==count2==1
W=witnesses[0]
assert W==wit1
CODE=[WORDS[i] for i in range(len(WORDS)) if (W>>i)&1]
EXPECTED=[
'00000','00001','00011','00100','00110','00111','01001','01100','01101','01111',
'10000','10010','10011','10110','11000','11001','11011','11100','11110','11111']
assert CODE==EXPECTED

# Directly recheck the scientific predicate and exact read-coverage.
nu=max(len(BALL[i]&BALL[j]) for i,j in combinations(range(len(WORDS)),2)
       if ((W>>i)&1) and ((W>>j)&1))
assert nu==1
assert all(len(BALL[i]&BALL[j])<=1 for i,j in combinations(range(len(WORDS)),2)
           if ((W>>i)&1) and ((W>>j)&1))
# Every 21-subset fails automatically from the exact maximum; explicitly ensure the
# unique optimum is maximal and all omitted words hit a forbidden pair with it.
for i in range(len(WORDS)):
    if not ((W>>i)&1):
        assert CONF[i] & W

def rev(w): return w[::-1]
def comp(w): return ''.join('1' if c=='0' else '0' for c in w)
C=set(CODE)
assert {rev(w) for w in C}==C
assert {comp(w) for w in C}==C

excluded=sorted(set(WORDS)-C)
weight_profile=[sum(w.count('1')==k for w in CODE) for k in range(N+1)]
print('VERIFY_OK maximum=20 labeled_maxima=1 read_coverage=1 '
      'reversal_invariant=true complement_invariant=true weight_profile='+','.join(map(str,weight_profile)))
print('CODE='+' '.join(CODE))
print('EXCLUDED='+' '.join(excluded))
