from fractions import Fraction as Q

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv2(M):
    a,b=M[0]; c,d=M[1]
    det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]],det

b=delta=gamma=Q(1)
xi=Q(0)
mustar=Q(4)
mu=Q(1)
q=mustar-mu
nu=Q(1,2)
alpha=Q(1,2)
eta=Q(0)
beta=Q(16,5)

s=(nu+delta)/q
ss=b/delta-s
assert s==Q(1,2) and ss==Q(1,2)
assert (b/delta)*q/(nu+delta)==Q(2)

F=[[beta*(1-alpha)*(1-alpha)*s, beta*(1-alpha)*s],
   [beta*(1-alpha)*ss, beta*ss]]
V=[[gamma+eta+delta+q*ss, -nu],
   [-q*ss, gamma+nu+delta]]
assert F==[[Q(2,5),Q(4,5)],[Q(4,5),Q(8,5)]]
assert V==[[Q(7,2),Q(-1,2)],[Q(-3,2),Q(5,2)]]
Vinv,detV=inv2(V)
NG=matmul(F,Vinv)
# Rank-one next-generation matrix: spectral radius equals trace.
rtrue=NG[0][0]+NG[1][1]
assert rtrue==Q(41,40)

D=gamma+eta+nu+delta+q*ss
rprint=beta*((1-alpha)*(1-alpha)*(1+(alpha*mu*ss/(1-alpha)-eta)/D)*s +(1-alpha*nu/D)*ss)/(gamma+delta+eta*nu/D)
assert rprint==Q(39,40)
assert rtrue-rprint==Q(1,20)

diff_formula=beta*alpha*(1-alpha)*s*ss*(mustar-2*mu)/((gamma+delta)*D+eta*nu)
assert diff_formula==Q(1,20)

J=[[F[i][j]-V[i][j] for j in range(2)] for i in range(2)]
assert J==[[Q(-31,10),Q(13,10)],[Q(23,10),Q(-9,10)]]
detJ=J[0][0]*J[1][1]-J[0][1]*J[1][0]
trJ=J[0][0]+J[1][1]
assert detJ==Q(-1,5)
assert trJ==Q(-4)
assert detJ < 0
print('VERIFY_OK')
