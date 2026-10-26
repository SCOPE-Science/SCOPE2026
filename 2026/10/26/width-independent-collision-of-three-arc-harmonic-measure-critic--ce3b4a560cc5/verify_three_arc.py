import math, cmath
for beta,alpha in [(.3,1.3),(.3,2*math.pi/3),(.3,2.25),(.8,1.9),(.8,2.18)]:
 b=math.cos(beta); x=math.cos(alpha); a=1+2*x; B=12*b*b+4*x*x+4*x-2; q=cmath.exp(1j*alpha)
 def der(z):return sum(c/(1-2*b*c*z+c*c*z*z) for c in (1,q,q.conjugate()))
 def den(z):
  out=1
  for c in (1,q,q.conjugate()):out*=1-2*b*c*z+c*c*z*z
  return out
 def num(z):return a*(z**4+1)-4*b*a*(z**3+z)+B*z*z
 for z in (.01,.1+.13j,-.25+.3j,.6j):assert abs(den(z)*der(z)-num(z))<1e-10
 if abs(a)<1e-12: roots=[0j,0j]
 else:
  discr=16*a*(1-x)*(1+x-2*b*b)
  ts=[2*b+cmath.sqrt(discr)/(2*a),2*b-cmath.sqrt(discr)/(2*a)]
  roots=[]
  for t in ts:
   v=(t-cmath.sqrt(t*t-4))/2
   if abs(v)>1:v=1/v
   roots.append(v)
 assert all(abs(r)<1 and abs(der(r))<1e-8 for r in roots)
 print(beta,alpha,roots)
print('rational numerator identity and five critical-point cases passed')
