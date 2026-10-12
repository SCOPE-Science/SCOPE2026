from fractions import Fraction as F
from decimal import Decimal, getcontext

# Exact 2x2 identity:
# q^2-rho^2=(a-b)^2(ab-c^2)/(ab(a+b)^2).
for a,b,c in [
    (F(2),F(3),F(1)),
    (F(5),F(2),F(1)),
    (F(7),F(7),F(3)),
    (F(10),F(4),F(-2)),
]:
    assert a*b-c*c > 0
    q2=((a-b)*(a-b)+4*c*c)/(a+b)**2
    rho2=c*c/(a*b)
    rhs=(a-b)**2*(a*b-c*c)/(a*b*(a+b)**2)
    assert q2-rho2 == rhs
    assert rhs >= 0

# kappa=10 integer family: A=I+u u^T, ||u||^2=9.
u=[F(1),F(-2),F(-2)]
A=[[F(int(i==j))+u[i]*u[j] for j in range(3)] for i in range(3)]
assert A == [[F(2),F(-2),F(-2)], [F(-2),F(5),F(4)], [F(-2),F(4),F(5)]]

# (A-I)^2=9(A-I), so A has only eigenvalues 1 and 10;
# trace(A)=12 fixes multiplicities 1,1,10.
N=[[A[i][j]-F(int(i==j)) for j in range(3)] for i in range(3)]
N2=[[sum(N[i][k]*N[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert N2 == [[F(9)*N[i][j] for j in range(3)] for i in range(3)]
assert sum(A[i][i] for i in range(3)) == F(12)

# D=diag(2,5,5). Antisymmetric vector (0,1,-1) has generalized eigenvalue 1/5.
v=[F(0),F(1),F(-1)]
Av=[sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
Dv=[F(2)*v[0],F(5)*v[1],F(5)*v[2]]
assert Av == [x/F(5) for x in Dv]

# det(J)=det(A)/det(D)=10/50=1/5 and tr(J)=3.
# Removing lambda0=1/5 leaves roots with sum 14/5 and product 1,
# hence (7 +/- 2 sqrt(6))/5.
detJ=F(1,5)
lam0=F(1,5)
sum_pair=F(3)-lam0
prod_pair=detJ/lam0
assert sum_pair == F(14,5)
assert prod_pair == F(1)

getcontext().prec=60
D=Decimal
sqrt6=D(6).sqrt()
cond10=D(7)+D(2)*sqrt6
assert cond10 > D(10)

# Closed family formula: strict worsening at representative kappa values.
def jacobi_cond(k):
    k=D(str(k))
    return (D(2)*k+D(1)+D(2)*(k-D(1))*((k+D(2))/(k+D(8))).sqrt())/D(3)

for k in [1.01,1.1,2,10,100,10000]:
    assert jacobi_cond(k) > D(str(k))

# Ratio approaches 4/3 numerically.
r=jacobi_cond(1000000)/D(1000000)
assert abs(r-D(4)/D(3)) < D("0.00001")

print("VERIFY_OK")
print("kappa10_equilibrated", cond10)
print("large_kappa_ratio", r)
