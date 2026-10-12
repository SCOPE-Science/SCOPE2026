"""Exact-symbolic checks for sharp 3-of-4 exchangeable Bernoulli bounds.
Run: python3 verify_exact.py . Requires SymPy (>= 1.10).
"""
import sympy as s

x, mu, nu, a, b = s.symbols('x mu nu a b', real=True)
R = s.Rational
f = 4*x**3 - 3*x**4
checks = 0

def equal(left, right):
    global checks
    delta = s.cancel(left-right)
    assert delta == 0, (left, right, delta)
    checks += 1

# Candidate quadratic contact polynomials and their exact factorizations.
up2 = 3*(2*mu/3-nu)**2 - 4*(2*mu/3-nu)*x + (R(4,3)+6*(2*mu/3-nu))*x**2
qcommon = b*((8-9*b)*x**2+(6*b**2-4*b)*x)
qlow = s.expand(f-3*(x-a)**2*(1-x)*(x-(R(1,3)-2*a)))
qcenter = x*(13*x-1)/12

# For a+b = 2/3, ab = 2mu/3-nu, both contacts vanish.
P = 2*mu/3-nu
b0 = R(2,3)-a
up2_as = s.expand((f+3*(x-a)**2*(x-b0)**2)-up2)
relation = a*b0-P
assert s.rem(up2_as, relation, a) == 0
checks += 1

equal(f+3*x*(x-b)**2*(x-(R(4,3)-2*b)), qcommon)
equal(f-3*x*(x-b)**2*(R(4,3)-2*b-x), qcommon)
equal(f-3*(x-a)**2*(1-x)*(x-(R(1,3)-2*a)), qlow)
equal(f-3*x*(1-x)*(x-R(1,6))**2, qcenter)

# Evaluate quadratic at prescribed first and second moments.
def moment(q, m=mu, v=nu):
    poly=s.Poly(q,x)
    assert poly.degree()<=2
    return poly.coeff_monomial(1)+poly.coeff_monomial(x)*m+poly.coeff_monomial(x*x)*v

equal(moment(up2), (4*nu+12*mu*nu-4*mu**2-9*nu**2)/3)
equal(moment(qcommon).subs(b,nu/mu), nu**2*(4*mu-3*nu)/mu**2)
equal(moment(qcenter), (13*nu-mu)/12)

# Symbolically demonstrate moment-matching for every support construction.
w_b=(mu-a)/(b-a)
equal((1-w_b)*a+w_b*b, mu)
equal(s.factor((1-w_b)*a*a+w_b*b*b-mu*(a+b)+a*b),0)

w1=(mu-a)/(1-a)
equal((1-w1)*a+w1,mu)
equal((1-w1)*a*a+w1,mu-(1-mu)*a)

w0=1-7*mu+6*nu
ws=R(36,5)*(mu-nu)
wtop=(6*nu-mu)/5
equal(w0+ws+wtop,1)
equal(ws/R(6)+wtop,mu)
equal(ws/R(36)+wtop,nu)
equal(w0*f.subs(x,0)+ws*f.subs(x,R(1,6))+wtop*f.subs(x,1),(13*nu-mu)/12)

# Three exact parameter pairs testing strictly different phases:
# (mu,nu)=(1/10,1/80): low-b regime; (2/5,19/100): central lower, low upper;
# (3/5,2/5): high lower, high upper.
def bound(m,v):
    assert 0<=m<=1 and m*m<=v<=m
    if m==0:return (R(0),R(0))
    if m==1:return (R(1),R(1))
    if v<=R(2,3)*m:
        U=(4*v+12*m*v-4*m*m-9*v*v)/3
        aa=R(1,3)-s.sqrt(v-R(2,3)*m+R(1,9))
        bb=R(1,3)+s.sqrt(v-R(2,3)*m+R(1,9))
        if aa==bb: upper={m:R(1)}
        else: upper={aa:s.simplify((bb-m)/(bb-aa)),bb:s.simplify((m-aa)/(bb-aa))}
    else:
        bb=v/m; U=v*v*(4*m-3*v)/(m*m)
        upper={0:1-m/bb,bb:m/bb}
    if v<=m/6:
        bb=v/m; L=v*v*(4*m-3*v)/(m*m)
        lower={0:1-m/bb,bb:m/bb}
    elif v<=(7*m-1)/6 and m>=R(1,6):
        aa=(m-v)/(1-m)
        lower={aa:(1-m)/(1-aa),s.Integer(1):(m-aa)/(1-aa)}
        L=sum(p*f.subs(x,z) for z,p in lower.items())
    else:
        lower={s.Integer(0):1-7*m+6*v,R(1,6):R(36,5)*(m-v),s.Integer(1):(6*v-m)/5}
        L=(13*v-m)/12
    return s.simplify(L),s.simplify(U),lower,upper

# Exact complete rational lattice test; every admissible (mu,nu) with grid spacing 1/12.
count=0
for i in range(13):
    m=R(i,12)
    for j in range(145):
        v=R(j,144)
        if v<m*m or v>m:continue
        if m in (0,1):continue
        lo,hi,lower,upper=bound(m,v)
        assert s.N(lo,16)<=s.N(hi,16)+R(1,10**12)
        for support,target in [(lower,lo),(upper,hi)]:
            assert s.simplify(sum(support.values())-1)==0
            assert s.simplify(sum(z*p for z,p in support.items())-m)==0
            assert s.simplify(sum(z*z*p for z,p in support.items())-v)==0
            assert s.simplify(sum(f.subs(x,z)*p for z,p in support.items())-target)==0
            for z,p in support.items():
                assert 0<=float(s.N(z))<=1 and float(s.N(p))>=-1e-12
            checks+=5
        count+=1

# Test distinct prior-case finite exchangeable bounds at (2/5,19/100).
m=R(2,5);v=R(19,100)
lo,hi,_,_=bound(m,v)
equal(lo,R(7747,40000))
equal(hi,R(2357,10000))
assert R(17,200)<lo<hi<R(19,50) # finite-exchangeable witnesses are strictly wider
print('PASS:',checks,'symbolic/rational checks;',count,'feasible interior rational moment pairs')
