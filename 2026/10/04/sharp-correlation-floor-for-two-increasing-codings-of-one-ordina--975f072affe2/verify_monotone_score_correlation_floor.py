#!/usr/bin/env python3
from fractions import Fraction
import random
import math

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def mean_var(xs,ps):
    mu=sum(p*x for x,p in zip(xs,ps))
    var=sum(p*(x-mu)**2 for x,p in zip(xs,ps))
    return mu,var

def cov(xs,ys,ps):
    mx=sum(p*x for x,p in zip(xs,ps))
    my=sum(p*y for y,p in zip(ys,ps))
    return sum(p*(x-mx)*(y-my) for x,y,p in zip(xs,ys,ps))

def endpoint_lambda2(ps):
    return ps[0]*ps[-1]/((1-ps[0])*(1-ps[-1]))

def cut_vector(ps,j):
    P=sum(ps[:j+1])
    return [-(1-P) if i<=j else P for i in range(len(ps))]

def corr_float(xs,ys,ps):
    _,vx=mean_var(xs,ps)
    _,vy=mean_var(ys,ps)
    c=cov(xs,ys,ps)
    return float(c)/math.sqrt(float(vx*vy))

def run():
    rng=random.Random(20261002)
    decomposition_checks=0
    cut_covariance_checks=0
    cut_minimum_checks=0
    global_lower_checks=0
    affine_checks=0
    binary_checks=0
    boundary_checks=0
    equal_mass_checks=0

    for _ in range(2500):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,31) for __ in range(m)])

        # Exact cut covariance matrix and minimum normalized correlation.
        H=[cut_vector(ps,j) for j in range(m-1)]
        lam2=endpoint_lambda2(ps)
        for j in range(m-1):
            Pj=sum(ps[:j+1])
            _,vj=mean_var(H[j],ps)
            assert vj==Pj*(1-Pj)
            for k in range(m-1):
                Pk=sum(ps[:k+1])
                cjk=cov(H[j],H[k],ps)
                expected=min(Pj,Pk)*(1-max(Pj,Pk))
                assert cjk==expected
                _,vk=mean_var(H[k],ps)
                assert cjk*cjk >= lam2*vj*vk
                cut_covariance_checks+=2
        cut_minimum_checks+=1

        # Random strict codings and exact decomposition.
        xs=[Fraction(0)]
        ys=[Fraction(-2)]
        dx=[]
        dy=[]
        for __ in range(1,m):
            gx=Fraction(rng.randrange(1,25),rng.randrange(1,9))
            gy=Fraction(rng.randrange(1,25),rng.randrange(1,9))
            dx.append(gx); dy.append(gy)
            xs.append(xs[-1]+gx)
            ys.append(ys[-1]+gy)
        mx,vx=mean_var(xs,ps)
        my,vy=mean_var(ys,ps)
        centered_x=[x-mx for x in xs]
        centered_y=[y-my for y in ys]
        recon_x=[sum(dx[j]*H[j][i] for j in range(m-1)) for i in range(m)]
        recon_y=[sum(dy[j]*H[j][i] for j in range(m-1)) for i in range(m)]
        assert centered_x==recon_x and centered_y==recon_y
        decomposition_checks+=2

        cxy=cov(xs,ys,ps)
        assert cxy>0
        if m==2:
            assert cxy*cxy==vx*vy
            binary_checks+=1
        else:
            assert cxy*cxy > lam2*vx*vy
            global_lower_checks+=1

        # Affine recoding has correlation exactly one.
        ya=[Fraction(7,5)+Fraction(11,4)*x for x in xs]
        _,vya=mean_var(ya,ps)
        ca=cov(xs,ya,ps)
        assert ca*ca==vx*vya and ca>0
        affine_checks+=1

        if m>=3:
            eps=Fraction(1,10**7)
            xb=[Fraction(0)]
            yb=[Fraction(0)]
            for j in range(m-1):
                xb.append(xb[-1]+(Fraction(1) if j==0 else eps))
                yb.append(yb[-1]+(Fraction(1) if j==m-2 else eps))
            rho=corr_float(xb,yb,ps)
            lam=math.sqrt(float(lam2))
            assert abs(rho-lam)<0.003
            boundary_checks+=1

    for m in range(3,101):
        ps=[Fraction(1,m)]*m
        assert endpoint_lambda2(ps)==Fraction(1,(m-1)*(m-1))
        equal_mass_checks+=1

    print(
        "VERIFY_OK "
        f"decomposition_checks={decomposition_checks} "
        f"cut_covariance_checks={cut_covariance_checks} "
        f"cut_minimum_checks={cut_minimum_checks} "
        f"global_lower_checks={global_lower_checks} "
        f"affine_checks={affine_checks} "
        f"binary_checks={binary_checks} "
        f"boundary_checks={boundary_checks} "
        f"equal_mass_checks={equal_mass_checks}"
    )

if __name__=="__main__":
    run()
