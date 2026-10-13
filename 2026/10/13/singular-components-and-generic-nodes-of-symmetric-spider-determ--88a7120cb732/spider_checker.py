#!/usr/bin/env python3
"""Exact finite-field stress tests for symmetric spider determinant singular sets.
Scientific checks only; finite testing does not certify a universal theorem.
"""
from itertools import product,combinations

MOD=101

def graph(arms):
    edges=[]; branches=[]; k=1
    for length in arms:
        verts=list(range(k,k+length)); branches.append(verts)
        edges.append((0,verts[0])); edges.extend(zip(verts[:-1],verts[1:])); k+=length
    return k,edges,branches

def build_mat(n,edges,d,b):
    m=[[0]*n for _ in range(n)]
    for i in range(n): m[i][i]=d[i]%MOD
    for (i,j),x in zip(edges,b): m[i][j]=m[j][i]=x%MOD
    return m

def rank(m):
    rows=[z[:] for z in m]; n=len(rows); pos=0
    for col in range(n):
        pivot=next((i for i in range(pos,n) if rows[i][col]),None)
        if pivot is None: continue
        rows[pos],rows[pivot]=rows[pivot],rows[pos]
        inv=pow(rows[pos][col],-1,MOD)
        for i in range(pos+1,n):
            if rows[i][col]:
                f=rows[i][col]*inv%MOD
                for j in range(col+1,n): rows[i][j]=(rows[i][j]-f*rows[pos][j])%MOD
                rows[i][col]=0
        pos+=1
        if pos==n:break
    return pos

def singular_spider_mat(m,edges,branches):
    n=len(m)
    for eidx,(a,b) in enumerate(edges):
        if m[a][b]!=0:continue
        comp={a}; stack=[a]
        while stack:
            x=stack.pop()
            for j in range(n):
                if j not in comp and m[x][j]!=0:
                    comp.add(j);stack.append(j)
        # Might be other cut edges, so the component of a in the graph
        # need not be the fixed two sides of the original tree cut.
        # Recover fixed side via graph edges rather than matrix edges.
        side={a}; stack=[a]
        while stack:
            x=stack.pop()
            for u,v in edges:
                if (u,v)==(a,b) or (u,v)==(b,a):continue
                if u==x and v not in side:side.add(v);stack.append(v)
                if v==x and u not in side:side.add(u);stack.append(u)
        other=set(range(n))-side
        s=sorted(side);t=sorted(other)
        if rank([[m[i][j] for j in s] for i in s])<len(s) and rank([[m[i][j] for j in t] for i in t])<len(t):
            return True
    if sum(rank([[m[i][j] for j in arm] for i in arm])<len(arm) for arm in branches)>=3:
        return True
    return False

def check(arms,values=(-1,0,1)):
    n,edges,branches=graph(arms)
    total=0;sing=0
    for coeff in product(values,repeat=n+len(edges)):
        m=build_mat(n,edges,coeff[:n],coeff[n:])
        reality=rank(m)<=n-2
        model=singular_spider_mat(m,edges,branches)
        if reality!=model:
            raise AssertionError((arms,coeff,reality,model))
        total+=1;sing+=int(reality)
    return total,sing

if __name__=='__main__':
    for arms in [(1,1,1),(2,1,1),(1,1,1,1),(2,2,1)]:
        total,sing=check(arms)
        n=1+sum(arms); c=n-1+len(list(combinations(range(len(arms)),3)))
        print(f'arms={arms}; variables={2*n-1}; configurations={total}; singular={sing}; predicted_components={c}; PASS')
    print('finite-field exhaustive checks PASS (characteristic 101); no universal claim inferred')

# These symbolic witnesses are intentionally a separate callable check from
# finite-field enumeration and use exact rational arithmetic.
def rational_nullspace(matrix):
    """Rational nullspace of an integer square matrix, no dependencies."""
    from fractions import Fraction as Q
    n=len(matrix); rows=[[Q(x) for x in r] for r in matrix]
    pivot_cols=[];p=0
    for j in range(n):
        k=next((k for k in range(p,n) if rows[k][j]),None)
        if k is None:continue
        rows[k],rows[p]=rows[p],rows[k]
        inv=1/rows[p][j]
        rows[p]=[x*inv for x in rows[p]]
        for i in range(n):
            if i==p:continue
            f=rows[i][j]
            if f:rows[i]=[a-f*b for a,b in zip(rows[i],rows[p])]
        pivot_cols.append(j);p+=1
        if p==n:break
    bases=[]
    for free in range(n):
        if free in pivot_cols:continue
        vec=[Q(0)]*n;vec[free]=Q(1)
        for i,j in enumerate(pivot_cols):vec[j]=-rows[i][free]
        bases.append(vec)
    return bases

def rational_rank(matrix):
    from fractions import Fraction as Q
    rows=[[Q(x) for x in row] for row in matrix]; nr=len(rows); nc=len(rows[0]);r=0
    for c in range(nc):
        k=next((k for k in range(r,nr) if rows[k][c]),None)
        if k is None:continue
        rows[k],rows[r]=rows[r],rows[k]
        pivot=rows[r][c]
        for i in range(r+1,nr):
            f=rows[i][c]/pivot
            if f:rows[i]=[a-f*b for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==nr:break
    return r

def check_transverse_witnesses(arms):
    n,edges,branches=graph(arms)
    def exact_matrix(diag,edge_vals):
        m=[[0]*n for _ in range(n)]
        for i in range(n):m[i][i]=diag[i]
        for (u,v),q in zip(edges,edge_vals):m[u][v]=m[v][u]=q
        return m
    def restricted_rank(M,directions):
        K=rational_nullspace(M)
        assert len(K)==2, ('expected corank two',arms)
        v,w=K;vals=[]
        for i,j in directions:
            if i==j:vals.append([v[i]*v[i],v[i]*w[i],w[i]*w[i]])
            else:vals.append([2*v[i]*v[j],v[i]*w[j]+v[j]*w[i],2*w[i]*w[j]])
        assert rational_rank(vals)==3, (arms,vals)
    edge_success=0
    for eidx,(u,v) in enumerate(edges):
        ev=[1]*len(edges);ev[eidx]=0
        deg=[0]*n
        for (i,j),z in zip(edges,ev):
            if z:deg[i]+=1;deg[j]+=1
        M=exact_matrix([-k for k in deg],ev)
        comps=[];seen=set()
        for start in range(n):
            if start in seen:continue
            s={start};stack=[start];seen.add(start)
            while stack:
                x=stack.pop()
                for (i,j),z in zip(edges,ev):
                    if not z:continue
                    y=j if i==x else i if j==x else -1
                    if y>=0 and y not in seen:seen.add(y);s.add(y);stack.append(y)
            comps.append(sorted(s))
        assert len(comps)==2
        restricted_rank(M,[(comp[0],comp[0]) for comp in comps]+[(u,v)])
        edge_success+=1
    triple_success=0
    for indices in combinations(range(len(arms)),3):
        diag=[0]*n;diag[0]=3
        for j,branch in enumerate(branches):
            for k,vertex in enumerate(branch):
                path_deg=int(k>0)+int(k+1<len(branch))
                diag[vertex]=-path_deg if j in indices else (path_deg+3)
        M=exact_matrix(diag,[1]*len(edges))
        restricted_rank(M,[(branches[j][0],branches[j][0]) for j in indices])
        triple_success+=1
    return edge_success,triple_success

if __name__ == '__main__':
    for spec in [(1,1,1),(2,1,1),(1,1,1,1),(2,2,1),(2,2,2,1)]:
        a,b=check_transverse_witnesses(spec)
        print(f'exact-rational-transverse: arms={spec}; cut_components={a}; triple_components={b}; Hessian-rank=3; PASS')
