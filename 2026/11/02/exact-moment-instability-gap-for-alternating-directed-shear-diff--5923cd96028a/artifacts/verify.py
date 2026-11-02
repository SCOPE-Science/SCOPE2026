"""Independent finite checks for the alternating-shear diffusion formulas.

Uses only the Python standard library. Run: python artifacts/verify.py
"""
from fractions import Fraction as F
from math import sqrt

checks = 0


def check(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)


def denominator(a,b,q):
    return 4*a*a*(a+q)-b*b*q


def covariance_parts(a,b,q,D):
    h=denominator(a,b,q)
    return (D*(2*a*(a+q)+b*b)/h,
            2*D*a*(a+q)/h,
            D*b*(a+q)/h)


def matrix(a,b,q):
    return ((-2*a-q, q, 2*b),
            (q,-2*a-q,0),
            (0,b,-2*a))


def matvec(A,v):
    return tuple(sum(t*x for t,x in zip(row,v)) for row in A)


def det3(A):
    a,b,c=A[0]
    d,e,f=A[1]
    g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

# Exact rational verification of the stationary generator equations,
# characteristic polynomial and threshold inequalities.
for a in [F(1,2),F(1),F(3,2),F(2)]:
    for b in [F(1),F(2),F(3),F(5),F(7)]:
        for q in [F(1,10),F(1,2),F(4,5),F(1),F(3,2),F(5)]:
            for D in [F(1,3),F(1),F(2)]:
                h=denominator(a,b,q)
                M=matrix(a,b,q)
                check(det3(M)==-2*h,'determinant')
                # Evaluate characteristic polynomial at four distinct points.
                for lam in (F(-3),F(0),F(1),F(4)):
                    A=tuple(tuple((lam if i==j else F(0))-M[i][j]
                                  for j in range(3)) for i in range(3))
                    poly=(lam**3+2*(3*a+q)*lam**2+
                          4*a*(3*a+2*q)*lam+2*h)
                    check(det3(A)==poly,'characteristic polynomial')
                routh=2*(32*a**3+32*a*a*q+8*a*q*q+b*b*q)
                check(routh>0,'positive Routh expression')
                if h != 0:
                    u,v,w=covariance_parts(a,b,q,D)
                    f=matvec(M,(u,v,w))
                    check(f[0]+D==0 and f[1]+D==0 and f[2]==0,'moment balance')
                    if h>0:
                        K=u+v; C=2*w
                        check(K>0 and K*K>C*C,'positive definite covariance')
                        check(K==D*(4*a*(a+q)+b*b)/h,'marginal variance')
                        check(C==2*b*D*(a+q)/h,'cross covariance')

# Exact critical-rate comparison, strictly nonempty instability gap.
for a in [F(1,2),F(1),F(2),F(3)]:
    for b in [2*a+F(1,3),3*a,5*a,10*a]:
        q2=4*a**3/(b*b-4*a*a)
        q1=a*a/(b-2*a)
        check(q2>0 and q1>q2, 'moment gap')
        check(q1-q2==a*a/(b+2*a),'gap width')
        check(denominator(a,b,q2)==0,'critical variance denominator')
        check(denominator(a,b,q2/2)>0,'stable below boundary')
        check(denominator(a,b,(q2+q1)/2)<0,'unstable before mean threshold')
        check((q2+q1)/2*(b-2*a)<a*a,'mean stable in gap')



# Critical covariance orientation: null right eigenvector and exact ratio.
for a in [F(1,2),F(1),F(2)]:
    for b in [3*a,4*a,7*a]:
        q=4*a**3/(b*b-4*a*a)
        v=(2*a*(a+q)+b*b, 2*a*(a+q), b*(a+q))
        check(matvec(matrix(a,b,q),v)==(0,0,0),'critical null direction')
        check(2*v[2]/(v[0]+v[1])==2*a/b,'critical correlation')


def rhs(y, a, b, q, D):
    u,v,w=y
    return (-(2*a+q)*u+q*v+2*b*w+D,
            q*u-(2*a+q)*v+D,
            b*v-2*a*w)


def integrate(a,b,q,D,T,dt=0.02):
    n=round(T/dt)
    y=(0.0,0.0,0.0)
    for _ in range(n):
        k1=rhs(y,a,b,q,D)
        k2=rhs(tuple(y[i]+dt*k1[i]/2 for i in range(3)),a,b,q,D)
        k3=rhs(tuple(y[i]+dt*k2[i]/2 for i in range(3)),a,b,q,D)
        k4=rhs(tuple(y[i]+dt*k3[i] for i in range(3)),a,b,q,D)
        y=tuple(y[i]+dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))
    return y

# A stable covariance, a critical linear growth and an unstable exponential
# increase. These finite numerical tests are diagnostics, not asymptotic proofs.
a,b,D=1.0,3.0,1.0
stable=integrate(a,b,0.5,D,100)
Kstable=stable[0]+stable[1]
check(abs(Kstable-10)<1e-5,'stable limiting variance')
critical1=integrate(a,b,0.8,D,100)
critical2=integrate(a,b,0.8,D,200)
V1=critical1[0]+critical1[1]
V2=critical2[0]+critical2[1]
check(V2>V1*1.8,'critical linear divergence')
unstable1=integrate(a,b,0.9,D,70)
unstable2=integrate(a,b,0.9,D,140)
check(unstable2[0]+unstable2[1]>4*(unstable1[0]+unstable1[1]),
      'exponential second-moment growth')
for q in (0.5,0.8,0.9,1.0,1.2):
    eigmean=-a-q+sqrt(q*(q+b))
    check((eigmean<0)==(q<1), 'first moment threshold for a=1,b=3')

print('VERIFY_OK', checks, 'finite checks; the theorem needs the separate analytic proof')
