"""Independent finite-field linear-algebra verification for Heisenberg local derivations.

All calculations use the Lie bracket and evaluation definition directly; no theorem
about local derivations is assumed.
"""
import itertools


def rref(a,p):
    if not a:
        return [], []
    a=[[(x%p) for x in row] for row in a]
    m=len(a); n=len(a[0]); piv=[]; rr=0
    for c in range(n):
        k=next((k for k in range(rr,m) if a[k][c]), None)
        if k is None: continue
        a[rr],a[k]=a[k],a[rr]
        t=pow(a[rr][c],-1,p)
        a[rr]=[(z*t)%p for z in a[rr]]
        for j in range(m):
            if j==rr or not a[j][c]:continue
            t=a[j][c]
            a[j]=[(a[j][i]-t*a[rr][i])%p for i in range(n)]
        piv.append(c); rr+=1
        if rr==m:break
    return a[:rr],piv


def kernel(a,p,ncols=None):
    n=len(a[0]) if a else ncols
    rows,piv=rref(a,p)
    others=[c for c in range(n) if c not in piv]
    output=[]
    for j in others:
        v=[0]*n;v[j]=1
        for i,c in enumerate(piv): v[c]=(-rows[i][j])%p
        output.append(v)
    return output


def bracket(n,i,j,p):
    if i<n and j==i+n: return 1
    if j<n and i==j+n: return (p-1)
    return 0


def der_equations(n,p):
    d=2*n+1;z=d-1; m=d*d
    eq=[]
    for i in range(d):
      for j in range(i+1,d):
        c=bracket(n,i,j,p)
        for k in range(d):
          row=[0]*m
          if c:row[k*d+z]=(row[k*d+z]+c)%p
          if k==z:
            for a in range(d):
              ba=bracket(n,a,j,p)
              bb=bracket(n,i,a,p)
              row[a*d+i]=(row[a*d+i]-ba)%p
              row[a*d+j]=(row[a*d+j]-bb)%p
          if any(row):eq.append(row)
    return eq


def independent_local_constraints(n,p):
    d=2*n+1;m=d*d
    D=kernel(der_equations(n,p),p,m)
    equations=[]
    for x in itertools.product(range(p),repeat=d):
        if all(v==0 for v in x):continue
        ev=[[sum(mat[a*d+b]*x[b] for b in range(d))%p for mat in D] for a in range(d)]
        annihilator=kernel(list(map(list,zip(*ev))),p,d)
        for h in annihilator:
            row=[(h[a]*x[b])%p for a in range(d) for b in range(d)]
            equations.append(row)
    L=kernel(equations,p,m)
    predicted=[v for v in L if all(v[a*d+(d-1)]==0 for a in range(d-1))]
    assert len(predicted)==len(L)
    return len(D),len(L),len(equations),len(rref(equations,p)[1])

if __name__=='__main__':
  for n,p in [(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)]:
    dg,loc,eq,rank=independent_local_constraints(n,p)
    expected_der=2*n*n+3*n+1
    expected_loc=4*n*n+2*n+1
    assert (dg,loc)==(expected_der,expected_loc),(n,p,dg,loc,expected_der,expected_loc)
    print('Heisenberg n=%d p=%d Der_dim=%d LDer_dim=%d local_rank=%d constraints=%d: PASS'%(n,p,dg,loc,rank,eq))
  print('ALL_CHECKS_PASS')
