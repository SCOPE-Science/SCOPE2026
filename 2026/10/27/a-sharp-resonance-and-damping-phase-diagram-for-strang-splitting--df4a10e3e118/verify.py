"""Independent elementary calculations for a partially damped oscillator splitting benchmark.
Only Python's standard library is required. Run: python verify.py.
"""
import math
import cmath

COUNT = 0

def close(a,b,rtol=4e-11,atol=2e-12):
    global COUNT
    COUNT+=1
    if abs(a-b)>atol+rtol*max(abs(a),abs(b)):
        raise AssertionError((a,b))

def matrix(gamma, omega, h):
    r=math.exp(-gamma*h/2)
    c=math.cos(omega*h)
    s=math.sin(omega*h)
    return ((r*r*c,-r*s),(r*s,c))

def exact_radius(gamma,omega,h):
    alpha=gamma*h/2
    r=math.exp(-alpha)
    t=abs(math.cos(omega*h))*math.cosh(alpha)
    return r if t<=1 else r*(t+math.sqrt(t*t-1))

def exact_norm(gamma,omega,h):
    r=math.exp(-gamma*h/2)
    c=math.cos(omega*h)
    tr=2*r*r+(1-r*r)**2*c*c
    det=r**4
    return math.sqrt((tr+math.sqrt(max(0.,tr*tr-4*det)))/2)

for gamma in (0.15,0.5,1.0,3.0):
 for omega in (0.75,1.0,2.0):
  for h in (0.001,0.08,0.5,1.3,2.6,4.2):
   A=matrix(gamma,omega,h)
   a,b=A[0]
   c,d=A[1]
   det=a*d-b*c
   tr=a+d
   close(det,math.exp(-gamma*h))
   disc=complex(tr*tr-4*det)
   roots=((tr+cmath.sqrt(disc))/2,(tr-cmath.sqrt(disc))/2)
   close(max(abs(z) for z in roots),exact_radius(gamma,omega,h))
   # Frobenius and determinant of A^T A independently define its largest singular value.
   frob2=a*a+b*b+c*c+d*d
   smax=math.sqrt((frob2+math.sqrt(max(0.,frob2*frob2-4*det*det)))/2)
   close(smax,exact_norm(gamma,omega,h))
   if not (smax<=1+3e-12 and exact_radius(gamma,omega,h)<=1+3e-12):
    raise AssertionError('passivity')

# Compare independent direct spectral evaluation to both analytic quadratic resonance laws.
for gamma,omega,m in ((0.5,1.0,1),(1.5,0.9,1),(2.0,1.3,2)):
 hm=m*math.pi/omega
 alpha=gamma*hm/2
 cs=0.5/math.tanh(alpha)
 cn=0.5*math.tanh(alpha)
 for delta in (0.0005,0.0002):
  h=hm+delta/omega
  kspec=(1-exact_radius(gamma,omega,h))/(delta*delta)
  knorm=(1-exact_norm(gamma,omega,h))/(delta*delta)
  if abs(kspec/cs-1)>0.015: raise AssertionError(('spectral expansion',kspec,cs))
  if abs(knorm/cn-1)>0.015: raise AssertionError(('norm expansion',knorm,cn))
  COUNT+=2

# Optimal phase plateau and sharp endpoints at fixed damping per step.
for alpha in (0.1,0.5,2,5):
 gamma=2*alpha
 omega=1
 h=1
 edge=math.acos(1/math.cosh(alpha))
 r=math.exp(-alpha)
 for angle in (edge+0.001,math.pi/2,math.pi-edge-0.001):
  close(exact_radius(gamma,angle,1),r)
 for angle in (0.25*edge,math.pi-0.25*edge):
  if exact_radius(gamma,angle,1)<=r:raise AssertionError('outside phase plateau')
  COUNT+=1

print('VERIFICATION_OK',COUNT,'deterministic assertions')
