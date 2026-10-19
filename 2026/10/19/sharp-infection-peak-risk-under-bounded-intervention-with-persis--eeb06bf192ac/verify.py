"""Independent numerical checks for a controlled epidemic peak-hitting theorem.

Only illustrative floating-point checks; the mathematical proof is analytic.
"""
import math


def normal_cdf(z):
    return 0.5 * math.erfc(-z / math.sqrt(2.0))


def quantities(i, L, gamma, delta, H, sigma, T):
    assert i > 0 and L > i and gamma > 0 and delta > 0 and H >= 0
    assert sigma > 0 and T > 0
    h = math.log(L / i)
    k = gamma + delta + H + sigma * sigma / 2
    d = sigma * math.sqrt(T)
    terminal = normal_cdf((-h - k*T)/d)
    hitting = terminal + math.exp(-2*k*h / sigma**2) * normal_cdf((-h + k*T)/d)
    eventual = math.exp(-2*k*h / sigma**2)
    return (terminal,hitting,eventual,h,k)


def hitting_density(t, h, k, sigma):
    if t <= 0:
        return 0.0
    return h/(sigma*math.sqrt(2*math.pi*t**3))*math.exp(-((h+k*t)**2)/(2*sigma*sigma*t))


def integrate_hitting(T, h, k, sigma, steps=50000):
    assert steps % 2 == 0
    ds=math.sqrt(T)/steps
    def density_s(s):
        return 0.0 if s == 0.0 else 2*s*hitting_density(s*s,h,k,sigma)
    total=density_s(0)+density_s(math.sqrt(T))
    for j in range(1,steps):
        total+=(4 if j%2 else 2)*density_s(j*ds)
    return total * ds / 3


def test():
    tuples=[(.25,.5,.2,.1,.25,1,1),(.1,1,.3,.1,.7,.6,2),(.6,.61,.1,.1,.5,1.3,.3),(.01,.2,1,.01,.8,2,1.5)]
    for i,L,gamma,delta,H,sigma,T in tuples:
        p_t, p_hit,p_infty,h,k=quantities(i,L,gamma,delta,H,sigma,T)
        integral=integrate_hitting(T,h,k,sigma)
        assert 0 < p_t < p_hit < p_infty < 1,(p_t,p_hit,p_infty)
        assert abs(integral-p_hit)<2e-8,(integral,p_hit)
        assert abs(p_infty - (i/L)**(1+2*(gamma+delta+H)/sigma**2))<1e-14
        print('i,L,T=',i,L,T,'terminal=',format(p_t,'.12f'),'hit=',format(p_hit,'.12f'),'ever=',format(p_infty,'.12f'),'integral error=',abs(integral-p_hit))
    print('4 parameter tests: PASS')

if __name__=='__main__':
    test()
