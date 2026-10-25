from itertools import combinations, product
from collections import Counter

def passive(adj,sel,rootblue):
    r=0
    blue=set(sel)
    if rootblue: blue.add(r)
    while True:
        force=None
        for v in sorted(blue):
            if v==r:continue
            allwhite=[w for w in adj[v] if w not in blue]
            if len(allwhite)==1 and allwhite[0]!=r:
                force=allwhite[0];break
        if force is None:break
        blue.add(force)
    return blue

def kind(adj,sel):
    r=0; nonroot=set(range(1,len(adj))); b=passive(adj,sel,True)
    A=nonroot <= b
    B=False
    if not A:
        white_r=[w for w in adj[r] if w not in b]
        if len(white_r)==1:
            B=(nonroot<=passive(adj, b|set(white_r), True))
    w=passive(adj,sel,False)
    act=any(u!=r and u in w and [v for v in adj[u] if v not in w]==[r] for u in w)
    return ('A' if A else 'B' if B else 'C'),act

def forcing(adj,sel):
    b=set(sel)
    while True:
        actions=[(v,[w for w in adj[v] if w not in b][0]) for v in b if len([w for w in adj[v] if w not in b])==1]
        if not actions:break
        b.update(w for v,w in actions)
    return len(b)==len(adj)

def edges_to_adj(n,edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def join(blocks):
    a=[set()]
    for b in blocks:
        offset=len(a)-1
        for j in range(1,len(b)):a.append(set())
        for i in range(len(b)):
            for j in b[i]:
                i0=0 if i==0 else offset+i
                j0=0 if j==0 else offset+j
                a[i0].add(j0)
    return a

def connected(a):
    reach={0};prev=set()
    while reach!=prev:
        prev=reach;reach=reach|{v for u in reach for v in a[u]}
    return len(reach)==len(a)

def actual_poly(adj):
    n=len(adj);hist=Counter()
    for m in range(1<<n):
        s={i for i in range(n) if (m>>i)&1}
        if forcing(adj,s):hist[len(s)]+=1
    return hist

def predicted_poly(blocks):
    a=[0];pa=[Counter() for _ in blocks];pb=[Counter() for _ in blocks];qa=[Counter() for _ in blocks];qb=[Counter() for _ in blocks]
    for i,b in enumerate(blocks):
        for mask in range(1<<(len(b)-1)):
            s={u+1 for u in range(len(b)-1) if mask>>u&1}
            k,act=kind(b,s)
            if k=='A':pa[i][len(s)]+=1;qa[i][len(s)]+=0 if act else 1
            if k=='B':pb[i][len(s)]+=1;qb[i][len(s)]+=0 if act else 1
    def mult(hist1,hist2):
        z=Counter()
        for k,v in hist1.items():
            for l,w in hist2.items():z[k+l]+=v*w
        return z
    all_arr=Counter();nonact_arr=Counter()
    for flagged in [None]+list(range(len(blocks))):
        fac=Counter({0:1});qac=Counter({0:1})
        for i in range(len(blocks)):
            fac=mult(fac,pb[i] if flagged==i else pa[i]);qac=mult(qac,qb[i] if flagged==i else qa[i])
        all_arr.update(fac);nonact_arr.update(qac)
    z=Counter()
    for k,v in all_arr.items():z[k]+=v;z[k+1]+=v
    for k,v in nonact_arr.items():z[k]-=v
    return +z

if __name__ == "__main__":
    # Exhaustively compare the cut-vertex identity with unrestricted zero forcing.
    b4 = []
    for n in range(2, 5):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            a = edges_to_adj(n, [e for i, e in enumerate(pairs) if (mask >> i) & 1])
            if connected(a):
                b4.append(a)
    assert len(b4) == 43
    pairs = 0
    for a in b4:
        for b in b4:
            assert actual_poly(join([a,b])) == predicted_poly([a,b])
            pairs += 1
    b3 = [a for a in b4 if len(a) <= 3]
    assert len(b3) == 5
    triples = 0
    for aa in product(b3, repeat=3):
        assert actual_poly(join(aa)) == predicted_poly(aa)
        triples += 1
    assert pairs == 1849 and triples == 125
    # Independently check the clique-bouquet consequence (nonuniform blade sizes).
    from math import prod
    example_count = 0
    for nblades in range(2, 5):
        for sizes in product((2,3), repeat=nblades):
            if sum(sizes) > 10: continue
            blocks=[edges_to_adj(m+1, combinations(range(m+1), 2)) for m in sizes]
            hist=actual_poly(join(blocks))
            exponent=sum(m-1 for m in sizes)
            # Coefficients of (1+z)prod(z+m) - prod(m).
            polynomial=Counter({0:1})
            for m in sizes:
                nxt=Counter()
                for deg,coef in polynomial.items():
                    nxt[deg]+=m*coef
                    nxt[deg+1]+=coef
                polynomial=nxt
            out=Counter()
            for deg,coef in polynomial.items():
                out[exponent+deg]+=coef
                out[exponent+deg+1]+=coef
            out[exponent]-=prod(sizes)
            assert hist == +out
            example_count+=1
    print("CUT_VERTEX_SPLIT_VERIFY_OK", "rooted_assemblies", pairs+triples,
          "two_branch", pairs, "three_branch", triples,
          "clique_bouquets", example_count)
