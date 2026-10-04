#!/usr/bin/env python3
from fractions import Fraction
import random, math

def normalize(v):
    s=sum(v); return [Fraction(x,s) for x in v]

def mean_var(xs,ps):
    mu=sum(p*x for p,x in zip(ps,xs))
    return mu,sum(p*(x-mu)**2 for p,x in zip(ps,xs))

def cov(xs,ys,ps):
    mx=sum(p*x for p,x in zip(ps,xs)); my=sum(p*y for p,y in zip(ps,ys))
    return sum(p*(x-mx)*(y-my) for p,x,y in zip(ps,xs,ys))

def coefficients(ps,tau):
    P=Fraction(0); a=[]
    for p in ps[:-1]:
        P+=p; a.append(min((1-tau)*P,tau*(1-P)))
    return a

def scores(ps,tau):
    P=Fraction(0); ss=[]
    for p in ps:
        lo=P; hi=P+p
        left=max(Fraction(0),min(hi,tau)-lo)
        right=max(Fraction(0),hi-max(lo,tau))
        integ=-(1-tau)*left+tau*right
        ss.append(integ/p); P=hi
    return ss

def loss_at(z,xs,ps,tau):
    return sum(p*(tau*max(Fraction(0),x-z)+(1-tau)*max(Fraction(0),z-x)) for p,x in zip(ps,xs))

def dmin(xs,ps,tau):
    return min(loss_at(z,xs,ps,tau) for z in xs)

def endpoints(ps,tau):
    a=coefficients(ps,tau)
    P=Fraction(0); l2=[]
    for aj,p in zip(a,ps[:-1]):
        P+=p; l2.append(aj*aj/(P*(1-P)))
    ss=scores(ps,tau)
    _,c2=mean_var(ss,ps)
    return min(l2),c2,ss

def run():
    rng=random.Random(20261002)
    direct_checks=0; covariance_checks=0; lower_checks=0; upper_checks=0
    formula_checks=0; two_point_checks=0; three_attain_checks=0; boundary_checks=0

    for _ in range(2500):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,31) for __ in range(m)])
        tau=Fraction(rng.randrange(1,40),40)
        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,25),rng.randrange(1,9)))
        D=dmin(xs,ps,tau)
        aa=coefficients(ps,tau)
        ds=[xs[i+1]-xs[i] for i in range(m-1)]
        assert D==sum(a*d for a,d in zip(aa,ds)); direct_checks+=1
        l2,c2,ss=endpoints(ps,tau)
        assert D==cov(xs,ss,ps); covariance_checks+=1
        _,vx=mean_var(xs,ps)
        assert D*D<=c2*vx; upper_checks+=1
        if m==2:
            assert D*D==l2*vx==c2*vx; two_point_checks+=1
        else:
            assert D*D>l2*vx; lower_checks+=1

        # explicit conditional-variance formula
        P=Fraction(0); delta=Fraction(0); hit_boundary=False
        for p in ps:
            if tau==P or tau==P+p: hit_boundary=True
            if P<tau<P+p:
                delta=(tau-P)*(P+p-tau)/p
            P+=p
        expected=tau*(1-tau)-(Fraction(0) if hit_boundary else delta)
        assert c2==expected; formula_checks+=1

        # lower boundary sequence
        if m>=3:
            P=Fraction(0); vals=[]
            for j,(aj,p) in enumerate(zip(aa,ps[:-1])):
                P+=p; vals.append((aj*aj/(P*(1-P)),j))
            _,jstar=min(vals)
            eps=Fraction(1,10**7)
            xb=[Fraction(0)]
            for j in range(m-1): xb.append(xb[-1]+(Fraction(1) if j==jstar else eps))
            Db=dmin(xb,ps,tau); _,vb=mean_var(xb,ps)
            assert abs(float(Db*Db/vb-l2))<0.003
            boundary_checks+=1

        # upper boundary: perturb score vector to strict order
        eps=Fraction(1,10**8)
        xu=[s+eps*i for i,s in enumerate(ss)]
        assert all(xu[i]<xu[i+1] for i in range(m-1))
        Du=dmin(xu,ps,tau); _,vu=mean_var(xu,ps)
        assert abs(float(Du*Du/vu-c2))<0.003
        boundary_checks+=1

    # exact three-category attainable upper cases
    for _ in range(1000):
        ps=normalize([rng.randrange(1,30) for __ in range(3)])
        P1=ps[0]; P2=ps[0]+ps[1]
        # choose a rational tau strictly in middle probability cell
        tau=(P1+P2)/2
        l2,c2,ss=endpoints(ps,tau)
        assert ss[0]<ss[1]<ss[2]
        D=dmin(ss,ps,tau); _,v=mean_var(ss,ps)
        assert D*D==c2*v
        three_attain_checks+=1

    print('VERIFY_OK '
          f'direct_checks={direct_checks} covariance_checks={covariance_checks} '
          f'lower_checks={lower_checks} upper_checks={upper_checks} '
          f'formula_checks={formula_checks} two_point_checks={two_point_checks} '
          f'three_attain_checks={three_attain_checks} boundary_checks={boundary_checks}')

if __name__=='__main__': run()
