"""Numerical verification of exact clipped-square Cheeger profile.
The general proof uses the planar inner-parallel characterization; finite checks only corroborate formulas.
"""
from mpmath import mp
mp.dps = 60
ROOT_TWO=mp.sqrt(2)
T_S=mp.mpf(2)/(2+mp.sqrt(mp.pi))
R_STAR=ROOT_TWO-(ROOT_TWO-1)*T_S

def cap_area(a,b):
    if b <= a: return mp.pi*b*b
    if b >= ROOT_TWO*a: return 4*a*a
    c=mp.sqrt(b*b-a*a)
    return 4*(a*c+b*b*(mp.asin(a/b)-mp.pi/4))

def cheeger_radius(R):
    R=mp.mpf(R)
    if R >= R_STAR: return T_S
    lo=mp.mpf('0.0000001'); hi=T_S
    for _ in range(250):
        t=(lo+hi)/2
        f=cap_area(1-t,R-t)-mp.pi*t*t
        if f > 0:lo=t
        else:hi=t
    return (lo+hi)/2

def f(R,t):return cap_area(1-t,R-t)-mp.pi*t*t

assert abs(f(1,mp.mpf('.5')))<mp.mpf('1e-58')
assert abs(f(ROOT_TWO,T_S))<mp.mpf('1e-58')
assert R_STAR>1 and R_STAR<ROOT_TWO
for r in [1,mp.mpf('1.01'),mp.mpf('1.05'),mp.mpf('1.1'),mp.mpf('1.15'),R_STAR-mp.mpf('0.0001'), R_STAR,R_STAR+mp.mpf('0.01'),ROOT_TWO]:
    t=cheeger_radius(r)
    assert abs(f(r,t))<mp.mpf('1e-52')
    assert mp.mpf('.5')<=t<=T_S
    print('r',mp.nstr(r,18),'t',mp.nstr(t,18),'h',mp.nstr(1/t,18))
for delta_str in ['0.01','0.001','0.0001','0.00001','0.000001']:
    d=mp.mpf(delta_str)
    t1=cheeger_radius(1+d)
    ca=( (1+d)/2-t1 )/d**mp.mpf('1.5')
    t2=cheeger_radius(R_STAR-d)
    cb=(T_S-t2)/(d*d)
    print('delta',delta_str,'disk-excess coefficient',mp.nstr(ca,18), 'target',mp.nstr(8/(3*mp.pi),18),'square-deficit coefficient',mp.nstr(cb,18),'target',mp.nstr(1/mp.sqrt(mp.pi),18))
    assert abs(ca-8/(3*mp.pi))<mp.mpf('0.5')*mp.sqrt(d)
    assert abs(cb-1/mp.sqrt(mp.pi))<mp.mpf('1')*d

# Independent quadrature of a square intersected with a disk, away from branch cuts.
for r in [mp.mpf('1.01'),mp.mpf('1.1'),mp.mpf('1.2')]:
  t=cheeger_radius(r)
  a,b=1-t,r-t
  if a<b<ROOT_TWO*a:
      c=mp.sqrt(b*b-a*a)
      q=4*(a*c+mp.quad(lambda x:mp.sqrt(b*b-x*x),[c,a]))
      assert abs(q-cap_area(a,b))<mp.mpf('1e-40')
print('VERIFY_OK clipped-square Cheeger profile; inner area, quadrature and both asymptotic constants')
