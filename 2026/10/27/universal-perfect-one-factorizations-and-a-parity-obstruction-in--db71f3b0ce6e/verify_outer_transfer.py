"""Independent outer-cycle transfer enumeration for GP(3k,k).

Enumerates possible length-k words of colour triples across the outer cycle.
A local transition is allowed when a column's three spokes get three
mutually distinct colours. The closure twists the row index cyclically.
No graph edge-search or backtracking propagation is used.
"""
from collections import Counter
from itertools import product

TRIPLES=list(product(range(3),repeat=3))

def compatible(prev,cur):
    if any(prev[r]==cur[r] for r in range(3)): return False
    spokes=[3-prev[r]-cur[r] for r in range(3)]
    return set(spokes)=={0,1,2}

NEXT={x:[y for y in TRIPLES if compatible(x,y)] for x in TRIPLES}

def factor_cycles(k, word, unused):
    n=3*k
    outer=[0]*n
    for i,t in enumerate(word):
        for r in range(3):outer[i+r*k]=t[r]
    spoke=[0]*n
    for j in range(n):
        assert outer[(j-1)%n]!=outer[j]
        spoke[j]=3-outer[(j-1)%n]-outer[j]
    E=[]; C=[]
    for j in range(n): E.append((j,(j+1)%n));C.append(outer[j])
    for j in range(n): E.append((j,n+j));C.append(spoke[j])
    for i in range(k):
        rows=[i,i+k,i+2*k]
        assert set(spoke[j] for j in rows)=={0,1,2}
        for r in range(3):
            a,b=rows[r],rows[(r+1)%3]
            third=rows[(r+2)%3]
            E.append((n+a,n+b)); C.append(spoke[third])
    inc=[[] for _ in range(2*n)]
    for e,(a,b) in enumerate(E):inc[a].append(e);inc[b].append(e)
    assert all(set(C[e] for e in star)=={0,1,2} for star in inc)
    counts=[]
    for excluded in range(3):
        active=[e for e in range(len(E)) if C[e]!=excluded]
        ad=[[] for _ in range(2*n)]
        for e in active:
            a,b=E[e];ad[a].append(b);ad[b].append(a)
        assert all(len(t)==2 for t in ad)
        seen=set();components=0
        for start in range(2*n):
            if start in seen:continue
            components+=1;todo=[start];seen.add(start)
            while todo:
                a=todo.pop()
                for b in ad[a]:
                    if b not in seen:seen.add(b);todo.append(b)
        counts.append(components)
    return tuple(sorted(counts))

def check(k):
    pattern=Counter(); families=Counter(); solutions=0
    def extend(word):
        nonlocal solutions
        if len(word)==k:
            last=word[-1]
            # The predecessor of row r=0,1,2 in column zero
            # comes from row r-1 at column k-1.
            before=(last[2],last[0],last[1])
            if not compatible(before,word[0]):return
            solutions+=1
            if len(set(word[0]))==3:families['distinct']+=1
            else:families['two-equal']+=1
            profile=factor_cycles(k,word,None)
            pattern[profile]+=1
            return
        for nxt in NEXT[word[-1]]:
            extend(word+[nxt])
    for first in TRIPLES:
        if NEXT[first]: extend([first])
    assert solutions%6==0
    factors=solutions//6
    J=(2**k-(-1)**k)//3
    assert factors==(J if k%2 else 4*J)
    # Each factorization occurs six times via global colour permutation.
    counts={p:q//6 for p,q in sorted(pattern.items())}
    assert all(q%6==0 for q in pattern.values())
    perfect=counts.get((1,1,1),0)
    assert perfect==(J if k%2 else 0)
    if k%2:assert families['two-equal']==0
    return f'k={k} factors={factors} perfect={perfect} triple_types={dict(families)} profiles={counts}'

if __name__=='__main__':
    for k in range(1,11):print(check(k),flush=True)
    print('ALL_OUTER_TRANSFER_CHECKS_PASS')
