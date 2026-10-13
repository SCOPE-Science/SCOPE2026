from fractions import Fraction as F

def check(a, x, delta, sigma, tau):
    assert a > 0 and x != 0 and 0 < delta < sigma < F(1,3)
    r = 1 - tau
    assert r != 0
    # Exact scalar strong-Wolfe conditions for d0=-g0.
    armijo = tau <= 2*(1-delta)
    curvature = abs(r) <= sigma
    assert armijo and curvature
    beta_cd = r*r
    beta_nv = r*(r-abs(r))/tau
    beta_target = -r
    lo=min(beta_cd,beta_nv); hi=max(beta_cd,beta_nv)
    assert not (lo <= beta_target <= hi)
    theta=(beta_target-beta_nv)/(beta_cd-beta_nv)
    assert theta == -1/abs(r)
    assert theta < 0
    # Reconstruct conjugacy residual after the source clipping theta=0.
    g0=a*x; d0=-g0; g1=a*r*x; y=-a*tau*x
    d1=-g1+beta_nv*d0
    assert d1*y != 0

for a in [F(1),F(2),F(7,3)]:
  for x in [F(1),F(-2),F(5,4)]:
    for delta,sigma in [(F(1,1000),F(1,10)),(F(1,20),F(1,5)),(F(1,100),F(1,4))]:
      for frac in [F(1,4),F(1,2),F(3,4),F(1)]:
        e=sigma*frac
        check(a,x,delta,sigma,1-e)
        check(a,x,delta,sigma,1+e)
print("VERIFY_OK")
