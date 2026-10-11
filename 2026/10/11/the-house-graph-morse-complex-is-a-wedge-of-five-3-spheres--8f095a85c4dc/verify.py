#!/usr/bin/env python3
import itertools, json
from collections import Counter, deque

# House graph: square 0-1-2-3-0 with roof vertex 4 adjacent to 1,2.
N=5
EDGES=((0,1),(1,2),(2,3),(3,0),(1,4),(2,4))
TOGGLE_ORDER=(7,5,4,11,3,9,10,1,6,8,2,0)
EXPECTED_F=(12,51,90,55)
EXPECTED_RANKS=(11,40,50)
EXPECTED_BETTI=(1,0,0,5)

def primitives():
    p=[]
    for ei,(u,v) in enumerate(EDGES):
        p.append((u,ei,v)); p.append((v,ei,u))
    return tuple(p)

P=primitives()

def enumerate_faces():
    faces=set()
    def rec(i,chosen,used_vertices,used_edges,succ):
        if i==len(P):
            if chosen: faces.add(frozenset(chosen))
            return
        rec(i+1,chosen,used_vertices,used_edges,succ)
        tail,ei,head=P[i]
        if tail in used_vertices or ei in used_edges: return
        x=head
        while x in succ:
            x=succ[x]
            if x==tail: return
        ns=dict(succ); ns[tail]=head
        rec(i+1,chosen+(i,),used_vertices|{tail},used_edges|{ei},ns)
    rec(0,tuple(),set(),set(),{})
    return faces

def matching(faces):
    unmatched=set(faces); pairs=[]
    for v in TOGGLE_ORDER:
        for f in sorted(list(unmatched),key=lambda x:(len(x),tuple(sorted(x)))):
            if f not in unmatched or v in f: continue
            g=f|{v}
            if g in unmatched:
                pairs.append((f,g)); unmatched.remove(f); unmatched.remove(g)
    return pairs,unmatched

def covers(faces):
    out=[]
    for g in faces:
        if len(g)>1:
            for v in g:
                f=g-{v}
                if f in faces: out.append((f,g))
    return out

def acyclic(faces,pairs,covs):
    fs=sorted(faces,key=lambda x:(len(x),tuple(sorted(x))))
    idx={f:i for i,f in enumerate(fs)}
    pairset=set(pairs); D=[[] for _ in fs]; indeg=[0]*len(fs)
    for f,g in covs:
        a,b=(f,g) if (f,g) in pairset else (g,f)
        ia,ib=idx[a],idx[b];D[ia].append(ib);indeg[ib]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0); seen=0
    while q:
        i=q.popleft();seen+=1
        for j in D[i]:
            indeg[j]-=1
            if indeg[j]==0:q.append(j)
    return seen==len(fs),seen

def modrank(A,p):
    A=[[x%p for x in row] for row in A];m=len(A);n=len(A[0]) if m else 0;r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p); A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                a=A[i][c]; A[i]=[(x-a*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def boundary_ranks(faces,p):
    by={d:sorted([f for f in faces if len(f)==d+1],key=lambda x:tuple(sorted(x))) for d in range(4)}
    ranks=[]
    for d in range(1,4):
        lo,hi=by[d-1],by[d];pos={f:i for i,f in enumerate(lo)}
        M=[[0]*len(hi) for _ in lo]
        for j,g in enumerate(hi):
            vs=sorted(g)
            for k,v in enumerate(vs): M[pos[g-{v}]][j]=1 if k%2==0 else -1
        ranks.append(modrank(M,p))
    return tuple(ranks)

def det_poly_coeffs():
    # Matrix-forest polynomial det(L+xI), computed exactly by permutation expansion.
    L=[[0]*N for _ in range(N)]
    for u,v in EDGES:
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    # Polynomial entries as coefficient arrays; diagonal L_ii+x.
    def pmul(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return out
    out=[0]
    for perm in itertools.permutations(range(N)):
        inv=sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
        term=[1]
        for i,j in enumerate(perm):
            a=[L[i][j],1] if i==j else [L[i][j]]
            term=pmul(term,a)
        if len(out)<len(term):out+= [0]*(len(term)-len(out))
        s=-1 if inv%2 else 1
        for k,c in enumerate(term):out[k]+=s*c
    return tuple(out) # constant upward

def main():
    faces=enumerate_faces()
    fv=tuple(sum(len(f)==d+1 for f in faces) for d in range(4));assert fv==EXPECTED_F,fv
    pairs,critical=matching(faces);assert len(pairs)==101,len(pairs)
    cc=Counter(len(f)-1 for f in critical);assert dict(cc)=={0:1,3:5},cc
    covs=covers(faces);ok,seen=acyclic(faces,pairs,covs);assert ok,(seen,len(faces))
    for p in (2,3,5):
        r=boundary_ranks(faces,p);assert r==EXPECTED_RANKS,(p,r)
        b=(EXPECTED_F[0]-r[0],EXPECTED_F[1]-r[0]-r[1],EXPECTED_F[2]-r[1]-r[2],EXPECTED_F[3]-r[2])
        assert b==EXPECTED_BETTI,(p,b)
    poly=det_poly_coeffs();assert poly==(0,55,90,51,12,1),poly
    critical_desc=[]
    for f in sorted(critical,key=lambda x:(len(x),tuple(sorted(x)))):
        critical_desc.append([{'tail':P[i][0],'edge':list(EDGES[P[i][1]]),'head':P[i][2]} for i in sorted(f)])
    out={
      'graph':'house graph H: 0-1-2-3-0 with roof 4 joined to 1 and 2',
      'edges':[list(e) for e in EDGES],
      'primitive_vector_fields':len(P),
      'nonempty_faces':len(faces),
      'face_vector':list(fv),
      'hasse_covers':len(covs),
      'toggle_order_indices':list(TOGGLE_ORDER),
      'toggle_order_primitives':[{'tail':P[i][0],'edge':list(EDGES[P[i][1]]),'head':P[i][2]} for i in TOGGLE_ORDER],
      'matching_pairs':len(pairs),
      'critical_counts':{str(k):v for k,v in sorted(cc.items())},
      'critical_faces':critical_desc,
      'directed_hasse_acyclic':ok,
      'matrix_forest_polynomial':'x^5 + 12*x^4 + 51*x^3 + 90*x^2 + 55*x',
      'boundary_ranks_mod_2_3_5':list(EXPECTED_RANKS),
      'betti_mod_2_3_5':list(EXPECTED_BETTI),
      'status':'VERIFY_OK'
    }
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
