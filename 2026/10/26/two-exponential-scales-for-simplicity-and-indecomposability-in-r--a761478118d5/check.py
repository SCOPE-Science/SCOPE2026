#!/usr/bin/env python3
"""Direct small finite-field checks for conditional GL support-connectivity counts."""
from itertools import product
from math import comb, prod

def det_nonzero(rows,q):
    a=[list(row) for row in rows]; n=len(a)
    for j in range(n):
        pivot=next((r for r in range(j,n) if a[r][j]%q),None)
        if pivot is None: return False
        a[j],a[pivot]=a[pivot],a[j]
        x=pow(a[j][j],-1,q)
        for r in range(j+1,n):
            s=a[r][j]*x%q
            for c in range(j+1,n): a[r][c]=(a[r][c]-s*a[j][c])%q
            a[r][j]=0
    return True

def graph_reaches(rows, root, directed=True, reverse=False):
    n=len(rows); seen={root}; todo=[root]
    for u in todo:
        for v in range(n):
            forward=rows[v][u] if reverse else rows[u][v]
            if not directed: forward=rows[u][v] or rows[v][u]
            if forward and v not in seen: seen.add(v);todo.append(v)
    return len(seen)==n

def graph_types(rows):
    strong=graph_reaches(rows,0) and graph_reaches(rows,0,reverse=True)
    weak=graph_reaches(rows,0,directed=False)
    return strong,weak

def gl(n,q): return prod(q**n-q**i for i in range(n))

def connected_rec(n,q):
    c={0:0}
    for m in range(1,n+1):
        c[m]=gl(m,q)-sum(comb(m-1,k-1)*c[k]*gl(m-k,q) for k in range(1,m))
    return c[n]

def test(q,n):
    total=simple=connected=0
    single_out=[0]*n; single_in=[0]*n; single_iso=[0]*n
    cuts={k:0 for k in range(1,n)}
    for entries in product(range(q),repeat=n*n):
        rows=[entries[i*n:(i+1)*n] for i in range(n)]
        if not det_nonzero(rows,q): continue
        total+=1; is_simple,is_connected=graph_types(rows)
        simple+=is_simple;connected+=is_connected
        for i in range(n):
            a=all(rows[i][j]==0 for j in range(n) if j!=i)
            b=all(rows[j][i]==0 for j in range(n) if j!=i)
            single_out[i]+=a;single_in[i]+=b;single_iso[i]+=(a and b)
        for k in range(1,n):
            for mask in range(1,1<<n):
                if mask.bit_count()!=k:continue
                if all(rows[i][j]==0 for i in range(n) if mask>>i&1 for j in range(n) if not(mask>>j&1)):
                    cuts[k]+=1
    assert total==gl(n,q),(q,n,total,gl(n,q))
    assert connected==connected_rec(n,q),(q,n,connected,connected_rec(n,q))
    for i in range(n):
        expect_out=gl(1,q)*gl(n-1,q)*q**(n-1)
        expect_iso=gl(1,q)*gl(n-1,q)
        assert single_out[i]==expect_out and single_in[i]==expect_out
        assert single_iso[i]==expect_iso
    for k in range(1,n):
        assert cuts[k]==comb(n,k)*gl(k,q)*gl(n-k,q)*q**(k*(n-k)),(q,n,k,cuts[k])
    print('OK',q,n,'GL',total,'simple',simple,'indecomposable',connected,'cut incidences',cuts)

if __name__=='__main__':
    for q,n in [(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)]:test(q,n)
    print('VERIFY_OK')
