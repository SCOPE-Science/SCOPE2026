from fractions import Fraction as F

def step(a,b,rho,z,y):
    x=(rho*z-y)/(a+rho)
    z2=(y+rho*x)/(b+rho)
    y2=y+rho*(x-z2)
    r=x-z2
    s=-rho*(z2-z)
    return x,z2,y2,r,s

def q(a,b,rho):
    return (rho*rho+a*b)/((a+rho)*(b+rho))

# Exact invariant and residual identities on a rational grid.
for a in map(F,[1,2,3,5,11]):
  for b in map(F,[1,2,4,7]):
    for rho in [F(1,3),F(2,3),F(1),F(3,2),F(5)]:
      for z0,y0 in [(F(2),F(-3)),(F(-1),F(4)),(F(3,2),F(1,5))]:
        x,z1,y1,r1,s1=step(a,b,rho,z0,y0)
        assert y1 == b*z1
        # One more step lies on the invariant manifold.
        x2,z2,y2,r2,s2=step(a,b,rho,z1,y1)
        assert y2 == b*z2
        assert rho*r2 == b*(z2-z1)
        assert z2 == q(a,b,rho)*z1
        if z2 != z1:
            assert abs(r2)/abs(s2) == b/(rho*rho)
        assert F(0) < q(a,b,rho) < F(1)

# Rationalized version of the penalty map using squared thresholds:
# low iff mu*rho^2 < b, high iff rho^2 > mu*b.
def phi_sq(b,mu,tau,rho):
    if mu*rho*rho < b:
        return tau*rho
    if rho*rho > mu*b:
        return rho/tau
    return rho

# tau <= mu: representative positive rational starts enter the deadband and freeze.
for b in [F(1),F(4),F(9)]:
  for mu,tau in [(F(10),F(2)),(F(3),F(3)),(F(5),F(4))]:
    for r0 in [F(1,100),F(1,3),F(1),F(7),F(100)]:
      r=r0
      for _ in range(100):
        r2=phi_sq(b,mu,tau,r)
        if r2==r:
          break
        r=r2
      assert phi_sq(b,mu,tau,r)==r
      assert b <= mu*r*r and r*r <= mu*b

# tau > mu: exact two-cycles. Choose b=1 and rational rho with U/tau < rho < L.
# Conditions can be checked without irrational square roots: tau^2*rho^2 > mu*b and mu*rho^2 < b.
for mu,tau,rho in [(F(2),F(3),F(1,2)),(F(3),F(4),F(1,2)),(F(5),F(6),F(2,5))]:
    b=F(1)
    assert tau*tau*rho*rho > mu*b
    assert mu*rho*rho < b
    hi=phi_sq(b,mu,tau,rho)
    assert hi==tau*rho
    assert hi*hi > mu*b
    assert phi_sq(b,mu,tau,hi)==rho

# Algebraic numerator sign for q'(rho): sample exact comparison around sqrt(ab).
for a,b in [(F(2),F(3)),(F(1),F(7)),(F(5),F(2))]:
    for rho in [F(1,10),F(1),F(3),F(10)]:
        sign_num=(a+b)*(rho*rho-a*b)
        # symmetric finite-difference direction agrees away from the minimizer on tested grid.
        h=F(1,10000)
        if rho>h and sign_num:
            diff=q(a,b,rho+h)-q(a,b,rho-h)
            assert (diff>0)==(sign_num>0)


# Coupled nonstationary penalty two-cycle: state contracts while rho alternates.
a,b,mu,tau=F(2),F(1),F(2),F(3)
rho=F(1,2)
z=F(1); y=b*z
seen=[]
for _ in range(6):
    x,z2,y2,r,s=step(a,b,rho,z,y)
    assert y2==b*z2 and z2==q(a,b,rho)*z
    assert r != 0 and s != 0 and abs(r)/abs(s)==b/(rho*rho)
    seen.append(rho)
    rho2=phi_sq(b,mu,tau,rho)
    z,y,rho=z2,y2,rho2
assert seen == [F(1,2),F(3,2),F(1,2),F(3,2),F(1,2),F(3,2)]
assert abs(z) < F(1)

print('VERIFY_OK')
