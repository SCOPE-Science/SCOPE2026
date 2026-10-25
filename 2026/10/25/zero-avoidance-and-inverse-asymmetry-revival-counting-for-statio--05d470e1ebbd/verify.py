"""Reproducibility checks for a stationary two-state phase-noise theorem.

Requires only the Python 3 standard library. Finite numerical checks corroborate,
but do not replace, the accompanying all-parameter analytic arguments.
"""
import cmath
import math


def mode_data(a, v, e):
    assert a > 0 and v > 0 and abs(e) < a
    z = cmath.sqrt(a*a - v*v + 2j*v*e)
    if abs(z) < 1e-14:
        raise ValueError('Use the continuous limit at the double root.')
    b = a + 1j*v*e/a
    cp = (1+b/z)/2
    cm = (1-b/z)/2
    return z, b, cp, cm


def coherence(a, v, e, t):
    z, b, _, _ = mode_data(a, v, e)
    return math.exp(-a*t)*(cmath.cosh(z*t)+(b/z)*cmath.sinh(z*t))


def rk4_coherence(a, v, e, t, steps=2500):
    # Independent propagation of the tilted two-state Markov generator.
    u, w = complex((a+e)/(2*a)), complex((a-e)/(2*a))
    dt = t/steps
    def rhs(x, y):
        return (1j*v-(a-e))*x+(a+e)*y, (a-e)*x+(-1j*v-(a+e))*y
    for _ in range(steps):
        k1, l1 = rhs(u, w)
        k2, l2 = rhs(u+dt*k1/2, w+dt*l1/2)
        k3, l3 = rhs(u+dt*k2/2, w+dt*l2/2)
        k4, l4 = rhs(u+dt*k3, w+dt*l3)
        u += dt*(k1+2*k2+2*k3+k4)/6
        w += dt*(l1+2*l2+2*l3+l4)/6
    return u+w


def turning_decomposition(a, v, e):
    if not e:
        raise ValueError('The decomposition for counting uses nonzero asymmetry.')
    z, _, cp, cm = mode_data(a, v, e)
    u, w = z.real, z.imag
    P, Q = abs(cp)**2, abs(cm)**2
    H = cp*cm.conjugate()
    C = (-a+1j*w)*H
    amp = 2*abs(C)
    theta = cmath.phase(C)
    def A(t):
        return (a-u)*P*math.exp(2*u*t)+(a+u)*Q*math.exp(-2*u*t)
    def dA(t):
        return 2*u*((a-u)*P*math.exp(2*u*t)-(a+u)*Q*math.exp(-2*u*t))
    def q(t):
        return amp*math.cos(2*w*t+theta)-A(t)
    def dq(t):
        return -2*w*amp*math.sin(2*w*t+theta)-dA(t)
    return u, abs(w), A, dA, q, dq, amp, theta


def revival_count(a, v, e):
    """Count positivity components of the coherence-modulus derivative.

    The oscillatory positive lobes each contain at most one positivity component,
    because their cosine is strictly concave and A is strictly convex.
    """
    assert v > a > abs(e) > 0
    if e < 0:
        return revival_count(a, v, -e)
    u, w, A, dA, q, dq, amp, theta = turning_decomposition(a, v, e)
    upper = (math.acosh(v/a)+3)/(2*u)
    assert A(upper) > amp and dA(upper) > 0
    lowk = math.floor((theta-math.pi/2)/(2*math.pi))-2
    highk = math.ceil((2*w*upper+theta+math.pi/2)/(2*math.pi))+2
    count = 0
    for k in range(lowk, highk+1):
        center = (2*math.pi*k-theta)/(2*w)
        left, right = max(0, center-math.pi/(4*w)), min(upper, center+math.pi/(4*w))
        if right <= left:
            continue
        if dq(left) <= 0:
            tstar = left
        elif dq(right) >= 0:
            tstar = right
        else:
            L, R = left, right
            for _ in range(58):
                mid = (L+R)/2
                if dq(mid)>0:
                    L=mid
                else:
                    R=mid
            tstar = (L+R)/2
        if q(tstar) > 1e-12:
            count += 1
    return count


def scalar_min(f, left, right):
    for _ in range(90):
        a = left + (right-left)*0.3819660112501051
        b = left + (right-left)*0.6180339887498949
        if f(a)<f(b):
            right=b
        else:
            left=a
    t = (left+right)/2
    return t, math.sqrt(f(t))


def main():
    matrix_checks = 0
    for a, v, e in [(1,2,.17),(1,2,-.17),(.7,1.8,.2),(.7,1.8,-.2),
                     (2,.8,.4),(2,.8,-.4),(1,1.3,0),(1,2,0)]:
        for t in [.2, .9, 2.3, 3.7]:
            exact = coherence(a,v,e,t)
            via_matrix = rk4_coherence(a,v,e,t)
            assert abs(exact-via_matrix) < 4e-10, (a,v,e,t,exact,via_matrix)
            matrix_checks += 1
    identity_checks = 0
    for a,v,e in [(1,2,.2),(1,2,-.2),(2,3,.1),(.5,1.3,-.23),(.7,.3,.35)]:
        z,b,_,_ = mode_data(a,v,e)
        u,w=z.real,z.imag
        assert 0<u<a
        assert abs((b*z.conjugate()).real-u*(a+w*w/a))<2e-12
        assert abs(b-z)<abs(b+z)
        if v>a:
            U,W,A,dA,q,dq,amp,theta = turning_decomposition(a,v,e)
            for t in [0.16,0.7,1.6,2.9]:
                h=1e-5
                left=abs(coherence(a,v,e,t-h))**2
                right=abs(coherence(a,v,e,t+h))**2
                numerical=(right-left)/(2*h)
                analytic=2*math.exp(-2*a*t)*q(t)
                assert abs(numerical-analytic)<4e-9, (t,numerical,analytic)
                identity_checks += 1
    a,v = 1.,2.
    omega=math.sqrt(v*v-a*a)
    depth_checks = 0
    for n in range(4):
        tn=((n+1)*math.pi-math.atan(omega/a))/omega
        coeff=math.exp(-a*tn)*v*v*(1+a*tn)/(a*omega*omega)
        for e in [.008,.004]:
            tm, minimum = scalar_min(lambda t: abs(coherence(a,v,e,t))**2,
                                     tn-.10, tn+.10)
            assert abs(tm-tn)<0.003
            assert abs(minimum/e/coeff-1)<.0005, (n,e,minimum/e/coeff)
            depth_checks += 1
    constant=(v*v-a*a)/(2*math.pi*v)*math.acosh(v/a)
    count_checks = []
    for e in [.1,.05,.02,.01,.005,.002,.001]:
        N=revival_count(a,v,e)
        assert N == revival_count(a,v,-e)
        count_checks.append((e,N,e*N))
    assert abs(count_checks[-1][2]/constant-1)<.006
    print('PASS: independent tilted-generator propagations:',matrix_checks)
    print('PASS: spectral zero-exclusion identities and derivative checks:',identity_checks)
    print('PASS: avoided-zero minimum linear coefficients:',depth_checks)
    print('PASS: exact cosine-lobe revival counts:',count_checks)
    print('Predicted singular-count coefficient:',repr(constant))
    print('Numerical tests are corroboration, not proofs of the asymptotic limit.')

if __name__ == '__main__':
    main()
