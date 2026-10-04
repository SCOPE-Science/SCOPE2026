import sympy as s
X,h,H,u,y,t=s.symbols('X h H u y t', nonnegative=True)
phi2=X**2+2*(H**2-h**2)*X+(h**2+H**2)**2
assert s.expand(phi2-(X+H**2-h**2)**2-4*H**2*h**2)==0
F=(u**2+y+2*H**2)/(2*s.sqrt((u**2+H**2)*(y+H**2)))
assert s.simplify(s.diff(F,y)-(y-u**2)/(4*s.sqrt(u**2+H**2)*(y+H**2)**s.Rational(3,2)))==0
G=(u**2+2*H**2)/(2*H*s.sqrt(u**2+H**2))
assert s.simplify(s.diff(G,u)-u**3/(2*H*(u**2+H**2)**s.Rational(3,2)))==0
Q=(t**2+2)/(2*s.sqrt(t**2+1))
assert s.simplify((1+t**2/4)-Q**2-t**2/(4*(t**2+1)))==0
print('VERIFY_OK')
