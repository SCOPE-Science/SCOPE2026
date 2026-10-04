from sympy import symbols, sin, diff, simplify

x1,x2,x3,x4,a,b,c,k=symbols("x1 x2 x3 x4 a b c k", nonzero=True)
f1=a*(x2-x1)
f2=k*x1*sin(x3)+x4
f3=b-x1*x2
f4=-c*x2
H=x3+x1**2/(2*a)
Hdot=diff(H,x1)*f1+diff(H,x2)*f2+diff(H,x3)*f3+diff(H,x4)*f4
assert simplify(Hdot-(b-x1**2))==0
assert simplify(f4+c*x2)==0
assert simplify(f1-a*(x2-x1))==0
assert simplify(f3-(b-x1*x2))==0
assert simplify(2*x1*f1-2*a*(x1*x2-x1**2))==0
print("VERIFY_OK")
