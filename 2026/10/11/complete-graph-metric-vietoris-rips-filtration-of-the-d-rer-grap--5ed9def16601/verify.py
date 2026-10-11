#!/usr/bin/env python3
from collections import Counter, deque

N=6
V=list(range(2*N))
ADJ={v:set() for v in V}
def add(a,b):
    ADJ[a].add(b); ADJ[b].add(a)
for i in range(N):
    add(i,(i+1)%N)
    add(i,N+i)
    add(N+i,N+((i+2)%N))
assert sum(map(len,ADJ.values()))//2==18

DIST=[]
for s in V:
    d=[None]*(2*N); d[s]=0; q=deque([s])
    while q:
        x=q.popleft()
        for y in ADJ[x]:
            if d[y] is None:
                d[y]=d[x]+1; q.append(y)
    assert all(z is not None for z in d)
    DIST.append(d)
assert max(max(row) for row in DIST)==4

def faces_at(r):
    faces=set()
    for mask in range(1,1<<(2*N)):
        vs=[i for i in V if mask>>i & 1]
        ok=True
        for a in range(len(vs)):
            for b in range(a+1,len(vs)):
                if DIST[vs[a]][vs[b]]>r:
                    ok=False; break
            if not ok: break
        if ok: faces.add(mask)
    return faces

def popcount(x): return x.bit_count()

def staged_matching(faces):
    rem=set(faces); pairs=[]
    for v in V:
        bit=1<<v
        lows=[]
        for f in sorted(rem):
            if f & bit: continue
            g=f|bit
            if g in rem: lows.append((f,g))
        for f,g in lows:
            assert f in rem and g in rem and g==f|bit and popcount(g)==popcount(f)+1
            rem.remove(f); rem.remove(g); pairs.append((f,g))
    return pairs,rem

def hasse_and_acyclic(faces,pairs):
    pairset=set(pairs)
    matched={}
    for a,b in pairs:
        assert a in faces and b in faces and a not in matched and b not in matched
        matched[a]=b; matched[b]=a
    out={f:[] for f in faces}; indeg={f:0 for f in faces}; covers=0
    for upper in faces:
        m=upper
        while m:
            bit=m & -m; lower=upper^bit; m-=bit
            if lower and lower in faces:
                covers += 1
                if (lower,upper) in pairset:
                    a,b=lower,upper
                else:
                    a,b=upper,lower
                out[a].append(b); indeg[b]+=1
    q=deque([f for f,d in indeg.items() if d==0]); seen=0
    while q:
        x=q.popleft(); seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0: q.append(y)
    return covers, seen==len(faces)

def fvec(faces):
    c=Counter(popcount(f)-1 for f in faces)
    return [c[d] for d in range(max(c)+1)]

expected={
    1:([12,18,2],{0:1,1:5}),
    2:([12,48,82,60,18,2],{0:1,2:1}),
    3:([12,63,190,363,456,377,198,60,8],{0:1}),
}
report={}
for r in (1,2,3):
    F=faces_at(r); pairs,crit=staged_matching(F); covers,acyc=hasse_and_acyclic(F,pairs)
    fv=fvec(F); cc=dict(sorted(Counter(popcount(f)-1 for f in crit).items()))
    assert fv==expected[r][0], (r,fv)
    assert cc==expected[r][1], (r,cc)
    assert acyc
    # Euler cross-check from faces equals Euler from critical cells.
    chi=sum(((-1)**d)*n for d,n in enumerate(fv))
    chi_crit=sum(((-1)**d)*n for d,n in cc.items())
    assert chi==chi_crit
    report[r]={"faces":len(F),"f_vector":fv,"hasse_covers":covers,"matched_pairs":len(pairs),"critical_cells":cc,"acyclic":acyc,"euler_characteristic":chi}

# threshold 0 and >=4 checks
assert len(faces_at(0))==12
assert len(faces_at(4))==(1<<(2*N))-1
print('Durer graph G(6,2): 12 vertices, 18 edges, diameter 4')
for r in (1,2,3): print(r,report[r])
print('PASS')
