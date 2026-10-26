"""Exact checks for optimum total domination and token exchanges in prism graphs.

Usage: python3 verify.py
Uses only the Python standard library. All vertex labels are zero-based.
This is finite corroboration; the manuscript contains the infinite proofs.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

POP = (0, 1, 1, 2)

def local(a, b, c):
    return bool((a & 1) or (c & 1) or (b & 2)) and bool((a & 2) or (c & 2) or (b & 1))

def prism_mask(word):
    n = len(word)
    return sum(((v & 1) << i) + (((v >> 1) & 1) << (n+i)) for i,v in enumerate(word))

def optimal_prism(n):
    """Enumerate *all* optimal cyclic words by exact two-column DP."""
    best = 10**5
    words = []
    for a in range(4):
        for b in range(4):
            @lru_cache(None)
            def suffix(i, prev, curr):
                if i == n:
                    return 0 if local(prev, curr, a) and local(curr, a, b) else 10**5
                return min(POP[nxt] + suffix(i+1, curr, nxt)
                           for nxt in range(4) if local(prev, curr, nxt))
            score = POP[a]+POP[b]+suffix(2,a,b)
            if score > best:
                continue
            if score < best:
                best, words = score, []
            def extend(i, prev, curr, score_now, word):
                if i == n:
                    if score_now == best and local(prev,curr,a) and local(curr,a,b):
                        words.append(tuple(word))
                    return
                for nxt in range(4):
                    if local(prev,curr,nxt) and score_now+POP[nxt]+suffix(i+1,curr,nxt) == best:
                        extend(i+1,curr,nxt,score_now+POP[nxt],word+[nxt])
            extend(2,a,b,POP[a]+POP[b],[a,b])
    return best, words

def prism_neighbors(n):
    out=[]
    for row in range(2):
        for i in range(n):
            out.append((1<<(row*n+(i-1)%n))|
                       (1<<(row*n+(i+1)%n))|
                       (1<<((1-row)*n+i)))
    return out

def total_dom(mask,neigh):
    return all(mask & adj for adj in neigh)

def cycle_sets(n):
    d=(n+2)//3
    out=[]
    for C in combinations(range(n),d):
        m=sum(1<<i for i in C)
        if all(m & ((1<<i)|(1<<((i-1)%n))|(1<<((i+1)%n))) for i in range(n)):
            out.append(m)
    return out

def cycle_adjacencies(sets,n):
    lookup={m:i for i,m in enumerate(sets)}
    adj=[set() for _ in sets]
    for i,m in enumerate(sets):
        for p in range(n):
            if not (m>>p)&1:continue
            for q in range(n):
                if (m>>q)&1:continue
                j=lookup.get(m^(1<<p)^(1<<q))
                if j is not None:adj[i].add(j)
    return adj

def components(adj):
    seen=set(); sizes=[]
    for x in range(len(adj)):
        if x in seen:continue
        todo=[x];seen.add(x);size=0
        while todo:
            u=todo.pop();size+=1
            for v in adj[u]:
                if v not in seen:seen.add(v);todo.append(v)
        sizes.append(size)
    return sorted(sizes)

def verify(n):
    gamma, words=optimal_prism(n)
    masks=[prism_mask(w) for w in words]
    assert len(set(masks))==len(masks)
    neigh=prism_neighbors(n)
    assert all(total_dom(m,neigh) and m.bit_count()==gamma for m in masks)
    ix={m:i for i,m in enumerate(masks)}
    N=2*n
    if n % 2 == 0:
        cs=cycle_sets(n)
        ca=cycle_adjacencies(cs,n)
        target=set()
        for p in cs:
            for q in cs:
                bits=0
                for j in range(n):
                    if p>>j&1:bits|=1<<(j if j%2==0 else n+j)
                    if q>>j&1:bits|=1<<(n+j if j%2==0 else j)
                target.add(bits)
        assert set(masks)==target
        expected={0:(9,0),2:(n*n,4),4:((n*(n+5)//6)**2,8)}[n%6]
        assert len(masks)==expected[0]
        factor_degree={0:0,2:2,4:4}[n%6]
        assert all(len(A)==factor_degree for A in ca)
        if n%6==0:
            assert components(ca)==[1,1,1]
        else:
            assert components(ca)==[len(cs)]
        # Product structure is proved by the A/B partition, verify one-token adjacency.
        if n<=20:
            for m in masks:
                obs={ix[m^(1<<u)^(1<<v)] for u in range(N) if m>>u&1
                     for v in range(N) if not(m>>v&1) and (m^(1<<u)^(1<<v)) in ix}
                assert len(obs)==expected[1], (n,m,len(obs))
        print('EVEN_OK',n,'minimum',gamma,'minima',len(masks),
              'factor_states',len(cs),'factor_degree',factor_degree,flush=True)
    elif n%6 == 3:
        assert gamma==2*n//3 and len(masks)==3
        for m in masks:
            assert all((m & a).bit_count()==1 for a in neigh)
        print('ODD_ZERO_EXCESS_OK',n,'minima',len(masks),flush=True)
    elif n%6 == 1:
        assert gamma==(2*n+1)//3 and len(masks)==2*n
        over={}
        for m in masks:
            excess=[j for j,a in enumerate(neigh) if (m&a).bit_count()==2]
            assert len(excess)==1
            assert excess[0] not in over
            over[excess[0]]=m
        assert len(over)==N
        for idx,m in over.items():
            target={((1-(idx//n))*n + ((idx % n)+d)%n) for d in (-3,3)}
            obs=set()
            for u in range(N):
                if not(m>>u&1):continue
                for v in range(N):
                    if m>>v&1:continue
                    other=m^(1<<u)^(1<<v)
                    if other in ix:
                        for x,y in over.items():
                            if y==other:obs.add(x);break
            assert obs==target,(n,idx,obs,target)
        print('ODD_ONE_EXCESS_OK',n,'minima',len(masks),'degree',2,flush=True)
    else:
        # The odd 5 (mod 6) class is intentionally outside the theorem.
        print('UNCLAIMED_BOUNDARY_CHECK_OK',n,'minimum',gamma,'minima',len(masks),flush=True)

    if n<=10:
        # An independent direct enumeration avoids relying solely on cyclic-word DP.
        direct=[]
        for size in range(1,gamma+1):
            for comb in combinations(range(N),size):
                m=sum(1<<j for j in comb)
                if total_dom(m,neigh):direct.append(m)
            if direct:
                assert size==gamma
                break
        assert set(direct)==set(masks)
        print('DIRECT_SUBSET_EXHAUSTIVE_OK',n,'count',len(direct),flush=True)

if __name__=='__main__':
    for N in range(3,27):verify(N)
    print('ALL_VERIFY_OK')
