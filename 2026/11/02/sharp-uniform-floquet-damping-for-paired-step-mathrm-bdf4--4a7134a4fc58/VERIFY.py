"""Exact coefficient, Schur-certificate, and sampling checks for paired-step BDF4."""
import sympy as S

r, t, u = S.symbols('r t u', positive=True)
h = [S.Integer(1),r,r,S.Integer(1)]

def bdf4_difference_step(i):
    offsets = [sum(h[(i-j)%4] for j in range(k)) for k in range(1,5)]
    nodes = [S.Integer(0)] + [-z for z in offsets]
    alpha = [sum(1/z for z in offsets)]
    for j in range(1,5):
        alpha.append(S.cancel(S.prod(-nodes[k] for k in range(1,5) if k!=j) /
                       S.prod(nodes[j]-nodes[k] for k in range(5) if k!=j)))
    assert S.factor(sum(alpha)) == 0
    top = [S.cancel(sum(alpha[j+1:])/alpha[0]) for j in range(1,4)]
    return S.Matrix([top,[1,0,0],[0,1,0]])

M = S.eye(3)
for i in range(4):
    M = (bdf4_difference_step(i)*M).applyfunc(S.cancel)

trace = S.factor(S.trace(M))
minor_sum = S.factor(M[0,0]*M[1,1]-M[0,1]*M[1,0]
                     +M[0,0]*M[2,2]-M[0,2]*M[2,0]
                     +M[1,1]*M[2,2]-M[1,2]*M[2,1])
det = S.factor(M.det(method='berkowitz'))
D=840*t**4+8988*t**3+35578*t**2+61702*t+39565
A=112*t**4+144*t**3-2232*t**2-6608*t-4909
B=40*t**4+180*t**3+210*t**2+62*t+95
C=(2*t+5)**2
for actual, num in [(trace,A),(minor_sum,B),(det,C)]:
    assert S.cancel(actual-num.subs(t,r+1/r)/D.subs(t,r+1/r))==0

# Strict cubic Schur tests on the disk |z|<21^(-1/2).
# For z^3+a z^2+b z+c: |c|<1, 1+a+b+c>0,
# 1-a+b-c>0, and 1-b+a*c-c*c>0.
root21=S.sqrt(21)
cert1 = D-21*root21*C
cert2 = D+21*B-root21*(A+21*C)
cert3 = D+21*B+root21*(A+21*C)
cert4 = S.factor(D*D-21*B*D+441*A*C-9261*C*C)
for p in (cert1,cert2,cert3,cert4):
    coeff = S.Poly(S.expand(p.subs(t,u+2)),u).all_coeffs()
    # 4 < sqrt(21) < 5 gives an exact rational lower bound.
    for x in coeff:
        y = S.expand(x)
        k=y.coeff(root21)
        bound=S.expand(y-k*root21+k*(S.Integer(4) if k>=0 else S.Integer(5)))
        assert bound>0,(p,x,bound)
assert S.expand(cert4-16*(273420*t**7+4574262*t**6+32337879*t**5+125193286*t**4+286533494*t**3+387470109*t**2+286403660*t+89159200))==0

z=S.symbols('z')
limpoly=S.factor(z**3-S.Rational(2,15)*z**2+S.Rational(1,21)*z)
assert S.limit(A/D,t,S.oo)==S.Rational(2,15)
assert S.limit(B/D,t,S.oo)==S.Rational(1,21)
assert S.limit(C/D,t,S.oo)==0
assert S.discriminant(limpoly/z,z)<0

# Direct exact or numerical monodromy confirmation at a range of positive ratios.
for R in (S.Rational(1,100),S.Rational(1,2),1,2,10,100):
    x=R+1/R
    expected=[float(q.subs(t,x)) for q in (A/D,B/D,C/D)]
    actual=[float(q.subs(r,R)) for q in (trace,minor_sum,det)]
    assert all(abs(a-b)<1e-12 for a,b in zip(actual,expected))
    roots=S.nroots(z**3-expected[0]*z**2+expected[1]*z-expected[2],maxsteps=100)
    assert max(abs(complex(v)) for v in roots)<float(1/root21)
print('PASS: 3 coefficient identities, 4 all-positive Schur polynomials, sharp limit, 6 ratio checks')
