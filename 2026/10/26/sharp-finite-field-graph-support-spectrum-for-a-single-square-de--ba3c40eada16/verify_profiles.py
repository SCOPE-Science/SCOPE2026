"""Finite-field checks for graph-support profiles of two-square dependence blocks.
Science only; no external packages or network access.
"""
from itertools import product,combinations

def rep(v,p):
    x,y=v
    if x%p: return (1,y*pow(x,-1,p)%p)
    if y%p: return (0,1)
    raise ValueError('zero line')
def ortho(L,lam,p):
    x,y=L
    return rep(((-lam*y)%p,x%p),p)
def pair_reps(p,lam):
    lines=[(1,t) for t in range(p)]+[(0,1)]
    iso={L for L in lines if (L[0]**2+lam*L[1]**2)%p==0}
    pairs={tuple(sorted((L,ortho(L,lam,p)))) for L in lines if L not in iso}
    assert all(len(P)==2 for P in pairs)
    return sorted(pairs),iso

def det(M,p):
    A=[list(map(lambda x:x%p,row)) for row in M]
    n=len(A)
    d=1
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None:return 0
        if k!=j: A[j],A[k]=A[k],A[j];d=-d
        v=A[j][j];d=d*v%p
        inv=pow(v,-1,p)
        for k in range(j+1,n):
            a=A[k][j]*inv%p
            for h in range(j,n): A[k][h]=(A[k][h]-a*A[j][h])%p
    return d%p

def obs_profile(vs,L,M,p):
    a,b=L;c,d=M
    delta=(a*d-b*c)%p
    assert delta
    return tuple(0 if x%p==0 and y%p==0 else
        int((d*x-c*y)%p!=0)+int((-b*x+a*y)%p!=0) for x,y in vs)

def run():
    ntests=0
    for p in (2,3,5,7,11):
      for lam in range(1,p):
        pairs,iso=pair_reps(p,lam)
        N=(p+1-len(iso))//2
        assert len(pairs)==N
        for n in (3,4,5):
          # Two dependent nonzero squares, n-2 other independent squares.
          # Choose u=e1, and each e_i^2=e_i+v_i with distinct assigned U directions.
          # The u_i are independent because of the unique e_i components.
          Ls=[P[0] for P in pairs]
          targets=Ls[:max(0,min(N,n-1)-1)]
          # First line (from u=e1) may correspond to either element of its orbit.
          own=tuple(sorted(((1,0),ortho((1,0),lam,p))))
          remaining=[P[0] for P in pairs if P!=own]
          targets=remaining[:min(len(remaining),n-2)]
          vs=[(1,0)]+targets+[(0,0)]*(n-2-len(targets))
          # if n-2 exceeds distinct remaining, repeat nonisotropic lines to retain independence
          if len(vs)<n-1:vs.extend([(1,0)]*(n-1-len(vs)))
          assert len(vs)==n-1
          profiles=set()
          hit=set()
          for P in pairs:
            prof=obs_profile(vs,*P,p)
            profiles.add(prof)
            for v in vs:
              if v!=(0,0) and (v[0]**2+lam*v[1]**2)%p:
                if rep(v,p) in P:hit.add(P)
            ntests+=1
          assert len(profiles)==len(hit)+int(N>len(hit)),(p,lam,n,len(profiles),N,len(hit),vs)
          assert len(profiles)==min(n,N),(p,lam,n,len(profiles),N,vs)
          # exhaustive 2x2 invertible B-orthogonal frames and line orbit uniqueness
          seen=set()
          for a,b,c,d in product(range(p),repeat=4):
            if (a*d-b*c)%p and (a*c+lam*b*d)%p==0:
              seen.add(tuple(sorted((rep((a,b),p),rep((c,d),p)))))
          assert seen==set(pairs)
          ntests+=1
    # Exhaustively ensure no unanticipated mixing when one twin pair has dependent squares.
    for p in (2,3):
      n=3
      for lam in range(1,p):
        count=0
        for flat in product(range(p),repeat=n*n):
          rows=[flat[i*n:(i+1)*n] for i in range(n)]
          if det(rows,p)==0:continue
          # f_j f_k=0 for j!=k: product (rows0,rows1) forms one independent component, row2 another
          if any((rows[0][j]*rows[0][k]+lam*rows[1][j]*rows[1][k])%p or
                 rows[2][j]*rows[2][k]%p for j,k in combinations(range(n),2)):continue
          count+=1
          # Outside singleton e3 must occupy precisely one column, and that column has no U component
          cols_with_e3=[j for j in range(n) if rows[2][j]!=0]
          assert len(cols_with_e3)==1
          j=cols_with_e3[0]
          assert rows[0][j]==rows[1][j]==0
        assert count>0
    print('VERIFY_OK; %d projective/support consistency checks; full 3x3 field-2/3 basis exhaustive' % ntests)
if __name__=='__main__':run()
