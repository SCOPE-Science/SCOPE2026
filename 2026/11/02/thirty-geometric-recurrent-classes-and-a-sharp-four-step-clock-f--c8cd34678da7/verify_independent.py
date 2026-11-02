"""Independent majority-dynamics census by functional-digraph indegree pruning.
Python >=3.10; no external libraries. The graph is Q_4 with vertices labelled 0,...,15.
"""
from collections import deque,Counter
from itertools import permutations
V=16
N=1<<V
neighborhood=[sum(1<<(v^(1<<i)) for i in range(4)) for v in range(V)]

def update(s):
    t=0
    for v,m in enumerate(neighborhood):
        k=(s&m).bit_count()
        if k>2 or (k==2 and (s>>v)&1): t|=1<<v
    return t

edges=[update(s) for s in range(N)]
in_degree=[0]*N
for z in edges: in_degree[z]+=1
q=deque(s for s,v in enumerate(in_degree) if not v)
order=[]
while q:
    s=q.popleft();order.append(s)
    w=edges[s];in_degree[w]-=1
    if in_degree[w]==0:q.append(w)
# Every unpeeled state is on a directed cycle.
recurrent=[s for s in range(N) if in_degree[s]>0]
period=[0]*N
seen=set(); cycle_sizes=Counter()
for x in recurrent:
    if x in seen: continue
    cyc=[];z=x
    while z not in seen:
        seen.add(z);cyc.append(z);z=edges[z]
    assert z==x
    for s in cyc:period[s]=len(cyc)
    cycle_sizes[len(cyc)]+=1
assert set(cycle_sizes)=={1,2}
distance=[0]*N
for s in reversed(order):
    period[s]=period[edges[s]]
    distance[s]=distance[edges[s]]+1
assert all(period)
assert max(distance)==4
assert cycle_sizes=={1:702,2:885}
assert Counter(distance)=={0:2472,1:17336,2:34944,3:8864,4:1920}
assert Counter(period)=={1:46166,2:19370}
assert Counter(distance[s] for s in range(N) if period[s]==2)=={0:1770,1:8000,2:9600}
print('independent graph-pruning verification passed: 65536 states; 702 fixed; 885 two-cycles; max entry 4')
print('entry count by (depth,eventual period):',sorted(Counter((distance[s],period[s]) for s in range(N)).items()))

pairs={min(s,edges[s]):max(s,edges[s]) for s in recurrent if period[s]==2}
assert len(pairs)==885

# The 384 graph automorphisms are all affine coordinate permutations on F_2^4.
autos=[]
for perm in permutations(range(4)):
    for shift in range(16):
        mapping=[shift ^ sum(((v>>i)&1)<<perm[i] for i in range(4)) for v in range(16)]
        autos.append(mapping)
assert len(autos)==384

def image(mask,permutation):
    result=0
    for v in range(16):
        if mask&(1<<v): result|=1<<permutation[v]
    return result

pending=set(pairs)
classes=[]
while pending:
    x=min(pending); y=pairs[x]
    orbit={min(image(x,a),image(y,a)) for a in autos}
    assert orbit<=pending
    classes.append((x,y,len(orbit)))
    pending.difference_update(orbit)
assert len(classes)==16
assert Counter(k for _,_,k in classes)=={192:2,96:2,48:4,24:4,8:2,4:1,1:1}
print('spatial two-cycle classes:',len(classes),'sizes:',sorted(Counter(k for _,_,k in classes).items()))

fixed_states={s for s in recurrent if period[s]==1}
fixed_classes=[]
while fixed_states:
    x=min(fixed_states)
    orbit={image(x,a) for a in autos}
    assert orbit<=fixed_states
    fixed_classes.append((x,len(orbit)))
    fixed_states.difference_update(orbit)
assert len(fixed_classes)==14
assert Counter(k for _,k in fixed_classes)=={1:2,8:1,12:1,24:3,32:1,48:2,96:3,192:1}
print('spatial fixed classes:',len(fixed_classes),'sizes:',sorted(Counter(k for _,k in fixed_classes).items()))

from csv import writer
with open('orbit_classes.csv','w',newline='',encoding='utf-8') as file:
    csv=writer(file)
    csv.writerow(('kind','representative_state','partner_state','spatial_class_size'))
    for x,size in sorted(fixed_classes):
        csv.writerow(('fixed',x,x,size))
        print('FIXED',x,size)
    for x,y,size in sorted(classes,key=lambda z:(-z[2],z[0])):
        csv.writerow(('two_cycle',x,y,size))
        print('TWO_CYCLE',x,y,size)
