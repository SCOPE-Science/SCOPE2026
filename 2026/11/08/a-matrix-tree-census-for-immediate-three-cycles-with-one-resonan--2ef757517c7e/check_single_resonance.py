"""Independent exact checks of the single-resonance chip-firing census."""
from itertools import combinations,product
import networkx as nx
import sympy as sp

def all_simple_cycles(G):
    cycles=set()
    for c in nx.simple_cycles(nx.DiGraph(G)):
        if len(c)>=3:
            E=frozenset(frozenset((c[i],c[(i+1)%len(c)])) for i in range(len(c)))
            cycles.add(E)
    return cycles

def tree_count_after_contract(G,C):
    cv=set().union(*[set(e) for e in C]); verts=[None]+[v for v in G if v not in cv]
    index={v:i for i,v in enumerate(verts)}
    def norm(v):return None if v in cv else v
    M=sp.zeros(len(verts))
    for a,b in G.edges():
        u,v=norm(a),norm(b)
        if u==v:continue
        i,j=index[u],index[v];M[i,i]+=1;M[j,j]+=1;M[i,j]-=1;M[j,i]-=1
    return int(M[:-1,:-1].det())

def weighted_color_count(G):
    vertices=list(G); nb=[[vertices.index(u) for u in G.neighbors(v)] for v in vertices]
    total=0
    for cs in product(range(3),repeat=len(vertices)):
        prod=1
        for i,nbrs in enumerate(nb):
            prod*=sum(cs[j]==(cs[i]-1)%3 for j in nbrs)
            if not prod:break
        total+=prod
    return 2*total

checked=0;no_res=0;maxN=0; examples=[]
for n in range(3,7):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from(pairs[i] for i in range(len(pairs)) if mask>>i&1)
        if not nx.is_connected(G):continue
        cyc=[C for C in all_simple_cycles(G) if len(C)%3==0]
        if len(cyc)==1:
            C=cyc[0]
            expect=12*tree_count_after_contract(G,C)
            observed=weighted_color_count(G)
            assert observed==expect,(list(G.edges()),observed,expect)
            checked+=1;maxN=max(maxN,n)
            if len(examples)<5 and (expect>12 or n>=5):examples.append((n,G.number_of_edges(),expect))
        elif len(cyc)==0:
            assert weighted_color_count(G)==0,(list(G.edges()),'unexpected three-cycle')
            no_res+=1
print('EXACT graph enumeration PASS, n=3..6')
print('one resonant cycle graphs:',checked,'; no resonant cycle graphs:',no_res)
print('examples (vertices,edges,period-three states):',examples)
print('All totals count both firing densities 1/3 and 2/3.')
