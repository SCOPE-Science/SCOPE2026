"""Finite independent checks for neighborhood complexes of finite block graphs.

Usage: python verify.py
Requires the Python standard library only.
This is a finite test of the stated all-order theorem, not its proof.
"""
from itertools import combinations
from collections import defaultdict, deque
import random


def is_connected(ad):
    seen={0}; q=deque([0]);
    while q:
        v=q.popleft()
        for w in ad[v]:
            if w not in seen: seen.add(w); q.append(w)
    return len(seen)==len(ad)


def blocks(ad):
    """Tarjan edge-stack biconnected components, as sets of vertices."""
    n=len(ad); idx=[-1]*n; low=[-1]*n; stack=[]; out=[]; tick=[0]
    def dfs(v,parent):
        idx[v]=low[v]=tick[0]; tick[0]+=1
        for w in sorted(ad[v]):
            if w==parent: continue
            if idx[w]<0:
                stack.append((v,w)); dfs(w,v); low[v]=min(low[v],low[w])
                if low[w]>=idx[v]:
                    comp=set()
                    while True:
                        a,b=stack.pop();comp.add(a);comp.add(b)
                        if (a,b)==(v,w):break
                    out.append(comp)
            elif idx[w]<idx[v]:
                stack.append((v,w));low[v]=min(low[v],idx[w])
    dfs(0,-1)
    assert all(t>=0 for t in idx)
    assert not stack
    return out


def faces_N(ad):
    bysize=defaultdict(set)
    for adjacent in ad:
        vals=sorted(adjacent)
        for k in range(1,len(vals)+1):
            bysize[k-1].update(combinations(vals,k))
    return [sorted(bysize[j]) for j in range(max(bysize,default=-1)+1)]


def rank_mod2(columns):
    pivots={}
    for c in columns:
        while c:
            v=c.bit_length()-1
            if v in pivots: c^=pivots[v]
            else: pivots[v]=c;break
    return len(pivots)


def betti_N(ad):
    faces=faces_N(ad)
    if not faces: return []
    ranks=[]
    for k in range(1,len(faces)):
        lookup={f:i for i,f in enumerate(faces[k-1])}
        columns=[]
        for f in faces[k]:
            col=0
            for sub in combinations(f,k):col ^=1<<lookup[sub]
            columns.append(col)
        ranks.append(rank_mod2(columns))
    dims=[len(f) for f in faces]
    return [dims[i]-(ranks[i-1] if i>0 else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(len(dims))]


def predict(ad):
    bs=blocks(ad)
    if any(any(w not in ad[v] for v,w in combinations(b,2)) for b in bs):
        return None
    nontrivial=[len(b) for b in bs if len(b)>=3]
    if not nontrivial:return [2]
    out=[1, len(nontrivial)-1]
    for r in nontrivial:
        while len(out)<=r-2:out.append(0)
        out[r-2]+=1
    return out


def match(ad):
    expected=predict(ad)
    if expected is None:return False
    actual=betti_N(ad)
    while len(expected)<len(actual):expected.append(0)
    while len(actual)<len(expected):actual.append(0)
    assert actual==expected, (ad,actual,expected)
    return True


def labeled_graphs(n):
    edges=list(combinations(range(n),2));
    for code in range(1<<len(edges)):
        ad=[set() for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            if (code>>i)&1:
                ad[u].add(v);ad[v].add(u)
        if is_connected(ad):yield ad


def random_block_graph(rng):
    n=rng.choice((3,4,5,6))
    ad=[set() for _ in range(n)]
    for u,v in combinations(range(n),2):ad[u].add(v);ad[v].add(u)
    for _ in range(rng.randint(0,6)):
        r=rng.randint(2,6)
        v=rng.randrange(len(ad))
        fresh=list(range(len(ad),len(ad)+r-1))
        ad.extend(set() for _ in fresh)
        for u,w in combinations([v]+fresh,2):ad[u].add(w);ad[w].add(u)
    return ad


def check_gluing(g,h,va,vb):
    # Directly verify N(G vee H) = N(G) U N(H) U simplex on union of two neighbor sets.
    n=len(g); m=len(h)
    hmap={i:(va if i==vb else n+(i if i<vb else i-1)) for i in range(m)}
    out=[s.copy() for s in g]+[set() for _ in range(m-1)]
    for i in range(m):
        for j in h[i]:out[hmap[i]].add(hmap[j])
    lhs=set().union(*(set(t) for t in faces_N(out)))
    gfaces=set().union(*(set(t) for t in faces_N(g)))
    hfaces=set(tuple(sorted(hmap[i] for i in f)) for t in faces_N(h) for f in t)
    A=g[va]; B={hmap[j] for j in h[vb]}; AB=sorted(A|B)
    df=set()
    for k in range(1,len(AB)+1):df.update(combinations(AB,k))
    assert lhs==gfaces|hfaces|df
    assert {(va,)}==set(gfaces)&set(hfaces)
    assert all(set(f)<=A or set(f)<=B for f in df & (gfaces|hfaces))



def sign_to_sorted(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1


def oriented_clique_boundary(clique):
    clique=tuple(sorted(clique))
    out={}
    for i in range(len(clique)):
        face=clique[:i]+clique[i+1:]
        out[face]=(-1)**i
    return out


def apply_perm_chain(chain,perm):
    out={}
    for face,coeff in chain.items():
        vals=tuple(perm[x] for x in face)
        key=tuple(sorted(vals))
        out[key]=out.get(key,0)+coeff*sign_to_sorted(vals)
    return {k:v for k,v in out.items() if v}


def symmetry_example():
    from itertools import permutations
    # K4 glued to K4 along 0. The full automorphism group swaps blocks.
    blocks0=[(0,1,2,3),(0,4,5,6)]
    ad=[set() for _ in range(7)]
    for c in blocks0:
        for v,w in combinations(c,2):ad[v].add(w);ad[w].add(v)
    assert betti_N(ad)[:3]==[1,1,2]
    good=0
    for perm in permutations(range(7)):
        if not all({perm[j] for j in ad[i]}==ad[perm[i]] for i in range(7)):
            continue
        good+=1
        for c in blocks0:
            target=tuple(sorted(perm[x] for x in c))
            assert target in blocks0
            lhs=apply_perm_chain(oriented_clique_boundary(c),perm)
            s=sign_to_sorted(tuple(perm[x] for x in c))
            assert lhs=={f:s*v for f,v in oriented_clique_boundary(target).items()}
    assert good==72
    return good


def random_tree_line_test(rng):
    from heapq import heapify,heappop,heappush
    for _ in range(100):
        n=rng.randrange(4,12)
        word=[rng.randrange(n) for j in range(n-2)]
        degree=[1]*n
        for j in word:degree[j]+=1
        leaves=[j for j in range(n) if degree[j]==1]
        heapify(leaves)
        edges=[]
        for x in word:
            leaf=heappop(leaves)
            edges.append((leaf,x))
            degree[x]-=1
            if degree[x]==1:heappush(leaves,x)
        a,b=leaves
        edges.append((a,b))
        L=[set() for e in edges]
        for i,j in combinations(range(len(edges)),2):
            if set(edges[i])&set(edges[j]):L[i].add(j);L[j].add(i)
        assert match(L)
        degrees=[0]*n
        for i,j in edges:degrees[i]+=1;degrees[j]+=1
        branch=[d for d in degrees if d>=3]
        if not branch:expected=[2]
        else:
            expected=[1,len(branch)-1]
            for d in branch:
                while len(expected)<=d-2:expected.append(0)
                expected[d-2]+=1
        actual=betti_N(L)
        while len(expected)<len(actual):expected.append(0)
        while len(actual)<len(expected):actual.append(0)
        assert expected==actual
    return 100

def main():
    cnt=0
    for n in range(2,7):
        for ad in labeled_graphs(n):
            if match(ad):cnt+=1
    rng=random.Random(193841)
    randomcnt=0; gluingcnt=0; sizes=set()
    for i in range(150):
        ad=random_block_graph(rng)
        assert match(ad)
        randomcnt+=1
        sizes.add(len(ad))
        # Gluing identity in arbitrary graphs built from nontrivial blocks.
        if len(ad)<=19:
            b=random_block_graph(rng)
            if len(b)<=19:
                check_gluing(ad,b,rng.randrange(len(ad)),rng.randrange(len(b)))
                gluingcnt+=1
    symmetrycnt=symmetry_example()
    treecnt=random_tree_line_test(rng)
    print('VERIFY_OK', 'exhaustive_labeled_block_graphs_n2_to6='+str(cnt),
          'random_block_graphs='+str(randomcnt),
          'gluing_identities='+str(gluingcnt),
          'branch_tree_line_graphs='+str(treecnt),
          'signed_automorphisms='+str(symmetrycnt),
          'random_orders='+str(sorted(sizes)))

if __name__=='__main__':main()
