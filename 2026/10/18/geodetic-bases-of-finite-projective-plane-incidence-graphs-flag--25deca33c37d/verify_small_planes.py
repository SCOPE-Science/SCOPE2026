"""Independent exhaustive geodetic-basis test for PG(2,2) and PG(2,3).
Uses shortest-path intervals, not the geometric classification, to test all subsets.
Run: python3 verify_small_planes.py
"""
from collections import Counter, deque
from itertools import combinations, product


def build(q):
    def normalize(v):
        z=next(a for a in v if a)
        zinv=pow(z,-1,q)
        return tuple((a*zinv)%q for a in v)
    points=sorted({normalize(v) for v in product(range(q),repeat=3) if any(v)})
    v=len(points); graph=[set() for _ in range(2*v)]
    for p,x in enumerate(points):
        for line,y in enumerate(points):
            if sum(a*b for a,b in zip(x,y))%q==0:
                graph[p].add(v+line);graph[v+line].add(p)
    distances=[]
    for s in range(2*v):
        d=[-1]*(2*v);d[s]=0;todo=deque([s])
        while todo:
            x=todo.popleft()
            for y in graph[x]:
                if d[y]<0:d[y]=d[x]+1;todo.append(y)
        assert -1 not in d
        distances.append(d)
    intervals={}
    for u in range(2*v):
        for w in range(u+1,2*v):
            mask=0
            for z in range(2*v):
                if distances[u][z]+distances[z][w]==distances[u][w]:
                    mask|=1<<z
            intervals[u,w]=mask
    return v,graph,intervals


def main():
    for q in (2,3):
        v,graph,I=build(q);n=2*v;full=(1<<n)-1
        counts={};bases=[]
        for size in range(1,2*q+1):
            num=0
            for S in combinations(range(n),size):
                covered=sum(1<<x for x in S)
                for u,w in combinations(S,2):covered|=I[u,w]
                if covered==full:
                    num+=1
                    if size==2*q:bases.append(frozenset(S))
            counts[size]=num
        assert counts[2*q]==v*(q+1)
        assert sum(counts[k] for k in range(1,2*q))==0
        flags=[]
        for x in range(v):
            for l in range(v):
                if v+l in graph[x]:
                    S=frozenset([p for p in range(v) if v+l in graph[p] and p!=x]+[v+j for j in range(v) if v+j in graph[x] and j!=l])
                    flags.append(S)
        assert len(set(flags))==v*(q+1)
        assert set(flags)==set(bases)
        dists=Counter(len(a-b) for a,b in combinations(flags,2))
        target=Counter()
        target[q+1]+=v*(q+1)*q
        target[2*q-2]+=v*(q+1)*q**3//2
        target[2*q]+=v*(q+1)*q*q
        assert dists==target,(q,dists,target)
        minmove=min(k for k in dists if dists[k])
        for radius in (minmove-1,minmove):
            todo=[flags[0]];seen={flags[0]}
            while todo:
                a=todo.pop()
                for b in flags:
                    if b not in seen and len(a-b)<=radius:
                        seen.add(b);todo.append(b)
            assert len(seen)==(1 if radius<minmove else len(flags))
        print('q=',q,'vertices=',n,'counts=',counts,'flags=',len(flags),'pair_distances=',sorted(dists.items()),'minimum_connected_jump=',minmove)
    print('ALL SMALL-PLANE EXHAUSTIVE CHECKS PASS')

if __name__=='__main__':main()
