"""Independent 120-state move model for Petersen Kempe 3-colourings.

A state (c,t,A,B,C) has disjoint colour classes:
A: all four two-subsets containing c;
B: the three pairs t-u for u outside {c,t};
C: the triangle on the other three letters.
"""
from collections import Counter, deque
from itertools import combinations, permutations

X = range(5)
colors = tuple(permutations(range(3)))
states = [(c,t,*q) for c in X for t in X if c!=t for q in colors]
assert len(states) == 120
idx={q:i for i,q in enumerate(states)}

def ordered_coloring(st):
    c,t,A,B,C=st
    rem=set(X)-{c,t}
    out={}
    for e in combinations(X,2):
        if c in e: out[e]=A
        elif t in e: out[e]=B
        else: out[e]=C
    assert Counter(out.values())==Counter({A:4,B:3,C:3})
    return out

map_color={tuple(sorted(ordered_coloring(st).items())): st for st in states}
assert len(map_color)==120

# The proven Kempe component types yield six moves, by exchanging
# A-C globally, B-C on one of three isolated 2-vertex components,
# and A-B on either its isolated vertex or its other 6-cycle.
def moves(st):
    c,t,A,B,C=st
    return {(c,t,C,B,A),
            *((c,u,A,C,B) for u in X if u not in (c,t)),
            (t,c,A,B,C), (t,c,B,A,C)}

G=[]
for st in states:
    ids={idx[u] for u in moves(st)}
    assert len(ids)==6
    G.append(ids)
assert all(i in G[j] for i in range(120) for j in G[i])
assert sum(map(len,G))//2==360

# Directly recheck, in an independent representation, that EACH move is
# a switch on one maximal 2-colour component, and vice versa.
def direct_moves(st):
    col=ordered_coloring(st)
    pairs=list(col)
    adj={e:{f for f in pairs if e!=f and not (set(e)&set(f))} for e in pairs}
    produced=set()
    for a,b in combinations(range(3),2):
        unseen={e for e in pairs if col[e] in (a,b)}
        while unseen:
            root=unseen.pop()
            todo=[root]
            for e in todo:
                for f in adj[e]:
                    if f in unseen:
                        unseen.remove(f)
                        todo.append(f)
            new=col.copy()
            for e in todo:
                new[e]=b if col[e]==a else a
            produced.add(map_color[tuple(sorted(new.items()))])
    return produced
assert all(moves(st)==direct_moves(st) for st in states)

# Structural 20-state quotient indexed by ordered pairs of distinct labels.
P=[(c,t) for c in X for t in X if c!=t]
Q={p:{q for q in P if ((q[0]==p[0] and q[1]!=p[1]) or q==p[::-1])}
   for p in P}
assert len(P)==20 and all(len(n)==4 for n in Q.values())
assert sum(map(len,Q.values()))//2==40
for c in X:
    clique=[(c,t) for t in X if t!=c]
    assert all(v in Q[u] for u,v in combinations(clique,2))
assert all(Q[(c,t)] - {(c,u) for u in X if u not in(c,t)} == {(t,c)}
           for c,t in P)
assert all({(s[0],s[1]) for s in moves(st)}-{(st[0],st[1])} == Q[(st[0],st[1])]
           for st in states)
for p in P:
    dd={p:0}; qq=deque([p])
    while qq:
        u=qq.popleft()
        for v in Q[u]:
            if v not in dd:
                dd[v]=dd[u]+1; qq.append(v)
    assert tuple(Counter(dd.values())[k] for k in range(4)) == (1,4,6,9)

# Exact breadth-first distance census and seven structural categories.
base=(0,1,0,1,2)
d={idx[base]:0}; queue=deque([idx[base]])
while queue:
    u=queue.popleft()
    for v in G[u]:
        if v not in d:
            d[v]=d[u]+1;queue.append(v)
assert len(d)==120
hist=Counter(d.values())
assert tuple(hist[k] for k in range(5))==(1,6,25,61,27)

cats={name:Counter() for name in ['01','0u','10','1u','u0','u1','uv']}
for st in states:
    c,t,*_=st
    typ=('01' if (c,t)==(0,1) else '10' if (c,t)==(1,0)
         else '0u' if c==0 else '1u' if c==1 else 'u0' if t==0
         else 'u1' if t==1 else 'uv')
    cats[typ][d[idx[st]]]+=1
expected={
'01':(1,1,1,3,0),'0u':(0,3,9,6,0),'10':(0,2,3,1,0),
'1u':(0,0,6,12,0),'u0':(0,0,6,12,0),
'u1':(0,0,0,15,3),'uv':(0,0,0,12,24)}
for name in expected:
    assert tuple(cats[name][i] for i in range(5))==expected[name]
# The S_5 x S_3 relabelling action is transitive, giving the same shell
# at all states. Independently check one BFS per vertex for transparency.
for root in range(120):
    distances={root:0}; queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in G[u]:
            if v not in distances:
                distances[v]=distances[u]+1;queue.append(v)
    assert Counter(distances.values())==hist
print('EXPLICIT_STATE_MODEL_PASS')
print('states=120 oriented_pairs=20 quotient_edges=40 each_state_six_moves=TRUE')
print('base_shells=(1,6,25,61,27) radius=4 diameter=4')
print('seven_category_table=',expected)
