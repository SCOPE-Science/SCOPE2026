import math
from scipy import integrate
alpha1=1.3; alpha2=0.8
xs=[[0.40,0.90],[0.60,1.40],[0.80,1.90]]; R=[1,0]
ys=[0.50,1.10,1.70]; S=[0,1,0]
def score1(a):
    return sum(-(1+R[j])*x+(x+1)/(a*(x+1)+1) for row in xs for j,x in enumerate(row))
def score2(a):
    return sum(-(1+s)*y+(y+1)/(a*(y+1)+1) for y,s in zip(ys,S))
def hess1(a): return -sum(((x+1)/(a*(x+1)+1))**2 for row in xs for x in row)
def hess2(a): return -sum(((y+1)/(a*(y+1)+1))**2 for y in ys)
h=1e-6
assert abs((score1(alpha1+h)-score1(alpha1-h))/(2*h)-hess1(alpha1))<1e-8
assert abs((score2(alpha2+h)-score2(alpha2-h))/(2*h)-hess2(alpha2))<1e-8
I1=-hess1(alpha1); I2=-hess2(alpha2)
assert I1>0 and I2>0
def surv(y,a): return math.exp(-a*y)/(1+y)
def pdf(y,a): return math.exp(-a*y)*(a*(y+1)+1)/(y+1)**2
def rel(a1,a2): return integrate.quad(lambda y:surv(y,a1)*pdf(y,a2),0,math.inf,epsabs=1e-12,epsrel=1e-12,limit=300)[0]
def d1(a1,a2,h=2e-5): return (rel(a1+h,a2)-rel(a1-h,a2))/(2*h)
def d2(a1,a2,h=2e-5): return (rel(a1,a2+h)-rel(a1,a2-h))/(2*h)
g=rel(alpha1,alpha2); g1=d1(alpha1,alpha2); g2=d2(alpha1,alpha2)
vc=g1*g1/I1+g2*g2/I2; vp=-vc
assert vc>0 and vp<0 and abs(vc-0.020434480354064)<5e-14
print('VERIFY_OK')
print('hessian_11',format(hess1(alpha1),'.15f'))
print('information_11_correct',format(I1,'.15f'))
print('hessian_22',format(hess2(alpha2),'.15f'))
print('information_22_correct',format(I2,'.15f'))
print('reliability_k1',format(g,'.15f'))
print('gradient',format(g1,'.15f'),format(g2,'.15f'))
print('variance_correct',format(vc,'.15f'))
print('variance_printed',format(vp,'.15f'))
