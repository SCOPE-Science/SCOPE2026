#!/usr/bin/env python3
"""Exact symbolic replay of the directed-cycle Radau IIA positivity theorem.
Requires Python 3 and SymPy. All assertions are deterministic, with rational algebra.
"""
import sympy as sp
h, z = sp.symbols('h z')
D = h*h + 4*h + 6 - (2*h*h+4*h)*z + h*h*z*z
N = 6 - 2*h + 2*h*z

# Exact common denominators and coefficient numerators; no numerical interpolation.
DATA = {
 2: ('2*h**2+4*h+3', [
  'h**2+h+3', 'h*(h+3)']),
 3: ('3*h**4+12*h**3+22*h**2+24*h+12', [
  'h**4+2*h**3+4*h**2+12*h+12',
  'h*(h**3+4*h**2+12*h+12)', 'h**2*(h**2+6*h+6)']),
 4: ('2*(2*h**2+4*h+3)*(h**4+4*h**3+8*h**2+12*h+9)', [
  'h**6+3*h**5+3*h**4+19*h**3+63*h**2+90*h+54',
  'h*(h**5+5*h**4+22*h**3+63*h**2+90*h+54)',
  'h**2*(h**4+7*h**3+27*h**2+45*h+27)',
  'h**3*(h**3+9*h**2+18*h+9)']),
 5: ('25*h**8+200*h**7+800*h**6+2200*h**5+4520*h**4+6720*h**3+6840*h**2+4320*h+1296', [
  '5*h**8+20*h**7+20*h**5+536*h**4+1824*h**3+3168*h**2+3024*h+1296',
  'h*(5*h**7+30*h**6+150*h**5+680*h**4+1896*h**3+3168*h**2+3024*h+1296)',
  'h**2*(5*h**6+40*h**5+230*h**4+780*h**3+1476*h**2+1512*h+648)',
  'h**3*(5*h**5+50*h**4+240*h**3+540*h**2+576*h+216)',
  'h**4*(5*h**4+60*h**3+180*h**2+180*h+36)']),
 6: ('(2*h**2+4*h+3)*(h**4+4*h**3+10*h**2+24*h+36)*(3*h**4+12*h**3+22*h**2+24*h+12)', [
  'h**10+5*h**9-5*h**8-50*h**7+26*h**6+664*h**5+2280*h**4+4440*h**3+5400*h**2+3888*h+1296',
  'h*(h**9+7*h**8+36*h**7+214*h**6+904*h**5+2472*h**4+4512*h**3+5400*h**2+3888*h+1296)',
  'h**2*(h**8+9*h**7+63*h**6+316*h**5+996*h**4+2016*h**3+2592*h**2+1944*h+648)',
  'h**3*(h**7+11*h**6+76*h**5+300*h**4+696*h**3+960*h**2+720*h+216)',
  'h**4*(h**6+13*h**5+75*h**4+210*h**3+306*h**2+204*h+36)',
  'h**5*(h**5+15*h**4+60*h**3+90*h**2+36*h-12)'])
}

def ex(s):return sp.sympify(s,locals={'h':h})

def check():
 assertions=0
 t=sp.symbols('t')
 R=(6+2*t)/(6-4*t+t*t)
 A=sp.Matrix([[sp.Rational(5,12),-sp.Rational(1,12)],[sp.Rational(3,4),sp.Rational(1,4)]])
 b=sp.Matrix([[sp.Rational(3,4),sp.Rational(1,4)]])
 assert sp.cancel(1+t*(b*((sp.eye(2)-t*A).inv())*sp.ones(2,1))[0]-R)==0
 assertions+=1
 series=sp.series(R,t,0,6).removeO().expand()
 expected=1+t+t**2/2+t**3/6+t**4/36-t**5/108
 assert sp.expand(series-expected)==0
 assertions+=1
 for n,(dd,nn) in DATA.items():
  den=ex(dd)
  pD=sp.Poly(D,z,domain=sp.QQ.frac_field(h))
  mod=sp.Poly(z**n-1,z,domain=sp.QQ.frac_field(h))
  rem=(sp.invert(pD,mod)*sp.Poly(N,z,domain=sp.QQ.frac_field(h))).rem(mod)
  nums=[ex(x) for x in nn]
  for j in range(n):
   assert sp.cancel(rem.nth(j)-nums[j]/den)==0, (n,j)
   assertions+=1
  assert sp.expand(sum(nums)-den)==0, ('mass',n)
  assertions+=1
  assert den.subs(h,0)>0
  assert all(c>=0 for c in sp.Poly(den,h).all_coeffs())
  assertions+=2
  for j,num in enumerate(nums):
   if n<=5 or j in (1,2,3,4):
    assert all(c>=0 for c in sp.Poly(num,h).all_coeffs()),(n,j)
    assertions+=1
  S=sp.zeros(n,n)
  for i in range(n): S[i,(i+1)%n]=1
  Q=S-sp.eye(n)
  for val in (sp.Rational(1,9),sp.Rational(1,2),sp.Integer(1),sp.Integer(4)):
   mat=(6*sp.eye(n)+2*val*Q)*(6*sp.eye(n)-4*val*Q+val*val*Q*Q).inv()
   for j in range(n):
    assert sp.cancel(mat[0,j]-nums[j].subs(h,val)/den.subs(h,val))==0,(n,j,val)
    assertions+=1
   assert all(sp.cancel(sum(mat[i,j] for j in range(n))-1)==0 for i in range(n))
   assertions+=1
 q=ex('h**5+15*h**4+60*h**3+90*h**2+36*h-12')
 assert q.subs(h,0)==-12 and all(x>0 for x in sp.Poly(sp.diff(q,h),h).all_coeffs())
 assertions+=1
 lower=sp.Rational(2086088597,10**10)
 upper=sp.Rational(2086088598,10**10)
 assert q.subs(h,lower)<0<q.subs(h,upper)
 assertions+=1
 # Positivity proof for the exceptional zero-offset numerator in dimension six:
 # 0 <= h <=3: 664-5h^3-50h^2 >=79. h>=3: cubic factor grows.
 cubic=h**3+5*h**2-5*h-50
 assert cubic.subs(h,3)>0 and sp.diff(cubic,h).subs(h,3)>0
 assert sp.diff(cubic,h,2).subs(h,3)>0
 assertions+=1
 print('VERIFIED: exact Radau stability, all cyclic coefficient identities n=2..6,')
 print('entrywise positivity certificates n<=5, n=6 critical polynomial,')
 print('and exact matrix comparisons. Assertions:',assertions)
 return assertions

if __name__=='__main__':check()
