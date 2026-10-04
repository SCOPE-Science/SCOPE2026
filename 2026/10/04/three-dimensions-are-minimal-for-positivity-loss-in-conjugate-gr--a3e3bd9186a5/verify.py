from fractions import Fraction as F

def dot(x,y):
    return sum((u*v for u,v in zip(x,y)), F(0))

def matvec(A,x):
    return [dot(row,x) for row in A]

def add(x,y,scale=F(1)):
    return [u+scale*v for u,v in zip(x,y)]

def cg_two(a,B):
    A=[[a,F(-1),F(0)],[F(-1),F(2),F(-1)],[F(0),F(-1),F(2)]]
    b=[F(1),F(0),B]
    x=[F(0),F(0),F(0)]
    r=b[:]
    p=r[:]
    alpha0=dot(r,r)/dot(p,matvec(A,p))
    x=add(x,p,alpha0)
    rnew=add(r,matvec(A,p),-alpha0)
    beta0=dot(rnew,rnew)/dot(r,r)
    p=add(rnew,p,beta0)
    alpha1=dot(rnew,rnew)/dot(p,matvec(A,p))
    x=add(x,p,alpha1)
    return x,alpha0,beta0,alpha1

def N(a,B):
    return ((F(4)-a)*B**4 + F(4)*B**3
            +(F(2)*a*a-F(9)*a+F(14))*B**2
            +(F(8)-F(2)*a)*B+F(2))

def Q(a,B):
    return (F(3)*B**4 + F(4)*(a-F(1))*B**3
            +(F(2)*a**3-F(10)*a*a+F(18)*a-F(10))*B**2
            +(-F(2)*a*a+F(8)*a-F(4))*B+(F(2)*a-F(1)))

def inverse_formula(a):
    den=F(3)*a-F(2)
    return [[F(3)/den,F(2)/den,F(1)/den],
            [F(2)/den,F(2)*a/den,a/den],
            [F(1)/den,a/den,(F(2)*a-F(1))/den]]

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum((A[i][q]*B[q][j] for q in range(k)),F(0))
             for j in range(m)] for i in range(n)]

I=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]

# Verify inverse and rational x2 formula on both sides of the threshold.
params=[(F(3,4),F(0)),(F(1),F(2)),(F(7,3),F(5)),
        (F(4),F(9)),(F(9,2),F(2)),(F(5),F(7)),(F(8),F(20))]
for a,B in params:
    A=[[a,F(-1),F(0)],[F(-1),F(2),F(-1)],[F(0),F(-1),F(2)]]
    inv=inverse_formula(a)
    assert matmul(A,inv)==I
    x,*_ = cg_two(a,B)
    assert Q(a,B)>0
    assert x[0]==N(a,B)/Q(a,B)

# Exact witness.
x,alpha0,beta0,alpha1=cg_two(F(5),F(7))
assert alpha0==F(50,103)
assert beta0==F(3641,10609)
assert alpha1==F(34093,75100)
assert x==[F(-5,751),F(1324,751),F(6881,1502)]

A=[[F(5),F(-1),F(0)],[F(-1),F(2),F(-1)],[F(0),F(-1),F(2)]]
b=[F(1),F(0),F(7)]
xstar=matvec(inverse_formula(F(5)),b)
assert xstar==[F(10,13),F(37,13),F(64,13)]
assert matvec(A,xstar)==b
assert all(z>0 for z in xstar)
assert x[0]<0

# Representative positivity before and at the family threshold.
for a in [F(3,4),F(1),F(2),F(4)]:
    for B in [F(0),F(1),F(3),F(10),F(100)]:
        assert N(a,B)>0
        assert cg_two(a,B)[0][0]>0

# Representative negativity beyond the threshold for large forcing.
for a,B in [(F(9,2),F(100)),(F(5),F(7)),(F(6),F(20)),(F(10),F(20))]:
    assert cg_two(a,B)[0][0]<0

print("VERIFY_OK")
