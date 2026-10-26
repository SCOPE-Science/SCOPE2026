"""Finite numerical diagnostics for geodesic S^3 Schoenberg coefficients."""
import cmath, math, random
PI=math.pi

def abc(a,w,e):
 z=complex(a,-w); beta=z*(1-e*cmath.exp(-PI*z))
 return beta.real,2*(beta*(z.conjugate()**2-1)).real,(beta*(z.conjugate()**2+1)**2).real

def p(c,x):
 A,B,C=c;return (A*x+B)*x+C

def test(a,w):
 for e,k0 in ((1,1),(-1,2)):
  c=abc(a,w,e);A,B,_=c
  if A<0:return False
  if A==0:
   if B<0 or p(c,k0*k0)<0:return False
  else:
   v=-B/(2*A)
   if v<=k0*k0:ks=[k0]
   else:
    j=math.floor((math.sqrt(v)-k0)/2);ks=[k0+2*j,k0+2*j+2]
   if any(p(c,k*k)<0 for k in ks):return False
 return True

def coef(a,w,n):
 z=complex(a,-w);D=(z*z+n*n)*(z*z+(n+2)**2)
 return 4*(n+1)**2/PI*(z*(1-(-1)**n*cmath.exp(-PI*z))/D).real

def simpson(a,w,n,N=3000):
 def f(t):return math.exp(-a*t)*math.cos(w*t)*math.sin(t)*math.sin((n+1)*t)
 h=PI/N;v=f(0)+f(PI)
 for j in range(1,N):v+=(4 if j%2 else 2)*f(j*h)
 return 2*(n+1)/PI*h*v/3

def main():
 samples=[(.5,.1),(.5,1),(.2,2),(2,2),(3,2),(.9,5),(30,10),(.005,1.2)]
 for a,w in samples:
  for n in (0,1,2,7,13):assert abs(coef(a,w,n)-simpson(a,w,n))<2e-8
 rng=random.Random(1729)
 for _ in range(500):
  a=10**rng.uniform(-1,1.4);w=rng.uniform(.01,14)
  accepted=test(a,w);negative=any(coef(a,w,n)<-1e-11 for n in range(900))
  if accepted:assert not negative
  else:
   if abc(a,w,1)[0]>=0 and abc(a,w,-1)[0]>=0:assert negative
 for m in range(2,12):
  t=math.sqrt(3*m*m-4)
  assert not test(t*.99,float(m))
  assert test(t*1.01,float(m))
 print('PASS: 40 quadratures, 500 finite comparisons, 20 threshold-side checks')

if __name__=='__main__':main()
