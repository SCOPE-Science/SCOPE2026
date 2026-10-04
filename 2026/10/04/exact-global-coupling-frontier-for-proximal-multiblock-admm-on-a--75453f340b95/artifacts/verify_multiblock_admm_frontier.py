from fractions import Fraction as F

def matmul(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(q)) for j in range(m)] for i in range(n)]

def matadd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def charpoly(A):
    # Faddeev--LeVerrier: lambda^n+c1 lambda^(n-1)+...+cn
    n=len(A)
    B=eye(n)
    coeff=[F(1)]
    for j in range(1,n+1):
        AB=matmul(A,B)
        c=-trace(AB)/j
        coeff.append(c)
        B=matadd(AB, [[c*F(int(i==k)) for k in range(n)] for i in range(n)])
    return coeff

def conv(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def step(state,chi,p):
    x0,x1,x2,l0,l1=state
    d0=chi+1+1/p
    d1=-chi+2+1/p
    assert d0 != 0 and d1 != 0
    y0=(x1+l0+x0/p)/d0
    y1=(y0+x2-l0+l1+x1/p)/d1
    y2=(y1-l1+x2/p)/d0
    m0=l0+y1-y0
    m1=l1+y2-y1
    return [y0,y1,y2,m0,m1]

def matrix(chi,p):
    n=5
    cols=[]
    for j in range(n):
        e=[F(0)]*n; e[j]=F(1)
        cols.append(step(e,chi,p))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def factors(chi,p):
    d=(chi-2)*(chi+1)
    A=1+3*p-d*p*p
    b=(chi*chi-2)*p*p-3*p-3
    q=[1+(1+chi)*p, -(2+chi*p), F(1)]
    c=[A,b,F(3),F(-1)]
    prod=conv(q,c)
    lead=prod[0]
    return [x/lead for x in prod], A,b

for chi,p in [(F(1),F(1)),(F(4),F(1,20)),(F(4),F(1,10)),(F(4),F(1,5)),(F(8),F(1,1000))]:
    cp=charpoly(matrix(chi,p))
    fp,A,b=factors(chi,p)
    assert cp==fp
    d=(chi-2)*(chi+1)
    e=2*chi*chi-chi-4
    A2=A*A-1
    B2=A*b+3
    C2=3*A+b
    assert A-1 == p*(3-d*p)
    assert A2-C2 == p*p*((d*p-3)*(d*p-3)-chi)
    assert A2+B2+C2 == chi*p*p*(2+3*p-d*p*p)
    assert A2-B2+C2 == p*(d*p-3)*(e*p*p-6*p-8)

# chi=4: blockwise strong convexity extends to p<1/2.
chi=F(4)
p=F(1,10)
_,A,b=factors(chi,p)
assert A==F(6,5)
assert b==F(-79,25)
# P(r)=(6r-5)(5r^2-9r+5)/25.
assert conv([F(6),F(-5)],[F(5),F(-9),F(5)]) == [F(30),F(-79),F(75),F(-25)]
# Quadratic boundary pair has product 1, hence modulus 1.
assert F(5,5)==1

# Open gap example: p=1/5 has all block Hessians positive,
# yet the necessary Schur condition A2-C2>0 fails.
p=F(1,5)
assert 1+(2-chi)*p > 0
_,A,b=factors(chi,p)
A2=A*A-1
C2=3*A+b
assert A2-C2 < 0

print("VERIFY_OK")
