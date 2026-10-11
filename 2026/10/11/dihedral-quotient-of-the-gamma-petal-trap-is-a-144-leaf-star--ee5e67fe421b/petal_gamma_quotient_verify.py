from collections import deque, Counter

GAMMA=(0,2,4,7,3,8,6,1,5)
CAP=11

def cyc_canon(p):
    p=tuple(p); n=len(p)
    return min(p[i:]+p[:i] for i in range(n))

def R(p):
    n=len(p)
    return cyc_canon(tuple((x+1)%n for x in p))

def S(p):
    n=len(p)
    return cyc_canon(tuple(n-1-x for x in reversed(p)))

def dihedral_orbit(p):
    p=cyc_canon(p); n=len(p)
    out=set(); q=p
    for _ in range(n):
        out.add(cyc_canon(q)); out.add(S(q)); q=R(q)
    return out

def tminus(p):
    p=tuple(p); n=len(p); out=set()
    for i in range(n):
        a,b=p[i],p[(i+1)%n]
        if abs(a-b)!=1: continue
        m=min(a,b)
        q=[]
        skip={i,(i+1)%n}
        for k,x in enumerate(p):
            if k in skip: continue
            q.append(x-2 if x>m+1 else x)
        out.add(cyc_canon(tuple(q)))
    return out

def tplus(p):
    p=tuple(p); n=len(p); out=set()
    if n+2>CAP: return out
    for j in range(n):
        for m in range(n+1):
            lifted=tuple(x if x<m else x+2 for x in p)
            for ab in ((m,m+1),(m+1,m)):
                q=lifted[:j+1]+ab+lifted[j+1:]
                out.add(cyc_canon(q))
    return out

def xmoves(p):
    p=tuple(p); N=len(p); out=set(); n=(N-1)//2
    for b in range(N):
        pairs=[]
        for k in range(n):
            i=(b+1+2*k)%N; j=(b+2+2*k)%N
            pairs.append((i,j,{p[i],p[j]}))
        for m in range(N-2):
            for w in range(m+2,N-1):
                A={m,w+1}; B={m+1,w}
                ia=[r for r,e in enumerate(pairs) if e[2]==A]
                ib=[r for r,e in enumerate(pairs) if e[2]==B]
                if not ia or not ib or ia[0]==ib[0]: continue
                lo,hi=m+2,w-1
                ok=True
                for r,(_,_,e) in enumerate(pairs):
                    if r in (ia[0],ib[0]): continue
                    inside=all(lo<=x<=hi for x in e) if lo<=hi else False
                    disjoint=all(not (lo<=x<=hi) for x in e) if lo<=hi else True
                    if not (inside or disjoint): ok=False; break
                if ok:
                    trans={m:m+1,m+1:m,w:w+1,w+1:w}
                    q=tuple(trans.get(x,x) for x in p)
                    out.add(cyc_canon(q))
    return out

def neighbors(p):
    out=[]
    for q in tplus(p): out.append((q,'T+'))
    for q in tminus(p): out.append((q,'T-'))
    for q in xmoves(p): out.append((q,'X'))
    out.append((R(p),'R')); out.append((S(p),'S'))
    return out

start=cyc_canon(GAMMA)
seen={start}; Q=deque([start]); edges=[]
while Q:
    p=Q.popleft()
    for q,typ in neighbors(p):
        if len(q)>CAP: continue
        edges.append((p,q,typ))
        if q not in seen:
            seen.add(q); Q.append(q)

counts=Counter(map(len,seen))
assert len(seen)==3186, len(seen)
assert counts==Counter({11:3168,9:18}), counts

# Partition each petal layer by its natural <R,S> dihedral action.
rep={}; orbit_sizes={}
for p in seen:
    if p in rep: continue
    orb=dihedral_orbit(p) & seen
    r=min(orb)
    for q in orb: rep[q]=r
    orbit_sizes[r]=len(orb)
assert len(rep)==len(seen)
assert len(orbit_sizes)==145
sizes_by_n=Counter((len(r),s) for r,s in orbit_sizes.items())
assert sizes_by_n==Counter({(11,22):144,(9,18):1}), sizes_by_n

# Quotient simple graph and move-type labels across distinct orbits.
qedges=set(); labels={}
for p,q,t in edges:
    a,b=rep[p],rep[q]
    if a==b: continue
    e=tuple(sorted((a,b)))
    qedges.add(e); labels.setdefault(e,set()).add(t)
assert len(qedges)==144, len(qedges)
deg=Counter()
for a,b in qedges: deg[a]+=1; deg[b]+=1
assert sorted(deg.values())==[1]*144+[144]
center=[v for v,d in deg.items() if d==144]
assert len(center)==1 and len(center[0])==9
assert all(ts <= {'T+','T-'} for ts in labels.values())
assert all(len(v)==11 for v,d in deg.items() if d==1)

print('VERIFY_OK')
print('states',len(seen),'layer_counts',dict(sorted(counts.items())))
print('dihedral_orbits',len(orbit_sizes),'orbit_profile',dict(sizes_by_n))
print('quotient_edges',len(qedges),'degree_profile',dict(Counter(deg.values())))
print('center',center[0])
print('interorbit_move_types',sorted(set().union(*labels.values())))
