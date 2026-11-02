import sympy as S
w=S.Symbol('w')
p=7
basis=[(1,S.Poly(1,w,modulus=7)),(2,S.Poly(w*w-1,w,modulus=7)),(3,S.Poly(w*w-1,w,modulus=7)),(3,S.Poly(w*(w*w-1),w,modulus=7)),(3,S.Poly(w*w*(w*w-1),w,modulus=7))]
def matrank7(M):
 A=[row[:] for row in M]; n=len(A); rank=0
 for c in range(n):
  k=next((r for r in range(rank,n) if A[r][c]%p),None)
  if k is None:continue
  A[rank],A[k]=A[k],A[rank]
  inv=pow(A[rank][c],-1,p)
  A[rank]=[a*inv%p for a in A[rank]]
  for r in range(n):
   if r!=rank:
    d=A[r][c]
    A[r]=[(a-d*b)%p for a,b in zip(A[r],A[rank])]
  rank+=1
 return rank
for t in range(2,7):
 for u in range(2,7):
  if t==u:continue
  F=S.Poly((w*w-1)**2*(w*w-t)*(w*w-u),w,modulus=7)
  M=[[0]*5 for i in range(5)]
  for col,(j,h) in enumerate(basis):
   jp={1:3,2:2,3:1}[j]
   P=(h*F**((7*jp-j)//4))
   coeff=[P.nth(7*k+6)%7 for k in range(5)]
   if j==1:
    assert coeff[1]==coeff[3]==0 and (coeff[0]+coeff[2]+coeff[4])%7==0
    M[2][col]=-coeff[0]%7
    M[4][col]=coeff[4]%7
   elif j==2:
    assert coeff[1]==coeff[3]==coeff[4]==0 and (coeff[0]+coeff[2])%7==0
    M[1][col]=coeff[2]%7
   else:
    assert coeff[1:]==[0]*4
    M[0][col]=coeff[0]%7
  rank=matrank7(M)
  exp=5-(2+int(u*pow(t,-1,7)%7 in [2,4,6])+2*int((t+u)%7==1 and t*u%7==1))
  assert rank==exp,(t,u,M,rank,exp)
print('DIRECT_OK')
