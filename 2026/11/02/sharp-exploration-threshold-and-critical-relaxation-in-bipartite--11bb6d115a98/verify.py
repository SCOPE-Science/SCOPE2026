"""Independent finite checks for a bipartite anti-coordination Q-learning theorem.
Run: python3 verify.py.  These tests supplement, not replace, the analytic proof.
"""
from math import exp, log, sqrt, tanh, isclose
import random


def field(z, a, b, J, T):
    ta = sum(tanh(v / 2) for v in z[:a])
    tb = sum(tanh(v / 2) for v in z[a:])
    return [-J * tb - T * v for v in z[:a]] + [-J * ta - T * v for v in z[a:]]


def phi(p, a, b, J, T):
    entropy = lambda x: -x * log(x) - (1-x) * log(1-x)
    return J * sum(p[i]*(1-p[j])+(1-p[i])*p[j]
                   for i in range(a) for j in range(a, a+b)) + T*sum(entropy(v) for v in p)


def rk4(y, dt, func):
    k1 = func(y)
    k2 = func([u+dt*v/2 for u,v in zip(y,k1)])
    k3 = func([u+dt*v/2 for u,v in zip(y,k2)])
    k4 = func([u+dt*v for u,v in zip(y,k3)])
    return [u+dt*(v1+2*v2+2*v3+v4)/6 for u,v1,v2,v3,v4 in zip(y,k1,k2,k3,k4)]


def positive_root(a,b,J,T):
    # Positive root of x = J*b/T*tanh((J*a/T)*tanh(x/2)/2).
    def f(x):
        return (J*b/T)*tanh((J*a/T)*tanh(x/2)/2)-x
    lo = 1.0e-6
    hi = J*b/T+1.0
    assert f(lo)>0 and f(hi)<0
    for _ in range(100):
        m = (lo+hi)/2
        if f(m)>0: lo=m
        else: hi=m
    return (lo+hi)/2


def run():
    random.seed(14017)
    tested = 0
    # Algebraic derivative identity for logit dynamics and free-energy potential.
    for a in range(1,5):
        for b in range(1,5):
            J = 0.7+random.random()
            T = 0.5+random.random()
            for _ in range(30):
                z = [random.uniform(-2.5,2.5) for _ in range(a+b)]
                p = [1/(1+exp(-v)) for v in z]
                f = field(z,a,b,J,T)
                # Explicit partial derivative of potential in probability coordinates.
                grad = [J*sum(1-2*p[j] for j in range(a,a+b))-T*log(p[i]/(1-p[i])) for i in range(a)] + [J*sum(1-2*p[j] for j in range(a))-T*log(p[i]/(1-p[i])) for i in range(a,a+b)]
                assert max(abs(u-v) for u,v in zip(f,grad))<1e-12
                h=1e-6
                for i in range(a+b):
                    plus=p[:];minus=p[:];plus[i]+=h;minus[i]-=h
                    derivative=(phi(plus,a,b,J,T)-phi(minus,a,b,J,T))/(2*h)
                    assert abs(derivative-grad[i])<3e-7
                derivative_potential=sum(p[i]*(1-p[i])*grad[i]**2 for i in range(a+b))
                assert derivative_potential>=0
                tested+=1
    # Sharp high-temperature weighted-sup estimate for arbitrary initial logits.
    for a,b,J in [(1,1,1.2),(2,3,1),(3,5,0.7),(4,4,1.3)]:
        tc = J*sqrt(a*b)/2
        T = 1.4*tc
        z=[random.uniform(-2,2) for _ in range(a+b)]
        norm=lambda u:max(max(abs(v)/sqrt(b) for v in u[:a]),max(abs(v)/sqrt(a) for v in u[a:]))
        initial=norm(z)
        f=lambda u: field(u,a,b,J,T)
        for step in range(1,101):
            z=rk4(z,0.01,f)
            assert norm(z)<=initial*exp(-(T-tc)*step*0.01)+1e-11
    # Polarized fixed point and square-root branch amplitude near criticality.
    checked_branch=0
    for a,b,J in [(1,1,1),(2,3,1),(3,5,0.7),(1,9,1),(4,4,1.3)]:
        tc=J*sqrt(a*b)/2
        for relative_gap in (1e-2,2e-3,4e-4):
            T=tc*(1-relative_gap)
            x=positive_root(a,b,J,T)
            y=(J*a/T)*tanh(x/2)
            assert abs(T*x-J*b*tanh(y/2))<1e-9
            assert abs(T*y-J*a*tanh(x/2))<1e-9
            predicted=sqrt(b)*sqrt(24*(tc-T)/(tc*(a+b)))
            assert abs(x/predicted-1)<0.045
            checked_branch+=1
    # Critical algebraic relaxation: two-part symmetry-invariant ODE.
    crit=[]
    for a,b,J in [(1,1,1),(2,3,1),(3,5,0.7)]:
        tc=J*sqrt(a*b)/2
        z=[sqrt(b)*0.45]*a + [-sqrt(a)*0.45]*b
        f=lambda y:field(y,a,b,J,tc)
        dt=0.1
        for _ in range(20000):
            z=rk4(z,dt,f)
        # Projection onto critical eigenvector, normalized q.q=2ab.
        s=(sqrt(b)*sum(z[:a])-sqrt(a)*sum(z[a:]))/(2*a*b)
        predicted=sqrt(12/(tc*(a+b)*2000.0))
        assert abs(abs(s)/predicted-1)<0.04,(a,b,s,predicted)
        crit.append((a,b,round(s/predicted,6)))
    # Cubic projection coefficient via explicit algebra for multiple integer part sizes.
    for a in range(1,11):
        for b in range(1,11):
            J=1.7;tc=J*sqrt(a*b)/2
            q=[sqrt(b)]*a+[-sqrt(a)]*b
            norm=sum(v*v for v in q)
            numerator=J/24*(sum(q[:a])*sum(v**3 for v in q[a:])+sum(q[a:])*sum(v**3 for v in q[:a]))
            coefficient=numerator/norm
            assert isclose(coefficient, -tc*(a+b)/24,rel_tol=1e-14)
    print(f'PASS: {tested} numerical field/free-energy checks; 400 weighted-norm steps; {checked_branch} positive branch checks; 3 critical t^-1/2 checks; 100 cubic projection numerical checks')
    print('Critical scaled amplitudes:',crit)

if __name__=='__main__':
    run()
