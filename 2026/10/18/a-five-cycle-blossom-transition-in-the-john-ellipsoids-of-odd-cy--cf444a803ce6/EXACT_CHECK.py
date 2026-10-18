"""Exact pentagon matrix/contact certificate (requires SymPy).
All identities are independently checkable from the displayed radicals."""
import sympy as s
D=s.sqrt(6)
t=(21-D)/60
a=12-2*D
b=8*D-18
c=252-102*D
r5=s.sqrt(5)
cc=[s.S(1),(r5-1)/4,-(r5+1)/4,-(r5+1)/4,(r5-1)/4]
M=s.Matrix(5,5,lambda i,j: a*int(i==j)+b*(2*int(i==j)+int((i-j)%5 in (1,4)))+c)
Q=M.inv()
q0=s.simplify(Q[0,0]);q1=s.simplify(Q[0,1])
checks=[q0-t**2,2*(q0+q1)-(1-2*t)**2,5*sum(Q[0,j] for j in range(5))-(2-5*t)**2,
    -a*t+2*b*(1-2*t)+c*(2-5*t)]
for k,z in enumerate(checks):
    assert s.simplify(s.radsimp(z))==0,(k,s.simplify(z))
assert all(float(z)>0 for z in [a,b,c,t,1-2*t,2-5*t])
assert all(float(a+b*(2+2*cc[j])+(5*c if j==0 else 0))>0 for j in range(3))
print('PASS: four exact radical support and balance identities; positive matrix and weights')
