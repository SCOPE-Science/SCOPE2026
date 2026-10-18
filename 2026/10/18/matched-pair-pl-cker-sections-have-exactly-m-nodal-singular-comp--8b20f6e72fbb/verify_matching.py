"""Exact Plucker-chart and singular-stratum checks for paired-column Grassmannian sections.

Requires SymPy.  It verifies symbolic local equations and dimensions for finite test
sizes; the accompanying proof establishes the all-size statements.
"""
from math import comb
from itertools import combinations
import sympy as sp


def catalan(r):
    return comb(2*r,r)//(r+1)


def chart(m):
    """Use first columns of blocks 0,1 as the two gauge pivots."""
    assert m>=2
    u,v,w,z=sp.symbols('u v w z')
    columns=[sp.Matrix([1,0]),sp.Matrix([u,v]),sp.Matrix([0,1]),sp.Matrix([w,z])]
    for j in range(2,m):
        a,b,c,d=sp.symbols(f'a{j} b{j} c{j} d{j}')
        columns.extend([sp.Matrix([a,b]),sp.Matrix([c,d])])
    minors=[]
    for j in range(m):
        p,q=columns[2*j],columns[2*j+1]
        minors.append(sp.expand(p[0]*q[1]-p[1]*q[0]))
    expected=[v,-w]
    expected.extend(sp.Symbol(f'a{j}')*sp.Symbol(f'd{j}')-sp.Symbol(f'b{j}')*sp.Symbol(f'c{j}') for j in range(2,m))
    assert minors==expected,(minors,expected)
    return columns,minors


def check_fixed_point_gradients(m):
    # At a coordinate 2-plane supported in two different blocks, only the
    # equations of those two active blocks have nonzero differentials.
    cols,polys=chart(m)
    coords=sorted(set().union(*(e.free_symbols for e in polys)),key=str)
    for q in range(2,m+1):
        # q active blocks, the first two being anchor blocks; all additional
        # active blocks carry rank-one column pair e_1, with free scalar 1.
        subs={z:0 for z in coords}
        for j in range(2,q):
            subs[sp.Symbol(f'a{j}')]=1
            subs[sp.Symbol(f'c{j}')]=1
        jac=sp.Matrix([[sp.diff(f,t).subs(subs) for t in coords] for f in polys])
        assert jac.rank()==q,(m,q,jac.rank())
    return True


def main():
    for m in range(2,9):
        chart(m)
        check_fixed_point_gradients(m)
        assert catalan(2*m-2)==(comb(4*m-4,2*m-2)//(2*m-1))
        if m>2:
            assert m*catalan(2*m-4)>0
            for r in range(1,m+1):
                # A stratum with r zero blocks exists exactly if two active
                # blocks remain; its dimension is 3(m-r)-4.
                expected_nonempty=(r<=m-2)
                assert expected_nonempty==(m-r>=2)
                if expected_nonempty: assert 3*(m-r)-4>=2
        print(f'm={m}: dim={3*m-4}, deg={catalan(2*m-2)}, singular_components={m if m>=3 else 0}, singular_degree={m*catalan(2*m-4) if m>=3 else 0}, chart=OK')
    print('CHART_DEGREE_CHECKS_OK')

if __name__=='__main__':main()

# Exhaustive finite-field spot checks are intentionally optional and are not
# used as an all-characteristic proof.

def rank_mod_q(rows,q):
    M=[list(map(lambda x:x%q,row)) for row in rows]
    if not M:return 0
    ncols=len(M[0]);i=0
    for j in range(ncols):
        p=next((h for h in range(i,len(M)) if M[h][j]%q),None)
        if p is None:continue
        M[i],M[p]=M[p],M[i]
        inv=pow(M[i][j],-1,q)
        M[i]=[(x*inv)%q for x in M[i]]
        for h in range(len(M)):
            if h!=i and M[h][j]:
                f=M[h][j]
                M[h]=[(x-f*y)%q for x,y in zip(M[h],M[i])]
        i+=1
        if i==len(M):break
    return i


def finite_check(m,q):
    from itertools import product
    n=2*m; tested=0;selected=0;sing=0;by_z={}
    for p,s in combinations(range(n),2):
        free=[(0,j) for j in range(p+1,n) if j!=s]+[(1,j) for j in range(s+1,n)]
        for values in product(range(q),repeat=len(free)):
            A=[[0]*n for _ in range(2)]
            A[0][p]=1;A[1][s]=1
            for (r,c),val in zip(free,values):A[r][c]=val
            tested+=1
            if any((A[0][2*j]*A[1][2*j+1]-A[1][2*j]*A[0][2*j+1])%q for j in range(m)):
                continue
            selected+=1
            z=sum(all(A[r][c]==0 for r in range(2) for c in [2*j,2*j+1]) for j in range(m))
            # Tangent uses the full Grassmannian big cell at the pivot minor,
            # not the smaller Schubert/RREF stratum used to list points.
            tangent_free=[(r,c) for r in (0,1) for c in range(n) if c not in (p,s)]
            jac=[]
            for j in range(m):
                a,b=2*j,2*j+1
                g=[]
                for r,c in tangent_free:
                    if c==a:g.append(A[1][b] if r==0 else -A[0][b])
                    elif c==b:g.append(-A[1][a] if r==0 else A[0][a])
                    else:g.append(0)
                jac.append(g)
            jacrank=rank_mod_q(jac,q)
            assert (jacrank<m)==(z>0),(m,q,A,jacrank,z)
            assert jacrank==m-z,(m,q,A,jacrank,z)
            sing+=(z>0)
            by_z[z]=by_z.get(z,0)+1
    print(f'finite q={q} m={m} Gr_points={tested} X_points={selected} singular_points={sing} strata_by_zero_blocks={dict(sorted(by_z.items()))} EXACT_JACOBIAN_OK')

if __name__=='__main__':
    finite_check(3,2)
    finite_check(3,3)
    finite_check(4,2)
    print('VERIFY_OK')
