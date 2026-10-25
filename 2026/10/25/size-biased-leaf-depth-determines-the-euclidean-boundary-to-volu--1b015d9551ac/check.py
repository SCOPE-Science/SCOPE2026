"""Independent finite checks for Euclidean order-polytope boundary ratios.

Requires only the Python standard library. This program enumerates all rooted
labeled trees of orders 3..7 via Prufer words, then checks the exact hook-ratio
formula against independently enumerated linear extensions on sample trees.
"""
from fractions import Fraction
from itertools import product
from math import sqrt
from collections import defaultdict


def tree_from_prufer(n,code):
    degree=[1]*n
    for t in code: degree[t]+=1
    edges=[]
    for t in code:
        leaf=min(i for i in range(n) if degree[i]==1)
        edges.append((leaf,t));degree[leaf]-=1;degree[t]-=1
    u,v=[i for i in range(n) if degree[i]==1]
    edges.append((u,v))
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    parent=[-2]*n; parent[0]=-1; stack=[0]
    for u in stack:
        for v in adj[u]:
            if v!=parent[u]: parent[v]=u;stack.append(v)
    return parent


def subtree(parent):
    n=len(parent);s=[1]*n
    for v in reversed(range(1,n)):
        # parent labels not necessarily topological, must use depth
        pass
    kids=[[] for _ in parent]
    for v in range(1,len(parent)):kids[parent[v]].append(v)
    def visit(v):
        s[v]=1+sum(visit(w) for w in kids[v]); return s[v]
    visit(0)
    return s,kids


def formula(parent):
    n=len(parent);s,kids=subtree(parent)
    total=Fraction(0)
    for v in range(1,n):
        u=parent[v];factor=Fraction(s[v],n)
        while u>=0:
            factor*=Fraction(s[u],s[u]-1);u=parent[u]
        total+=factor
    return total


def spine_formula(parent):
    """Independent recursive calculation of expected leaf depth.

    Each interior vertex chooses descendant child with probability
    proportional to the child's subtree size.
    """
    sizes,children=subtree(parent)
    def walk(u):
        if not children[u]: return Fraction(0)
        return 1+sum(Fraction(sizes[v],sizes[u]-1)*walk(v) for v in children[u])
    return walk(0)


def facet_ratio_from_extensions(parent):
    """Independent linear-extension enumeration of facet-to-volume ratios.

    The lower coordinate facet fixes the root to zero. Upper coordinate
    facets sum over choices of the last vertex; diagonal facets contract
    a cover pair in a linear extension.
    """
    n=len(parent)
    cnt=0; lower=0; upper=0; adjacency=0
    def go(mask,seq):
        nonlocal cnt,lower,upper,adjacency
        if mask==(1<<n)-1:
            cnt+=1
            lower+=int(seq[0]==0)
            upper+=int(not any(parent[j]==seq[-1] for j in range(n)))
            adjacency+=sum(parent[seq[i+1]]==seq[i] for i in range(n-1))
            return
        for j in range(n):
            if not(mask&(1<<j)) and (parent[j]<0 or mask&(1<<parent[j])):
                go(mask|(1<<j),seq+(j,))
    go(0,())
    assert lower==upper==cnt
    return Fraction(lower+upper,cnt),Fraction(adjacency,cnt)


def enumeration(parent):
    n=len(parent); acc=[0,0]; a=[0]*n
    def go(mask,seq):
        if mask==(1<<n)-1:
            acc[0]+=1
            acc[1]+=sum(parent[seq[i+1]]==seq[i] for i in range(n-1))
            return
        for j in range(n):
            if not(mask&(1<<j)) and (parent[j]<0 or mask&(1<<parent[j])):
                go(mask|(1<<j),seq+(j,))
    go(0,())
    return Fraction(acc[1],acc[0])


def classification(parent):
    n=len(parent);s,kids=subtree(parent)
    star=sum(1 for v in range(1,n) if parent[v]==0)==n-1
    chain=all(len(k)<=1 for k in kids)
    minimal_nonstar=(sum(len(k) for k in kids[1:])==1)
    terminal_cherry=(sum(len(k)>1 for k in kids)==1 and
                     next((len(k) for k in kids if len(k)>1),None)==2 and
                     all(not kids[v] for v in range(n) if v in
                         next((kids[w] for w in range(n) if len(kids[w])==2),[])))
    return star,chain,minimal_nonstar,terminal_cherry


def main():
    total=0
    for n in range(3,8):
        per=0
        for ix,word in enumerate(product(range(n),repeat=n-2)):
            par=tree_from_prufer(n,word)
            a=formula(par)
            b=spine_formula(par)
            assert a==b,(n,word,a,b,'spine')
            star,chain,minimal,terminal=classification(par)
            assert Fraction(1)<=a<=n-1,(n,word,a)
            assert (a==1)==star,(n,word,a,'star')
            assert (a==n-1)==chain,(n,word,a,'chain')
            if not star:
                assert a>=Fraction(n+1,n-1),(n,word,a,'second min')
                assert (a==Fraction(n+1,n-1))==minimal,(n,word,a,'second min equality')
            if not chain:
                assert a<=n-2,(n,word,a,'second max')
                assert (a==n-2)==terminal,(n,word,a,'second max equality')
            if n<=5 or (ix%137)==0:
                assert a==enumeration(par),(n,word,a,'extension')
                coordinate,cover=facet_ratio_from_extensions(par)
                assert coordinate==2 and cover==a,(n,word,'facet')
            per+=1;total+=1
        print(f'n={n}: verified {per} rooted labeled trees')
    print('TOTAL',total,'VERIFY_OK')

if __name__=='__main__':main()
