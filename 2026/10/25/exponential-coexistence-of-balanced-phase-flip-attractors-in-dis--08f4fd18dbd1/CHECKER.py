"""Finite diagnostic for balanced two-cluster flip orbits.
This script is evidence for numerical examples, not a proof of the all-size theorem.
"""
import itertools
import math

PI = math.pi

def bisect(fun, lo, hi):
    flo = fun(lo)
    assert flo * fun(hi) < 0
    for _ in range(90):
        mid = (lo+hi)/2
        if fun(mid)*flo > 0:
            lo, flo = mid, fun(mid)
        else:
            hi = mid
    return (lo+hi)/2

def threshold(m):
    return bisect(lambda d: (m+1)*d*math.cos(d)-math.sin(d), 0.0001, PI/2)

def forward(z,h):
    s=[math.sin(v) for v in z]
    total=sum(s)
    return [v+h*(sv+total) for v,sv in zip(z,s)]

def on_circle_error(a,b):
    return max(abs((x-y+PI)%(2*PI)-PI) for x,y in zip(a,b))

def check():
    total_cases=0
    for m in (4,6,8,10,12):
        d0=threshold(m)
        h0=2*d0/math.sin(d0)
        assert 2 < h0 < PI
        d=0.5*(d0+PI/2)
        h=2*d/math.sin(d)
        q=math.cos(d)
        mu_c=1-h*(m+1)*q
        mu_t=1-h*q
        assert max(mu_c*mu_c,mu_t*mu_t)<1
        assert (m+1)*d*math.cos(d)<math.sin(d)
        cycles=set()
        for subset in itertools.combinations(range(m),m//2):
            signs=tuple(1 if j in subset else -1 for j in range(m))
            p=[PI+d*t for t in signs]
            v=[PI-d*t for t in signs]
            assert on_circle_error(forward(p,h),v)<1e-12
            assert on_circle_error(forward(v,h),p)<1e-12
            cycles.add(min(signs,tuple(-t for t in signs)))
            total_cases+=1
            # Finite-difference verification of each entry of the Jacobian.
            f0=forward(p,h)
            for j in range(m):
                eps=1e-6
                w=list(p);w[j]+=eps
                fw=forward(w,h)
                for i in range(m):
                    got=(fw[i]-f0[i])/eps
                    expected=(1.0 if i==j else 0.0)-h*q*(1.0+(1.0 if i==j else 0.0))
                    assert abs(got-expected)<7e-6,(m,i,j,got,expected)
        assert len(cycles)==math.comb(m,m//2)//2
        print('m=%d stable_cycles=%d h_star=%.12f sample_h=%.12f max_return_residual<1e-12' % (m,len(cycles),h0,h))
    print('BALANCED_EXCHANGE_AND_JACOBIAN_CHECK_PASS',total_cases)
    print('ALL_DIMENSIONAL_EXISTENCE_AND_STRUCTURAL_PERSISTENCE_REQUIRE_ANALYTIC_PROOF')

if __name__=='__main__':
    check()
