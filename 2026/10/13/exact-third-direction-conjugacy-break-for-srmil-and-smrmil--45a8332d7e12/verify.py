from fractions import Fraction as F

def dot(u,v):
    return sum((a*b for a,b in zip(u,v)), F(0))

def mv(A,x):
    return [sum((A[i][j]*x[j] for j in range(len(x))), F(0)) for i in range(len(A))]

def axpy(x,a,d):
    return [xi+a*di for xi,di in zip(x,d)]

A=[[F(1),F(0),F(0)],[F(0),F(2),F(0)],[F(0),F(0),F(3)]]
x=[F(1),F(1),F(1)]
g=mv(A,x)
d=[-v for v in g]
alpha0=-dot(g,d)/dot(d,mv(A,d))
x=axpy(x,alpha0,d)
g1=mv(A,x)
y=[g1[i]-g[i] for i in range(3)]
beta1=dot(g1,y)/dot(d,d)
d1=[-g1[i]+beta1*d[i] for i in range(3)]
assert alpha0 == F(7,18)
assert beta1 == F(19,324)
assert dot(g1,d) == 0
assert dot(d1,mv(A,d)) == 0

g=g1; d=d1
alpha1=-dot(g,d)/dot(d,mv(A,d))
x=axpy(x,alpha1,d)
g2=mv(A,x)
y=[g2[i]-g[i] for i in range(3)]
beta2=dot(g2,y)/dot(d,d)
d2=[-g2[i]+beta2*d[i] for i in range(3)]
assert alpha1 == F(342,581)
assert x == [F(18,83),F(-9,83),F(2,83)]
assert g2 == [F(18,83),F(-18,83),F(6,83)]
assert beta2 == F(1889568,16540489)
assert dot(g2,d) == 0
assert dot(d2,mv(A,d)) == F(-38,4067)

g=g2; d=d2
alpha2=-dot(g,d)/dot(d,mv(A,d))
x=axpy(x,alpha2,d)
g3=mv(A,x)
assert alpha2 == F(9764867,13418142)
assert x == [F(32871,9769349),F(26268,9769349),F(-15327,9769349)]
assert g3 == [F(32871,9769349),F(52536,9769349),F(-45981,9769349)]
assert dot(g3,g3) == F(5954786298,95440179883801)
assert dot(g3,g3) > 0
print("VERIFY_OK")
