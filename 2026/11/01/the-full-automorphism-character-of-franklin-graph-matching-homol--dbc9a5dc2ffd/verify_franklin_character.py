#!/usr/bin/env python3
"""Exact, standard-library verification of a finite symmetry-homology calculation.

The graph is specified by the Franklin LCF list [5,-5] repeated six times.
All simplices, automorphisms, fixed-cell traces and Morse incidences are
constructed rather than read from a recorded numerical table.
"""
from collections import Counter, deque
from itertools import combinations
from math import factorial
import json

N = 12
adj = [set() for _ in range(N)]
def edge(u, v):
    assert u != v
    adj[u].add(v); adj[v].add(u)
for i in range(N):
    edge(i, (i+1)%N)
    edge(i, (i+(5 if i%2==0 else -5))%N)
E = sorted((u,v) for u in range(N) for v in adj[u] if u<v)
assert len(E) == 18 and all(len(a)==3 for a in adj)
eindex = {e:i for i,e in enumerate(E)}

# Complete adjacency- and nonadjacency-preserving permutation backtracking.
# At each step all candidate images are tried, in a connected BFS ordering.
order=[0]
while len(order)<N:
    choices=[i for i in range(N) if i not in order]
    order.append(min(choices,key=lambda i:(-len(adj[i].intersection(order)), i)))
perms=[]
def search(mapping, used):
    if len(mapping)==N:
        p=tuple(mapping[i] for i in range(N))
        perms.append(p);return
    u=order[len(mapping)]
    for v in range(N):
        if v in used:continue
        if all((w in adj[u])==(mapping[w] in adj[v]) for w in mapping):
            mapping[u]=v;used.add(v)
            search(mapping,used)
            used.remove(v);del mapping[u]
search({},set())
perms=sorted(set(perms))
assert len(perms)==48
assert tuple(range(N)) in perms
assert all(all((p[v] in adj[p[u]])==(v in adj[u]) for v in range(N) for u in range(N)) for p in perms)

# Every face is a matching of edges, represented by a nonzero 18-bit mask.
faces=[]
for k in range(1,7):
    for ids in combinations(range(len(E)),k):
        verts = [v for i in ids for v in E[i]]
        if len(set(verts)) == 2*k:
            faces.append(sum(1<<i for i in ids))
counts=Counter(m.bit_count() for m in faces)
assert tuple(counts[k] for k in range(1,7))==(18,117,336,417,186,17)
assert len(faces)==1091
face_set=set(faces)

# Deterministic acyclic discrete Morse matching on the full nonempty face poset.
unused=set(faces); matching=[]
for i in range(len(E)):
    for m in sorted(unused):
        co=m|(1<<i)
        if co != m and m in unused and co in unused:
            matching.append((m,co))
            unused.remove(m);unused.remove(co)
assert len(matching)==539
assert Counter(m.bit_count()-1 for m in unused)==Counter({0:1,3:12})
assert len(matching)*2+len(unused)==len(faces)

# Reverse exactly the matched Hasse arrows; all unmatched arrows go downward.
matched=set(matching)
indegree={m:0 for m in faces}
out={m:[] for m in faces}
incidences=0
for top in faces:
    for i in range(len(E)):
        if top&(1<<i):
            bot=top^(1<<i)
            if bot:
                incidences+=1
                a,b=(bot,top) if (bot,top) in matched else (top,bot)
                out[a].append(b);indegree[b]+=1
queue=deque(m for m in faces if indegree[m]==0)
visited=0
while queue:
    m=queue.popleft();visited+=1
    for v in out[m]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==len(faces)
assert incidences==3942

# Recover the induced permutation of the 18 edge-vertices of the complex.
def perm_edges(p):
    return tuple(eindex[tuple(sorted((p[u],p[v])))] for u,v in E)
def parity(seq):
    return (-1)**sum(a>b for k,a in enumerate(seq) for b in seq[k+1:])
def cycles(perm):
    seen=set();out=[]
    for i in range(len(perm)):
        if i not in seen:
            orbit=[];j=i
            while j not in seen:
                orbit.append(j);seen.add(j);j=perm[j]
            out.append(tuple(orbit))
    return out

def simplicial_trace(edgeperm,k):
    ans=0
    for m in faces:
        if m.bit_count()!=k:continue
        aa=[edgeperm[i] for i in range(len(E)) if m&(1<<i)]
        if sum(1<<j for j in aa)==m:ans+=parity(aa)
    return ans

# Independent alternative character formula: a fixed matching is a union
# of admissible edge-permutation cycles. Each chosen cycle contributes -1
# to the reduced fixed-chain Euler polynomial, regardless of its length.
def orbit_polynomial_at_minus_one(edgeperm):
    good=[]
    for orb in cycles(edgeperm):
        vertices=[v for i in orb for v in E[i]]
        if len(set(vertices))==len(vertices):good.append(set(vertices))
    total=0
    for mask in range(1<<len(good)):
        occupied=set();ok=True
        for j,V in enumerate(good):
            if mask&(1<<j):
                if not occupied.isdisjoint(V):ok=False;break
                occupied.update(V)
        if ok:total+=(-1)**mask.bit_count()
    return total

# Four Hamiltonian cycles determine a faithful four-letter quotient action.
ham=(0,1,2,3,10,11,6,7,8,9,4,5)
assert len(set(ham))==N and all(ham[(j+1)%N] in adj[ham[j]] for j in range(N))
def cycle_edges(c):
    return frozenset(tuple(sorted((c[j],c[(j+1)%len(c)]))) for j in range(len(c)))
H0=cycle_edges(ham)
Hset={frozenset(tuple(sorted((p[u],p[v]))) for u,v in H0) for p in perms}
assert len(Hset)==4
H=sorted(Hset,key=lambda z:sorted(z))
Hindex={h:i for i,h in enumerate(H)}

def perm_four(p):
    return tuple(Hindex[frozenset(tuple(sorted((p[u],p[v]))) for u,v in h)] for h in H)
fourmaps=[perm_four(p) for p in perms]
assert len(set(fourmaps))==factorial(4)
z=tuple((i+6)%12 for i in range(N))
assert z in perms and perm_four(z)==tuple(range(4))
assert [p for p in perms if perm_four(p)==tuple(range(4))]==[tuple(range(N)),z]
assert parity(perm_edges(z))==-1

# Full S4 character table by cycle types on the four Hamiltonian cycles.
S4={
 (1,1,1,1):(1,1,3,2,3),
 (1,1,2):(1,-1,1,0,-1),
 (2,2):(1,1,-1,2,-1),
 (1,3):(1,1,0,-1,0),
 (4,):(1,-1,-1,0,1),
}
# Irreps listed: trivial, sign, (3,1), (2,2), (2,1,1).
characters=[]
for p in perms:
    q=perm_edges(p)
    chain=[simplicial_trace(q,k) for k in range(1,7)]
    chi=1-sum((-1)**(k-1)*chain[k-1] for k in range(1,7))
    assert chi==orbit_polynomial_at_minus_one(q)
    eta=parity(q)
    f=perm_four(p)
    typ=tuple(sorted(map(len,cycles(f))))
    assert typ in S4
    triv,sign,standard,two_dim,twisted=S4[typ]
    predicted=eta+standard+standard*eta+two_dim+twisted
    assert chi==predicted
    characters.append({'permutation':list(p),
                       'edge_permutation':list(q),
                       'four_cycle_type':list(typ),
                       'edge_sign':eta,
                       'chain_traces':chain,
                       'h3_trace':chi})
assert Counter(c['h3_trace'] for c in characters)==Counter({0:26,-2:14,2:6,12:1,4:1})
assert sum(c['h3_trace'] for c in characters)==0
assert sum(c['h3_trace'] for c in characters if c['edge_sign']==1)==24
assert sum(c['h3_trace'] for c in characters if c['permutation']==list(z))==4

# Exact irreducible multiplicities from the inner-product formula.
mult={}
labels=['trivial','sign','standard','two_dimensional','standard_sign']
for j,label in enumerate(labels):
    for twist in [0,1]:
        numerator=sum(c['h3_trace']*S4[tuple(c['four_cycle_type'])][j]*
                      (c['edge_sign'] if twist else 1) for c in characters)
        assert numerator%48==0 and numerator>=0
        mult[label+('_edge_sign' if twist else '')]=numerator//48
assert mult=={
 'trivial':0,'trivial_edge_sign':1,
 'sign':0,'sign_edge_sign':0,
 'standard':1,'standard_edge_sign':1,
 'two_dimensional':1,'two_dimensional_edge_sign':0,
 'standard_sign':1,'standard_sign_edge_sign':0,
}

# Full conjugacy-class partition determined, not guessed from cycle types.
p_index={p:i for i,p in enumerate(perms)}
def mul(a,b):return tuple(a[b[i]] for i in range(N))
def inverse(a):return tuple(a.index(i) for i in range(N))
conjugacy=[];seen=set()
for i,p in enumerate(perms):
    if i in seen:continue
    cl={p_index[mul(mul(t,p),inverse(t))] for t in perms}
    assert seen.isdisjoint(cl)
    seen|=cl
    c=characters[i]
    assert all(characters[j]['h3_trace']==c['h3_trace'] and
               characters[j]['edge_sign']==c['edge_sign'] and
               characters[j]['four_cycle_type']==c['four_cycle_type'] for j in cl)
    conjugacy.append({'size':len(cl),'element_order':__import__('math').lcm(*(len(q) for q in cycles(p))),
                      'four_cycle_type':c['four_cycle_type'], 'edge_sign':c['edge_sign'],
                      'h3_trace':c['h3_trace'],'chain_traces':c['chain_traces'],
                      'representative_vertex_permutation':list(p)})
assert len(seen)==48 and len(conjugacy)==10
conjugacy.sort(key=lambda x:(tuple(x['four_cycle_type']),-x['edge_sign']))

certificate={
 'graph':'Franklin graph LCF [5,-5] repeated six times',
 'graph_edges':[list(e) for e in E],
 'face_counts_by_cardinality':[counts[k] for k in range(1,7)],
 'total_nonempty_faces':len(faces),
 'morse_matched_pairs':len(matching),
 'morse_critical_cell_counts_by_dimension':{'0':1,'3':12},
 'morse_oriented_incidences':incidences,
 'morse_dag_processed_faces':visited,
 'automorphism_count':len(perms),
 'four_hamiltonian_cycles_edge_sets':[[list(e) for e in sorted(h)] for h in H],
 'kernel_of_four_letter_action':[list(tuple(range(N))),list(z)],
 'central_half_turn_h3_trace':4,
 'homology_h3_dimension':12,
 'character_trace_histogram':{str(k):v for k,v in sorted(Counter(c['h3_trace'] for c in characters).items())},
 'conjugacy_classes':conjugacy,
 'irreducible_multiplicities':mult,
 'full_group_invariant_h3_dimension':0,
 'edge_sign_kernel_invariant_h3_dimension':1,
 'method':'finite face enumeration; acyclic Morse Hasse DAG; independent signed fixed-simplex and fixed-edge-orbit traces',
}
with open('franklin_character_certificate.json','w',encoding='utf-8') as f:
    json.dump(certificate,f,indent=2,ensure_ascii=False,sort_keys=True)
    f.write('\n')
print('FRANKLIN_CHARACTER_VERIFIED')
print('faces',len(faces),'Morse pairs',len(matching),'automorphisms',len(perms))
print('irreducibles',mult)
print('trace histogram',certificate['character_trace_histogram'])
print('conjugacy classes',len(conjugacy))
