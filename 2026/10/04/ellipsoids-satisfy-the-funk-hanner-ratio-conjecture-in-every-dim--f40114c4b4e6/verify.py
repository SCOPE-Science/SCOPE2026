from math import exp, log, tanh, sinh, pi, gamma, factorial

def omega(n):
    return pi**(n/2)/gamma(n/2 + 1)

def z_of_R(R):
    return 0.5*log(2*exp(R)-1)

def simpson(f, a, b, N=20000):
    if N % 2:
        N += 1
    h=(b-a)/N
    s=f(a)+f(b)
    for i in range(1,N):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3

def v_ellipsoid_s(n,R):
    z=z_of_R(R)
    I=simpson(lambda s: sinh(s)**(n-1),0.0,z)
    return n*omega(n)*I

def v_ellipsoid_t(n,R):
    rho=1-exp(-R)
    I=simpson(lambda t: t**(n-1)/(1-t*t)**((n+1)/2),0.0,rho)
    return n*omega(n)*I

def v_hanner(n,R):
    L=log(2*exp(R)-1)
    return (2**n/(factorial(n)*omega(n)))*L**n

def q_closed(n,R):
    z=z_of_R(R)
    I=simpson(lambda s: sinh(s)**(n-1),0.0,z)
    return (n*factorial(n)*omega(n)**2/4**n)*I/z**n

# Independent numerical consistency of the two ellipsoid integral coordinates.
for n in range(2,9):
    for R in (0.02,0.1,0.4,1.0,2.0):
        a=v_ellipsoid_s(n,R)
        b=v_ellipsoid_t(n,R)
        assert abs(a-b) <= 2e-9*max(1.0,a,b), (n,R,a,b)
        q=a/v_hanner(n,R)
        qc=q_closed(n,R)
        assert abs(q-qc) <= 2e-10*max(1.0,q,qc)

# Numerical stress test of the strict monotonicity proved analytically.
for n in range(2,13):
    Rs=[0.01,0.03,0.08,0.2,0.5,1.0,1.7,2.5]
    qs=[q_closed(n,R) for R in Rs]
    assert all(qs[i+1] > qs[i] for i in range(len(qs)-1)), (n,qs)

# The small-radius limit is the Mahler-product ratio ellipsoid/Hanner.
for n in range(2,9):
    R=1e-4
    q=q_closed(n,R)
    target=factorial(n)*omega(n)**2/4**n
    assert abs(q-target) <= 2e-4*target, (n,q,target)

# z is exactly artanh(rho), where rho is the Funk-ball dilation factor.
for R in (0.01,0.2,0.9,2.0):
    rho=1-exp(-R)
    z=z_of_R(R)
    assert abs(tanh(z)-rho) < 2e-14

print("VERIFY_OK Funk ellipsoid Hanner ratio")
