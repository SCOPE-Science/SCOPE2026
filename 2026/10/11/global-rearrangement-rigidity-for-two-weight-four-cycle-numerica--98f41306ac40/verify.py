"""Numerical corroboration for four-cycle spatial numerical-radius rearrangements.
Run: python3 verify.py; standard-library only. Finite checks do not prove the theorem.
"""
import math, random

def quotient(p,weights,x):
    d=sum(z**p for z in x)
    return sum(weights[i]*x[i]**(p-1)*x[(i+1)%4] for i in range(4))/d

def optimum_alternating(p,a,b):
    def f(log_t):
        t=math.exp(log_t)
        return (a*t**(p-1)+b*t)/(1+t**p)
    # The root lies in a fixed moderate range for the tested inputs.
    lo,hi=-12.,12.
    for _ in range(220):
        m1=lo+(hi-lo)*0.3819660112501051
        m2=hi-(hi-lo)*0.3819660112501051
        if f(m1)<f(m2):lo=m1
        else:hi=m2
    t=math.exp((lo+hi)/2)
    return t,f((lo+hi)/2)

def main():
    random.seed(381944)
    ps=[1.05,1.12,1.5,1.8,1.99,2.,2.01,2.2,3.,4.,8.,20.]
    ratios=[1.001,1.1,2.,3.,10.,100.]
    cases=0;alt_random=0;grp_gaps=0;hilbert=0
    for p in ps:
        for a in ratios:
            b=1.
            t,va=optimum_alternating(p,a,b)
            # An independent finite search over positive four-coordinate vectors.
            for _ in range(220):
                x=[math.exp(random.uniform(-5,5)) for _ in range(4)]
                test=quotient(p,[a,b,a,b],x)
                assert test<=va+2e-7,(p,a,t,va,test,x)
                alt_random+=1
            if p!=2.:
                if p>2:
                    assert t>1, (p,a,t)
                    x=[t,t,1.,1.]
                    bound=(t-1)*(a*t**(p-1)-b)/(2*(1+t**p))
                else:
                    assert t<1, (p,a,t)
                    x=[t,1.,1.,t]
                    bound=(1-t**(p-1))*(a-b*t)/(2*(1+t**p))
                actual=quotient(p,[a,a,b,b],x)-va
                assert actual>0 and abs(actual-bound)<=2e-10*max(1.,abs(va)),(p,a,t,actual,bound)
                grp_gaps+=1
            else:
                assert abs(va-(a+b)/2)<1e-9
                hilbert_exact=math.sqrt((a*a+b*b)/2)
                assert hilbert_exact>va
                for _ in range(110):
                    x=[math.exp(random.uniform(-4,4)) for _ in range(4)]
                    assert quotient(2,[a,a,b,b],x)<=hilbert_exact+1e-10
                    hilbert+=1
            cases+=1
    print('PASS | cases=%d alt_random_bounds=%d constructive_gap=%d Hilbert_bounds=%d'%(cases,alt_random,grp_gaps,hilbert))
    for p,a,b in [(1.5,3.,1.),(2.,3.,1.),(4.,3.,1.),(10.,3.,1.)]:
        t,va=optimum_alternating(p,a,b)
        if p==2: vg=math.sqrt((a*a+b*b)/2)
        else:
            x=[t,t,1.,1.] if p>2 else [t,1.,1.,t]
            vg=quotient(p,[a,a,b,b],x)
        print('p=%s a=%s b=%s t*=%.12f alternating=%.12f grouped_lower=%.12f'%(p,a,b,t,va,vg))

if __name__=='__main__':main()
