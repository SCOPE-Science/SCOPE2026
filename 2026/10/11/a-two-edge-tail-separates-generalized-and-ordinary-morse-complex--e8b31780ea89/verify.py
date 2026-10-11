from itertools import combinations
from collections import defaultdict, deque
V=range(6)
E=[(0,1),(1,2),(2,3),(0,3),(0,4),(4,5)]
P=[(v,i) for i,e in enumerate(E) for v in e]
# encode primitives 0..11
# a face chooses incidences with unique vertex and unique edge

def gm_ok(face):
    vs=[P[i][0] for i in face]; es=[P[i][1] for i in face]
    return len(vs)==len(set(vs)) and len(es)==len(set(es))

def m_ok(face):
    if not gm_ok(face): return False
    arcs=[]
    for i in face:
        v,eidx=P[i]; a,b=E[eidx]; w=b if v==a else a
        arcs.append((v,w))
    out={u:w for u,w in arcs}
    # each vertex outdegree <=1; cycle iff iterate returns start
    for s in out:
        seen=set(); x=s
        while x in out:
            if x in seen: return False
            seen.add(x); x=out[x]
    return True

def faces(ok):
    F=[]
    for mask in range(1,1<<len(P)):
        f=tuple(i for i in range(len(P)) if mask>>i&1)
        if ok(f): F.append(f)
    return set(F)

def elem_matching(F, order):
    unmatched=set(F)
    pairs=[]
    for x in order:
        # pair lower faces first deterministic by size/tuple
        lowers=sorted((f for f in unmatched if x not in f), key=lambda z:(len(z),z))
        for f in lowers:
            if f not in unmatched: continue
            g=tuple(sorted(f+(x,)))
            if g in unmatched:
                unmatched.remove(f); unmatched.remove(g); pairs.append((f,g))
    return pairs, unmatched

def hasse(F):
    covers=[]
    for g in F:
        if len(g)>=2:
            for x in g:
                f=tuple(y for y in g if y!=x)
                if f in F: covers.append((f,g))
    return covers

def acyclic_matching(F,pairs):
    pairset=set(pairs)
    verts=list(F); idx={f:i for i,f in enumerate(verts)}
    adj=[[] for _ in verts]; indeg=[0]*len(verts)
    for f,g in hasse(F):
        # Forman orientation: unmatched cover downward g->f; matched upward f->g
        a,b=(f,g) if (f,g) in pairset else (g,f)
        adj[idx[a]].append(idx[b]); indeg[idx[b]]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0); cnt=0
    while q:
        u=q.popleft(); cnt+=1
        for w in adj[u]:
            indeg[w]-=1
            if indeg[w]==0:q.append(w)
    return cnt==len(verts), len(hasse(F))

def rank_mod(A,p):
    if not A:return 0
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(z*inv)%p for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                fac=A[i][c]%p; A[i]=[(A[i][j]-fac*A[r][j])%p for j in range(n)]
        r+=1
        if r==m:break
    return r

def betti(F,p):
    by=defaultdict(list)
    for f in F: by[len(f)-1].append(f)
    maxd=max(by)
    ranks={}
    for d in range(1,maxd+1):
        rows=by[d-1]; cols=by[d]; ridx={f:i for i,f in enumerate(rows)}
        A=[[0]*len(cols) for _ in rows]
        for j,g in enumerate(cols):
            for k,x in enumerate(g):
                f=tuple(y for y in g if y!=x)
                A[ridx[f]][j]=(-1 if k%2 else 1)%p
        ranks[d]=rank_mod(A,p)
    b=[]
    for d in range(maxd+1):
        n=len(by[d]); rd=ranks.get(d,0); rnext=ranks.get(d+1,0)
        b.append(n-rd-rnext)
    return b,ranks

expected={'GM':([12,53,106,94,30,2],147,{0:1,3:2},962,[1,0,0,2,0,0]),'M':([12,53,106,92,24],141,{0:1,3:4},912,[1,0,0,4,0])}
for name,ok in [('GM',gm_ok),('M',m_ok)]:
    F=faces(ok)
    fv=[sum(len(f)==k for f in F) for k in range(1,max(map(len,F))+1)]
    print(name,'nfaces',len(F),'fvec',fv)
    order=list(range(len(P)))
    pairs,crit=elem_matching(F,order)
    print(' default pairs',len(pairs),'crit',[(len(f)-1,f) for f in sorted(crit,key=lambda z:(len(z),z))])
    ac,hc=acyclic_matching(F,pairs)
    print(' acyclic',(ac,hc))
    critvec=defaultdict(int)
    for f in crit: critvec[len(f)-1]+=1
    efv,epairs,ecrit,ehc,eb=expected[name]
    assert fv==efv and len(pairs)==epairs and dict(critvec)==ecrit and ac and hc==ehc
    for p in [2,3,5]:
        b=betti(F,p)[0]; print(' betti',p,b); assert b==eb
print('P',P)
print('VERIFY_OK')
