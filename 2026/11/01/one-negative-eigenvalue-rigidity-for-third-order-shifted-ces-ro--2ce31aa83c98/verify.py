"""Reproduce exact finite Gram identities for the third-order Cesàro defect.
The universal theorem requires the analytical argument in RESULT.md.
"""
from fractions import Fraction as F

a=F(-1,2)
D=lambda t:(t+4)*(t+5)*(t+6)
H=lambda t:(t+1)*(t+2)*(t+3)
poly=lambda x,z:3*(z+1)*(z+2)-24*x*(z+1)+30*x*(x-1)
ncols=7
B=[[F(0) for _ in range(ncols)] for _ in range(ncols+3)]
for j in range(ncols):
    t=F(j)+a
    for i in range(j+3):
        B[i][j]=poly(F(i)+a,t)/D(t)
    B[j+3][j]=-H(t)/D(t)
vs=[]
for j in range(ncols):
    t=F(j)+a; denom=D(t)
    p0=(t+1)*(t+2)+4*(1-a)*(t+1)+F(10,3)*(1-a)*(2-a)
    p1=t+1+F(5,4)*(2-a)
    vs.append((p0/denom,p1/denom,1/denom))
lam=(9*a,48*a*(a*a-1),5*a*(a*a-1)*(a*a-4))
for i in range(ncols):
    for j in range(ncols):
        gram=F(i==j)-sum(B[k][i]*B[k][j] for k in range(ncols+3))
        defect=F(i==j)*(1-H(F(i)+a)/D(F(i)+a))+sum(lam[r]*vs[i][r]*vs[j][r] for r in range(3))
        assert gram==defect,(i,j,gram,defect)

N=100
r_total=F(0)
v_total=[F(0)]*3
weighted=F(0)
for n in range(N):
    t=F(n)+a; denom=D(t); h=H(t); r=1-h/denom
    p0=(t+1)*(t+2)+4*(1-a)*(t+1)+F(10,3)*(1-a)*(2-a)
    p1=t+1+F(5,4)*(2-a)
    vn=(p0/denom,p1/denom,1/denom)
    r_total+=r
    for j in range(3):v_total[j]+=vn[j]
    weighted+=vn[2]*vn[2]/r
qform=r_total+sum(lam[j]*v_total[j]*v_total[j] for j in range(3))
assert qform<0
assert abs(lam[2])*weighted<F(1,72)
print('PASS 49 exact rational Gram entries; negative quadratic witness and strict rank-one domination')
