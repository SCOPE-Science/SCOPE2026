"""Independent linear-equation checks for ordinary vs square-Jordan derivations.
No reliance on a proposed normal form.
"""
from math import gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def incidence_pairs(covers, n):
    rel = [[i == j for j in range(n)] for i in range(n)]
    for i,j in covers: rel[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                rel[i][j] |= rel[i][k] and rel[k][j]
    assert all(not(rel[i][j] and rel[j][i]) for i in range(n) for j in range(n) if i!=j)
    pairs = [(i,j) for i in range(n) for j in range(n) if rel[i][j]]
    return pairs


def equations(pairs, kind):
    d=len(pairs); idx={p:i for i,p in enumerate(pairs)}
    def prod(a,b):
        i,j=pairs[a]; k,l=pairs[b]
        return idx[(i,l)] if j==k else None
    rows=[]
    for a in range(d):
        for b in range(d):
            if kind=='jordan' and b<a: continue
            if kind=='jordan' and b==a: products=[(a,a,1)]; modes=[(a,a,1)]
            elif kind=='jordan': products=[(a,b,1),(b,a,1)]; modes=[(a,b,1),(b,a,1)]
            else: products=[(a,b,1)]; modes=[(a,b,1)]
            for out in range(d):
                row=[0]*(d*d)
                for x,y,sgn in products:
                    p=prod(x,y)
                    if p is not None: row[out*d+p]+=sgn
                if kind=='jordan' and a==b:
                    # x^2 identity: one product on LHS, two Leibniz terms RHS
                    modes=[(a,a,1)]
                for x,y,sgn in modes:
                    # -D(x)*y - x*D(y)
                    for z in range(d):
                        if prod(z,y)==out: row[z*d+x]-=sgn
                        if prod(x,z)==out: row[z*d+y]-=sgn
                if any(row): rows.append(row)
    return rows


def rank_mod(rows,p):
    if not rows:return 0
    a=[[v%p for v in row] for row in rows]; m=len(a); n=len(a[0]); r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if a[i][col]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][col],-1,p)
        for j in range(col,n): a[r][j]=a[r][j]*inv%p
        for i in range(r+1,m):
            c=a[i][col]
            if c:
                for j in range(col,n):a[i][j]=(a[i][j]-c*a[r][j])%p
        r+=1
        if r==m:break
    return r


def mod4_count(rows):
    n=len(rows[0]); diag=smith_normal_form(Matrix(rows),domain=ZZ)
    cnt=4**n
    for i in range(min(diag.rows,diag.cols)):
        v=int(diag[i,i])
        if v:cnt=cnt//4*gcd(v,4)
    return cnt


def beta1(pairs,n):
    # 1-cocycles on comparable strict pairs, constraints c_ik-c_ij-c_jk=0.
    edges=[p for p in pairs if p[0]!=p[1]]; m=len(edges)
    if not m:return 0,n
    edge_idx={p:i for i,p in enumerate(edges)}
    rows=[]
    for i,j in edges:
      for j2,k in edges:
        if j==j2 and (i,k) in edge_idx:
          row=[0]*m
          for key,sign in [((i,k),1),((i,j),-1),((j,k),-1)]: row[edge_idx[key]]+=sign
          rows.append(row)
    rk=rank_mod(rows,2)
    # connected components of undirected comparable graph
    adj=[set() for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen=set();cc=0
    for u in range(n):
        if u in seen:continue
        cc+=1;stack=[u];seen.add(u)
        while stack:
            for v in adj[stack.pop()]:
                if v not in seen:seen.add(v);stack.append(v)
    return m-rk-(n-cc),cc


def run(name,n,covers,runmod4=True):
    pairs=incidence_pairs(covers,n); d=len(pairs); J=equations(pairs,'jordan');D=equations(pairs,'derivation'); beta,cc=beta1(pairs,n)
    print('POSET',name,'vertices',n,'algebra_dim',d,'comparables',d-n,'beta1_F2',beta,'components',cc)
    for p in [2,3,5]:
        jr=rank_mod(J,p); dr=rank_mod(D,p); expected=d-cc+beta
        print(' FIELD',p,'Jordan_dimension',d*d-jr,'Derivation_dimension',d*d-dr,'Predicted',expected)
        assert jr==dr and d*d-dr==expected
    if runmod4:
        j=mod4_count(J); der=mod4_count(D)
        print(' RING Z/4: #square-Jordan maps',j,'#derivations',der)
        assert j==der==4**(d-cc+beta)
    print(' PASS')

if __name__=='__main__':
    run('singleton',1,[],True)
    run('antichain_3',3,[],True)
    run('chain_2',2,[(0,1)],True)
    run('chain_3',3,[(0,1),(1,2)],True)
    run('V_fork_3',3,[(0,2),(1,2)],True)
    run('diamond_4',4,[(0,1),(0,2),(1,3),(2,3)],False)
    run('hexagon_order_complex',6,[(0,3),(0,5),(1,3),(1,4),(2,4),(2,5)],False)
    print('SQUARE_JORDAN_INCIDENCE_POSETS_OK 7 POSETS; 21 FIELD AND 5 Z4 CHECKS')
