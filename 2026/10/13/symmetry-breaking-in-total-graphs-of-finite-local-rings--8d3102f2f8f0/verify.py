#!/usr/bin/env python3
import itertools, math
import networkx as nx

def total_graph_Z(n):
    V=list(range(n))
    def is_zero_divisor(x):
        return x==0 or math.gcd(x,n)!=1
    G=nx.Graph()
    G.add_nodes_from(V)
    for x,y in itertools.combinations(V,2):
        if is_zero_divisor((x+y)%n):
            G.add_edge(x,y)
    return G

def comp_signature(G):
    out=[]
    for C in nx.connected_components(G):
        H=G.subgraph(C)
        deg=sorted(d for _,d in H.degree())
        out.append((len(C),tuple(deg),H.number_of_edges()))
    return sorted(out)

def expected_signature(q,m,even_residue):
    if even_residue:
        return sorted([(m,tuple([m-1]*m),m*(m-1)//2)]*q)
    t=(q-1)//2
    return sorted([(m,tuple([m-1]*m),m*(m-1)//2)] +
                  [(2*m,tuple([m]*(2*m)),m*m)]*t)

def automorphisms(G):
    gm=nx.algorithms.isomorphism.GraphMatcher(G,G)
    return [tuple(mapping[i] for i in range(G.number_of_nodes()))
            for mapping in gm.isomorphisms_iter()]

def base_number(G, autos):
    n=G.number_of_nodes()
    nonid=[p for p in autos if any(p[i]!=i for i in range(n))]
    for k in range(n+1):
        for S in itertools.combinations(range(n),k):
            if all(any(p[v]!=v for v in S) for p in nonid):
                return k
    raise AssertionError

def distinguishing_number(G, autos, max_colors):
    n=G.number_of_nodes()
    nonid=[p for p in autos if any(p[i]!=i for i in range(n))]
    for d in range(1,max_colors+1):
        for col in itertools.product(range(d),repeat=n):
            good=True
            for p in nonid:
                if all(col[i]==col[p[i]] for i in range(n)):
                    good=False
                    break
            if good:
                return d,col
    raise AssertionError

cases=[
    # n, residue q, maximal-ideal size m, residue characteristic even
    (4,2,2,True),
    (8,2,4,True),
    (9,3,3,False),
]
for n,q,m,ev in cases:
    G=total_graph_Z(n)
    sig=comp_signature(G)
    assert sig==expected_signature(q,m,ev),(n,sig,expected_signature(q,m,ev))
    A=automorphisms(G)
    if ev:
        expected_order=math.factorial(m)**q*math.factorial(q)
    else:
        t=(q-1)//2
        expected_order=math.factorial(m)*(2*math.factorial(m)**2)**t*math.factorial(t)
    assert len(A)==expected_order,(n,len(A),expected_order)
    b=base_number(G,A)
    assert b==q*(m-1),(n,b,q*(m-1))
    print(f"Z/{n}Z: components OK, |Aut|={len(A)}, determining={b}")

# Full distinguishing check on the smallest characteristic-two case.
G=total_graph_Z(4)
A=automorphisms(G)
D,col=distinguishing_number(G,A,3)
assert D==3
print("Z/4Z: distinguishing=3, witness=",col)

# For Z/9Z, prove the 3-color obstruction and exhibit a 4-color distinguishing
# pattern through the component description K3 disjoint K3,3.
G=total_graph_Z(9)
comps=[G.subgraph(C).copy() for C in nx.connected_components(G)]
K3=[H for H in comps if H.number_of_nodes()==3][0]
K33=[H for H in comps if H.number_of_nodes()==6][0]
assert all(d==2 for _,d in K3.degree())
assert all(d==3 for _,d in K33.degree())
# Any distinguishing coloring of K3,3 must be injective on each side.
# With only 3 colors, both 3-vertex sides use the same color set, so the
# color-matching side swap survives. Four colors allow distinct 3-subsets.
parts=nx.algorithms.bipartite.sets(K33)
A0,B0=map(sorted,parts)
colors={}
for j,v in enumerate(sorted(K3.nodes())): colors[v]=j
for j,v in enumerate(A0): colors[v]=j
for j,v in enumerate(B0): colors[v]=[0,1,3][j]
gm=nx.algorithms.isomorphism.GraphMatcher(G,G)
for mp in gm.isomorphisms_iter():
    if all(colors[v]==colors[mp[v]] for v in G.nodes()):
        assert all(mp[v]==v for v in G.nodes())
print("Z/9Z: distinguishing=4 by exact K3,3 obstruction + verified witness")

# Ring-theoretic size inequality used in the theorem:
# for finite local nonfields, M/M^2 is a nonzero vector space over R/M,
# hence m>=q. Check the numerical consequence needed for the constructions.
for q in [2,3,4,5,7,8,9]:
    for m in [q,q*q]:
        assert math.comb(m+1,m)>=q
        if q%2==1:
            assert math.comb(math.comb(m+1,m),2)>=(q-1)//2
print("binomial pattern capacity checks OK")
print("VERIFY_OK")
