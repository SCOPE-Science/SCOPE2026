#!/usr/bin/env python3
"""Independent, finite checks for Haar full-bunching probability identities."""
import math
import itertools
import random
from fractions import Fraction

rng = random.Random(741141)

def raw_moment(m, n, t):
    return math.exp(math.lgamma(m)+n*math.lgamma(1+t)-math.lgamma(m+n*t))

def alpha_scgf(alpha,t):
    if math.isinf(alpha):
        return math.lgamma(1+t)
    return math.lgamma(1+t)+t-(alpha+t)*math.log1p(t/alpha)

def main():
    exact = 0
    for m in range(2,11):
        for n in range(1,m+1):
            for t in (1,2,3):
                q = Fraction(math.factorial(m-1)*math.factorial(t)**n, math.factorial(m+n*t-1))
                assert abs(float(q)-raw_moment(m,n,t)) < 1e-10 * max(1.,float(q))
                exact += 1
    moments=0
    for m,n in ((3,2),(5,3),(8,4)):
        reps=100000
        vals=[]
        for _ in range(reps):
            sample=[rng.expovariate(1) for j in range(m)]
            val=math.prod(sample[:n])/sum(sample)**n
            vals.append(val)
        em=sum(vals)/reps
        es=sum(z*z for z in vals)/reps
        a,b=raw_moment(m,n,1),raw_moment(m,n,2)
        assert abs(em/a-1)<0.035,(m,n,em,a)
        assert abs(es/b-1)<0.065,(m,n,es,b)
        moments+=1
    scgf=0
    for alpha in (1.,2.,5.,float('inf')):
        for t in (-0.35,0.6,1.2):
            for n in (3000,):
                m=round(alpha*n) if math.isfinite(alpha) else n*n
                f=(math.lgamma(m)+n*math.lgamma(1+t)-math.lgamma(m+n*t)+n*t*math.log(m))/n
                assert abs(f-alpha_scgf(alpha,t))<0.02, (alpha,t,f,alpha_scgf(alpha,t))
                scgf+=1
    gap=0
    for alpha in (1.,1.7,3.,float('inf')):
        for n in (2000,):
            m=max(n,round(alpha*n)) if math.isfinite(alpha) else n*n
            mean_scaled=(math.lgamma(m)-math.lgamma(m+n)+n*math.log(m))/n
            integral=0 if not math.isfinite(alpha) else (alpha+1)*math.log1p(1/alpha)-1
            assert abs(mean_scaled+integral)<0.01,(alpha,mean_scaled,integral)
            delta=0.57721566490153286-integral
            assert delta>0
            variance_per_n=math.pi**2/6-n*(math.pi**2/6-sum(1/(k*k) for k in range(1,m)))
            assert abs(variance_per_n-(math.pi**2/6-(0 if math.isinf(alpha) else 1/alpha)))<0.01
            gap+=1
    # Independently evaluate the symmetrized internal-state tensor for
    # two and three photons and compare with the Gram permanent.
    sym=0
    for states in (
        [(1.,0.),(0.6,0.8)],
        [(1.,0.),(0.6,0.8),(0.8,0.6)],
        [(1.,0.),(1.,0.),(1.,0.)],
    ):
        n=len(states)
        gram=[[sum(states[i][k]*states[j][k] for k in (0,1)) for j in range(n)] for i in range(n)]
        permanent=sum(math.prod(gram[i][order[i]] for i in range(n)) for order in itertools.permutations(range(n)))
        amplitudes={}
        for order in itertools.permutations(range(n)):
            for assignment in itertools.product((0,1),repeat=n):
                coefficient=math.prod(states[order[i]][assignment[i]] for i in range(n))/math.sqrt(math.factorial(n))
                amplitudes[assignment]=amplitudes.get(assignment,0.)+coefficient
        norm=sum(v*v for v in amplitudes.values())
        assert abs(norm-permanent)<1e-12,(norm,permanent)
        sym+=1
    print(f'VERIFY_OK internal_symmetrization={sym} exact_integer_Mellin={exact} normalized_exponential_samples={moments} finite_to_limit_SCgf={scgf} mean_typical_variance={gap}')

if __name__ == '__main__':main()
