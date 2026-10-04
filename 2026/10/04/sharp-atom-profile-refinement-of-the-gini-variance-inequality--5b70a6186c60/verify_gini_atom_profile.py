#!/usr/bin/env python3
from fractions import Fraction
import random

def moments(xs, ps):
    mu=sum(x*p for x,p in zip(xs,ps))
    var=sum(p*(x-mu)*(x-mu) for x,p in zip(xs,ps))
    return mu,var

def midranks(ps):
    out=[]
    c=Fraction(0)
    for p in ps:
        out.append(c+p/2)
        c+=p
    assert c==1
    return out

def gmd(xs,ps):
    return sum(ps[i]*ps[j]*abs(xs[i]-xs[j])
               for i in range(len(xs)) for j in range(len(xs)))

def cov_xy(xs,ys,ps):
    ex=sum(p*x for p,x in zip(ps,xs))
    ey=sum(p*y for p,y in zip(ps,ys))
    return sum(p*(x-ex)*(y-ey) for p,x,y in zip(ps,xs,ys))

def minmax_corr(xs,ps):
    ey=ez=ey2=ez2=eyz=Fraction(0)
    for i,x in enumerate(xs):
        for j,z0 in enumerate(xs):
            w=ps[i]*ps[j]
            y=min(x,z0); z=max(x,z0)
            ey+=w*y; ez+=w*z
            ey2+=w*y*y; ez2+=w*z*z; eyz+=w*y*z
    vy=ey2-ey*ey; vz=ez2-ez*ez; cv=eyz-ey*ez
    return cv,vy,vz

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def run():
    rng=random.Random(20261002)
    identity_checks=0
    inequality_checks=0
    equality_checks=0
    cardinality_checks=0
    symmetry_checks=0
    uniform_checks=0

    for _ in range(24000):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,25) for __ in range(m)])
        gaps=[rng.randrange(1,20) for __ in range(m-1)]
        xs=[Fraction(0)]
        for g in gaps:
            xs.append(xs[-1]+Fraction(g,rng.randrange(1,8)))

        mu,var=moments(xs,ps)
        q=midranks(ps)
        delta=gmd(xs,ps)
        cv=cov_xy(xs,q,ps)
        s3=sum(p**3 for p in ps)
        mq=sum(p*qv for p,qv in zip(ps,q))
        vq=sum(p*(qv-mq)**2 for p,qv in zip(ps,q))

        assert mq==Fraction(1,2)
        assert delta==4*cv
        assert vq==Fraction(1,12)*(1-s3)
        identity_checks += 3

        assert delta*delta <= Fraction(4,3)*(1-s3)*var
        inequality_checks += 1

        N=m+rng.randrange(0,5)
        assert s3 >= Fraction(1,N*N)
        assert delta*delta <= Fraction(4*(N*N-1),3*N*N)*var
        cardinality_checks += 2

        # Equality support: affine in the midranks.
        xe=[Fraction(7,5)+Fraction(13,4)*qv for qv in q]
        _,vare=moments(xe,ps)
        de=gmd(xe,ps)
        assert de*de == Fraction(4,3)*(1-s3)*vare
        for i in range(m-1):
            assert xe[i+1]-xe[i] == Fraction(13,8)*(ps[i]+ps[i+1])
        equality_checks += m

    # Reflection-symmetric profiles: exact min-max correlation.
    for _ in range(9000):
        m=rng.randrange(2,9)
        raw=[rng.randrange(1,20) for __ in range((m+1)//2)]
        if m%2==0:
            full=raw+raw[::-1]
        else:
            full=raw+raw[-2::-1]
        ps=normalize(full)
        q=midranks(ps)
        xs=[2*qv-1 for qv in q]
        # Exact symmetry.
        for i in range(m):
            assert ps[i]==ps[m-1-i]
            assert xs[i]==-xs[m-1-i]
        cv,vy,vz=minmax_corr(xs,ps)
        assert vy==vz and vy>0
        s3=sum(p**3 for p in ps)
        target=Fraction(1)-s3
        # corr = target/(2+s3), checked cross-multiplied.
        assert cv*(2+s3)==vy*target
        symmetry_checks += 1

    # Uniform arithmetic progressions recover the N-point constants.
    for N in range(2,101):
        ps=[Fraction(1,N)]*N
        xs=[Fraction(i) for i in range(N)]
        _,var=moments(xs,ps)
        d=gmd(xs,ps)
        assert d*d == Fraction(4*(N*N-1),3*N*N)*var
        s3=Fraction(1,N*N)
        # For centered arithmetic progression the min-max correlation is exact.
        cv,vy,vz=minmax_corr(xs,ps)
        assert vy==vz
        assert cv*(2+s3)==vy*(1-s3)
        uniform_checks += 2

    print(
        "VERIFY_OK "
        f"identity_checks={identity_checks} "
        f"inequality_checks={inequality_checks} "
        f"equality_checks={equality_checks} "
        f"cardinality_checks={cardinality_checks} "
        f"symmetry_checks={symmetry_checks} "
        f"uniform_checks={uniform_checks}"
    )

if __name__=="__main__":
    run()
