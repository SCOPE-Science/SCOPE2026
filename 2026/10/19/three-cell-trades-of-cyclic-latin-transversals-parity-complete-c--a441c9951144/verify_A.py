"""Exact cyclic-Latin transversal three-row-switch graph: recursive orthomorphism generation."""
from collections import Counter,deque
from itertools import combinations

def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def gen(n):
    # Assign one column and one symbol to each row; both must be permutations.
    p=[-1]*n
    def rec(i, cols,syms):
        if i==n:
            yield tuple(p)
            return
        for j in range(n):
            if cols & (1<<j) or syms & (1<<((j-i)%n)): continue
            p[i]=j
            yield from rec(i+1,cols|(1<<j),syms|(1<<((j-i)%n)))
    return list(rec(0,0,0))

def run(n):
    verts=gen(n);lookup={p:i for i,p in enumerate(verts)}
    neighbors=[set() for _ in verts]
    for u,p in enumerate(verts):
        for a,b,c in combinations(range(n),3):
            for q in ((p[b],p[c],p[a]),(p[c],p[a],p[b])):
                t=list(p);t[a],t[b],t[c]=q
                v=lookup.get(tuple(t))
                if v is not None:
                    neighbors[u].add(v)
    assert all(u in neighbors[v] for v,ad in enumerate(neighbors) for u in ad)
    classes={}
    for i,p in enumerate(verts):
        d=tuple((p[r]-r)%n for r in range(n))
        k=(parity(p),parity(d))
        classes.setdefault(k,set()).add(i)
    seen=set();comps=[];parts=[];maxdiam={}
    for i in range(len(verts)):
        if i in seen:continue
        reach={i};todo=[i]
        for u in todo:
            for v in neighbors[u]:
                if v not in reach:reach.add(v);todo.append(v)
        seen.update(reach);comps.append(reach)
        parts.append((len(reach), next(k for k,xx in classes.items() if i in xx)))
    for k,ids in classes.items():
        # Certificate: each parity class is connected if & only if one component fully covers it.
        ss={next(c for c in range(len(comps)) if v in comps[c]) for v in ids}
        maxdiam[k] = None
        if len(ss)==1:
            C=comps[next(iter(ss))]
            if len(C)<=600:
                diam=0
                for s in C:
                    dist={s:0};Q=deque([s])
                    while Q:
                        u=Q.popleft()
                        for v in neighbors[u]:
                            if v not in dist:
                                dist[v]=dist[u]+1;Q.append(v)
                    assert len(dist)==len(C)
                    diam=max(diam,max(dist.values()))
                maxdiam[k]=diam
    e=sum(map(len,neighbors))//2
    print('n',n,'vertices',len(verts),'edges',e,'parities',dict(sorted((k,len(v)) for k,v in classes.items())),
          'components',len(comps),'component-size-counts',dict(sorted(Counter(map(len,comps)).items())),
          'components-by-parity',dict(sorted(Counter(parts).items(),key=lambda x:str(x[0]))),
          'degrees',dict(sorted(Counter(map(len,neighbors)).items())),
          'max-distance-parity-class',maxdiam)
    return verts,neighbors,classes

if __name__=='__main__':
    for n in (3,5,7,9): run(n)
    print('VERIFY_A_OK')
