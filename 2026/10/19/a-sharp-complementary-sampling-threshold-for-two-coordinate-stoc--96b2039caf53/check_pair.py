from fractions import Fraction as Q
import itertools

def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def transpose(A): return list(map(list,zip(*A)))
def plus(A,B): return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def scale(c,A): return [[c*A[i][j] for j in range(2)] for i in range(2)]
def I(): return [[Q(int(i==j)) for j in range(2)] for i in range(2)]
def T(eta,i,j):
 E=I(); J=[[Q(0),Q(1)],[Q(-1),Q(0)]]
 P=lambda k:[[Q(int(u==v==k)) for v in range(2)] for u in range(2)]
 Gj=scale(Q(2),matmul(P(j),J)); Gi=scale(Q(2),matmul(P(i),J))
 return plus(plus(E,scale(-eta,Gj)),scale(eta*eta,matmul(Gj,Gi)))
def verified(eta,r):
 S=scale(Q(0),I()); B=scale(Q(0),I())
 for i,j in itertools.product(range(2),repeat=2):
  prob = (r if i!=j else 1-r)/2
  A=T(eta,i,j)
  S=plus(S,scale(prob,matmul(transpose(A),A)))
  B=plus(B,scale(prob,A))
 q=1+(2-4*r)*eta*eta+8*r*eta**4
 proposed_B=[[1-2*r*eta*eta,-eta],[eta,1-2*r*eta*eta]]
 assert S==scale(q,I()),(eta,r,S,q)
 assert B==proposed_B,(eta,r,B,proposed_B)
 factor=(1-2*r*eta*eta)**2+eta*eta
 assert matmul(transpose(B),B)==scale(factor,I())
 return q,factor
n=0
for d1 in range(1,17):
 for a in range(d1+1):
  r=Q(a,d1)
  for de in (2,3,4,7,11):
   for num in range(de+1):
    eta=Q(num,de)
    verified(eta,r);n+=1
print('Exact arithmetic (r,eta) samples checked:',n)
for r in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
 for eta in [Q(1,8),Q(1,4),Q(1,2),Q(1)]:
  q,b=verified(eta,r)
  print('r',r,'eta',eta,'mean-square factor',q,'mean factor',b)
