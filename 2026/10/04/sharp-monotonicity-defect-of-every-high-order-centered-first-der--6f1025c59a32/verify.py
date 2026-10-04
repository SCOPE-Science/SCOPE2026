from fractions import Fraction as F
from math import factorial

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0))

def alpha(m,j):
    return F(((-1)**(j+1))*factorial(m)*factorial(m),
             j*factorial(m-j)*factorial(m+j))

def weights(m):
    c={0:F(0)}
    for j in range(1,m+1):
        a=alpha(m,j)
        c[j]=a
        c[-j]=-a
    return c

for m in range(1,41):
    c=weights(m)

    # Exactness through degree 2m.
    for p in range(0,2*m+1):
        lhs=sum(c[j]*F(j)**p for j in range(-m,m+1))
        rhs=F(1) if p==1 else F(0)
        assert lhs==rhs

    # Positive-side magnitudes strictly decrease.
    for j in range(1,m):
        assert abs(alpha(m,j+1)) < abs(alpha(m,j))

    S=sum((alpha(m,j) for j in range(1,m+1)), F(0))
    assert S == harmonic(2*m)-harmonic(m)

    if m==1:
        assert S==F(1,2)
        continue

    A={}
    for q in range(1,m+1):
        A[q]=sum((alpha(m,j) for j in range(q,m+1)), F(0))
        if q%2:
            assert A[q] > 0
        else:
            assert A[q] < 0

    neg=[(v,q) for q,v in A.items() if v<0]
    assert min(neg)[1] == 2

    V=F(m,m+1)-(harmonic(2*m)-harmonic(m))
    assert V>0 and A[2]==-V

    # Right-side step: y_j=0 for j<=1, y_j=1 for j>=2.
    y={j:(F(0) if j<=1 else F(1)) for j in range(-m,m+1)}
    D=sum(c[j]*y[j] for j in range(-m,m+1))
    assert D==-V

    # Reflected step: y_j=0 for j<=-2, y_j=1 for j>=-1.
    y2={j:(F(0) if j<=-2 else F(1)) for j in range(-m,m+1)}
    D2=sum(c[j]*y2[j] for j in range(-m,m+1))
    assert D2==-V

    if m<40:
        Vnext=F(m+1,m+2)-(harmonic(2*m+2)-harmonic(m+1))
        assert Vnext>V

# Independent check of the first nontrivial rule.
assert alpha(2,1)==F(2,3)
assert alpha(2,2)==-F(1,12)
assert F(2,3)-F(1,12)-F(2,3)==-F(1,12)

print("VERIFY_OK")
