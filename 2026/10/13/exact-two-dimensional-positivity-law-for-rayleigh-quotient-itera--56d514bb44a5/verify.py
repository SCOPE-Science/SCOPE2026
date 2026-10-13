from fractions import Fraction as F

def solve2(M,b):
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert det != 0
    return [(M[1][1]*b[0]-M[0][1]*b[1])/det,(-M[1][0]*b[0]+M[0][0]*b[1])/det],det
A=[[F(1),F(-1)],[F(-1),F(2)]]
x=[F(1),F(4)]
assert A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]*A[1][0]==1
Ax=[sum(A[i][j]*x[j] for j in range(2)) for i in range(2)]
mu=sum(x[i]*Ax[i] for i in range(2))/sum(v*v for v in x)
assert mu==F(25,17) and mu<F(3,2)
B=[[A[i][j]-(mu if i==j else F(0)) for j in range(2)] for i in range(2)]
y,det=solve2(B,x)
assert det==F(-361,289) and y==[F(-1309,361),F(255,361)] and y[0]<0<y[1]
for l1,l2,t in [(F(1),F(3),F(1,2)),(F(2),F(7),F(-2,3)),(F(-1),F(5),F(3,4)),(F(4),F(9),F(-1,5))]:
    m=(l1+l2*t*t)/(1+t*t)
    tp=(t/(l2-m))/(F(1)/(l1-m))
    assert tp==-t*t*t
print('VERIFY_OK')
