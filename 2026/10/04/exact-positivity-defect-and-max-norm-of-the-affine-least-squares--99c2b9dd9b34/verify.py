from fractions import Fraction as F
from math import comb

def matmul(A,B):
    n=len(A); m=len(B); p=len(B[0])
    return [[sum((A[i][k]*B[k][j] for k in range(m)), F(0))
             for j in range(p)] for i in range(n)]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def exact_C_by_integral(d):
    # d(d+1) int_0^a (1-(d+2)t)(1-t)^(d-1) dt
    # with a=1/(d+2), expanded exactly.
    a=F(1,d+2)
    total=F(0)
    for k in range(d):
        coeff=F(((-1)**k)*comb(d-1,k))
        # t^k - (d+2)t^(k+1)
        total += coeff * (
            a**(k+1)/F(k+1)
            - F(d+2)*a**(k+2)/F(k+2)
        )
    return F(d*(d+1))*total

for d in range(1,51):
    n=d+1
    den=F(1,(d+1)*(d+2))
    G=[[den*(2 if i==j else 1) for j in range(n)] for i in range(n)]
    scale=F((d+1)*(d+2))
    Gi=[[scale*((F(1) if i==j else F(0))-F(1,d+2))
         for j in range(n)] for i in range(n)]
    assert matmul(G,Gi)==eye(n)
    assert matmul(Gi,G)==eye(n)

    # Kernel normalization: first barycentric moments are 1/(d+1).
    # K=(d+1)[(d+2) a·b -1] at |T|=1.
    # Integrating over b yields one for every barycentric a.
    for a in ([F(1)]+[F(0)]*d,
              [F(1,n)]*n):
        integral=F(d+1)*(
            F(d+2)*sum(a_i*F(1,d+1) for a_i in a)-F(1)
        )
        assert integral==1

    C1=exact_C_by_integral(d)
    C2=F(d+1)*F(d+1,d+2)**d-F(1)
    assert C1==C2
    assert C1>0

    norm=F(1)+2*C1
    assert norm==2*F(d+1)*F(d+1,d+2)**d-F(1)

assert exact_C_by_integral(1)==F(1,3)
assert exact_C_by_integral(2)==F(11,16)
assert exact_C_by_integral(3)==F(131,125)
assert F(1)+2*exact_C_by_integral(1)==F(5,3)
assert F(1)+2*exact_C_by_integral(2)==F(19,8)
assert F(1)+2*exact_C_by_integral(3)==F(387,125)

# Strictly positive perturbation threshold: value = eps-(1-eps)C.
for d in range(1,15):
    C=exact_C_by_integral(d)
    eps=C/(2*(1+C))
    val=eps-(1-eps)*C
    assert eps>0 and val<0

print("VERIFY_OK")
