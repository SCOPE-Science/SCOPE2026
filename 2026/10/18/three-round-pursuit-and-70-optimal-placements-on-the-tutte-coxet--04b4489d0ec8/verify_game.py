"""Exact capture-time and optimal-start census for the Tutte--Coxeter graph.

Standalone Python 3, standard library only. Players may stay put. Cops move first
and see the robber. A game round consists of a simultaneous cop move followed
by one robber move, unless a cop has already landed on the robber.
"""
from itertools import combinations, combinations_with_replacement, product
from functools import reduce
from collections import Counter, deque
import hashlib


def symplectic(a,b):
    return (((a&1)*((b>>2)&1) + ((a>>2)&1)*(b&1) +
             ((a>>1)&1)*((b>>3)&1) + ((a>>3)&1)*((b>>1)&1)) & 1)

POINTS=range(1,16)
LINES=sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(POINTS,2)
              if symplectic(a,b)==0})
assert len(LINES)==15
ADJ=[set() for _ in range(30)]
for j,line in enumerate(LINES):
    for a in line:
        ADJ[a-1].add(j+15)
        ADJ[j+15].add(a-1)
assert all(len(s)==3 for s in ADJ)
assert sum(map(len,ADJ))//2==45
CLOSED=[s|{v} for v,s in enumerate(ADJ)]
NEIGHBORHOOD=[sum(1<<v for v in s) for s in CLOSED]
ALL=(1<<30)-1

# Additional structural checks of the graph: its distances and girth.
DIST=[]
for start in range(30):
    ds=[-1]*30;ds[start]=0;q=deque([start])
    while q:
        v=q.popleft()
        for w in ADJ[v]:
            if ds[w]==-1:ds[w]=ds[v]+1;q.append(w)
    DIST.append(ds)
assert max(map(max,DIST))==4
assert all(len([d for d in row if d<=2])==10 for row in DIST)
GIRTH=30
for a in range(30):
    for b in ADJ[a]:
        if a<b:
            ds=[-1]*30;ds[a]=0;q=deque([a])
            while q:
                v=q.popleft()
                for w in ADJ[v]:
                    if (v==a and w==b) or (v==b and w==a):continue
                    if ds[w]==-1:ds[w]=ds[v]+1;q.append(w)
            GIRTH=min(GIRTH,ds[b]+1)
assert GIRTH==8


def placements(k):
    ss=list(combinations_with_replacement(range(30),k))
    ix={C:i for i,C in enumerate(ss)}
    nextc=[]
    for C in ss:
        nextc.append(sorted({ix[tuple(sorted(m))] for m in
                             product(*(CLOSED[v] for v in C))}))
    masks=[reduce(lambda m,v:m|(1<<v),C,0) for C in ss]
    return ss, nextc, masks


def solve(k, maxrounds=4):
    states, moves, masks=placements(k)
    win=masks[:]
    counts=[sum(x.bit_count() for x in win)]
    winners=[]
    for t in range(1,maxrounds+1):
        # Every possible robber move must enter the previous-stage winning set.
        forced=[sum((1<<r) for r,nm in enumerate(NEIGHBORHOOD)
                    if nm&(~previous)==0) for previous in win]
        nxt=[]
        for index,opts in enumerate(moves):
            reachable=masks[index]
            for j in opts:
                reachable |= masks[j] | forced[j]
            nxt.append(reachable)
        counts.append(sum(x.bit_count() for x in nxt))
        winners=[states[i] for i,x in enumerate(nxt) if x==ALL]
        if winners:return t,counts,winners,states,moves,masks
        if nxt==win:return None,counts,[],states,moves,masks
        win=nxt
    raise AssertionError('Horizon insufficient')

r1=solve(1)
r2=solve(2)
r3=solve(3)
assert r1[0] is None and r2[0] is None and r3[0]==3
assert r1[1]==[30,120,120]
assert r2[1]==[900,3420,3420]
assert r3[1]==[13950,50520,55080,75360]
WIN=set(r3[2]);assert len(WIN)==70 and all(len(set(C))==3 for C in WIN)

# Even if the robber stays still, cops cannot reach every initial vertex
# within two cop turns: every two radius-two balls overlap in diameter four.
assert all(reduce(lambda m,v:m|(sum(1<<w for w,d in enumerate(DIST[v]) if d<=2)),
                  C,0)!=ALL for C in r3[3])

# A projective F_2 line comprises the nonzero elements a,b,a xor b.
PROJECTIVE={tuple(sorted((a-1,b-1,(a^b)-1)))
            for a,b in combinations(POINTS,2)}
assert len(PROJECTIVE)==35
WIN_POINTS={C for C in WIN if C[2]<15}
assert WIN_POINTS==PROJECTIVE

PENCILS={tuple(sorted(v for v in range(15,30) if a in LINES[v-15]))
         for a in POINTS}
assert len(PENCILS)==15
REGULI=set()
for C in combinations(range(15,30),3):
    sets=[set(LINES[c-15]) for c in C]
    disjoint=all(not sets[i]&sets[j] for i,j in combinations(range(3),2))
    common=sum(all(set(LINES[q-15])&s for s in sets)
               for q in range(15,30) if q not in C)
    if disjoint and common==3:REGULI.add(C)
assert len(REGULI)==20 and not PENCILS&REGULI
WIN_LINES={C for C in WIN if C[0]>=15}
assert WIN_LINES==PENCILS|REGULI
assert all(not (C[0]<15<=C[-1]) for C in WIN)

canonical='\n'.join(','.join(map(str,C)) for C in sorted(WIN))+'\n'
print('vertices=30 edges=45 girth=8 diameter=4')
print('k1_winning_position_counts='+str(r1[1])+' cop_wins=no')
print('k2_winning_position_counts='+str(r2[1])+' cop_wins=no')
print('k3_winning_position_counts='+str(r3[1])+' capture_time=3')
print('three_cop_multiset_positions='+str(len(r3[3]))+' initial_optimal_positions='+str(len(WIN)))
print('point_projective_lines=35 line_pencils=15 line_reguli=20 mixed=0')
print('optimal_position_list_sha256='+hashlib.sha256(canonical.encode()).hexdigest())
print('VERIFY_OK')
