from sympy import symbols, diff, simplify
x1,x2,R1,R2,s1,s2,A3,B3 = symbols("x1 x2 R1 R2 s1 s2 A3 B3", positive=True)
f1=x1*(R1-s1*x1-A3*x2)
f2=x2*(R2-B3*x1-s2*x2)
B=1/(x1*x2)
dulac=simplify(diff(B*f1,x1)+diff(B*f2,x2))
assert simplify(dulac + s1/x2 + s2/x1)==0
C1,C2,m1,m2,M1,M2,D = symbols("C1 C2 m1 m2 M1 M2 D")
g=C1*(1-m1)*x1+C2*(1-m2)*x2-D
gamma=C1*(1-m1)*M1+C2*(1-m2)*M2-D
assert simplify((gamma-g)-(C1*(1-m1)*(M1-x1)+C2*(1-m2)*(M2-x2)))==0
print("VERIFY_OK")
