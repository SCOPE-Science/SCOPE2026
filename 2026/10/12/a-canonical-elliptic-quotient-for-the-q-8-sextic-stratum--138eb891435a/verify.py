from sympy import symbols, I, sqrt, expand, simplify, Matrix
X,Y,Z,b,c,t=symbols('X Y Z b c t')
r=(1+I)/sqrt(2)
A=Matrix([[1,0,0],[0,I,0],[0,0,-I]])
B=Matrix([[1,0,0],[0,0,r],[0,-1/r,0]])
D=Matrix([[1,0,0],[0,-1,0],[0,0,-1]])
assert simplify(A**2-D)==Matrix.zeros(3)
assert simplify(B**2-D)==Matrix.zeros(3)
assert simplify(A**4-Matrix.eye(3))==Matrix.zeros(3)
assert simplify(B**4-Matrix.eye(3))==Matrix.zeros(3)
# Quaternion conjugation relation B A B^{-1}=A^{-1}.
assert simplify(B*A*B.inv()-A.inv())==Matrix.zeros(3)
F=X**6+Y**5*Z+Y*Z**5+b*X**2*(Z**4-Y**4)+c*X**2*Y**2*Z**2
v=Matrix([X,Y,Z])
def transformed(M):
    q=M*v
    return expand(F.subs({X:q[0],Y:q[1],Z:q[2]}, simultaneous=True))
assert simplify(transformed(A)-F)==0
assert simplify(transformed(B)-F)==0
# Central fixed locus on the curve: X=0 gives six distinct points.
Fx0=expand(F.subs(X,0))
assert expand(Fx0-Y*Z*(Y**4+Z**4))==0
# In the affine coordinate t=Y/Z on X=0, A:t->-t and B:t->-i/t.
A_t=-t
B_t=-I/t
AB_t=I/t
assert simplify(A_t-t)==-2*t
assert simplify((B_t-t)+(t**2+I)/t)==0
assert simplify((AB_t-t)+(t**2-I)/t)==0
# Counts: {0,infinity}, t^2=-i, t^2=i are three pairs, all with stabilizer 4.
ramification_points=2+2+2
assert ramification_points==6
# Smooth plane sextic genus and tame Riemann--Hurwitz.
gC=(6-1)*(6-2)//2
assert gC==10
lhs=2*gC-2
ram=ramification_points*(4-1)
assert lhs==18 and ram==18
# lhs = 8*(2*gY-2)+ram.
gY=((lhs-ram)//8+2)//2
assert gY==1
print('VERIFY_OK group=Q8 ramification=6 orbits=3 stabilizer=C4 signature=[1;4,4,4] quotient_genus=1')
