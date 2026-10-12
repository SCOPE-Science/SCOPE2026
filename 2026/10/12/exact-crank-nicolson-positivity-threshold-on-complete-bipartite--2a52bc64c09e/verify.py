from fractions import Fraction as F

def inv(A):
    n=len(A); M=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        piv=next(r for r in range(c,n) if M[r][c])
        M[c],M[piv]=M[piv],M[c]
        z=M[c][c]; M[c]=[x/z for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]; M[r]=[a-z*b for a,b in zip(M[r],M[c])]
    return [row[n:] for row in M]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def kpq(p,q):
    n=p+q; L=[[F(0) for _ in range(n)] for __ in range(n)]
    for i in range(p):
        L[i][i]=q
        for j in range(p,n): L[i][j]=F(-1)
    for i in range(p,n):
        L[i][i]=p
        for j in range(p): L[i][j]=F(-1)
    return L

def cn(p,q,h):
    L=kpq(p,q); n=p+q; s=F(h,2)
    A=[[F(int(i==j))+s*L[i][j] for j in range(n)] for i in range(n)]
    B=[[F(int(i==j))-s*L[i][j] for j in range(n)] for i in range(n)]
    return mm(inv(A),B), inv(A)

for p in range(1,6):
  for q in range(p,7):
    n=p+q
    for h in [F(1,10),F(1,2),F(1),F(2)]:
      C,R=cn(p,q,h); s=h/2
      dp=F(1,n)+F(p-1,p)/(1+s*q)+F(q,p*n)/(1+s*n)
      dq=F(1,n)+F(q-1,q)/(1+s*p)+F(p,q*n)/(1+s*n)
      assert all(R[i][i]==dp for i in range(p))
      assert all(R[i][i]==dq for i in range(p,n))
      diff= s*F(p-q)*(1+(n-1)*s)/((1+p*s)*(1+q*s)*(1+n*s))
      assert dp-dq==diff
      num = 1+p*s-q*(n-2)*s*s
      assert dp-F(1,2)==num/(2*(1+q*s)*(1+n*s))
      assert all(sum(row)==1 for row in C)
      assert all(C[i][j]>0 for i in range(n) for j in range(n) if i!=j)
# exact witness K_{2,3} at h=1
C,R=cn(2,3,F(1))
assert C[0][0]==F(-1,35)
assert C[1][1]==F(-1,35)
assert min(C[i][i] for i in range(2,5))>0
print('VERIFY_OK')
print('K23_h1_diag=', [str(C[i][i]) for i in range(5)])
