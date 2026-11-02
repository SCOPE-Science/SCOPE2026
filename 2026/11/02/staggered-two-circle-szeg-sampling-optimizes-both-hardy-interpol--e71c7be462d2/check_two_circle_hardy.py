"""Finite numerical consistency tests for two-circle normalized Hardy kernels.

Run with Python 3 standard library. The all-degree statements rely on the
analytical proof; these tests check the explicit finite algebra.
"""
import cmath
import math

COUNT = 0

def near(a, b, rel=4e-10, abs_tol=4e-12):
    global COUNT
    COUNT += 1
    if abs(a-b) > abs_tol+rel*max(abs(a),abs(b)):
        raise AssertionError(f"{a!r} differs from {b!r}")

def require(v, message):
    global COUNT
    COUNT += 1
    if not v:
        raise AssertionError(message)

def block(k, r, s, theta, j):
    a = k*(1-r*r)*r**(2*j)/(1-r**(2*k))
    b = k*(1-s*s)*s**(2*j)/(1-s**(2*k))
    c = k*math.sqrt((1-r*r)*(1-s*s))*(r*s)**j / abs(1-(r*s)**k*cmath.exp(1j*k*theta))
    return a,b,c

def eigenvalues(k, r, s, theta, j):
    a,b,c = block(k,r,s,theta,j)
    plus = (a+b+math.hypot(a-b,2*c))/2
    # Algebraically positive determinant avoids catastrophic cancellation.
    rr, ss, z = r**k, s**k, (r*s)**k*cmath.exp(1j*k*theta)
    det = (k*k*(1-r*r)*(1-s*s)*(r*s)**(2*j)
           *abs(rr-ss*cmath.exp(1j*k*theta))**2
           /((1-rr*rr)*(1-ss*ss)*abs(1-z)**2))
    return det/plus, plus, det

def kernel(z,w):
    return math.sqrt((1-abs(z)**2)*(1-abs(w)**2))/(1-z.conjugate()*w)

for k in range(2,10):
    for r,s in [(0.21,0.62),(0.44,0.83),(0.61,0.74)]:
        for step in (0,0.27,0.66,1):
            theta=math.pi*step/k
            roots=[cmath.exp(2j*math.pi*m/k) for m in range(k)]
            rings=[[r*z for z in roots],[s*cmath.exp(1j*theta)*z for z in roots]]
            # DFT of the exact full Gram, confirming each 2x2 cyclic block.
            for j in range(k):
                expected=block(k,r,s,theta,j)
                for ia in range(2):
                    for ib in range(2):
                        actual=sum(kernel(rings[ia][0],rings[ib][m])
                                   *cmath.exp(-2j*math.pi*j*m/k)
                                   for m in range(k))
                        if ia==ib:
                            near(actual.real,expected[ia]); near(actual.imag,0)
                        else:
                            near(abs(actual),expected[2])
                minus,plus,det=eigenvalues(k,r,s,theta,j)
                require(minus>0 and plus>=minus,"positivity")
                a,b,c=expected
                near(minus+plus,a+b)
                near(minus*plus,det)
                near(det,a*b-c*c,rel=5e-8,abs_tol=5e-12)
                if j>0:
                    prev_min,prev_max,_=eigenvalues(k,r,s,theta,j-1)
                    require(minus < prev_min and plus < prev_max,"mode ordering")
        # Unique minimax and condition-number optimizer modulo 2pi/k.
        m_opt,M_opt,_=eigenvalues(k,r,s,math.pi/k,k-1)
        top_opt=eigenvalues(k,r,s,math.pi/k,0)[1]
        for step in (0,.1,.3,.6,.85):
            theta=step*math.pi/k
            m,M,_=eigenvalues(k,r,s,theta,k-1)
            top=eigenvalues(k,r,s,theta,0)[1]
            require(m < m_opt,"strict minimum-eigenvalue optimum")
            require(top > top_opt,"strict maximum-eigenvalue optimum")
            require(top/m > top_opt/m_opt,"strict conditioning optimum")
        near(eigenvalues(k,r,s,-math.pi/k,k-1)[0],m_opt)

# The genuinely two-radius large-degree law, tested with a stable determinant.
for r,s in [(.32,.77),(.59,.85),(.4,.68)]:
    errors=[]
    for k in (15,22,30,40):
        small=eigenvalues(k,r,s,math.pi/k,k-1)[0]
        law=k*(1-r*r)/r**2*(r*s)**(2*k)
        errors.append(abs(small/law-1))
    require(errors[-1]<errors[0] and errors[-1]<0.01,"sharp asymptotic")

print(f"PASS: {COUNT} standard-library numerical assertions")
