from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def inv2(A):
    a,b=A[0]; c,d=A[1]
    det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]

I=[[F(1),F(0)],[F(0),F(1)]]
T=[[F(2),F(-1)],[F(-1),F(2)]]
s=F(5,2)
t=F(2,3)*s
Rs=inv2(add(I,scale(s,T)))
Rt=inv2(add(I,scale(t,T)))
left=inv2(add(scale(F(3),I),scale(F(2)*s,T)))
form1=mm(left,add(scale(F(4),Rs),scale(F(-1),I)))
form2=add(scale(F(4),Rs),scale(F(-3),Rt))
expected=[[F(-11,1904),F(45,1904)],[F(45,1904),F(-11,1904)]]
assert form1==form2==expected
assert Rs==[[F(24,119),F(10,119)],[F(10,119),F(24,119)]]
# Exact numerator for the n=2 endpoint condition, up to a positive denominator.
p=-4*s**3+5*s**2+8*s+3
assert p<0
assert expected[0][0]<0 and expected[0][1]>0
print('VERIFY_OK')
print('R_s=',Rs)
print('F_2(5/2)=',form2)
print('endpoint_polynomial_at_5/2=',p)
