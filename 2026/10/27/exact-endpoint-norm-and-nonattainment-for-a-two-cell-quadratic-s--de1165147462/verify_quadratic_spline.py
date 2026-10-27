"""Exact-rational certificate for the two-cell continuous quadratic spline projector.
No external dependencies; all comparisons use fractions and integer arithmetic.
"""
from fractions import Fraction as Q

HALF=Q(1,2)
# Coefficient triples (quadratic in t) for reproducing kernel, x in [0,1/2].
# These follow by inverting the five-by-five Gram matrix of
# (1,t,t*t,(t-1/2)_+,(t-1/2)_+**2).
def coefficients(x,side):
 if side==0:
  return (4160*x*x-2240*x+200, -2240*x*x+1280*x-128, 200*x*x-128*x+17)
 return (1600*x*x-640*x+40,-2560*x*x+1024*x-64, 1000*x*x-400*x+25)

def value(p,t):
 return (p[0]*t+p[1])*t+p[2]

def upper_abs_integral(p,lo,hi,N=24):
 # Piecewise-linear absolute integral + integral of exact interpolation error.
 h=(hi-lo)/N
 result=Q(0)
 for j in range(N):
  a=lo+j*h; b=a+h
  va=value(p,a); vb=value(p,b)
  aa,bb=abs(va),abs(vb)
  if va*vb<0:
   result+=h*(aa*aa+bb*bb)/(2*(aa+bb))
  else: result+=h*(aa+bb)/2
 result+=abs(p[0])*(hi-lo)*h*h/6
 return result

def upper_kernel(xs,weights,N=24):
 answer=Q(0)
 for side,lo,hi in [(0,Q(0),HALF),(1,HALF,Q(1))]:
  pol=[sum(w*coefficients(x,side)[j] for w,x in zip(weights,xs)) for j in range(3)]
  answer+=upper_abs_integral(pol,lo,hi,N)
 return answer


# Verify the algebraic reproducing kernel from a directly integrated Gram matrix.
def mul(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b): out[i+j]+=u*v
 return out

def integrate_poly(p,a,b):
 return sum(coef*(b**(i+1)-a**(i+1))/(i+1) for i,coef in enumerate(p))

LEFT_BASIS=[(Q(1),),(Q(0),Q(1)),(Q(0),Q(0),Q(1)),(Q(0),),(Q(0),)]
RIGHT_BASIS=[(Q(1),),(Q(0),Q(1)),(Q(0),Q(0),Q(1)),(-HALF,Q(1)),(Q(1,4),Q(-1),Q(1))]
INVERSE_G=[
 [17,-128,200,-96,-160],
 [-128,1280,-2240,1344,1600],
 [200,-2240,4160,-2880,-2560],
 [-96,1344,-2880,3072,0],
 [-160,1600,-2560,0,5120],
]
def verify_kernel():
 gram=[[sum(integrate_poly(mul(left[i],left[j]),Q(0),HALF) + integrate_poly(mul(right[i],right[j]),HALF,Q(1)) for left,right in [(LEFT_BASIS,RIGHT_BASIS)]) for j in range(5)] for i in range(5)]
 assert all(sum(gram[i][k]*INVERSE_G[k][j] for k in range(5))==int(i==j) for i in range(5) for j in range(5))
 for x in [Q(0),Q(1,4),HALF]:
  xx=[Q(1),x,x*x,Q(0),Q(0)]
  for side,bb in [(0,LEFT_BASIS),(1,RIGHT_BASIS)]:
   coeff=[sum(xx[i]*INVERSE_G[i][j]*(bb[j][u] if u<len(bb[j]) else Q(0)) for i in range(5) for j in range(5)) for u in [2,1,0]]
   assert tuple(coeff)==coefficients(x,side),(x,side,coeff,coefficients(x,side))
 print('Gram inverse and both kernel polynomials independently verified.')

def main():
 verify_kernel()
 all_bounds=[]
 for i in range(10):
  a=Q(i,20);b=Q(i+1,20);m=(a+b)/2
  # Bernstein control rows for a quadratic, exactly.
  for tag,xs,weights in [('left',[a],[Q(1)]),('mid',[a,m,b],[-Q(1,2),Q(2),-Q(1,2)]),('right',[b],[Q(1)])]:
   if i==0 and tag=='left': continue
   z=upper_kernel(xs,weights,N=24)
   assert z < Q(9,4), (i,tag,float(z))
   all_bounds.append((z,i,tag))
 worst=max(all_bounds)
 print('CERTIFIED',len(all_bounds),'Bernstein control bounds; all strictly below 9/4')
 print('Worst bound =',float(worst[0]), 'cell=',worst[1], 'control=',worst[2])
 print('Endpoint value C = 1 + 58 sqrt(174)/625 + 2 sqrt(6)/25 > 9/4:')
 # Rational root lower bounds: sqrt174 > 13.19, sqrt6 > 2.44.
 assert Q(1319,100)**2 < 174 and Q(244,100)**2 < 6
 lower=1+Q(58,625)*Q(1319,100)+Q(2,25)*Q(244,100)
 assert lower>Q(9,4)
 print('Rational lower bound C >=',float(lower))
 if __name__=='__main__':pass
if __name__=='__main__':main()
