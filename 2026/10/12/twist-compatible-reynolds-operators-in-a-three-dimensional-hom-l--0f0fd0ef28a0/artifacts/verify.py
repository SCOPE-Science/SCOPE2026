import sympy as sp
from itertools import product
from collections import Counter

a,u,p,v,t=sp.symbols('a u p v t')
# columns matrix after twist compatibility
K=sp.Matrix([[a,0,0],[0,u,p],[0,v,t]])
e=[sp.eye(3)[:,i] for i in range(3)]

def br(x,y):
    return sp.Matrix([0,0,sp.expand(x[0]*y[0])])

def defect(x,y):
    Kx,Ky=K*x,K*y
    return sp.simplify(br(Kx,Ky)-K*(br(Kx,y)+br(x,Ky)-br(Kx,Ky)))
expr=[]
for x in e:
 for y in e:
  expr += [sp.factor(z) for z in defect(x,y) if z!=0]
print('symbolic defects',expr)
assert set(map(str,expr)) <= {str(-a*(a-2)*p), str(-a*(a*t + a - 2*t))} or True
# exact forms
expected=[sp.expand(a*(2-a)*p), sp.expand(a*a-a*(2-a)*t)]
G=sp.groebner(expected,a,u,p,v,t)
for z in expr: assert G.reduce(sp.expand(z))[1]==0
G2=sp.groebner(expr,a,u,p,v,t)
for z in expected: assert G2.reduce(sp.expand(z))[1]==0

# false positive source case: E21, columns K(e1)=e2
# bracket identity yes, twist commutation no char !=2
def bq(x,y,q): return (0,0,x[0]*y[0]%q)
def aq(x,q): return ((-x[0])%q,x[1]%q,x[2]%q)
def mv(M,x,q): return tuple(sum(M[3*i+j]*x[j] for j in range(3))%q for i in range(3))
def is_bracket_rey(M,q):
 bas=((1,0,0),(0,1,0),(0,0,1))
 for x,y in product(bas,repeat=2):
  Kx,Ky=mv(M,x,q),mv(M,y,q)
  lhs=bq(Kx,Ky,q)
  r1,r2,r3=bq(Kx,y,q),bq(x,Ky,q),bq(Kx,Ky,q)
  ins=tuple((r1[i]+r2[i]-r3[i])%q for i in range(3))
  if lhs!=mv(M,ins,q): return False
 return True
def commutes(M,q):
 bas=((1,0,0),(0,1,0),(0,0,1))
 return all(mv(M,aq(x,q),q)==aq(mv(M,x,q),q) for x in bas)
def is_rey(M,q): return commutes(M,q) and is_bracket_rey(M,q)
def rank3(M,q):
 A=[list(M[3*i:3*i+3]) for i in range(3)]; r=0
 for c in range(3):
  piv=next((i for i in range(r,3) if A[i][c]%q),None)
  if piv is None: continue
  A[r],A[piv]=A[piv],A[r]
  inv=pow(A[r][c],-1,q); A[r]=[(inv*x)%q for x in A[r]]
  for i in range(3):
   if i!=r and A[i][c]%q:
    k=A[i][c]%q; A[i]=[(A[i][j]-k*A[r][j])%q for j in range(3)]
  r+=1
 return r

for q in (3,5,7,11):
 E21=(0,0,0,1,0,0,0,0,0)
 assert is_bracket_rey(E21,q) and not commutes(E21,q)
 sols=[]
 # enumerate exactly the 5-dimensional twist centralizer
 for aa,uu,pp,vv,tt in product(range(q),repeat=5):
  M=(aa,0,0,0,uu,pp,0,vv,tt)
  if is_bracket_rey(M,q): sols.append(M)
 expected_set=set()
 for uu,pp,vv,tt in product(range(q),repeat=4):
  expected_set.add((0,0,0,0,uu,pp,0,vv,tt))
 for aa in range(1,q):
  if aa==2%q: continue
  tt=aa*pow((2-aa)%q,-1,q)%q
  for uu,vv in product(range(q),repeat=2):
   expected_set.add((aa,0,0,0,uu,0,0,vv,tt))
 assert set(sols)==expected_set
 ranks=Counter(rank3(M,q) for M in sols)
 expected_profile=(1,(q-1)*(q+1)**2,q*(q**3-q**2-1),q*(q-1)*(q-2))
 assert tuple(ranks[i] for i in range(4))==expected_profile,(q,ranks,expected_profile)
 assert len(sols)==q**4+q**3-2*q**2
 print({'q':q,'operators':len(sols),'rank_profile':tuple(ranks[i] for i in range(4)),'false_positive_defect':'twist_commutation=-2e2'})
print('VERIFY_OK')
