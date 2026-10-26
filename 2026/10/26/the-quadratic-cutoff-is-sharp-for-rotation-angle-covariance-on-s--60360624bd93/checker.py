"""Reproduction of finite diagnostic checks for the truncated-rotation-angle theorem.
Requires Python 3 and mpmath. The universal proof is in RESULT.md.
"""
import mpmath as mp
mp.mp.dps=65

def J(n, alpha, r):
    if n == 0:
        return r**(alpha+1)/(alpha+1)
    z=mp.mpc(0,n)*r
    return mp.re(mp.exp(z)*mp.gammainc(alpha+1,0,z)/(mp.mpc(0,n)**(alpha+1)))

def J_quad(n,alpha,r):
    return mp.quad(lambda t:(r-t)**alpha*mp.cos(n*t),[0,r])

def exact_quadratic_J(n,r):
    if n==0:return r**3/3
    return 2*r/n**2 - 2*mp.sin(n*r)/n**3

checks=0
for r in [mp.pi,mp.pi/2,mp.mpf('1.31'),mp.mpf('2.27')]:
    for n in [0,1,2,3,5,10]:
        assert abs(J(n,2,r)-exact_quadratic_J(n,r))<mp.mpf('1e-48')
        assert abs(J_quad(n,2,r)-exact_quadratic_J(n,r))<mp.mpf('1e-48')
        checks+=2
    for l in range(0,70):
        assert exact_quadratic_J(l,r)-exact_quadratic_J(l+1,r)>0
        checks+=1

for alpha in [mp.mpf('0.45'),mp.mpf('1.0'),mp.mpf('1.35'),mp.mpf('1.6')]:
    for r in [mp.pi,mp.pi/2,mp.mpf('1.31'),mp.mpf('2.27')]:
        neg=[l for l in range(5,600) if J(l,alpha,r)-J(l+1,alpha,r)<0]
        assert neg, (alpha,r)
        checks+=1
        print('alpha',str(alpha),'radius',mp.nstr(r,8),'first_negative_l',neg[0],'negative_count_to_600',len(neg))

# Verifying the exact character identity by independent numeric quadrature.
for r in [mp.pi,mp.mpf('1.31')]:
 for alpha in [mp.mpf('0.7'),mp.mpf('1.4'),mp.mpf('2.0')]:
  for l in [0,1,2,5,7]:
   chi=lambda t: (2*l+1 if t==0 else mp.sin((l+mp.mpf('0.5'))*t)/mp.sin(t/2))
   lhs=mp.quad(lambda t:(r-t)**alpha*(1-mp.cos(t))*chi(t) if t<=r else mp.mpf(0),[0,r])/mp.pi
   rhs=(J(l,alpha,r)-J(l+1,alpha,r))/mp.pi
   assert abs(lhs-rhs)<mp.mpf('1e-43'),(alpha,r,l,lhs,rhs)
   checks+=1
print('PASS',checks,'finite checks; no finite test is used to certify the infinite theorem')
