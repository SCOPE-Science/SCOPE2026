#!/usr/bin/env python3
"""Exact finite quotient for three-state threshold-two excitation on complete tripartite graphs.
Reproducible with Python standard library: python verification/verify_tripartite.py [table.csv]."""
from itertools import product
from collections import Counter
from pathlib import Path
import csv, sys

# Signature: nine counts capped at two, ordered by shore then initial color.
# Group states are tagged by their initial color; empty groups have state -1.
def factor(sig):
    x = tuple(i % 3 if sig[i] else -1 for i in range(9))
    seen = {}
    while x not in seen:
        seen[x] = len(seen)
        exc = [sum(sig[3*s+j] for j in range(3) if x[3*s+j] == 1) for s in range(3)]
        y = []
        for s in range(3):
            enabled = sum(exc[k] for k in range(3) if k != s) >= 2
            for color in x[3*s:3*s+3]:
                y.append(-1 if color == -1 else (color + 1) % 3 if color else int(enabled))
        x = tuple(y)
    return seen[x], len(seen)-seen[x]

# Independent microscopic simulator, using an explicit labelled configuration.
def microscopic(sig):
    shores=[]
    for s in range(3):
        shores.append(tuple(color for color in range(3) for _ in range(sig[3*s+color])))
    state=tuple(z for shore in shores for z in shore)
    sizes=tuple(len(shore) for shore in shores)
    indices=[]; k=0
    for size in sizes:
        indices.append(tuple(range(k,k+size))); k+=size
    seen={}
    while state not in seen:
        seen[state]=len(seen)
        exc=[sum(state[k]==1 for k in indices[s]) for s in range(3)]
        state=tuple((state[k]+1)%3 if state[k]!=0 else int(sum(exc[j] for j in range(3) if j!=s)>=2)
                    for s in range(3) for k in indices[s])
    return seen[state], len(seen)-seen[state]

def realized(v,m):
    total=sum(v)
    return total <= m and (total == m or 2 in v)

def conditions(a,b,c):
    a,b,c=sorted((a,b,c))
    return {1:True, 3:(a>=2 or (b>=5 and c>=5)),
            4:(a==b==2 and c>=4), 12:(a<=3 and b>=4)}

rows=[]; hist=Counter(); patterns=[]
for sig in product(range(3),repeat=9):
    if any(sum(sig[3*s:3*s+3])==0 for s in range(3)):
        continue
    x=factor(sig)
    y=microscopic(sig)
    assert x==y,(sig,x,y)
    rows.append((sig,*x)); hist[x]+=1
assert len(rows)==26**3
assert sum(hist.values())==17576
assert max(t for sig,t,p in rows)==11
assert set(p for sig,t,p in rows)=={1,3,4,12}
expected={
 (0,1):8,(0,3):1790,(0,4):6,(0,12):42,
 (1,1):504,(1,3):627,(1,4):24,(1,12):210,
 (2,1):2916,(2,3):1086,(2,4):54,(2,12):390,
 (3,1):3520,(3,3):1158,(3,4):12,(3,12):240,
 (4,1):2001,(4,3):546,(4,12):84,
 (5,1):921,(5,3):117,
 (6,1):312,(6,3):30,
 (7,1):384,(7,3):24,
 (8,1):270,(9,1):258,(10,1):30,(11,1):12}
assert hist == expected

# Each shore size >=7 has exactly the same realizable truncated signatures;
# hence checking 1..7 establishes all positive shore sizes.
for a in range(1,8):
 for b in range(a,8):
  for c in range(b,8):
   eligible=[(sig,t,p) for sig,t,p in rows if all(
      realized(sig[3*s:3*s+3],m) for s,m in enumerate((a,b,c)))]
   got={p for sig,t,p in eligible}
   want={p for p,truth in conditions(a,b,c).items() if truth}
   assert got==want,(a,b,c,got,want)
   sharp11=any(t==11 for sig,t,p in eligible)
   assert sharp11==(a==2 and b>=3 and c>=5),(a,b,c,sharp11)

# Exact small-graph labelled counts by a separate enumeration of every initial state.
def direct_graph_census(a,b,c):
    shores=[tuple(range(0,a)),tuple(range(a,a+b)),tuple(range(a+b,a+b+c))]
    record=Counter()
    for conf in product(range(3),repeat=a+b+c):
        state=conf; seen={}
        while state not in seen:
            seen[state]=len(seen)
            excited=[sum(state[k]==1 for k in shore) for shore in shores]
            state=tuple((state[k]+1)%3 if state[k] else int(sum(excited[j] for j in range(3) if j!=s)>=2)
                        for s,shore in enumerate(shores) for k in shore)
        record[(seen[state],len(seen)-seen[state])]+=1
    return record

def factor_count_for_sizes(a,b,c):
    result=Counter()
    for sig,t,p in rows:
        shore_counts=[]
        for s,m in enumerate((a,b,c)):
            v=sig[3*s:3*s+3]
            if not realized(v,m):
                break
            # Sum the multinomial counts over every realization of signature.
            counts=0
            for r in range(m+1):
             for e in range(m-r+1):
              f=m-r-e
              if tuple(min(2,j) for j in (r,e,f))==v:
               from math import factorial
               counts+=factorial(m)//(factorial(r)*factorial(e)*factorial(f))
            shore_counts.append(counts)
        if len(shore_counts)==3:
            result[t,p]+=shore_counts[0]*shore_counts[1]*shore_counts[2]
    return result

for sizes in [(1,1,1),(1,2,3),(2,2,2),(2,2,4)]:
    a,b,c=sizes
    first=direct_graph_census(a,b,c)
    second=factor_count_for_sizes(a,b,c)
    assert first==second,(sizes,first,second)
    print('FULL_LABELLED_CHECK_OK',sizes,3**(a+b+c),sorted(first.items()))

out=Path(sys.argv[1]) if len(sys.argv)>1 else Path('certificates/tripartite_signatures.csv')
out.parent.mkdir(parents=True,exist_ok=True)
with out.open('w',newline='',encoding='utf-8') as stream:
    wr=csv.writer(stream)
    wr.writerow(['c00','c01','c02','c10','c11','c12','c20','c21','c22','first_entry','primitive_period'])
    for sig,t,p in rows:wr.writerow([*sig,t,p])
print('ALL_QUOTIENT_AND_MICROSCOPIC_CHECKS_PASSED',len(rows),'cases', 'maxT=11','periods=1,3,4,12')
print('JOINT_HISTOGRAM',sorted(hist.items()))
print('CERTIFICATE',out,'rows',len(rows))
