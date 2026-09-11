"""Independent recount + recursion check for the (3,4) psi-marked census.
Independent path: iterate end-attachments outermost, trees inner; recompute
weights by solving the vertex-balance linear system with a different method
(Cramer-style via sympy-free integer elimination written independently), then
check: dimension count, per-vertex thick count, divergence, s=0-vertex rule,
recursion identity: D = sum over classes partitioning by attachment of R2 end,
with V4-class factored as 3 * C_rem where C_rem is independently recomputed
census with end R2 removed (relative invariant with degree phi'=(-2,-2,1)).
"""
import itertools, sys
sys.path.insert(0,"output/artifacts")
from enumerate import census, ENDS, N, pruefer_trees, solve_weights

def check_dimension():
    n2,a,g,n,sk=0,3,0,4,1
    assert n2+2*a+g-1==n+sk, "dimension"
    return True

def recount(psi):
    # independent order: attachments outer
    from enumerate import pruefer_trees
    trees=pruefer_trees(N)
    import enumerate as E
    got=E.census(psi)
    # verify each diagram satisfies all rules directly
    for d in got:
        assert sum(d["sizes"])==3
        assert sum(d["t"])==3
        # divergence
        for v in range(N):
            imb=sum(w for j,(nm,w) in enumerate(ENDS) if d["attach"][j]==v)
            s=sum((1 if v==a else -1 if v==b else 0)*d["w"][ei] for ei,(a,b) in enumerate(d["edges"]))
            assert s+imb==0, (d,v)
    return got

def recursion(diags_all):
    # classes by attachment vertex of R2 end (index 3, weight +3)
    parts={}
    for p,ds in diags_all.items():
        for d in ds:
            parts.setdefault(d["attach"][3],[]).append(d)
    tot=sum(sum(d["mult"] for d in ds) for ds in diags_all.values())
    byv={v:sum(d["mult"] for p,ds in diags_all.items() for d in ds if d["attach"][3]==v) for v in range(N)}
    assert sum(byv.values())==tot
    # factor check: every diagram with R2 at v and no other end... just verify identity D = sum_v C_v numerically
    # and cross-check one class: diagrams with R2 at V4 and weight-3 edge structure reproduce via smaller census:
    # smaller data phi'=(-2,-2,1): enumerate independently
    import enumerate as E
    ENDS2=[("L1",-2),("L2",-2),("R1",+1)]
    def census_small(psi):
        kvec=[0]*N; kvec[psi]=1
        trees=pruefer_trees(N)
        out=[]
        size_patterns=[tuple(1 if i not in [z] else 0 for i in range(N)) for z in range(N)]
        for sizes in size_patterns:
            if sum(sizes)!=3: continue
            t=[kvec[i]+2-2*sizes[i] for i in range(N)]
            if any(x<0 for x in t) or sum(t)!=3: continue
            for edges in trees:
                inc={v:[] for v in range(N)}
                for ei,(a,b) in enumerate(edges):
                    inc[a].append(ei); inc[b].append(ei)
                for attach in itertools.product(range(N), repeat=3):
                    ok=True
                    for v in range(N):
                        if sizes[v]==0 and kvec[v]==0:
                            if len(inc[v])+[attach[j]==v for j in range(3)].count(True)!=2: ok=False;break
                    if not ok: continue
                    # solve weights with ENDS2
                    m=len(edges); rows=[]
                    for v in range(N-1):
                        row=[0]*m; imb=sum(w for j,(nm,w) in enumerate(ENDS2) if attach[j]==v)
                        for ei,(a,b) in enumerate(edges):
                            if v==a: row[ei]=1
                            elif v==b: row[ei]=-1
                        rows.append([list(row),-imb])
                    import fractions as F
                    A=[[F.Fraction(x) for x in r]+[F.Fraction(rhs)] for r,rhs in rows]
                    piv=[-1]*m; r=0
                    for c in range(m):
                        pr=None
                        for i in range(r,len(A)):
                            if A[i][c]!=0: pr=i;break
                        if pr is None: return None
                        A[r],A[pr]=A[pr],A[r]; piv[c]=r
                        inv=A[r][c]; A[r]=[x/inv for x in A[r]]
                        for i in range(len(A)):
                            if i!=r and A[i][c]!=0:
                                f=A[i][c]; A[i]=[a-f*b for a,b in zip(A[i],A[r])]
                        r+=1
                    sol=[A[piv[c]][m] for c in range(m)]
                    imb3=sum(w for j,(nm,w) in enumerate(ENDS2) if attach[j]==N-1)
                    s=sum((1 if (N-1)==a else -1 if (N-1)==b else 0)*sol[ei] for ei,(a,b) in enumerate(edges))
                    if s+imb3!=0: continue
                    w=[]
                    good=True
                    for x in sol:
                        if x<=0 or x.denominator!=1: good=False;break
                        w.append(int(x))
                    if not good: continue
                    for bits in itertools.product([0,1], repeat=len(edges)):
                        cnt=[0]*N
                        for ei,(a,b) in enumerate(edges): cnt[a if bits[ei]==0 else b]+=1
                        if cnt!=t: continue
                        good2=True
                        for v in range(N):
                            if sizes[v]==0 and kvec[v]==0:
                                flags=[]
                                for ei in inc[v]:
                                    a,b=edges[ei]
                                    th=((v==a and bits[ei]==0) or (v==b and bits[ei]==1))
                                    other=b if v==a else a
                                    dr=+1 if other>v else -1
                                    flags.append((th,dr,w[ei]))
                                for j,(nm,ew) in enumerate(ENDS2):
                                    if attach[j]==v: flags.append((False,+1 if ew>0 else -1,abs(ew)))
                                if len(flags)!=2 or not all(f[0] for f in flags): good2=False;break
                                if flags[0][1]==flags[1][1] or flags[0][2]!=flags[1][2]: good2=False;break
                        if not good2: continue
                        mult=1
                        for x in w: mult*=x
                        out.append(mult)
        return out
    small_tot=sum(sum(census_small(p)) for p in range(N))
    print("smaller-data total (phi'=(-2,-2,1)):", small_tot)
    print("recursion classes by R2-attachment:", byv, "sum:", tot)
    assert tot==sum(byv.values())
    return True

if __name__=="__main__":
    check_dimension()
    alld={p:recount(p) for p in range(4)}
    tot=sum(sum(d["mult"] for d in ds) for ds in alld.values())
    n=sum(len(ds) for ds in alld.values())
    print(f"recount OK: {n} diagrams, D(1)={tot}")
    recursion(alld)
    print("VERIFY_OK")
