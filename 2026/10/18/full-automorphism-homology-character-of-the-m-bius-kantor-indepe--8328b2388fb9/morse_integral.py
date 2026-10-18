"""Self-contained integer discrete-Morse certificate for Ind(GP(8,3))."""
from functools import lru_cache
from collections import Counter, deque
ORDER=(12,9,2,3,0,11,6,13,5,15,14,10,8,4,1,7)
N=8; V=16
E={tuple(sorted(e)) for e in ({(i,(i+1)%N) for i in range(N)}|{(i,8+i) for i in range(N)}|{(8+i,8+(i+3)%N) for i in range(N)})}
neighbors=[0]*V
for a,b in E:neighbors[a]|=1<<b;neighbors[b]|=1<<a
FACES={m for m in range(1,1<<V) if all(not(m>>i&1 and m&neighbors[i]) for i in range(V))}
assert len(FACES)==1090
unmatched=FACES|{0};pairs=[]
for v in ORDER:
    bit=1<<v
    for s in sorted(unmatched):
        if not s&bit and s|bit in unmatched and s in unmatched:
            unmatched.remove(s);unmatched.remove(s|bit);pairs.append((s,s|bit))
assert 0 not in unmatched
pairs=[(l,u) for l,u in pairs if l!=0]
# The unmatched singleton formerly paired with the augmented empty face is the ordinary critical vertex.
# Recover that singleton by checking which nonempty face is neither critical nor present in a retained pair.
paired={f for a,b in pairs for f in (a,b)}
critical=FACES-paired
assert Counter(m.bit_count()-1 for m in critical)==Counter({0:1,3:4,4:1})
assert len(pairs)==542
# Explicit acyclicity of the directed Hasse graph: unmatched face covers high->low, matched low->high.
upper={a:b for a,b in pairs}; lower={b:a for a,b in pairs}
arrows={f:[] for f in FACES}; indeg={f:0 for f in FACES};covers=0
for tau in FACES:
    bits=[1<<i for i in range(V) if tau>>i&1]
    if len(bits)<=1:continue
    for b in bits:
        sigma=tau^b;covers+=1
        a,z=(sigma,tau) if upper.get(sigma)==tau else (tau,sigma)
        arrows[a].append(z);indeg[z]+=1
assert covers==4272
queue=deque(f for f in FACES if indeg[f]==0);seen=0
while queue:
    s=queue.popleft();seen+=1
    for t in arrows[s]:
        indeg[t]-=1
        if indeg[t]==0:queue.append(t)
assert seen==len(FACES)

def boundary(s):
    assert s.bit_count()>=2
    result=[];k=0
    for i in range(V):
        if s>>i&1:
            result.append((s^(1<<i),1 if k%2==0 else -1));k+=1
    return result
@lru_cache(None)
def project(s):
    if s in lower:return {}    # upper cell in an eliminated pair
    if s in critical:return {s:1}
    u=upper[s]
    bd=boundary(u)
    coeff=next(a for t,a in bd if t==s)
    ans={}
    for t,a in bd:
        if t==s:continue
        for k,v in project(t).items():ans[k]=ans.get(k,0)-a*coeff*v
    return {k:v for k,v in ans.items() if v}
crit4=[s for s in critical if s.bit_count()==5]
assert len(crit4)==1
morse={}
for f,s in boundary(crit4[0]):
    for k,v in project(f).items():morse[k]=morse.get(k,0)+s*v
assert all(v==0 for v in morse.values()),morse
print('MORSE_OK: 1090 faces; 542 matched pairs; six critical cells (1,4,1); 4272 covers; directed acyclic')
print('MORSE_OK: exact integral degree-four Morse attaching vector is zero')
