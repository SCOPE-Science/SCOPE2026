import sympy as sp
s=sp.sqrt(2); a=s-1; t=sp.symbols('t', real=True); u=sp.symbols('u', real=True)
C=sp.simplify((12+11*s)/8)
# Edge-interior cases: x=(1,t), |t|<=a, y=(0,+/-1)
t0=(3-2*s)/2
P_e1=sp.expand((t+2)*(3-2*t)/2)  # y=(0,1), t<=t0
assert sp.simplify(P_e1.subs(t,-sp.Rational(1,4))-sp.Rational(49,16))==0
P_e2=sp.simplify(s*(t+2))          # y=(0,1), t>=t0
assert sp.simplify(P_e2.subs(t,a)-(2+s))==0
P_e3=sp.simplify(s*(2-t))          # y=(0,-1), t<=-t0
assert sp.simplify(P_e3.subs(t,-a)-(2+s))==0
P_e4=sp.expand((2-t)*(3+2*t)/2)   # y=(0,-1), t>=-t0
assert sp.simplify(P_e4.subs(t,sp.Rational(1,4))-sp.Rational(49,16))==0
# Vertex x=(1,a): four allowed boundary segments for y.
P_v1=sp.expand((2+u)*(s+1-u)/s)    # y=(-u,1), 0<=u<=a
uc1=a/2
assert sp.simplify(sp.diff(P_v1,u).subs(u,uc1))==0
assert sp.simplify(P_v1.subs(u,uc1)-C)==0
P_v2=sp.expand((3+u-s)*(1+2*s-u)/2) # y=(u,-1), 0<=u<=a; increasing there
assert sp.simplify(sp.diff(P_v2,u).subs(u,a))>0
assert sp.simplify(P_v2.subs(u,a)-(2+s))==0
P_v3=sp.expand((2+u)*(2*s-1-u))    # y=(-u,s-u), a<=u<=s/2; decreasing
assert sp.simplify(sp.diff(P_v3,u).subs(u,a))<0
assert sp.simplify(P_v3.subs(u,a)-(2+s))==0
P_v4=sp.expand((1+u)*(3-s*u))      # y=(u,-s+u), a<=u<=s/2
uc4=sp.simplify((3-s)/(2*s))
assert sp.simplify(uc4-a)>=0 and sp.simplify(s/2-uc4)>=0
assert sp.simplify(sp.diff(P_v4,u).subs(u,uc4))==0
assert sp.simplify(P_v4.subs(u,uc4)-C)==0
# compare all subsidiary maxima with C
assert sp.simplify(C-(2+s))>0
assert sp.simplify(C-sp.Rational(49,16))>0
print('VERIFY_OK', sp.simplify(C), sp.sqrt(C))
