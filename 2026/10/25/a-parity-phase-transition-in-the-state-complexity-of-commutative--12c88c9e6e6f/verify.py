"""Reproducible finite checks of the dihedral identity-language theorem.
Run: python verify.py. Uses only the Python standard library.
"""
from collections import deque
from itertools import product


def exact_from_group(n,x,y):
    # (k,e) represents a^k b^e, b a b = a^{-1}.
    from functools import lru_cache
    @lru_cache(None)
    def dp(i,j):
        if (i,j)==(0,0): return frozenset({(0,0)})
        res=set()
        if i:
            res.update(((k+(-1)**e)%n,e) for k,e in dp(i-1,j))
        if j:
            res.update((k,e^1) for k,e in dp(i,j-1))
        return frozenset(res)
    return (0,0) in dp(x,y)


def criterion(n,x,y):
    if y==0:
        return x%n==0
    if y&1:
        return False
    return x%2==0 or (n%2==1 and x>=n)


def canonical(n,x,y):
    if n%2==0:
        if y==0: return ('Z',x%n)
        return ('P',y%2,x%2)
    if y==0:
        if x<n-1: return ('L',x)
        return ('H',x%n)
    return ('P',y%2,min(x,n-1))


def build(n):
    init=canonical(n,0,0)
    ids={init:0}; queue=deque([init]); rows=[]; final=[]
    def transitions(st, letter):
        if st[0]=='Z':
            x=st[1]
            return canonical(n,x+(letter=='a'),(letter=='b'))
        if st[0]=='L':
            x=st[1]
            return canonical(n,x+(letter=='a'),(letter=='b'))
        if st[0]=='H':
            # any chosen witness x>=n-1 with residue r
            x=(n-1)+((st[1]-(n-1))%n)
            return canonical(n,x+(letter=='a'),(letter=='b'))
        if st[0]=='P':
            parity,x=st[1:]
            # y=1 for odd; y=2 for even
            y=1 if parity else 2
            if n%2==0:
                # x is parity and positive acceptance depends only on parity
                return canonical(n,x+(letter=='a'),y+(letter=='b'))
            return canonical(n,x+(letter=='a'),y+(letter=='b'))
        raise ValueError(st)
    def accepted(st):
        if st[0]=='Z': return st[1]==0
        if st[0]=='L': return st[1]==0
        if st[0]=='H': return st[1]==0
        if st[0]=='P':
            if st[1]==1:return False
            x=st[2]
            return x%2==0 or (n%2==1 and x==n-1)
        raise ValueError(st)
    while queue:
        st=queue.popleft()
        final.append(accepted(st))
        rr=[]
        for a in 'ab':
            nxt=transitions(st,a)
            if nxt not in ids:
                ids[nxt]=len(ids);queue.append(nxt)
            rr.append(ids[nxt])
        rows.append(rr)
    assert len(ids)==len(rows)
    return ids,rows,final


def equivalent_pairs(rows,final):
    # Direct distinguishability via reverse product graph. Every unequal
    # accepting-bit pair is initially distinguishable by epsilon.
    N=len(rows)
    parent=[[] for _ in range(N*N)]
    for i in range(N):
        for j in range(N):
            for a in range(2):
                v=rows[i][a]*N+rows[j][a]
                parent[v].append(i*N+j)
    seen=[False]*(N*N); q=deque()
    for i in range(N):
        for j in range(N):
            if final[i]!=final[j]:
                k=i*N+j;seen[k]=True;q.append(k)
    while q:
        t=q.popleft()
        for k in parent[t]:
            if not seen[k]:seen[k]=True;q.append(k)
    eq=[(i,j) for i in range(N) for j in range(i+1,N) if not seen[i*N+j]]
    return eq


def run():
    checks=0;words=0
    for n in range(2,31):
        # independent group multiplication check in finite rectangle
        bnd=min(2*n+3,25)
        for x in range(bnd):
            for y in range(7):
                assert exact_from_group(n,x,y)==criterion(n,x,y), (n,x,y)
                checks+=1
        ids,rows,final=build(n)
        eq=equivalent_pairs(rows,final)
        # Count equivalence classes with union-find; do not assume pair disjointness.
        parent=list(range(len(ids)))
        def root(v):
            while parent[v]!=v:
                parent[v]=parent[parent[v]]
                v=parent[v]
            return v
        for i,j in eq: parent[root(i)]=root(j)
        minimal=len({root(i) for i in range(len(ids))})
        pred=4 if n==2 else (n+4 if n%2==0 else 4*n-1)
        assert minimal==pred,(n,len(ids),eq,pred)
        for word_length in range(0,10 if n<11 else 7):
            for letters in product('ab',repeat=word_length):
                word=''.join(letters)
                st=0
                for l in word:st=rows[st]['ab'.index(l)]
                assert final[st]==criterion(n,word.count('a'),word.count('b'))
                words+=1
    print(f'VERIFY_OK: {checks} independent group-count cases; {words} complete word/automaton checks; n=2..30')

if __name__=='__main__':run()
