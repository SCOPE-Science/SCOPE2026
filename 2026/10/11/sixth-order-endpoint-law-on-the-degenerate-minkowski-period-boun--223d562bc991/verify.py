import sympy as sp

d,s,y,t,x = sp.symbols("d s y t x", positive=True)
p=(s-d)/2
q=(s+d)/2

Up=(sp.exp(y)-1)/(q*sp.exp(y)-p)
U=sp.integrate(sp.series(Up,y,0,9).removeO(),(y,0,y))

a=sp.symbols("a1:9")
yser=sum(a[i-1]*t**i for i in range(1,9))
expr=sp.series(U.subs(y,yser),t,0,10).removeO()-t**2
sol={a[0]:sp.sqrt(2*d)}
for power in range(3,10):
    var=a[power-2]
    eq=sp.expand(expr.subs(sol)).coeff(t,power)
    roots=sp.solve(sp.Eq(eq,0),var)
    assert len(roots)==1
    sol[var]=sp.factor(roots[0])

assert sp.simplify(sol[a[2]]-sp.sqrt(2)*(3*d**2+s**2)/(72*sp.sqrt(d)))==0
assert sp.simplify(sol[a[4]]-sp.sqrt(2)*(3*d**2+s**2)**2/(17280*d**sp.Rational(3,2)))==0
assert sp.simplify(sol[a[6]] + sp.sqrt(2)*(2025*d**6+7209*d**4*s**2-477*d**2*s**4+139*s**6)/(43545600*d**sp.Rational(5,2)))==0

ws=[sol[a[0]],3*sol[a[2]],5*sol[a[4]],7*sol[a[6]]]
ks=[sp.sqrt(2)/2,-sp.sqrt(2)/4,sp.sqrt(2)/48,sp.sqrt(2)/96]
cs=[]
for N in range(4):
    c=0
    for n in range(N+1):
        m=N-n
        beta=sp.gamma(sp.Rational(2*n+1,2))*sp.gamma(sp.Rational(2*m+1,2))/sp.gamma(N+1)
        c += ws[n]*ks[m]*beta
    cs.append(sp.factor(c/d))

A=(3*d**2-12*d+s**2)/4
assert sp.simplify(cs[0]-sp.pi/sp.sqrt(d))==0
assert sp.simplify(cs[1]-sp.pi*A/(12*d**sp.Rational(3,2)))==0
assert sp.simplify(cs[2]-sp.pi*A**2/(576*d**sp.Rational(5,2)))==0

boundary={s**2:12*d-3*d**2}
c3b=sp.factor(cs[3].subs(boundary))
target_c3=sp.pi*(d-4)*(d-1)**2/(720*sp.sqrt(d))
assert sp.simplify(c3b-target_c3)==0

# Leading conversion W(E)=d log r: W(E)=2 sqrt(2d) sqrt(E)+O(E^(3/2)).
# Therefore E=(d/8)(log r)^2+O((log r)^4).
final=sp.factor(c3b*d**3/sp.Integer(512))
target=sp.pi*d**sp.Rational(5,2)*(d-4)*(d-1)**2/sp.Integer(368640)
assert sp.simplify(final-target)==0

# Off-boundary consistency with the published Li--Wan coefficient.
quad=sp.factor(cs[1]*d/sp.Integer(8))
assert sp.simplify(quad-sp.pi*A/(96*sp.sqrt(d)))==0

# Boundary zeros and sign.
assert sp.factor((d-4)*(d-1)**2).subs(d,1)==0
assert sp.factor((d-4)*(d-1)**2).subs(d,4)==0

print("VERIFY_OK")
print("inverse_series_through_t7=true")
print("boundary_c1_c2_zero=true")
print("boundary_c3=pi*(d-4)*(d-1)^2/(720*sqrt(d))")
print("final_log_coefficient=pi*d^(5/2)*(d-4)*(d-1)^2/368640")
print("published_quadratic_consistency=true")
