import math,itertools,random,cmath

def perimeter(thetas, mask):
 n=len(thetas); ts=[0.0]
 for v in thetas:ts.append(ts[-1]+v)
 idx=[i for i in range(n) if mask&(1<<i)]
 if len(idx)<2:return 0.0
 return sum(abs(cmath.exp(1j*ts[idx[j]])-cmath.exp(1j*ts[idx[(j+1)%len(idx)]])) for j in range(len(idx)))

def formula(thetas,p):
 n=len(thetas);q=1-p; total=0
 for k in range(1,n):
  for i in range(n):
   s=sum(thetas[(i+j)%n] for j in range(k))
   total+=2*p*p*q**(k-1)*math.sin(s/2)
 return total

def brute(thetas,p):
 n=len(thetas);q=1-p
 return sum((p**(mask.bit_count()))*(q**(n-mask.bit_count()))*perimeter(thetas,mask) for mask in range(1<<n))

def max_form(n,p):
 q=1-p;alpha=math.pi/n
 return 2*n*p*p*math.sin(alpha)*(1+q**n)/(1-2*q*math.cos(alpha)+q*q)

random.seed(493102)
for n in range(3,9):
 for rep in range(5):
  v=[random.expovariate(1) for _ in range(n)]; S=sum(v);v=[2*math.pi*t/S for t in v]
  p=.13+random.random()*.82
  a=brute(v,p);b=formula(v,p);mx=max_form(n,p)
  assert abs(a-b)<1e-9,(n,a,b)
  assert a < mx -1e-11,(n,a,mx)
  reg=[2*math.pi/n]*n
  assert abs(formula(reg,p)-mx)<1e-9

n=7;p=.37;q=1-p;alpha=math.pi/n
pert=[.4,-.6,.9,-.7,.1,.3,-.4]
assert abs(sum(pert))<1e-12
reg=[2*math.pi/n]*n
kcoeff=sum(q**(k-1)*math.sin(k*alpha)*sum(sum(pert[(i+j)%n] for j in range(k))**2 for i in range(n)) for k in range(1,n))
for t in [.006,.003,.0015]:
 values=[reg[i]+t*pert[i] for i in range(n)]
 deficit=max_form(n,p)-formula(values,p)
 ratio=deficit/(p*p*t*t*kcoeff/4)
 assert abs(ratio-1)<.006,(t,ratio)
print('ALL_CHECKS_PASSED')
# Independent fixed-cardinality enumeration and spectral diagonalization.
for n in range(3,8):
 for r in range(2,n+1):
  angles=[(2*math.pi/n)*(1+.12*math.sin(j+1)) for j in range(n)]
  zz=sum(angles);angles=[2*math.pi*a/zz for a in angles]
  brute_r=sum(perimeter(angles,mask) for mask in range(1<<n) if mask.bit_count()==r)/math.comb(n,r)
  def wr(k):return (math.comb(n-k-1,r-2)/math.comb(n,r)) if 0<=r-2<=n-k-1 else 0
  exact_r=sum(2*wr(k)*sum(math.sin(sum(angles[(i+j)%n] for j in range(k))/2) for i in range(n)) for k in range(1,n))
  assert abs(brute_r-exact_r)<2e-11
for n in [5,7,9]:
 p=.37;q=1-p
 v=[math.sin(2*math.pi*(j+1)/n)+.3*math.cos(4*math.pi*(j+1)/n) for j in range(n)]
 H_direct=sum(q**(k-1)*math.sin(math.pi*k/n)*sum(sum(v[(i+j)%n] for j in range(k))**2 for i in range(n)) for k in range(1,n))
 coeff=[sum(v[j]*cmath.exp(-2j*math.pi*m*j/n) for j in range(n))/n for m in range(n)]
 H_fourier=n*sum(abs(coeff[m])**2*sum(q**(k-1)*math.sin(math.pi*k/n)*(math.sin(math.pi*k*m/n)/math.sin(math.pi*m/n))**2 for k in range(1,n)) for m in range(1,n))
 assert abs(H_direct-H_fourier)<1e-10
print('FIXED_SIZE_AND_FOURIER_CHECKS_PASSED')
