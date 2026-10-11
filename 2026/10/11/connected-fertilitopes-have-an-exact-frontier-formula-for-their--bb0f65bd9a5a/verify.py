#!/usr/bin/env python3
import itertools, math

def solve(A,b,eps=1e-11):
    n=len(A)
    M=[list(map(float,A[i]))+[float(b[i])] for i in range(n)]
    for c in range(n):
        p=max(range(c,n), key=lambda i:abs(M[i][c]))
        if abs(M[p][c])<eps:
            return None
        M[c],M[p]=M[p],M[c]
        z=M[c][c]
        M[c]=[x/z for x in M[c]]
        for i in range(n):
            if i==c: continue
            z=M[i][c]
            if z:
                M[i]=[M[i][j]-z*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def tree_nodes(lo,hi):
    if hi-lo==1:
        return {frozenset([lo])}, []
    mid=(lo+hi)//2
    L,Li=tree_nodes(lo,mid)
    R,Ri=tree_nodes(mid,hi)
    root=frozenset(range(lo,hi))
    return L|R|{root}, Li+Ri+[root]

def frontiers(B,m):
    proper=[I for I in B if len(I)<m]
    out=[]
    for r in range(1,len(proper)+1):
        for F in itertools.combinations(proper,r):
            if sum(len(I) for I in F)!=m:
                continue
            seen=set()
            ok=True
            for I in F:
                if seen.intersection(I):
                    ok=False; break
                seen.update(I)
            if ok and len(seen)==m:
                out.append(F)
    return out

def zvals(B,y):
    return {I:sum(y[J] for J in B if J.issubset(I)) for I in B}

def radius_frontier(B,y,m):
    z=zvals(B,y)
    root=frozenset(range(m))
    vals=[]
    for F in frontiers(B,m):
        den=sum(math.sqrt(len(I)*(m-len(I))/m) for I in F)
        num=z[root]-sum(z[I] for I in F)
        vals.append(num/den)
    return min(vals)

def radius_brutelp(B,y,m):
    z=zvals(B,y)
    root=frozenset(range(m))
    proper=[I for I in B if I!=root]
    # variables c_0,...,c_{m-1},rho; equality total=z_root.
    rows=[]
    rhs=[]
    for I in proper:
        nu=math.sqrt(len(I)*(m-len(I))/m)
        row=[0.0]*(m+1)
        for i in I: row[i]=1.0
        row[m]=-nu
        rows.append(row); rhs.append(z[I])
    best=-1e100
    # equality plus m active facets gives a square (m+1)x(m+1) system.
    for act in itertools.combinations(range(len(rows)),m):
        A=[[1.0]*m+[0.0]]
        bb=[z[root]]
        for t in act:
            A.append(rows[t]); bb.append(rhs[t])
        sol=solve(A,bb)
        if sol is None: continue
        if sol[m] < -1e-9: continue
        if all(sum(rows[j][k]*sol[k] for k in range(m+1)) >= rhs[j]-1e-8
               for j in range(len(rows))):
            best=max(best,sol[m])
    return best

cases=0
for m in range(2,7):
    full,internals=tree_nodes(0,m)
    root=frozenset(range(m))
    optional=[I for I in internals if I!=root and len(I)>1]
    # Vary which nontrivial internal nodes are retained; leaves and root stay.
    for mask in range(1<<len(optional)):
        B={frozenset([i]) for i in range(m)}|{root}
        B|={optional[j] for j in range(len(optional)) if (mask>>j)&1}
        for scheme in (0,1):
            y={}
            for I in B:
                s=sum(i+1 for i in I)
                if scheme==0:
                    y[I]=1+((s+len(I))%3)
                else:
                    y[I]=1+((min(I)+2*len(I))%4)
            rf=radius_frontier(B,y,m)
            rl=radius_brutelp(B,y,m)
            if not math.isfinite(rl) or abs(rf-rl)>2e-8*max(1.0,abs(rf)):
                raise SystemExit(("mismatch",m,B,y,rf,rl))
            cases+=1

print(f"VERIFY_OK fertilitope-frontier-inradius cases={cases} m=2..6 brute_lp=yes")
