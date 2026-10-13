from collections import Counter, deque
from math import comb

def crown(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def distances(adj):
    out=[]
    for s in range(len(adj)):
        d=[99]*len(adj); d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==99:
                    d[v]=d[u]+1; q.append(v)
        out.append(d)
    return out

def semitotal(adj,D,S):
    S=set(S)
    for v in range(len(adj)):
        if v not in S and not (adj[v] & S):
            return False
    for v in S:
        if not any(w!=v and D[v][w] <= 2 for w in S):
            return False
    return True

def predicted(n,S):
    S=set(S); A=set(range(n)); B=set(range(n,2*n))
    p=len(S&A); q=len(S&B)
    if S==A or S==B: return True
    if p>=2 and q>=2: return True
    if p==1 and q>=2:
        i=next(iter(S&A)); return n+i in S
    if q==1 and p>=2:
        j=next(iter(S&B))-n; return j in S
    return False

def predicted_minimal(n,S):
    S=set(S); A=set(range(n)); B=set(range(n,2*n))
    if S==A or S==B: return True
    p=len(S&A); q=len(S&B)
    if p==1 and q==2:
        i=next(iter(S&A)); return n+i in S
    if p==2 and q==1:
        j=next(iter(S&B))-n; return j in S
    if p==2 and q==2:
        I=S&A; J={j-n for j in S&B}
        return I.isdisjoint(J)
    return False

total_subsets=0
for n in range(3,8):
    adj=crown(n); D=distances(adj)
    profile=Counter(); minimal=Counter()
    for mask in range(1<<(2*n)):
        S={v for v in range(2*n) if mask>>v & 1}
        actual=semitotal(adj,D,S)
        assert actual==predicted(n,S)
        total_subsets += 1
        if actual:
            profile[len(S)] += 1
            is_min=all(not semitotal(adj,D,S-{v}) for v in S)
            assert is_min==predicted_minimal(n,S)
            if is_min: minimal[len(S)] += 1
    formula=Counter(); formula[n]+=2
    for p in range(2,n+1):
        for q in range(2,n+1):
            formula[p+q]+=comb(n,p)*comb(n,q)
    for q in range(2,n+1):
        formula[q+1]+=2*n*comb(n-1,q-1)
    assert profile==formula
    expected_min=Counter(); expected_min[n]+=2; expected_min[3]+=2*n*(n-1)
    if n>=4: expected_min[4]+=comb(n,2)*comb(n-2,2)
    assert minimal==expected_min
    assert min(profile)==3 and max(minimal)==n
    print(f'n={n}: semitotal_sets={sum(profile.values())}, minimal_profile={dict(minimal)}')
print('VERIFY_OK')
print('vertex_subsets_checked =', total_subsets)
print('all direct semitotal tests matched the all-set classification')
print('all semitotal-polynomial coefficients and minimal-set profiles matched')
