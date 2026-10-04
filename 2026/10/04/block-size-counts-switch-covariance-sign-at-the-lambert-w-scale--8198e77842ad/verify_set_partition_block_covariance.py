from fractions import Fraction
from math import comb
import math

def rgs_partitions(n):
    if n == 0:
        yield ()
        return
    a=[0]*n
    a[0]=0
    def rec(pos,mx):
        if pos==n:
            yield tuple(a)
            return
        for v in range(mx+2):
            a[pos]=v
            yield from rec(pos+1,max(mx,v))
    yield from rec(1,0)

def stats(a):
    if not a:
        return 0, {}
    counts={}
    for v in a:
        counts[v]=counts.get(v,0)+1
    sizes={}
    for s in counts.values():
        sizes[s]=sizes.get(s,0)+1
    return len(counts), sizes

def bells(N):
    B=[0]*(N+2)
    B[0]=1
    for n in range(N+1):
        B[n+1]=sum(comb(n,k)*B[k] for k in range(n+1))
    return B

def lambert_w_newton(x):
    w=math.log(x)
    if x>math.e:
        w-=math.log(max(1.0,w))
    for _ in range(40):
        ew=math.exp(w)
        f=w*ew-x
        den=ew*(w+1)-((w+2)*f)/(2*w+2)
        nw=w-f/den
        if abs(nw-w)<1e-14:
            return nw
        w=nw
    return w

def run():
    B=bells(301)
    enumerated=0
    mean_checks=0
    palm_checks=0
    covariance_checks=0
    monotone_checks=0
    threshold_checks=0
    asymptotic_sanity_checks=0

    cache={m:[stats(a)[0] for a in rgs_partitions(m)] for m in range(10)}
    for n in range(1,10):
        rows=[]
        for a in rgs_partitions(n):
            K,sizes=stats(a)
            rows.append((K,sizes))
            enumerated+=1
        assert len(rows)==B[n]
        N=B[n]
        EK=Fraction(sum(K for K,_ in rows),N)
        assert EK==Fraction(B[n+1],B[n])-1

        for r in range(1,n+1):
            EX=Fraction(sum(sizes.get(r,0) for _,sizes in rows),N)
            target_EX=Fraction(comb(n,r)*B[n-r],B[n])
            assert EX==target_EX
            mean_checks+=1

            vals=cache[n-r]
            for power in (0,1,2):
                lhs=Fraction(sum(sizes.get(r,0)*(K**power) for K,sizes in rows),N)
                rhs_inner=Fraction(sum((1+k)**power for k in vals),B[n-r])
                assert lhs==EX*rhs_inner
                palm_checks+=1

            for t in range(1,n+1):
                lhs=Fraction(sum(sizes.get(r,0)*int(K==t) for K,sizes in rows),N)
                rhs_inner=Fraction(sum(int(1+k==t) for k in vals),B[n-r])
                assert lhs==EX*rhs_inner
                palm_checks+=1

            EKX=Fraction(sum(K*sizes.get(r,0) for K,sizes in rows),N)
            cov=EKX-EK*EX
            bracket=Fraction(1)+Fraction(B[n-r+1],B[n-r])-Fraction(B[n+1],B[n])
            assert cov==EX*bracket
            covariance_checks+=1

    for n in range(2,301):
        qs=[Fraction(B[m+1],B[m]) for m in range(n+1)]
        cs=[Fraction(1)+qs[n-r]-qs[n] for r in range(1,n+1)]
        assert all(cs[i]>cs[i+1] for i in range(len(cs)-1))
        assert cs[-1] < 0
        monotone_checks+=1
        t=next(r for r,c in enumerate(cs,1) if c<=0)
        assert all(c>0 for c in cs[:t-1])
        assert all(c<0 for c in cs[t:])
        threshold_checks+=1

    for n in (30,50,80,120,180,250,300):
        qs=[Fraction(B[m+1],B[m]) for m in range(n+1)]
        cs=[Fraction(1)+qs[n-r]-qs[n] for r in range(1,n+1)]
        t=next(r for r,c in enumerate(cs,1) if c<=0)
        alpha=lambert_w_newton(n+1)
        ratio=t/(alpha+1)
        assert 0.75 < ratio < 1.35
        asymptotic_sanity_checks+=1

    print(
        'VERIFY_OK '
        f'partitions_enumerated={enumerated} '
        f'mean_checks={mean_checks} '
        f'palm_checks={palm_checks} '
        f'covariance_checks={covariance_checks} '
        f'monotone_checks={monotone_checks} '
        f'threshold_checks={threshold_checks} '
        f'asymptotic_sanity_checks={asymptotic_sanity_checks}'
    )

if __name__=='__main__':
    run()
