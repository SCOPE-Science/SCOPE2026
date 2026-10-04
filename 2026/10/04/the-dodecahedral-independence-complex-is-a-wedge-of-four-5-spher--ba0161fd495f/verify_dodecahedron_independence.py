#!/usr/bin/env python3
from collections import Counter, deque
N=20
edges=set()
for i in range(10):
    edges.add(tuple(sorted((i,(i+1)%10))))
    edges.add(tuple(sorted((i,10+i))))
    edges.add(tuple(sorted((10+i,10+((i+2)%10)))))
assert len(edges)==30
adj=[0]*N
for a,b in edges:
    adj[a]|=1<<b; adj[b]|=1<<a
faces=[]
for m in range(1<<N):
    ok=True; t=m
    while t:
        b=t & -t; v=b.bit_length()-1
        if adj[v] & m:
            ok=False; break
        t-=b
    if ok: faces.append(m)
assert len(faces)==5828
fv=Counter(m.bit_count() for m in faces)
assert [fv[k] for k in range(1,9)]==[20,160,660,1510,1912,1240,320,5]
nonempty=set(faces); nonempty.remove(0)
unmatched=set(nonempty); pairs=[]
for v in range(N):
    bit=1<<v
    for m in sorted([x for x in unmatched if not (x&bit) and (x|bit) in unmatched]):
        if m in unmatched and (m|bit) in unmatched:
            pairs.append((m,m|bit,v)); unmatched.remove(m); unmatched.remove(m|bit)
assert len(pairs)==2911
crit=sorted(unmatched)
def verts(m): return tuple(i for i in range(N) if (m>>i)&1)
expected=[(0,), (3,8,10,11,15,16), (4,9,11,12,16,17), (2,7,10,14,15,19), (1,6,13,14,18,19)]
assert sorted(map(verts,crit))==sorted(expected)
assert sorted(m.bit_count()-1 for m in crit)==[0,5,5,5,5]
pairset={(lo,hi) for lo,hi,_ in pairs}
assert len(pairset)==len(pairs)
for lo,hi,v in pairs:
    assert lo in nonempty and hi in nonempty
    assert hi==lo|(1<<v) and (lo&(1<<v))==0 and hi.bit_count()==lo.bit_count()+1
# Forman orientation of the nonempty face-poset Hasse graph:
# unmatched cover relations go low->high; matched relations are reversed.
indeg={m:0 for m in nonempty}; out={m:[] for m in nonempty}; edge_count=0
for hi in nonempty:
    t=hi
    while t:
        b=t & -t; lo=hi^b; t-=b
        if lo==0: continue
        a,c=(hi,lo) if (lo,hi) in pairset else (lo,hi)
        out[a].append(c); indeg[c]+=1; edge_count+=1
q=deque([m for m,d in indeg.items() if d==0]); seen=0
while q:
    x=q.popleft(); seen+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(nonempty), 'matching orientation has a directed cycle'
assert edge_count==27620
chi=sum(((-1)**(k-1))*fv[k] for k in range(1,9))
assert chi==-3
print('faces=5828')
print('f_vector=20,160,660,1510,1912,1240,320,5')
print('matched_pairs=2911')
print('critical_cells=1x0-cell+4x5-cells')
print('hasse_edges=27620')
print('euler_characteristic=-3')
print('ACYCLIC_MATCHING_OK')
print('VERIFY_OK')
