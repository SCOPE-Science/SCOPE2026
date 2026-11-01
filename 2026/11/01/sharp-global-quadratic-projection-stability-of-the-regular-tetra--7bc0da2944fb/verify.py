import math,random,itertools
random.seed(236)
C=(3-math.sqrt(3))/8
U=[tuple(s/2 for s in sg) for sg in itertools.product([-1,1],repeat=4) if sum(sg)==0]
def q(a):return max(sum(x*y for x,y in zip(a,u)) for u in U)
def ratio(a):
 v=sum(abs(x) for x in a)/2
 D=2*(1-q(a))
 return (1-v)/D if D>1e-12 else None
x=(3,-1,-1,-1);x=tuple(z/math.sqrt(12) for z in x)
print('witness',C,ratio(x),q(x),sum(abs(z) for z in x)/2)
best=(1,None)
for i in range(200000):
 a=[random.gauss(0,1) for j in range(4)]
 m=sum(a)/4
 a=[z-m for z in a]
 n=math.sqrt(sum(z*z for z in a));a=[z/n for z in a]
 r=ratio(a)
 if r is not None and r<best[0]:best=(r,a)
 if r is not None and r<C-1e-9: raise ValueError((i,r,a))
print('best random', best)
