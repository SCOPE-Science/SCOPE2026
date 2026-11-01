"""Independent symbolic replay of polynomial identities used in the accompanying theorem.
Run: python check.py. Requires SymPy. This checks algebra, not historical originality."""
import sympy as S
b, s, n = S.symbols('b s n')

def numerator(m):
    q=S.Poly(S.prod(n+b+j for j in range(m+1)), n)
    f=sum(c * sum(S.functions.combinatorial.numbers.stirling(i,j,kind=2)*S.factorial(j)*s**j/(1-s)**(j+1) for j in range(i+1)) for (i,),c in q.terms())
    return S.factor(S.cancel((1-s)**(m+2)*f))

expected=[
    1-2*b,
    16*b**2*(2*b**2-1),
    -432*b**2*(b+1)**2*(2*b+1)**3*(2*b**2+2*b-3),
    7077888*b**2*(b+1)**4*(b+2)**2*(b**2+2*b+3)**2*(2*b**4+8*b**3+4*b**2-8*b-3),
    -88473600000*b**2*(b-2)**2*(b+1)**4*(b+2)**4*(b+3)**2*(b+5)**2*(2*b+3)**5*(2*b**4+12*b**3+12*b**2-18*b-5)
]
assertions=0
p=[]
for m in range(5):
    t=numerator(m); p.append(t)
    assert S.expand(t.subs(b,1)-(S.factorial(m+1)))==0
    assert S.expand(t.subs(s,1)-S.factorial(m+1))==0
    reciprocal=S.Poly(S.expand(s**(m+1)*t.subs(s,1/s)),s).as_expr()
    assert S.simplify(S.resultant(t,reciprocal,s)-expected[m])==0
    assertions+=3

q=p[4]
assert S.expand(q.subs(b,2)+120*(s-2)*(s*s-3*s+3)*(s*s-s+1))==0; assertions+=1
assert S.simplify(S.discriminant(q,s)-24883200000*b**3*(b-1)**4*(b+1)**3*(b+2)**3*(b+3)**3*(b+4)**4)==0;assertions+=1
w=(1+S.I*S.sqrt(3))/2
velocity=S.simplify(-2*S.re(S.conjugate(w)*(S.diff(q,b).subs({b:2,s:w})/S.diff(q,s).subs({b:2,s:w}))))
assert velocity==-S.Rational(49,360);assertions+=1
for B,expected_in in [(S.Rational(3,2),0),(S.Rational(199,100),0),(S.Rational(201,100),2),(S.Rational(3),2),(S.Rational(5),2),(S.Rational(50),2)]:
    roots=S.nroots(q.subs(b,B),n=20,maxsteps=200)
    actual=sum(abs(complex(r))<1-1e-8 for r in roots)
    assert actual==expected_in, (B, actual)
    assertions+=1
print(f'PASS: {assertions} exact symbolic identities and sample root-count checks')
