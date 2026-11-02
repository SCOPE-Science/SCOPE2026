"""Reproducible numerical diagnostics for a stationary run/rest harmonic swimmer.

Run: python3 verify.py (Python standard library only).
Numerical checks support, but do not replace, the proof in RESULT.md.
"""
import math
import random

SEED = 410902

def sample_on(rng, a, p, depth=55):
    s = 0.0
    for _ in range(depth):
        e = rng.random() ** (1.0 / a)  # Beta(a,1)
        z = rng.random() ** (1.0 / p)  # Beta(p,1)
        s = (1-e)**2 + (e*e*z)*s
    return s

def theoretical_means(a, p):
    m_on = 2*(p+1)/((a+1)*(a+2*p+2))
    m_off = (p/(p+1))*m_on
    m = (2*p*m_on + a*m_off)/(a+2*p)
    return m_on, m_off, m

def run():
    rng = random.Random(SEED)
    checks = 0
    for a,p in ((1.0,.5),(.5,1.5),(2.0,2.5),(4.0,.75)):
        m_on,m_off,m=theoretical_means(a,p)
        expected = (2*p/(a+2*p))/(a+1)
        assert math.isclose(m,expected,abs_tol=3e-15)
        assert 0 < m_off < m_on < 1
        checks += 2
        num=24000
        ons=[sample_on(rng,a,p) for _ in range(num)]
        onbar=sum(ons)/num
        assert abs(onbar-m_on) < 0.015
        offbar=sum((rng.random()**(1/p))*s for s in ons)/num
        assert abs(offbar-m_off) < 0.015
        checks += 2
    # High-dimensional sphere inner-product moments, checked by Monte Carlo.
    d=24; n=5000
    w=(.27,.16,.10,.05)
    expected_var=4*sum(w[i]**2*w[j]**2 for i in range(len(w)) for j in range(i+1,len(w)))/d
    sample_variance=0.0
    for _ in range(n):
        vectors=[]
        for wi in w:
            v=[rng.gauss(0,1) for _ in range(d)]
            norm=math.sqrt(sum(t*t for t in v))
            vectors.append([wi*t/norm for t in v])
        norm_sq=sum(sum(v[k] for v in vectors)**2 for k in range(d))
        sample_variance+=(norm_sq-sum(wi*wi for wi in w))**2/n
    assert abs(sample_variance/expected_var-1) < .15
    checks+=1
    # Tail exponent diagnostics for a=1, p=1/2. The theoretical upper constant is 1/4.
    a,p=1.,.5; num=110000
    on=[sample_on(rng,a,p) for _ in range(num)]
    pi_on=2*p/(a+2*p)
    values=[]
    for s in on:
        if rng.random()<pi_on: values.append(s)
        else: values.append((rng.random()**(1/p))*s)
    for eps in (.05,.08):
        actual=sum(s>1-eps for s in values)/num
        predicted=pi_on*(eps/2)**a
        assert abs(actual-predicted)<.16*predicted+.0003
        checks+=1
    # Lower exponent (power p) yields a slowly varying positive ratio.
    lower=[]
    for eps in (.025,.04,.06):
        q=sum(s<eps for s in values)/num
        lower.append(q/(eps**p))
        assert 0.5<lower[-1]<3.0
        checks+=1
    assert max(lower)/min(lower)<1.25
    checks+=1
    print(f'{checks} reproducible mathematical/numerical diagnostics passed.')
    print(f'finite-d conditional variance: predicted={expected_var:.8g}, sampled={sample_variance:.8g}')
    print(f'lower-tail rescaled values: {lower}')

if __name__=='__main__':
    run()
