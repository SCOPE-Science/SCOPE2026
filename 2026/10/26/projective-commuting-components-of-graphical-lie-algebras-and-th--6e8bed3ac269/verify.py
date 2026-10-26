"""Direct small-field verification of commuting-projective components.

Construct the bracket from graph edges, without using the proposed centralizer formula
when computing actual edges. Compare full connected-component partitions with the
structural prediction obtained solely from complement connectivity and support.
"""
from itertools import product
from collections import deque


def projective(n,q):
    ans=[]
    for v in product(range(q),repeat=n):
        if not any(v):
            continue
        a=next(x for x in v if x)
        if a==1:
            ans.append(v)
    return ans


def comp_vertices(n,edges):
    es=set(tuple(sorted(e)) for e in edges)
    unseen=set(range(n)); comps=[]
    while unseen:
        a=min(unseen);seen={a}; stack=[a];unseen.remove(a)
        while stack:
            u=stack.pop()
            for v in sorted(unseen):
                if u != v and (min(u,v),max(u,v)) not in es:
                    unseen.remove(v);stack.append(v);seen.add(v)
        comps.append(frozenset(seen))
    return comps


def cdom_count(V,E,q):
    V=set(V); adj={u:set() for u in V}
    for u,v in E:
        if u in V and v in V:
            adj[u].add(v);adj[v].add(u)
    out=0
    vv=sorted(V)
    for bits in range(1,1<<len(vv)):
        S={vv[j] for j in range(len(vv)) if bits>>j &1}
        dom=S.copy()
        for u in S:dom.update(adj[u])
        if dom!=V:continue
        visited={next(iter(S))};stack=list(visited)
        while stack:
            u=stack.pop()
            for v in adj[u]&S:
                if v not in visited: visited.add(v);stack.append(v)
        if visited==S: out+=(q-1)**(len(S)-1)
    return out



def is_connected_dominating_support(V,E,v):
    V=set(V); S={i for i in V if v[i] != 0}
    if not S: return False
    adj={u:set() for u in V}
    for a,b in E:
        if a in V and b in V:adj[a].add(b);adj[b].add(a)
    dom=set(S)
    for u in S:dom.update(adj[u])
    if dom!=V:return False
    stack=[next(iter(S))]; seen=set(stack)
    while stack:
        u=stack.pop()
        for w in adj[u]&S:
            if w not in seen:seen.add(w);stack.append(w)
    return seen==S

def check(n,q,edges):
    E=set(tuple(sorted(x)) for x in edges)
    deg=[0]*n
    for u,v in E:deg[u]+=1;deg[v]+=1
    if min(deg)==0:return False
    comps=comp_vertices(n,E)
    lines=projective(n,q)
    N=len(lines)
    adj=[[] for _ in lines]
    for i in range(N):
        u=lines[i]
        for j in range(i):
            v=lines[j]
            if all((u[a]*v[b]-u[b]*v[a])%q==0 for a,b in E):
                adj[i].append(j);adj[j].append(i)
    # Full actual graph components, computed only using determinants
    observed=[];visited=set()
    for i in range(N):
        if i in visited:continue
        stack=[i];visited.add(i);C={i}
        while stack:
            u=stack.pop()
            for w in adj[u]:
                if w not in visited:visited.add(w);stack.append(w);C.add(w)
        observed.append(frozenset(C))
    predicted=[];claimed=[]
    for V in comps:
        indices=frozenset(i for i,v in enumerate(lines) if all(v[j]==0 for j in range(n) if j not in V))
        eligible=frozenset(i for i in indices if not is_connected_dominating_support(V,E,lines[i]))
        # Eligibility uses only support connectivity/dominance, independently
        # of any adjacencies constructed in the direct bracket graph.
        if len(V)>=2:predicted.append(eligible)
        claimed.append((V,len(indices),len(eligible),cdom_count(V,E,q)))
        if len(indices)-len(eligible) != claimed[-1][3]:
            raise AssertionError(('connected-dom count',n,q,E,claimed))
    claimed_nontrivial=set().union(*predicted) if predicted else set()
    predicted+= [frozenset({i}) for i in range(N) if i not in claimed_nontrivial]
    if set(observed)!=set(predicted):
        raise AssertionError(('component partition',n,q,E,comps,[len(a) for a in observed],claimed))
    if len(predicted)!=len(set(predicted)):
        raise AssertionError(('duplicate',n,q,E))
    # Independence check via general cardinality formula
    isolates=sum(1 for a in adj if not a)
    expected=(q**n-1)//(q-1)-sum((q**len(V)-1)//(q-1)- cdom_count(V,E,q) for V in comps)
    assert isolates==expected,(n,q,E,isolates,expected)
    # Tree specialization, separately check leaf count without support combinatorics
    if n>=3 and len(E)==n-1:
        # connectivity of G since no isolated isn't sufficient
        todo={0};front=[0]
        while front:
            u=front.pop()
            for v in range(n):
                if tuple(sorted((u,v))) in E and v not in todo:
                    todo.add(v);front.append(v)
        if len(todo)==n:
            leaves=deg.count(1)
            assert isolates==q**leaves*(q-1)**(n-leaves-1),(n,q,E,isolates,leaves)
            if max(deg)==n-1:
                assert len([C for C in observed if len(C)>1])==1
            else:
                assert len([C for C in observed if len(C)>1])==1
    return True


def tree_prufer(seq,n):
    deg=[1]*n
    for x in seq:deg[x]+=1
    E=[]
    for x in seq:
        leaf=next(i for i in range(n) if deg[i]==1)
        E.append((leaf,x));deg[leaf]-=1;deg[x]-=1
    leafs=[i for i in range(n) if deg[i]==1]
    E.append(tuple(leafs))
    return E


def main():
    cases=0
    for q in (2,3):
        for n in range(2,6):
            for mask in range(1<<(n*(n-1)//2)):
                pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
                E=[e for i,e in enumerate(pairs) if mask>>i & 1]
                if check(n,q,E):cases+=1
    for q in (2,3):
        for n in (6,):
            # Prüfer codes: all trees (6**4=1296) for q=2, and a targeted
            # sample for q=3; nonisomorphic shapes appear among these.
            seqs=product(range(n),repeat=n-2)
            for i,seq in enumerate(seqs):
                if q==3 and i%50!=0:continue
                if check(n,q,tree_prufer(seq,n)):cases+=1
    print('VERIFY_OK', cases, 'direct bracket component comparisons')

if __name__=='__main__':main()
