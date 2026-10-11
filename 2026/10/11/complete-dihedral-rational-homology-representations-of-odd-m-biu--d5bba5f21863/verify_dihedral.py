"""Exact finite checks of odd-ladder perfect-matching dihedral characters.

Uses integer face masks, independent recursive perfect-matching generation,
and signed traces of vertex permutations on oriented simplicial chains.
Python 3 standard library only.
"""

def path_sum(m):
    a,b=1,0
    if m==0:return a
    if m==1:return b
    for _ in range(2,m+1):a,b=b,b-a
    return b


def predicted(n, kind, j):
    degree=(n+1)//3
    if kind=='rotation':
        if j%2:return 0
        if n%3:return 2
        return 4 if j%6==0 else -2
    if j%2==0:return 0
    return 2*(-1)**degree*path_sum((n-1)//2)


def build(n):
    N=2*n
    edges=sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} |
                 {tuple(sorted((i,i+n))) for i in range(n)})
    index={e:i for i,e in enumerate(edges)}
    incid=[[] for _ in range(N)]
    for i,(a,b) in enumerate(edges):
        incid[a].append(i);incid[b].append(i)
    full=(1<<N)-1
    maximal=[]
    def visit(used, chosen):
        if used==full:
            maximal.append(chosen);return
        a=next(k for k in range(N) if not(used>>k)&1)
        for i in incid[a]:
            u,v=edges[i];b=u^v^a
            if not (used>>b)&1:visit(used|(1<<a)|(1<<b),chosen|(1<<i))
    visit(0,0)
    faces={0}
    for facet in maximal:
        subsets=[0]
        while facet:
            lsb=facet&-facet;facet-=lsb
            subsets += [s|lsb for s in subsets]
        faces.update(subsets)
    rim=[index[tuple(sorted((i,(i+1)%N)))] for i in range(N)]
    P=[sum(1<<rim[i] for i in range(j,N,2)) for j in (0,1)]
    forbidden=[]
    for i in range(N):
        for shift in (n-1,n+1):
            j=(i+shift)%N
            forbidden.append((1<<rim[i])|(1<<rim[j]))
    U={mask for mask in faces if all(mask&pair!=pair for pair in forbidden)}
    return edges,faces,U,P,forbidden,len(maximal)


def structural(n, faces, U, P, forbidden):
    assert all((F in U) or ((F&P[0]==F) or (F&P[1]==F)) for F in faces)
    for parity in (0,1):
        # The induced forbidden-pair graph on either rim-perfect-matching
        # simplex must be exactly an n-cycle.
        verts=[j for j in range(P[parity].bit_length()) if (P[parity]>>j)&1]
        adj={j:set() for j in verts}
        for pair in forbidden:
            if pair&P[parity]!=pair:continue
            a,b=[j for j in verts if (pair>>j)&1]
            adj[a].add(b);adj[b].add(a)
        assert len(verts)==n and all(len(adj[v])==2 for v in verts)
        seen={verts[0]};stack=[verts[0]]
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:seen.add(w);stack.append(w)
        assert len(seen)==n
        for F in faces:
            if F&P[parity]!=F:continue
            assert (F in U)==all(F&pair!=pair for pair in forbidden)


def permutation(edges,n,kind,j):
    N=2*n;idx={edge:i for i,edge in enumerate(edges)}
    if kind=='rotation':f=lambda x:(x+j)%N
    else:f=lambda x:(j-x)%N
    return [idx[tuple(sorted((f(a),f(b))))] for a,b in edges]


def signed_trace(faces,perm):
    acc=-1
    for F in faces:
        if F==0:continue
        cols=[];out=0;mask=F
        while mask:
            low=mask&-mask;mask-=low
            i=low.bit_length()-1
            t=perm[i];out|=1<<t;cols.append(t)
        if out!=F:continue
        inversions=sum(a>b for k,a in enumerate(cols) for b in cols[k+1:])
        acc+=-1 if (len(cols)+inversions)%2==0 else 1
    return acc


def mod2_betti(faces):
    by_size={}
    for F in faces:by_size.setdefault(F.bit_count(),[]).append(F)
    rank={}
    for k in range(1,max(by_size)+1):
        rows={v:i for i,v in enumerate(by_size[k-1])}
        pivots={}
        for cell in by_size.get(k,[]):
            mask=cell;v=0
            while mask:
                low=mask&-mask;mask-=low
                v^=1<<rows[cell^low]
            while v:
                p=v.bit_length()-1
                if p not in pivots:pivots[p]=v;break
                v^=pivots[p]
        rank[k]=len(pivots)
    return {d:(len(cells)-rank.get(d+1,0)-rank.get(d+2,0)) for d,cells in ((k-1,v) for k,v in by_size.items())}


def main():
    cases=0; faces_total=0
    for n in (3,5,7,9,11):
        edges,faces,U,P,forbidden,nfacets=build(n)
        structural(n,faces,U,P,forbidden)
        if n<=7:
            betti=mod2_betti(faces)
            d=(n+1)//3
            assert betti.get(d)==(4 if n%3==0 else 2), (n,betti)
            assert all(v==0 for k,v in betti.items() if k!=d),(n,betti)
            u_betti=mod2_betti(U)
            assert all(v==0 for v in u_betti.values()),(n,u_betti)
        if n<=9:
            elements=[(k,j) for k in ('rotation','reflection') for j in range(2*n)]
        else:
            elements=[('rotation',j) for j in (0,1,2,3,4,6,n)]+[('reflection',j) for j in (0,1,2,3)]
        for kind,j in elements:
            perm=permutation(edges,n,kind,j)
            actual=(-1)**((n+1)//3)*signed_trace(faces,perm)
            expected=predicted(n,kind,j)
            assert actual==expected,(n,kind,j,actual,expected)
            cases+=1
        faces_total+=len(faces)
        print('n=',n,'facets=',nfacets,'faces=',len(faces),'orbital-traces=',len(elements),flush=True)
    print('VERIFY_OK cases=',cases,'faces_total=',faces_total,flush=True)

if __name__=='__main__':main()
