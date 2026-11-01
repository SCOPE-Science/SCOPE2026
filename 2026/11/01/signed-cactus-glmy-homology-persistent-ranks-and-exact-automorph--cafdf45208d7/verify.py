"""Standalone finite checks of signed low-degree path chains.
No external dependencies.
"""
from collections import defaultdict,deque
from itertools import combinations
import random

def rankmod(cols, nrows, p=1009):
    piv = {}
    for col in cols:
        a = dict((i,v%p) for i,v in col.items() if v%p)
        while a:
            j=min(a)
            if j not in piv:
                s=pow(a[j],-1,p)
                piv[j]={i:v*s%p for i,v in a.items() if v%p}
                break
            fact=a[j]
            for i,v in piv[j].items():
                w=(a.get(i,0)-fact*v)%p
                if w: a[i]=w
                elif i in a: del a[i]
    return len(piv)

def components(n,E):
    adj=[[] for _ in range(n)]
    for (u,v),s in E.items(): adj[u].append((v,s));adj[v].append((u,s))
    unseen=set(range(n));cs=[]
    while unseen:
        root=min(unseen); unseen.remove(root);q=[root];cp={root:1};ok=True
        for u in q:
            for v,s in adj[u]:
                val=cp[u]*s
                if v in cp:
                    if cp[v]!=val:ok=False
                else: cp[v]=val;q.append(v);unseen.remove(v)
        cs.append((set(cp),ok))
    return cs

def highgirth(n,E):
    adj=[set() for _ in range(n)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    for u in range(n):
      for v in adj[u]:
        for w in adj[v]-{u}:
          if w in adj[u]:return False
          for z in adj[w]-{v,u}:
            if z in adj[u]:return False
    return True

def signed_path_h1(n,E,p=1009):
    # Enumerate the allowed 0/1/2 paths with the *actual* signed double-cover differential.
    dirs=[];sign={}
    for (u,v),s in E.items():
        for a,b in ((u,v),(v,u)):
            dirs.append((a,b));sign[a,b]=s
    dirs.sort(); dindex={e:i for i,e in enumerate(dirs)}
    b1=[]
    for u,v in dirs:b1.append({u:-1,v:sign[u,v]})
    paths=[(u,v,w) for (u,v) in dirs for (v2,w) in dirs if v==v2]
    # Nonallowed regular signed 1-paths may have a nontrivial sheet even when a base edge exists.
    # Distinguish them by the second-vertex sheet relative to the first.
    allowed=[];forbidden=[];findex={}
    for u,v,w in paths:
        s=sign[u,v];t=sign[v,w];a=defaultdict(int);f=defaultdict(int)
        a[dindex[v,w]]+=s
        a[dindex[u,v]]+=1
        if u!=w:
            endpoint=s*t
            if (u,w) in dindex and sign[u,w]==endpoint:
                a[dindex[u,w]]-=1
            else:
                key=(u,w,endpoint)
                if key not in findex:findex[key]=len(findex)
                f[findex[key]]-=1
        allowed.append(dict((i,v) for i,v in a.items() if v))
        forbidden.append(dict((i,v) for i,v in f.items() if v))
    nf=len(findex)
    tot=[dict(list(f.items())+[(nf+i,v) for i,v in a.items()]) for f,a in zip(forbidden,allowed)]
    rf=rankmod(forbidden,nf,p)
    rt=rankmod(tot,nf+len(dirs),p)
    img=rt-rf
    rd=rankmod(b1,n,p)
    return len(dirs)-rd-img,img,rd,rf,len(paths)

def example_graphs():
    def cy(n):return n,{tuple(sorted((i,(i+1)%n))):1 for i in range(n)}
    n,E=cy(5);yield ('C5',n,E)
    n,E=cy(6);yield ('C6',n,E)
    n,E=cy(7);yield ('C7',n,E)
    E={**cy(5)[1], **{(u+5,v+5):1 for u,v in cy(5)[1]}};yield ('two_C5',10,E)
    E=dict(E);E[4,5]=1;yield ('bridge_two_C5',10,E)
    # theta with three internally disjoint paths of length 3 from 0 to 1
    E={};s=2
    for k in range(3):
       a=s;b=s+1;s+=2
       for u,v in ((0,a),(a,b),(b,1)): E[tuple(sorted((u,v)))]=1
    yield ('theta_3x3',s,E)
    # Petersen graph (10,15) with outer/inner star and spokes
    E={}
    for i in range(5):
       for u,v in ((i,(i+1)%5),(5+i,5+(i+2)%5),(i,5+i)):
           E[tuple(sorted((u,v)))]=1
    yield ('petersen',10,E)
    # Heawood incidence of Fano plane
    triples=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
    E={}
    for j,t in enumerate(triples):
        for v in t:E[v,7+j]=1
    yield ('heawood',14,E)

def test():
  rng=random.Random(281014)
  cases=0;paths=0;edges=0;births=0
  for name,n,base in example_graphs():
    assert highgirth(n,base), name
    for trial in range(13):
      # test full and arbitrary spanning filtration prefix, independently randomly signed
      S={e:(-1 if rng.randrange(2) else 1) for e in base}
      key=list(S);rng.shuffle(key)
      for k in ([len(key)] if trial>1 else range(len(key)+1)):
        E={e:S[e] for e in key[:k]}
        comps=components(n,E)
        b=sum(bal for v,bal in comps)
        pred=len(E)-n+b
        h,img,rd,rf,pcs=signed_path_h1(n,E)
        assert img==len(E),(name,trial,k,'backtrack',img,len(E))
        assert h==pred,(name,trial,k,h,pred)
        if k and (k==len(key) or trial<=1):
          old={e:S[e] for e in key[:k-1]}
          bo=sum(bal for v,bal in components(n,old))
          h0=len(old)-n+bo
          assert pred-h0 in (0,1)
          births+=pred-h0
        cases+=1;paths+=pcs;edges+=len(E)
  print('VERIFY_OK signed_GLMY_cases=%d allowed_two_paths=%d edges=%d birth_events=%d'%(cases,paths,edges,births))

if __name__=='__main__':test()

def nullspace_basis_cols(B,nrows,ncols,p=1009):
    # B is a column list of sparse signed-incidence vectors.
    mat=[[B[j].get(i,0)%p for j in range(ncols)] for i in range(nrows)]
    piv=[];r=0
    for c in range(ncols):
        k=next((i for i in range(r,nrows) if mat[i][c]%p),None)
        if k is None:continue
        mat[r],mat[k]=mat[k],mat[r]
        s=pow(mat[r][c],-1,p)
        mat[r]=[v*s%p for v in mat[r]]
        for k2 in range(nrows):
            if k2!=r and mat[k2][c]:
                q=mat[k2][c]
                mat[k2]=[(a-q*b)%p for a,b in zip(mat[k2],mat[r])]
        piv.append(c);r+=1
        if r==nrows:break
    frees=[c for c in range(ncols) if c not in piv]
    basis=[]
    for c in frees:
        vec=[0]*ncols;vec[c]=1
        for i,pc in enumerate(piv):vec[pc]=-mat[i][c]%p
        basis.append(vec)
    return frees,basis

def symmetry_trace(n,E,g,p=1009):
    assert sorted(g)==list(range(n))
    assert {tuple(sorted((g[u],g[v]))):s for (u,v),s in E.items()}==E
    basis_edges=sorted(E);pos={e:i for i,e in enumerate(basis_edges)}
    B=[{u:-1,v:s} for (u,v),s in zip(basis_edges,[E[e] for e in basis_edges])]
    frees,nb=nullspace_basis_cols(B,n,len(B),p)
    tb=[]
    for v in nb:
        out=[0]*len(B)
        for i,(u,w) in enumerate(basis_edges):
            a,b=g[u],g[w];j=pos[tuple(sorted((a,b)))]
            coeff=1 if a<b else -E[u,w]
            out[j]=(out[j]+coeff*v[i])%p
        assert all(sum(col.get(t,0)*out[i] for i,col in enumerate(B))%p==0 for t in range(n))
        tb.append(out)
    direct=sum(v[frees[j]] for j,v in enumerate(tb))%p
    tfixed=sum(1 for (u,v) in basis_edges if g[u]==u and g[v]==v)
    tswap=sum(-E[u,v] for u,v in basis_edges if g[u]==v and g[v]==u)
    t0=sum(g[u]==u for u in range(n))
    # Zero-homology trace: one signed component eigenline for each fixed balanced component.
    h0trace=0
    for vertices,balanced in components(n,E):
        if not balanced or {g[v] for v in vertices}!=vertices: continue
        root=min(vertices)
        pot={root:1};queue=[root]
        for u in queue:
            for (a,b),sgn in E.items():
                if a==u and b not in pot:pot[b]=pot[u]*sgn;queue.append(b)
                if b==u and a not in pot:pot[a]=pot[u]*sgn;queue.append(a)
        h0trace+=pot[g[root]]*pot[root]
    expected=(tfixed+tswap-t0+h0trace)%p
    assert direct==expected,(direct,expected)
    return ((direct+p//2)%p)-p//2, tfixed,tswap,t0,h0trace,len(nb)

def test_symmetries():
    n,E=5,{tuple(sorted((i,(i+1)%5))):1 for i in range(5)}
    assert symmetry_trace(n,E,[(-i)%5 for i in range(5)])[0]==-1
    E[2,3]=-1
    assert symmetry_trace(n,E,[(-i)%5 for i in range(5)])[0]==0
    n,E=6,{tuple(sorted((i,(i+1)%6))):-1 for i in range(6)}
    assert symmetry_trace(n,E,[(i+1)%6 for i in range(6)])[0]==-1
    for bridge_sign in (-1,1):
        E={tuple(sorted((i,(i+1)%5))):1 for i in range(5)}
        E.update({tuple(sorted((5+i,5+(i+1)%5))):1 for i in range(5)})
        E[1,2]=-1;E[6,7]=-1;E[0,5]=bridge_sign
        got=symmetry_trace(10,E,[(i+5)%10 for i in range(10)])
        assert got[0]==-bridge_sign and got[-1]==1,got
    print('SYMMETRY_OK 5 exact signed character comparisons')

if __name__=='__main__':test_symmetries()

def short_balanced_cycles(n,E):
    edges=set(E)
    seen=set();ans=[]
    from itertools import permutations
    for k in (3,4):
      for vs in combinations(range(n),k):
        u=vs[0]
        for other in permutations(vs[1:]):
          cy=(u,)+other
          if cy[1]>cy[-1]:continue
          if any(tuple(sorted((cy[i],cy[(i+1)%k]))) not in edges for i in range(k)):continue
          if cy in seen:continue
          seen.add(cy)
          sg=1
          for i in range(k):sg*=E[tuple(sorted((cy[i],cy[(i+1)%k])))]
          if sg==1:ans.append(cy)
    return ans

def short_cycle_presentation(n,E,p=1009):
    keys=sorted(E);idx={e:i for i,e in enumerate(keys)}
    B=[{u:-1,v:s} for (u,v),s in zip(keys,[E[e] for e in keys])]
    rd=rankmod(B,n,p)
    cyc_cols=[]
    for cy in short_balanced_cycles(n,E):
        sg=1;col={}
        for i,u in enumerate(cy):
            v=cy[(i+1)%len(cy)];e=tuple(sorted((u,v)))
            coeff=sg*(1 if u<v else -E[e])
            col[idx[e]]=coeff
            sg*=E[e]
        assert sg==1
        assert all(sum(B[j].get(v,0)*coef for j,coef in col.items())==0 for v in range(n)), (cy,col)
        cyc_cols.append(col)
    rb=rankmod(cyc_cols,len(keys),p)
    return len(keys)-rd-rb,rd,rb,len(cyc_cols)

def all_graph_tests():
    rng=random.Random(55)
    graphs=[]
    def edges(n, es):return n,{tuple(sorted(e)):1 for e in es}
    graphs.extend(list(example_graphs()))
    graphs.append(('triangle',*edges(3,[(0,1),(1,2),(2,0)])))
    graphs.append(('square',*edges(4,[(0,1),(1,2),(2,3),(3,0)])))
    graphs.append(('K4',*edges(4,combinations(range(4),2))))
    graphs.append(('K5',*edges(5,combinations(range(5),2))))
    graphs.append(('K23',*edges(5,((i,j) for i in range(2) for j in range(2,5)))))
    graphs.append(('bowtie',*edges(5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)])))
    graphs.append(('wheel5',*edges(5,[(0,1),(1,2),(2,3),(3,0)]+[(4,i) for i in range(4)])))
    graphs.append(('C5chord',*edges(5,[(i,(i+1)%5) for i in range(5)]+[(0,2)])))
    checked=0;balanced_short=0
    for name,n,base in graphs:
      for k in range(20):
        E={e:(-1 if rng.randrange(2) else 1) for e in base}
        direct,im,rd,rf,npaths=signed_path_h1(n,E)
        pred,rd2,rc,ncy=short_cycle_presentation(n,E)
        assert direct==pred,(name,k,direct,pred)
        assert rd==rd2
        checked+=1;balanced_short+=ncy
    print('ALL_GRAPH_SHORT_CYCLE_OK cases=%d balanced_short_cycles=%d'%(checked,balanced_short))

if __name__=='__main__':all_graph_tests()

def cycle_flow(E,cy):
    out={};coef=1
    for i,u in enumerate(cy):
        v=cy[(i+1)%len(cy)]
        e=tuple(sorted((u,v)))
        out[e]=coef*(1 if u<v else -E[e])
        coef*=E[e]
    assert coef==1
    return out

def trace_short_relations(E,g):
    cycles=short_balanced_cycles(max(max(e) for e in E)+1 if E else 1,E)
    subtotal=0
    for cy in cycles:
        if {g[v] for v in cy}!={v for v in cy}:
            continue
        phi=cycle_flow(E,cy)
        edge=cy[0],cy[1]
        e=tuple(sorted(edge))
        image_e=tuple(sorted((g[edge[0]],g[edge[1]])))
        image_value=phi[e]*(1 if g[edge[0]]<g[edge[1]] else -E[e])
        subtotal+=int(image_value//phi[image_e])
        assert abs(image_value)==abs(phi[image_e])
    return subtotal

def friendship(m,sign=-1):
    n=2*m+1;E={}
    for j in range(m):
        a=2*j+1;b=a+1
        for u,v in [(0,a),(a,b),(b,0)]:E[tuple(sorted((u,v)))]=sign
    return n,E

def cactus_checks():
    rng=random.Random(55161)
    cases=0; filtration_pairs=0; cycles=0
    for m in (1,2,3,4):
        n,base=friendship(m)
        for iteration in range(16):
            signs={e:(-1 if rng.randrange(2) else 1) for e in base}
            key=list(base);rng.shuffle(key)
            last=None
            for step in range(len(key)+1):
                E={e:signs[e] for e in key[:step]}
                h,img,rd,rf,pcs=signed_path_h1(n,E)
                b=sum(int(ok) for _,ok in components(n,E))
                k=len(short_balanced_cycles(n,E))
                expected=len(E)-n+b-k
                assert h==expected,(m,iteration,step,h,expected)
                if last is not None:
                    assert h>=last,(m,iteration,step,h,last)
                    assert h-last<=1
                    filtration_pairs+=1
                last=h;cases+=1;cycles+=k
    # Exact automorphism-character comparisons for all-negative friendship graphs.
    chars=0
    for m in (2,3,4):
        n,E=friendship(m)
        for perm in (list(range(m)),list(reversed(range(m))),list(range(1,m))+[0]):
            g=[0]*n;g[0]=0
            for i,j in enumerate(perm):
                g[2*i+1]=2*j+1
                g[2*i+2]=2*j+2
            total, *_=symmetry_trace(n,E,g)
            fixed=sum(i==perm[i] for i in range(m))
            assert total==fixed-1,(m,perm,total,fixed-1)
            assert trace_short_relations(E,g)==0
            chars+=1
        # Positive signing destroys all degree-one homology; its relation lines explain cancellation.
        n,Ep=friendship(m,sign=1)
        assert signed_path_h1(n,Ep)[0]==0
        assert short_cycle_presentation(n,Ep)[0]==0
    print('CACTUS_FILTRATION_OK cases=%d adjacent_maps=%d balanced_short=%d'%(cases,filtration_pairs,cycles))
    print('FRIENDSHIP_SYMMETRY_OK characters=%d'%chars)

if __name__=='__main__':cactus_checks()
