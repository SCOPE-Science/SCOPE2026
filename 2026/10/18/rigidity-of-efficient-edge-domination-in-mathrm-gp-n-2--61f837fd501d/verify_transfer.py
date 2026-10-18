"""Independent finite-state, all-length DIM classification.

State: four consecutive triples (outer-edge,spoke,inner-edge) each in {0,1}^3.
An arrow appends a fifth triple iff the middle index's three closed-edge
neighborhoods each contain exactly one selected edge. Cyclic paths of length n
correspond bijectively to DIMs of GP(n,2), n>=5. No external dependencies.
"""
import itertools,json
triples=list(itertools.product((0,1),repeat=3))
arrows={}
for seq in itertools.product(triples,repeat=4):
    a,b,c,d=seq
    for e in triples:
        o0,s0,i0=a; o1,s1,i1=b; o2,s2,i2=c; o3,s3,i3=d; o4,s4,i4=e
        if o1+o2+o3+s2+s3!=1:continue
        if o1+o2+s2+i0+i2!=1:continue
        if i0+i2+i4+s2+s4!=1:continue
        arrows.setdefault(seq,[]).append(seq[1:]+(e,))
V=set(arrows)
for nbrs in arrows.values():V.update(nbrs)
assert len(V)==346
assert sum(map(len,arrows.values()))==576
# Tarjan's algorithm; prove the only directed cyclic SCC is one 5-cycle.
index=0;ids={};low={};stack=[];on=set();scc=[]
def dfs(v):
    global index
    ids[v]=index;low[v]=index;index+=1;stack.append(v);on.add(v)
    for w in arrows.get(v,[]):
        if w not in ids:
            dfs(w);low[v]=min(low[v],low[w])
        elif w in on:
            low[v]=min(low[v],ids[w])
    if low[v]==ids[v]:
        group=[]
        while True:
            w=stack.pop();on.remove(w);group.append(w)
            if w==v:break
        scc.append(group)
for v in sorted(V):
    if v not in ids:dfs(v)
cyclic=[comp for comp in scc if len(comp)>1 or any(w in arrows.get(w,()) for w in comp)]
assert len(cyclic)==1
H=set(cyclic[0]); assert len(H)==5
assert all(sum(w in H for w in arrows.get(v,[]))==1 for v in H)
assert sum(sum(w in H for w in arrows.get(v,[])) for v in H)==5
# Also check independent predicted 5-periodic selector triple word.
period=[(0,0,1),(0,1,0),(0,0,0),(1,0,0),(0,0,0)]
expected_states={tuple(period[(i+j)%5] for j in range(4)) for i in range(5)}
assert H==expected_states,(H,expected_states)
print(json.dumps({'status':'PASS','triple_alphabet_size':8,'state_memory':4,'active_states':len(V),'transition_edges':sum(map(len,arrows.values())),'strongly_connected_components':len(scc),'cyclic_scc_count':len(cyclic),'cyclic_scc_sizes':[len(x) for x in cyclic],'cyclic_internal_edges':5,'all_periodic_solutions':'five shifts of the unique period-five word, if 5 divides n; none otherwise'},sort_keys=True,separators=(',',':')))
