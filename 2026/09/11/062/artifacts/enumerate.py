"""Exhaustive psi-marked floor-diagram census, F0 bidegree (3,4) data.
Conventions: CJMR Def 4.1 verbatim (see DRAFT). k_surf=0 so divergence zero.
phi=(-2,-2,1,3) non-thick ends; mu=() ; g=0; n=4; one k=1 rest 0; sum s=3.
"""
import itertools

ENDS = [("L1",-2),("L2",-2),("R1",+1),("R2",+3)]  # distinct marked ends
N = 4

def pruefer_trees(n):
    trees=[]
    for seq in itertools.product(range(n), repeat=n-2):
        deg=[1]*n
        for s in seq: deg[s]+=1
        import bisect
        leaves=sorted(i for i in range(n) if deg[i]==1)
        d=list(deg); edges=[]
        for s in seq:
            leaf=leaves.pop(0)
            edges.append((min(leaf,s),max(leaf,s)))
            d[leaf]-=1; d[s]-=1
            if d[s]==1: bisect.insort(leaves,s)
        l1,l2=leaves
        edges.append((min(l1,l2),max(l1,l2)))
        trees.append(tuple(sorted(edges)))
    uniq=sorted(set(trees))
    return uniq

def solve_weights(edges, attach):
    # attach: dict end_idx -> vertex. end imbalance per vertex: Rend - Lend
    import fractions
    m=len(edges)
    # Build 4x3 system; solve via brute force rational: use integer elimination.
    # Use fractions gaussian elimination on first 3 rows (drop last, dependent).
    import copy
    rows=[]
    for v in range(N-1):  # first 3 vertices
        row=[0]*m
        rhs=0
        for j,(nm,w) in enumerate(ENDS):
            if attach[j]==v:
                rhs += - (w if w>0 else w)  # end imbalance: +w for right, w(neg) for left; move to rhs
                # equation: sum_orient*w_e + imb = 0 -> sum = -imb
        # orient: edge (a,b): at v==a contributes +w_e; at v==b contributes -w_e
        for ei,(a,b) in enumerate(edges):
            if v==a: row[ei]=1
            elif v==b: row[ei]=-1
        rows.append((row, -rhs if False else None))
    # recompute rhs correctly: imb(v)=sum of signed end weights at v
    rows=[]
    for v in range(N-1):
        row=[0]*m
        imb=0
        for j,(nm,w) in enumerate(ENDS):
            if attach[j]==v: imb+=w
        for ei,(a,b) in enumerate(edges):
            if v==a: row[ei]=1
            elif v==b: row[ei]=-1
        rows.append([list(row), -imb])
    # gaussian elimination fractions
    import fractions as F
    A=[[F.Fraction(x) for x in r]+[F.Fraction(rhs)] for r,rhs in rows]
    nrows=len(A); ncols=m
    piv=[-1]*ncols; r=0
    for c in range(ncols):
        pivrow=None
        for i in range(r,nrows):
            if A[i][c]!=0: pivrow=i; break
        if pivrow is None: continue
        A[r],A[pivrow]=A[pivrow],A[r]
        piv[c]=r
        inv=A[r][c]
        A[r]=[x/inv for x in A[r]]
        for i in range(nrows):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[a-f*b for a,b in zip(A[i],A[r])]
        r+=1
        if r==nrows: break
    # check consistency + extract (need full rank 3)
    sol=[None]*m
    for c in range(m):
        if piv[c]==-1: return None
        sol[c]=A[piv[c]][m]
    for i in range(nrows):
        if all(A[i][c]==0 for c in range(m)) and A[i][m]!=0: return None
    # verify 4th equation
    imb3=sum(w for j,(nm,w) in enumerate(ENDS) if attach[j]==N-1)
    s=sum((1 if (N-1)==a else -1 if (N-1)==b else 0)*sol[ei] for ei,(a,b) in enumerate(edges))
    if s+imb3!=0: return None
    # positivity + integrality
    out=[]
    for x in sol:
        if x<=0 or x.denominator!=1: return None
        out.append(int(x))
    return out

def census(psi_pos):
    kvec=[0]*N; kvec[psi_pos]=1
    trees=pruefer_trees(N)
    diagrams=[]
    size_patterns=[tuple(1 if i not in [z] else 0 for i in range(N)) for z in range(N)]  # position of the unique s=0
    for sizes in size_patterns:
        if sum(sizes)!=3: continue
        t=[kvec[i]+2-2*sizes[i] for i in range(N)]  # g=0
        if any(x<0 for x in t): continue
        if sum(t)!=3: continue
        for edges in trees:
            # incidence per vertex
            inc={v:[] for v in range(N)}
            for ei,(a,b) in enumerate(edges):
                inc[a].append(ei); inc[b].append(ei)
            for attach in itertools.product(range(N), repeat=len(ENDS)):
                # quick degree prune for s=0 primary vertices (mult!=0 => exactly 2 flags)
                ok=True
                for v in range(N):
                    if sizes[v]==0 and kvec[v]==0:
                        if len(inc[v])+[attach[j]==v for j in range(len(ENDS))].count(True)!=2:
                            ok=False; break
                if not ok: continue
                # s=1 primary: no thickened halves -> each incident compact edge thick on other side; check later
                w=solve_weights(edges, attach)
                if w is None: continue
                # thickening orientations: bit per edge: 0=thick at left endpoint(a),1=thick at right(b)
                for bits in itertools.product([0,1], repeat=len(edges)):
                    cnt=[0]*N
                    for ei,(a,b) in enumerate(edges):
                        cnt[a if bits[ei]==0 else b]+=1
                    if cnt!=t: continue
                    # s=0 primary: both flags thickened + opposite dirs + equal weights
                    good=True
                    for v in range(N):
                        if sizes[v]==0 and kvec[v]==0:
                            # exactly 2 flags guaranteed; check both thickened
                            # collect flag descriptors
                            flags=[]
                            for ei in inc[v]:
                                a,b=edges[ei]
                                thick=( (v==a and bits[ei]==0) or (v==b and bits[ei]==1) )
                                # direction from v: to larger => right(+), to smaller => left(-)
                                other=b if v==a else a
                                dr=+1 if other>v else -1
                                flags.append(("c",thick,dr,w[ei]))
                            for j,(nm,ew) in enumerate(ENDS):
                                if attach[j]==v:
                                    flags.append(("e",False,+1 if ew>0 else -1,abs(ew)))
                            if len(flags)!=2 or not all(f[1] for f in flags): good=False; break
                            if flags[0][2]==flags[1][2] or flags[0][3]!=flags[1][3]: good=False; break
                        if sizes[v]==1 and kvec[v]==0:
                            # t=0: no thickened incident (cnt=0 already); also no thick ends (none) OK
                            pass
                    if not good: continue
                    mult=1
                    for x in w: mult*=x
                    diagrams.append(dict(sizes=sizes,edges=edges,attach=tuple(attach),w=tuple(w),bits=tuple(bits),mult=mult,t=tuple(t)))
    return diagrams

if __name__=="__main__":
    trees=pruefer_trees(4)
    print("trees:",len(trees))
    total=0
    for p in range(4):
        d=census(p)
        s=sum(x["mult"] for x in d)
        print(f"psi_pos={p}: ndiag={len(d)} D1part={s}")
        total+=s
        # show psi-vertex flag summary
        from collections import Counter
        c=Counter()
        for x in d:
            v=p
            flags=[]
            for ei,(a,b) in enumerate(x["edges"]):
                if v==a or v==b:
                    other=b if v==a else a
                    dr=+1 if other>v else -1
                    th=(v==a and x["bits"][ei]==0) or (v==b and x["bits"][ei]==1)
                    flags.append((dr,x["w"][ei],"T" if th else "N"))
            for j,(nm,ew) in enumerate(ENDS):
                if x["attach"][j]==v: flags.append((+1 if ew>0 else -1,abs(ew),"E"))
            c[tuple(sorted(flags))]+=1
        for k,v in sorted(c.items(), key=lambda z:-z[1])[:12]:
            print("   psi-flags",k,"x",v)
    print("TOTAL D(1) =",total)
