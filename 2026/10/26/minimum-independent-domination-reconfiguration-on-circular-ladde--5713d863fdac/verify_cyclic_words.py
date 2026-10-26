"""Independent finite-state word enumerator and gap-transfer checks for prisms."""
from collections import Counter, deque
from itertools import combinations, product
from math import comb


def valid(word):
    n=len(word)
    if any(word[i] and word[i]==word[(i+1)%n] for i in range(n)):
        return False
    for i,x in enumerate(word):
        if x==0 and sorted((word[(i-1)%n],word[(i+1)%n])) != [1,2]:
            return False
    return True


def encode(word):
    return frozenset((i,x) for i,x in enumerate(word) if x)


def verify_words(n):
    feasible = [w for w in product((0,1,2),repeat=n) if valid(w)]
    k = min(sum(x!=0 for x in w) for w in feasible)
    words = [w for w in feasible if sum(x!=0 for x in w)==k]
    assert k==2*((n+3)//4)
    index={encode(w):i for i,w in enumerate(words)}
    adj=[set() for _ in words]
    for p,w in enumerate(words):
        S=encode(w)
        for i,x in enumerate(w):
            if not x:continue
            for j in ((i-1)%n,(i+1)%n):
                if w[j]==0:
                    t=(S-{(i,x)}) | {(j,x)}
                    if t in index and index[t]!=p:
                        adj[p].add(index[t])
    seen=set()
    components=[]
    for i in range(len(words)):
        if i in seen:continue
        q=[i];seen.add(i)
        for x in q:
            for y in adj[x]:
                if y not in seen:seen.add(y);q.append(y)
        components.append(len(q))
    z=n-k
    count=2*n*comb(k,z)//k
    edges=2*n*comb(k-2,z-1) if z<k else 0
    assert len(words)==count
    assert sum(map(len,adj))==2*edges
    assert sorted(components,reverse=True)==([1]*4 if z==k else [count])
    if z==k-1:assert all(len(a)==2 for a in adj)
    degrees=Counter(len(a) for a in adj)
    expected_degrees={0:4} if z==k else {
        2*r: (2*n*comb(z-1,r-1)*comb(k-z-1,r-1)//r)
        for r in range(1,min(z,k-z)+1)
    }
    assert degrees == expected_degrees,(n,degrees,expected_degrees)
    colors={}
    for start in range(len(words)):
        if start in colors:continue
        colors[start]=0
        q=[start]
        for v in q:
            for u in adj[v]:
                if u not in colors:colors[u]=1-colors[v];q.append(u)
                else:assert colors[u]==1-colors[v],(n,u,v)
    return k,count,edges,sorted(components,reverse=True),dict(sorted(degrees.items()))


def verify_labeled_gap_connectivity(k,z):
    n=k+z
    words=[sum(1<<i for i in I) for I in combinations(range(k),z)]
    states={(p,b) for p in range(n) for b in words}
    a=states.pop()
    q=[a]
    for p,b in q:
        for i in range(k):
            older=(b>>((i-1)%k))&1
            later=(b>>i)&1
            if older==later:continue
            pp=(p+(1 if later else -1))%n if i==0 else p
            cc=b^(1<<((i-1)%k))^(1<<i)
            nxt=(pp,cc)
            if nxt in states:
                states.remove(nxt)
                q.append(nxt)
    assert not states,(k,z,len(states))
    return len(q)


def main():
    for n in range(3,14):
        k,N,E,comps,degrees=verify_words(n)
        print(f'n={n} i={k} sets={N} edges={E} components={comps} degrees={degrees} bipartite=YES PASS')
    for k in range(2,10,2):
        for z in range(1,k):
            count=verify_labeled_gap_connectivity(k,z)
            print(f'gap k={k} z={z} states={count} connected PASS')
    print('WORD AND GAP CHECK PASS')

if __name__=='__main__':
    main()
