# Exact-integer interval certificate for a three-patch population monodromy.
from math import factorial
N=430
Eden=10**12
A1=[[-16,0,2],[12,6,0],[0,2,8]]
A2=[[-9,0,2],[12,-7,0],[0,2,-3]]
B1=[[A1[i][j]+(16 if i==j else 0) for j in range(3)] for i in range(3)]
B2=[[A2[i][j]+(9 if i==j else 0) for j in range(3)] for i in range(3)]
def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def matvec(A,v):return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
def matadd(A,B):return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def matrix_polynomial(M):
 # Horner evaluation of N! * (I + M + ... + M^N/N!)
 from math import factorial
 coeff=[factorial(N)//factorial(k) for k in range(N+1)]
 C=[[int(i==j) for j in range(3)] for i in range(3)]
 for k in range(N-1,-1,-1):
  C=matmul(M,C)
  for i in range(3):C[i][i]+=coeff[k]
 return C
J=[[1]*3 for _ in range(3)]
def witness(T,v,a=None,b=None):
 t=T//2
 mats=[]
 for B in (B1,B2):
  M=[[t*z for z in row] for row in B]
  R=max(sum(row) for row in M)
  assert R<N+2
  # Tail ≤ R^(N+1)/(N+1)! * (N+2)/(N+2-R) < 1/Eden.
  assert Eden*(R**(N+1))*(N+2)<factorial(N+1)*(N+2-R)
  mats.append(matrix_polynomial(M))
 P1,P2=mats;d=factorial(N)
 if a is not None:
  vout=matvec(matmul(P2,P1),v)
  gaps=[vout[i]-a*d*d*v[i] for i in range(3)]
  print('T',T,'lower',min(gaps)>0,'rel margins', [round(g/(a*d*d*v[i]),7) for i,g in enumerate(gaps)])
  assert all(g>0 for g in gaps)
 if b is not None:
  U1=[[Eden*P1[i][j]+d for j in range(3)] for i in range(3)]
  U2=[[Eden*P2[i][j]+d for j in range(3)] for i in range(3)]
  vout=matvec(matmul(U2,U1),v)
  gaps=[b*Eden**2*d*d*v[i]-vout[i] for i in range(3)]
  print('T',T,'upper',min(gaps)>0,'rel margins',[round(g/(b*Eden**2*d*d*v[i]),7) for i,g in enumerate(gaps)])
  assert all(g>0 for g in gaps)
if __name__=='__main__':
 assert all(sum([[-12,0,2],[12,-2,0],[0,2,-2]][i][j] for i in range(3))==0 for j in range(3))
 a=778*10**11;b=356*10**53
 assert a**4>b
 witness(2,[276,629,1000],a=a)
 witness(8,[276,629,1000],b=b)
 print('CERT_OK',a,b, 'a4/b=',round(a**4/b,7))
