#!/usr/bin/env python3
from fractions import Fraction
import random

F=Fraction

def normalize(d):
    s=sum(d.values(),F(0))
    return {x:w/s for x,w in d.items() if w}

def push_G(nu):
    G={}
    for lam,w in nu.items():
        x=lam*lam
        G[x]=G.get(x,F(0))+(1+lam)*w
    return {x:w for x,w in G.items() if w}

def moment(d,k):
    return sum(w*x**k for x,w in d.items())

def paired(nu,k):
    return moment(nu,2*k)+moment(nu,2*k+1)

def split_from_nu(nu,G):
    eta={}
    for x,g in G.items():
        if x==1:
            continue
        if x==0:
            eta[x]=F(1)  # branch label is immaterial at zero
            continue
        # test generator uses rational square roots already present
        roots=[lam for lam in nu if lam*lam==x and lam>0]
        s=roots[0] if roots else next(-lam for lam in nu if lam*lam==x and lam<0)
        alpha=nu.get(s,F(0))
        eta[x]=(1+s)*alpha/g
        assert 0<=eta[x]<=1
    return eta

def reconstruct(G,eta):
    nu={}
    T=F(0)
    for x,g in G.items():
        if x==1:
            w=g/2
            nu[F(1)]=nu.get(F(1),F(0))+w
            T+=w
            continue
        # x values in tests are perfect rational squares
        s=None
        for den in range(1,61):
            n2=x.numerator*den*den
            d2=x.denominator
            n=int((n2//d2)**0.5) if d2 and n2%d2==0 else -1
            if n>=0 and F(n,den)**2==x:
                s=F(n,den); break
        if s is None:
            raise AssertionError(("no rational sqrt",x))
        e=eta.get(x,F(1))
        wp=e*g/(1+s)
        wm=(1-e)*g/(1-s) if s!=1 else F(0)
        nu[s]=nu.get(s,F(0))+wp
        nu[-s]=nu.get(-s,F(0))+wm
        T+=wp+wm
    assert T<=1
    nu[F(-1)]=nu.get(F(-1),F(0))+(1-T)
    return {x:w for x,w in nu.items() if w}

def J_of_G(G):
    out=F(0)
    for x,g in G.items():
        # rational sqrt finder for generated supports
        s=None
        for den in range(1,61):
            n2=x.numerator*den*den
            d2=x.denominator
            n=int((n2//d2)**0.5) if d2 and n2%d2==0 else -1
            if n>=0 and F(n,den)**2==x:
                s=F(n,den); break
        assert s is not None
        out+=g/(1+s)
    return out

def two_state_eigen(lam):
    # P * (1,-1)^T = lam * (1,-1)^T
    a=(1+lam)/2
    b=(1-lam)/2
    return (a-b, b-a)

def run():
    rng=random.Random(20261002)
    fiber_checks=0
    moment_checks=0
    compat_checks=0
    eigen_checks=0

    vals=[F(i,12) for i in range(-11,12)]
    for _ in range(12000):
        support=rng.sample(vals,rng.randrange(1,min(6,len(vals))+1))
        raw=[rng.randrange(1,30) for __ in support]
        nu=normalize(dict(zip(support,raw)))
        G=push_G(nu)
        eta=split_from_nu(nu,G)
        rec=reconstruct(G,eta)
        assert rec==nu
        assert J_of_G(G)<=1
        fiber_checks+=1
        compat_checks+=1
        for k in range(11):
            assert paired(nu,k)==moment(G,k)
            assert paired(rec,k)==moment(G,k)
            moment_checks+=2
        for lam in support:
            u,v=two_state_eigen(lam)
            assert u==lam and v==-lam
            eigen_checks+=1

    A={
        F(1,2):F(1,3),
        F(1,3):F(1,12),
        F(-1,3):F(7,12),
    }
    B={
        F(1,2):F(3,16),
        F(-1,2):F(7,16),
        F(1,3):F(3,8),
    }
    GA=push_G(A); GB=push_G(B)
    expected={F(1,4):F(1,2),F(1,9):F(1,2)}
    assert GA==GB==expected
    assert moment(A,1)==moment(B,1)==0
    assert moment(A,2)==F(17,108)
    assert moment(B,2)==F(19,96)
    assert moment(A,3)==F(5,216)
    assert moment(B,3)==-F(5,288)
    for k in range(40):
        target=F(1,2)*F(1,4)**k+F(1,2)*F(1,9)**k
        assert paired(A,k)==paired(B,k)==target
        moment_checks+=2

    sum_gamma=F(1,2)/(1-F(1,4))+F(1,2)/(1-F(1,9))
    tau=-1+2*sum_gamma
    assert tau==F(35,24)
    V3A=(3+4*moment(A,1)+2*moment(A,2))/9
    V3B=(3+4*moment(B,1)+2*moment(B,2))/9
    assert V3A==F(179,486)
    assert V3B==F(163,432)
    assert V3A!=V3B

    # Exact uniqueness sanity checks at finite support.
    # J=1 forces all nontrivial mass to the positive branch.
    Guniq={F(1,4):F(3,2)}
    assert J_of_G(Guniq)==1
    rec=reconstruct(Guniq,{F(1,4):F(1)})
    assert rec=={F(1,2):F(1)}

    # Interior mass plus positive slack admits two distinct fibers.
    assert J_of_G(expected)<1
    A2=reconstruct(expected,{F(1,4):F(1),F(1,9):F(2,9)})
    B2=reconstruct(expected,{F(1,4):F(9,16),F(1,9):F(1)})
    assert A2==A and B2==B and A2!=B2
    fiber_checks+=2
    compat_checks+=2

    print(
        "VERIFY_OK "
        f"fiber_reconstruction_checks={fiber_checks} "
        f"paired_moment_checks={moment_checks} "
        f"compatibility_checks={compat_checks} "
        f"two_state_eigen_checks={eigen_checks} "
        "explicit_alias_pair=passed"
    )

if __name__=="__main__":
    run()
