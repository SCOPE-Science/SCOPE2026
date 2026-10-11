"""Reproducible small-order checks for the affine-incidence Rips homotopy formula.
No external packages; exact arithmetic throughout.
"""
from collections import defaultdict, deque
from itertools import product


def incidence(q):
    assert q in (2, 3), 'The executable examples use prime fields F_2 and F_3.'
    pts = [(x, y) for x in range(q) for y in range(q)]
    ip = {p: j for j, p in enumerate(pts)}
    lines = []
    for slope in range(q):
        for intercept in range(q):
            lines.append(frozenset(ip[(x, (slope*x+intercept)%q)] for x in range(q)))
    for x in range(q):
        lines.append(frozenset(ip[(x,y)] for y in range(q)))
    assert len(lines) == q*(q+1)
    assert all(len(ln) == q for ln in lines)
    assert all(sum(p in ln for ln in lines) == q+1 for p in range(q*q))
    assert all(sum(p in ln and r in ln for ln in lines) == 1 for p in range(q*q) for r in range(p+1,q*q))
    return lines


def maximal_cliques(graph):
    n=len(graph)
    found=set()
    def bronk(R,P,X):
        if not P and not X:
            found.add(frozenset(R));return
        pivot=max(P|X,key=lambda u:len(P & graph[u]),default=None)
        for v in list(P - (graph[pivot] if pivot is not None else set())):
            bronk(R|{v},P&graph[v],X&graph[v])
            P.remove(v);X.add(v)
    bronk(set(),set(range(n)),set())
    return found


def compute(q):
    ls=incidence(q);p=q*q;n=p+len(ls)
    edges=[set() for _ in range(n)]
    for i,line in enumerate(ls):
        for j in line:
            edges[j].add(p+i);edges[p+i].add(j)
    assert sum(map(len,edges))//2==q*q*(q+1)
    dist=[]
    for v in range(n):
        d=[10**4]*n;d[v]=0; queue=deque([v])
        while queue:
            w=queue.popleft()
            for z in edges[w]:
                if d[z]>d[w]+1:
                    d[z]=d[w]+1;queue.append(z)
        dist.append(d)
    assert max(max(row) for row in dist)==4 and all(max(row)<=4 for row in dist)
    near=[{w for w in range(n) if w!=v and dist[v][w]<=2} for v in range(n)]
    computed=maximal_cliques(near)
    predicted=[set(range(p))]
    predicted.extend([{p+i}|set(line) for i,line in enumerate(ls)])
    predicted.extend([{v}|{p+i for i,L in enumerate(ls) if v in L} for v in range(p)])
    for choices in product(range(q),repeat=q+1):
        predicted.append({p+k*q+choices[k] for k in range(q+1)})
    predicted={frozenset(x) for x in predicted}
    # Remove nonmaximal proposals, if any, rather than assuming facet maximality.
    pred_max={x for x in predicted if not any(x < y for y in predicted)}
    assert computed==pred_max, (q,len(computed),len(pred_max))
    faces={0}
    for facet in computed:
        full=sum(1<<v for v in facet)
        x=full
        while x:
            faces.add(x);x=(x-1)&full
    fs=defaultdict(list)
    for m in faces:fs[m.bit_count()-1].append(m)
    ranks=[]
    for d in range(max(fs)+1):
        index={m:i for i,m in enumerate(fs[d-1])}
        pivots={}
        for f in fs[d]:
            col=0;u=f
            while u:
                bit=u&-u;u-=bit
                col ^= 1 << index[f^bit]
            while col:
                h=col.bit_length()-1
                if h not in pivots:pivots[h]=col;break
                col ^= pivots[h]
        ranks.append(len(pivots))
    b=[len(fs[d])-ranks[d]-(ranks[d+1] if d+1<len(ranks) else 0) for d in range(max(fs)+1)]
    expected={2:{2:4},3:{2:16,3:16}}[q]
    assert {d:v for d,v in enumerate(b) if v}==expected,(q,b)
    assert len(computed)==len(pred_max)
    chi=sum((-1)**d*len(fs[d]) for d in range(max(fs)+1))
    assert chi==1+sum((-1)**d*v for d,v in expected.items())
    print(f'q={q}: vertices={n}, facets={len(computed)}, simplices={len(faces)-1}, reduced_H={expected}, Euler={chi}')

if __name__=='__main__':
    compute(2);compute(3);print('VERIFY_OK')
