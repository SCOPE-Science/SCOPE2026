"""Independent symbolic reconstruction of stationary telegraph-oscillator cumulants."""
import sympy as s

k,u=s.symbols('k u', positive=True)
M={(0,0):s.Integer(1)}
L={}
for n in range(1,5):
    is_m=(n%2==0)
    names=[(i,n-i) for i in range(n+1)]
    x=s.symbols('h0:'+str(n+1))
    here={ij:z for ij,z in zip(names,x)}
    eq=[]
    for i,j in names:
        term=s.Integer(0)
        if i: term+=i*here[(i-1,j+1)]
        term-=j*here[(i,j)]
        if j: term-=k*j*here[(i+1,j-1)]
        if is_m:
            if j: term+=j*L[(i,j-1)]
        else:
            term-=u*here[(i,j)]
            if j:term+=j*M[(i,j-1)]
        eq.append(term)
    # The square generator system already contains all required identities.
    A,b=s.linear_eq_to_matrix(eq,x)

    sol=A.inv()*b
    target=M if is_m else L
    for ij,z in zip(names,sol):target[ij]=s.cancel(z)

P_x=(12-9*u)*k**2+(33+119*u+112*u**2+26*u**3)*k+18+69*u+102*u**2+72*u**3+24*u**4+3*u**5
P_v=-9*k**3+(-18+16*u+26*u**2)*k**2+(6*u+10*u**2+4*u**3+3*u**4)*k+6*u**2+9*u**3+3*u**4
H=(3+4*k)*(k+u+u**2)**2*(3*u+9*k+u**2)*(2+3*u+k+u**2)
kx=s.factor(M[(4,0)]-3*M[(2,0)]**2)
kv=s.factor(M[(0,4)]-3*M[(0,2)]**2)
assert s.cancel(M[(2,0)]-(1+u)/(k*(k+u+u**2)))==0
assert s.cancel(M[(0,2)]-u/(k+u+u**2))==0
assert s.cancel(kx+6*P_x/(k*H))==0
assert s.cancel(kv+6*u*P_v/H)==0
assert s.simplify(s.limit(kx/(M[(2,0)]**2),k,s.oo)-(3*u-4)/(2*(1+u)**2))==0
assert s.simplify(s.limit(kv/(M[(0,2)]**2),k,s.oo)-s.Rational(3,2)/u)==0
assert s.simplify(s.limit(kv/(M[(0,2)]**2),k,0)+6/(u+3))==0
assert s.simplify(s.diff(P_x/k,k)-(12-9*u)+(18+69*u+102*u**2+72*u**3+24*u**4+3*u**5)/k**2)==0
assert s.simplify(s.diff(P_v/k**2,k)+9+(6*u+10*u**2+4*u**3+3*u**4)/k**2+2*(6*u**2+9*u**3+3*u**4)/k**3)==0
for uv in (s.Rational(1,3),s.Rational(4,3),s.Rational(2),s.Rational(5)):
    for kk in (s.Rational(1,4),s.Rational(3),s.Rational(25),s.Rational(500)):
        assert s.N(kx.subs({k:kk,u:uv}),24)==s.N((-6*P_x/(k*H)).subs({k:kk,u:uv}),24)
        assert s.N(kv.subs({k:kk,u:uv}),24)==s.N((-6*u*P_v/H).subs({k:kk,u:uv}),24)
print('PASS: exact fourth-cumulant identities, limiting ratios, monotone sign polynomials, 32 rational samples')
print('At u=2: k_v=',s.nroots(P_v.subs(u,2)), 'k_x=',s.nroots(P_x.subs(u,2)))
