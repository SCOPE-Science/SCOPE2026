"""Final self-checks: trace, hand-sum for P*, stationary normalization."""
from fractions import Fraction
import numpy as np
P=np.zeros((8,8))
P[0,0]=0.75; P[0,1]=0.25
for i in range(1,7):
    P[i,i-1]=0.75; P[i,i+1]=0.25
P[7,6]=0.25; P[7,7]=0.75
eig=np.linalg.eigvals(P)
print("trace P:", np.trace(P), "sum eig:", np.sum(eig))
print("det check via prod eig:", np.prod(eig), "det P:", np.linalg.det(P))
# hand sum d_i = 2*3^{i+1}-2
ds=[2*3**(i+1)-2 for i in range(7)]
print("hand d:", ds, "sum:", sum(ds))
assert sum(ds)==6544
# recursion Fractions for P*
p=[Fraction(1,4)]*7; q=[Fraction(0,1)]+[Fraction(3,4)]*6
d=Fraction(1,1)/p[0]; tot=d; seq=[d]
for i in range(1,7):
    d=(Fraction(1,1)+q[i]*d)/p[i]; tot+=d; seq.append(d)
print("fraction d:", seq, "sum:", tot)
assert tot==6544
# stationary closed form: pi_i proportional to 3^{-i} for i<=6? pi0*(1/3)^i, pi7=pi6
# unnormalized: [1,1/3,...,1/3^6,1/3^6]; normalize
w=[Fraction(3)**(-i) if i<=6 else Fraction(3)**(-6) for i in range(8)]
# as floats
s=sum(float(x) for x in w)
print("closed-form pi:", [float(x)/s for x in w])
