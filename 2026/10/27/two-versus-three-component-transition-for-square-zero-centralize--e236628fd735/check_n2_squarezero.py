"""Reproducible coordinate enumeration and matrix-model cross-check for Jordan type (n,2)."""
import itertools,sys

def mul(p,r,n,q):
    return tuple(sum(p[i]*r[k-i] for i in range(max(0,k-len(r)+1),min(k+1,len(p))))%q for k in range(n))

def count(n,q):
    polya=tuple(itertools.product(range(q),repeat=n))
    poly2=tuple(itertools.product(range(q),repeat=2))
    cnt=0
    for a in polya:
      aa=mul(a,a,n,q)
      # a0 and d0 must vanish, so prune
      if a[0]: continue
      for d in poly2:
        if d[0]:continue
        dd=mul(d,d,2,q)
        if any(dd):continue
        v=((a[0]+d[0])%q,(a[1]+d[1])%q)
        for b in poly2:
          if any(mul(b,v,2,q)):continue
          for c in poly2:
            if any(mul(c,v,2,q)):continue
            bc=mul(b,c,2,q)
            if (aa[n-2]+bc[0])%q==0 and (aa[n-1]+bc[1])%q==0 and not any(aa[:n-2]):
              cnt+=1
    return cnt

def predicted(n,q):
    return q**(n//2+1)*(2*q*q-1) if n%2==0 else q**((n-1)//2+2)*(3*q-2)
if __name__=='__main__':
  for n,q in [(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(6,3)]:
    t=count(n,q); v=predicted(n,q)
    print('n',n,'q',q,'actual',t,'predicted',v,'OK' if t==v else 'MISMATCH',flush=True)
    assert t==v
  print('NONHOOK_SQUARE_ZERO_COUNTS_OK')

def verify_matrix_model(n,q):
  import itertools
  dim=n+2
  count_actual=0
  j=[[0]*dim for _ in range(dim)]
  for i in range(1,n):j[i][i-1]=1
  j[n+1][n]=1
  for vals in itertools.product(range(q),repeat=n+6):
    a=vals[:n];b=vals[n:n+2];c=vals[n+2:n+4];d=vals[n+4:]
    m=[[0]*dim for _ in range(dim)]
    for col in range(n):
      for k in range(n-col):m[col+k][col]=a[k]
      if col<2:
        for k in range(2-col):m[n+col+k][col]=c[k]
    for col in range(2):
      for k in range(2-col):
        m[n-2+col+k][n+col]=b[k]
        m[n+col+k][n+col]=d[k]
    def zero(A,B):
      return all(sum(A[i][k]*B[k][j] for k in range(dim))%q==0 for i in range(dim) for j in range(dim))
    if not zero(m,j) or not zero(j,m):
      # actually m,j must commute, not vanish; check via difference
      assert all((sum(m[i][k]*j[k][r] - j[i][k]*m[k][r] for k in range(dim)))%q==0 for i in range(dim) for r in range(dim))
    if zero(m,m): count_actual+=1
  assert count_actual==predicted(n,q),(n,q,count_actual,predicted(n,q))
  return count_actual
if __name__=='__main__':
 for n,q in [(4,2),(5,2),(4,3)]:
  print('MATRIX_MODEL',n,q,verify_matrix_model(n,q),flush=True)
 print('MATRIX_MODEL_CROSSCHECK_OK')
