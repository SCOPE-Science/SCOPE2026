"""Exact trigonometric and numerical checks for rotated two-harmonic width-2 ovals.
No third-party dependencies; finite checks corroborate the analytic classification.
"""
import math
import random

def A(theta, a, b, eps):
    return math.pi*(1 - .5*eps**2*(8*a*a*math.cos(1.5*theta)**2 + 80*b*b*math.cos(4.5*theta)**2))

def dA(theta, a, b, eps):
    return 6*math.pi*eps**2*(a*a*math.sin(3*theta)+30*b*b*math.sin(9*theta))

def h(t,a,b,eps): return 1+eps*(a*math.cos(3*t)+b*math.cos(9*t))
def rho(t,a,b,eps): return 1-eps*(8*a*math.cos(3*t)+80*b*math.cos(9*t))
def area_support(theta,a,b,eps,N=12000):
    # independent midpoint quadrature of (h^2-h'^2)/2 of rotated mean
    dt=2*math.pi/N; s=0
    for j in range(N):
        t=(j+.5)*dt
        v=.5*(h(t,a,b,eps)+h(t-theta,a,b,eps))
        prime=eps/2*(-3*a*(math.sin(3*t)+math.sin(3*(t-theta)))-9*b*(math.sin(9*t)+math.sin(9*(t-theta))))
        s+=(v*v-prime*prime)/2
    return s*dt

def run():
    rng=random.Random(4212)
    tests=0
    for a,b in [(1,0), (0,1), (1,1), (6,1), (math.sqrt(30),1), (2,1)]:
        eps=.001/(1+abs(a)+abs(b))
        for k in range(51):
            theta=(math.pi/3)*k/50
            assert abs(A(theta,a,b,eps)-area_support(theta,a,b,eps,1200))<1e-10
            assert abs(A(theta,a,b,eps)+A(math.pi/3-theta,a,b,eps)-A(0,a,b,eps)-math.pi)<1e-13
            t=2*math.pi*rng.random()
            assert rho(t,a,b,eps)>0
            assert abs(h(t,a,b,eps)+h(t+math.pi,a,b,eps)-2)<1e-13
            tests+=4
    for a,b in [(0,1),(1,1),(3,1),(math.sqrt(30),1),(6,1),(1,0)]:
        eps=.0001
        for j in range(1,400):
            theta=j*math.pi/(3*400)
            analytic=dA(theta,a,b,eps)
            exp=6*math.pi*eps**2*math.sin(3*theta)*(a*a+90*b*b-120*b*b*math.sin(3*theta)**2)
            assert abs(analytic-exp)<1e-12
            if a*a>=30*b*b: assert analytic>=-1e-15
            tests+=1
    assert dA(math.pi/6,1,1,.01)<0
    print('PASS:',tests,'support-integration, curvature, complementarity, derivative and monotonicity checks')
if __name__=='__main__':run()
