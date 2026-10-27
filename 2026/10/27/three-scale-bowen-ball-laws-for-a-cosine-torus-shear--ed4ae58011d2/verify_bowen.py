"""Finite numerical and elementary-identity checks for the cosine-shear Bowen correlation law.
Run: python3 verify_bowen.py (Python standard library only).
These finite checks do not prove the n->infinity asymptotic.
"""
import math

PI=math.pi

def velocity_difference(x,h,a):
    return a*(math.cos(2*PI*(x+h))-math.cos(2*PI*x))

def inner_kernel(B,eps):
    c=2*eps
    if B<=c:
        return c-2*B/PI
    r=c/B
    v=math.sqrt(1-r*r)
    return (2/PI)*c*(math.asin(r)-r/(1+v))

def simpson(fn,lower,upper,steps):
    assert steps%2==0
    step=(upper-lower)/steps
    sm=fn(lower)+fn(upper)
    for i in range(1,steps):
        sm+=(4 if i%2 else 2)*fn(lower+step*i)
    return sm*step/3

def mean_bowen(n,a,eps,steps=4000):
    # Integrates the exact arcsine inner integral; logarithmic h coordinate
    # resolves the small-h contribution without exponentially many grid cells.
    h0=math.asin(min(1.,eps/(a*n)))/PI
    h0=min(eps,h0)
    first=simpson(lambda v:inner_kernel(2*a*n*math.sin(PI*h0*v),eps)*h0,0,1,steps)
    if h0==eps:
        return 2*first
    upper=math.log(eps/h0)
    second=simpson(lambda t:inner_kernel(2*a*n*math.sin(PI*h0*math.exp(t)),eps)*h0*math.exp(t),0,upper,steps)
    return 2*(first+second)

def test():
    a=0.1; eps=0.06
    assert a<1/8 and eps<1/8
    for x_i in range(40):
        for h_i in range(-20,21):
            x=x_i/40;h=h_i/100
            expected=-2*a*math.sin(PI*h)*math.sin(2*PI*x+PI*h)
            assert abs(velocity_difference(x,h,a)-expected)<2e-15
    print('COSINE_TWO_POINT_DIFFERENCE_IDENTITY_PASS',40*41)
    for n in [2,3,9,30]:
        for eta_i in range(-8,9):
            eta=eta_i*eps/8
            for del_i in range(-16,17):
                delta=del_i*a/8
                all_ok=all(abs((eta+k*delta)-round(eta+k*delta))<eps+1e-14 for k in range(n+1))
                endpoints=(abs(eta)<eps+1e-14 and abs(eta+n*delta)<eps+1e-14)
                if abs(eta)<eps+1e-14 and all_ok:
                    assert endpoints
                if endpoints:
                    assert all_ok
    print('NO_MODULAR_WRAP_AND_ENDPOINT_CONVEXITY_PASS')
    # Compare exact integral of (c-B|sin theta|)_+ to independent Riemann-midpoint sums.
    for B in [0.02,0.10,0.25,3.0]:
        exact=inner_kernel(B,eps)
        q=18000
        independent=sum(max(0.,2*eps-B*abs(math.sin(2*PI*(i+0.5)/q))) for i in range(q))/q
        assert abs(exact-independent)<2e-6,(B,exact,independent)
    print('ARCSINE_INNER_INTEGRAL_PASS',4)
    C=4*eps*eps/(a*PI*PI)
    ns=[1000,10000,100000,1000000]
    masses=[mean_bowen(n,a,eps) for n in ns]
    for n,v in zip(ns,masses):
        assert v>0
        print('TWO_POINT_BOWEN_MASS',n,'%.12g'%v)
    for i in range(len(ns)-1):
        slope=(ns[i+1]*masses[i+1]-ns[i]*masses[i])/math.log(ns[i+1]/ns[i])
        assert abs(slope-C)<0.00008,(slope,C)
        print('LOGARITHMIC_SLOPE',ns[i],ns[i+1],'%.12g'%slope)
    print('PREDICTED_ANALYTIC_COEFFICIENT','%.12g'%C)
    print('INFINITE_TIME_LIMIT_REQUIRES_ANALYTIC_PROOF')

if __name__=='__main__':
    test()
