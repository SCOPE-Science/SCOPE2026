#!/usr/bin/env python3
"""Self-contained numerical and algebraic diagnostics for asymptotic eigenmode selection.
Scientific objects only: an open asymmetric-hopping chain and normalized position probabilities.
"""
import math

def v_bulk(u):
    if abs(u)<1e-5:
        u2=u*u
        return 1/12-u2/240+u2*u2/6048
    return 1/(u*u)-1/(4*math.sinh(u/2)**2)

def v_mode(m,u):
    a=2*math.pi*m
    return v_bulk(u)+2*(u*u-a*a)/(u*u+a*a)**2

def v_star(u):
    return max(v_bulk(u),v_mode(1,u))

def moments(n,m,u):
    z=mu=second=0.0
    for j in range(1,n+1):
        y=j/(n+1)
        w=math.exp(u*y)*math.sin(math.pi*m*y)**2
        z+=w; mu+=w*y; second+=w*y*y
    mu/=z
    return second/z-mu*mu

def fisher_direct(n,m,u):
    theta=math.exp(u/(n+1))
    return ((n+1)**2)*moments(n,m,u)/(theta*theta)

def classical_fisher(n,m,u):
    theta=math.exp(u/(n+1))
    weights=[]; z=0.0
    for j in range(1,n+1):
        w=math.exp(u*j/(n+1))*math.sin(math.pi*m*j/(n+1))**2
        weights.append(w);z+=w
    probs=[w/z for w in weights]
    mean=sum(p*j for j,p in enumerate(probs,start=1))
    cfi=sum(p*(j-mean)**2/(theta*theta) for j,p in enumerate(probs,start=1))
    return cfi


def main():
    tests=0
    # Direct Hamiltonian right-eigenvector residual, not merely a probability ansatz.
    for n in [2,3,4,6,10,18,40]:
        for theta in [0.7,1.0,1.3,2.5]:
            jl=1.7; jr=jl*theta
            for m in [1,(n+1)//2,n]:
                v=[theta**(j/2)*math.sin(math.pi*m*j/(n+1)) for j in range(1,n+1)]
                eigenvalue=2*math.sqrt(jl*jr)*math.cos(math.pi*m/(n+1))
                for j in range(n):
                    hv=(jl*v[j+1] if j+1<n else 0.0)+(jr*v[j-1] if j>0 else 0.0)
                    assert abs(hv-eigenvalue*v[j])<1e-10*max(1,abs(hv),abs(eigenvalue*v[j]))
                tests+=1
    # Independent variance and probability score evaluations, including all modes.
    for n in [3,4,5,6,9,12,24,64]:
        for u in [-10,-6,-1,0,1,6,10]:
            for m in range(1,n+1):
                f=fisher_direct(n,m,u)
                c=classical_fisher(n,m,u)
                assert abs(f-c) < 2e-10*max(1, f)
                assert abs(moments(n,m,u)-moments(n,n+1-m,u)) < 1e-11
                tests+=2
    # Riemann limit for fixed mode and oscillatory regime.
    for u in [-12,-7,0,4,8,12]:
        for m in [1,2,3,5]:
            v=moments(6000,m,u)
            assert abs(v-v_mode(m,u))<0.0015, (u,m,v,v_mode(m,u))
            tests+=1
        v=moments(6000,501,u)
        assert abs(v-v_bulk(u))<0.0005, (u,v,v_bulk(u))
        tests+=1
    # Independent exact limit integral differentiation by symmetric finite differences.
    for m in [1,2,4]:
        for u in [0,2,5,10,18]:
            a=2*math.pi*m
            def logz(v):
                if abs(v)<1e-13:
                    return math.log(.5)
                return math.log(math.expm1(v)/v/2) + math.log(a*a/(v*v+a*a))
            h=0.008
            approx=(logz(u+h)-2*logz(u)+logz(u-h))/(h*h)
            assert abs(approx-v_mode(m,u))<1e-5,(m,u,approx,v_mode(m,u))
            tests+=1
    # Optimize finite chain over all eigenspaces, check convergence and predicted transition.
    for u in [0,4,5.8,6.2,7,8,12,-8]:
        vals=[moments(1200,m,u) for m in range(1,1201)]
        opt=max(vals)
        assert abs(opt-v_star(u))<0.001,(u,opt,v_star(u))
        if abs(u)>2*math.pi+0.6:
            winners=[m+1 for m,v in enumerate(vals) if opt-v<1e-10]
            assert winners==[1,1200], (u,winners)
        tests+=1
    # Continuous analytic inequality: compare g_m across modes for dense real u.
    for k in range(-400,401):
        u=k/20
        gap=v_mode(1,u)-v_bulk(u)
        winner=max(v_mode(m,u) for m in range(1,100))
        assert abs(max(winner,v_bulk(u))-v_star(u))<1e-12,(u,winner,gap)
        tests+=1
    print('VERIFY_OK',tests,'finite scores/integral/argmax comparisons')

if __name__=='__main__':main()
