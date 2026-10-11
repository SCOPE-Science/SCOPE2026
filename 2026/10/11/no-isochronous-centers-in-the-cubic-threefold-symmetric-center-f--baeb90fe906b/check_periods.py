"""Exact Fourier certificate for local period coefficients in a cubic reversible center.
Run with SymPy. Rational symbolic identities, not sampled numerical evidence.
"""
import collections
import sympy as s

I=s.I
a,b,c=s.symbols('a b c', real=True)

def expand(p):
    return {k:s.expand(v) for k,v in p.items() if v != 0}

def add(*parts):
    out=collections.defaultdict(lambda:s.Integer(0))
    for p in parts:
        for k,v in p.items():out[k]+=v
    return expand(out)

def product(*parts):
    out={0:s.Integer(1)}
    for p in parts:
        nxt=collections.defaultdict(lambda:s.Integer(0))
        for j,v in out.items():
            for k,w in p.items():nxt[j+k]+=v*w
        out=expand(nxt)
    return out

def times(p,k):return expand({n:k*v for n,v in p.items()})
def power(p,n):return product(*([p]*n)) if n else {0:s.Integer(1)}

def primitive(p):
    assert s.simplify(p.get(0,0)) == 0, 'unexpected secular radial term'
    out={j:val/(I*j) for j,val in p.items() if j}
    out[0]=-sum(out.values())
    return expand(out)

def circle_integral(p):return 2*s.pi*s.expand(p.get(0,0))

C={1:s.Rational(1,2),-1:s.Rational(1,2)}
S={1:1/(2*I),-1:-1/(2*I)}
R2=add(times(product(power(C,2),S),a+1),times(power(S,3),2))
R3=add(times(product(power(C,3),S),b),times(product(C,power(S,3)),c+2))
H1=add(power(C,3),times(product(C,power(S,2)),2-a))
H2=add(times(product(power(C,2),power(S,2)),2-b),times(power(S,4),-c))
B2=add(power(H1,2),times(H2,-1))
B3=add(times(power(H1,3),-1),times(product(H1,H2),2))
B4=add(power(H1,4),times(product(power(H1,2),H2),-3),power(H2,2))
S3=add(R3,times(product(R2,H1),-1))
S4=add(product(R2,B2),times(product(R3,H1),-1))
u2=primitive(R2)
u3=primitive(add(times(product(u2,R2),2),S3))
u4=primitive(add(product(add(times(u3,2),power(u2,2)),R2),times(product(u2,S3),3),S4))
T2=circle_integral(add(times(product(u2,H1),-1),B2))
T3=circle_integral(add(times(product(u3,H1),-1),times(product(u2,B2),2),B3))
T4=circle_integral(add(times(product(u4,H1),-1),product(add(times(u3,2),power(u2,2)),B2),times(product(u2,B3),3),B4))

q=a*a-11*a+3*b+9*c+40
expected2=s.pi*q/12
expected3=s.pi*(a+5)*q/18
expected4=s.pi*(49*a**4-310*a**3+198*a*a*b+546*a*a*c+537*a*a+30*a*b+954*a*c+320*a+153*b*b+630*b*c+7008*b+945*c*c+12720*c+49120)/1152
for got,exp in [(T2,expected2),(T3,expected3),(T4,expected4)]:
    assert s.simplify(got-exp)==0,(got,exp)

A,D=s.symbols('A D',real=True)
source_parameters={a:-3*A-D-s.Rational(5,3),b:-2*A-D-s.Rational(2,3),c:D}
assert s.simplify((b-(2*a-c)/3-s.Rational(4,9)).subs(source_parameters))==0
source_t2=s.factor((T2/s.pi).subs(source_parameters))
assert s.simplify(source_t2-(81*A*A+54*A*D+333*A+9*D*D+183*D+532)/108)==0
center_relation={b:(2*a-c)/3+s.Rational(4,9)}
zero_quadratic={c:-(a*a-9*a+s.Rational(124,3))/8}
reduction=lambda v:s.factor(s.cancel(s.expand((v/s.pi).subs(center_relation).subs(zero_quadratic))))
assert reduction(T2)==0
assert reduction(T3)==0
Q=3*a**4-46*a**3+1147*a*a+6416*a+69904
assert s.simplify(reduction(T4)-Q/4608)==0
sos=3*(a*a-s.Rational(23,3)*a)**2+s.Rational(2912,3)*(a+s.Rational(1203,364))**2+s.Rational(5396458,91)
assert s.expand(Q-sos)==0
assert s.Rational(5396458,91)>0
example={A:s.Rational(7,6), D:-s.Rational(31,6)}
assert s.simplify(source_t2.subs(example))==0
assert s.simplify(reduction(T4).subs(a,0)-s.Rational(69904,4608))==0
print('CHECK_OK')
