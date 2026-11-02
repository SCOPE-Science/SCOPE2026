"""Exact small-case verification of the group-with-zero DSC normal form.

Mathematical input: finite group supplied as a multiplication table.
No external dependencies.
"""
from itertools import permutations


def cyclic_group(n):
    return [[(i+j)%n for j in range(n)] for i in range(n)]


def sym_group(n):
    perms = list(permutations(range(n)))
    idx = {p:i for i,p in enumerate(perms)}
    return [[idx[tuple(a[b[k]] for k in range(n))] for b in perms]
            for a in perms]


def all_subgroups(t):
    m=len(t)
    identity=next(i for i in range(m) if all(t[i][x]==x==t[x][i] for x in range(m)))
    return [frozenset(i for i in range(m) if mask>>i&1)
            for mask in range(1<<m)
            if mask>>identity&1 and all(t[a][b] in (i for i in range(m) if mask>>i&1)
                                     for a in range(m) if mask>>a&1 for b in range(m) if mask>>b&1)]


def normal_subgroups(t):
    sub=all_subgroups(t);m=len(t)
    ident=next(i for i in range(m) if all(t[i][x]==x==t[x][i] for x in range(m)))
    inv={g:next(h for h in range(m) if t[g][h]==ident==t[h][g]) for g in range(m)}
    normals=[N for N in sub if all(t[t[g][n]][inv[g]] in N for g in range(m) for n in N)]
    return normals,inv


def normal_form(t,N,inv,row,col):
    m=len(t);R={(i,i) for i in range(m+1)}
    R.update((i,j) for i in range(m) for j in range(m) if t[i][inv[j]] in N)
    if row:R.update((i,m) for i in range(m))
    if col:R.update((m,j) for j in range(m))
    return frozenset(R)


def verify(t,exhaustive=False):
    m=len(t);z=m
    ns,inv=normal_subgroups(t)
    def mul(i,j):return z if i==z or j==z else t[i][j]
    made={normal_form(t,N,inv,a,b) for N in ns for a in (False,True) for b in (False,True)}
    assert len(made)==4*len(ns)
    for R in made:
        assert all((mul(a,c),mul(b,d)) in R for a,b in R for c,d in R)
    congs={R for R in made if all((b,a) in R for a,b in R) and
           all((a,c) in R for a,b in R for bb,c in R if bb==b)}
    assert len(congs)==len(ns)+1
    if exhaustive:
        off=[(i,j) for i in range(m+1) for j in range(m+1) if i!=j]
        diag={(i,i) for i in range(m+1)}
        actual=set()
        for mask in range(1<<len(off)):
            R=diag|{x for j,x in enumerate(off) if mask>>j&1}
            if all((mul(a,c),mul(b,d)) in R for a,b in R for c,d in R):
                actual.add(frozenset(R))
        assert actual==made,(m,len(actual),len(made))
    return len(ns),len(made),len(congs)


if __name__=='__main__':
    for n in (1,2,3,4,5):
        r=verify(cyclic_group(n),exhaustive=(n<=3))
        print(f'C_{n} k={r[0]} D={r[1]} C={r[2]} exhaustive={n<=3}')
    r=verify(sym_group(3))
    print(f'S_3 k={r[0]} D={r[1]} C={r[2]} all_normal_forms_checked')
    print('VERIFY_OK')
