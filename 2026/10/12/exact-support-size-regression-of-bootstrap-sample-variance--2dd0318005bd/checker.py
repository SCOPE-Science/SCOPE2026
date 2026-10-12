from fractions import Fraction
from itertools import product

def stirling_table(N):
    S=[[0]*(N+1) for _ in range(N+1)]
    S[0][0]=1
    for n in range(1,N+1):
        for k in range(1,n+1):
            S[n][k]=S[n-1][k-1]+k*S[n-1][k]
    return S

def sample_var(vals):
    n=len(vals)
    mean=sum(vals,Fraction())/n
    return sum((v-mean)**2 for v in vals)/(n-1)

def verify_profile(xs,S):
    n=len(xs)
    orig=sample_var(xs)
    rows=[]
    byk={k:[] for k in range(1,n+1)}
    for idx in product(range(n), repeat=n):
        ys=[xs[i] for i in idx]
        k=len(set(idx))
        v=sample_var(ys)
        rows.append((k,v))
        byk[k].append(v)
    N=n**n
    EK=sum((Fraction(k,N) for k,v in rows),Fraction())
    EV=sum((Fraction(v,N) for k,v in rows),Fraction())
    EKV=sum((Fraction(k*v,N) for k,v in rows),Fraction())
    cov=EKV-EK*EV
    p0=Fraction(n-1,n)**n
    assert cov == p0*orig/Fraction(n-1)
    cond_checks=0
    for k,vals in byk.items():
        assert vals
        mean=sum(vals,Fraction())/len(vals)
        q=Fraction(S[n-1][k],S[n][k])
        assert mean == (1-q)*orig
        cond_checks += 1
    assert EV == Fraction(n-1,n)*orig
    return N,cond_checks

def run():
    S=stirling_table(200)
    profiles=0
    resamples=0
    conditional_checks=0
    covariance_checks=0
    mean_checks=0
    for n in range(2,7):
        data_profiles=[
            [Fraction(i) for i in range(n)],
            [Fraction(i*i+2*i+1) for i in range(n)],
            [Fraction((-1)**i*(i+1)) for i in range(n)],
        ]
        for xs in data_profiles:
            N,c=verify_profile(xs,S)
            profiles += 1
            resamples += N
            conditional_checks += c
            covariance_checks += 1
            mean_checks += 1

    stirling_checks=0
    coefficient_checks=0
    for n in range(2,201):
        for k in range(1,n+1):
            assert S[n][k] == S[n-1][k-1] + k*S[n-1][k]
            stirling_checks += 1
            q=Fraction(S[n-1][k],S[n][k])
            assert Fraction(0) <= q <= Fraction(1)
            if k==1:
                assert q==1
            if k==n:
                assert q==0
            coefficient_checks += 1

    print("VERIFY_OK")
    print(f"profiles={profiles}")
    print(f"ordered_resamples={resamples}")
    print(f"conditional_mean_checks={conditional_checks}")
    print(f"covariance_checks={covariance_checks}")
    print(f"unconditional_mean_checks={mean_checks}")
    print(f"stirling_recurrence_checks={stirling_checks}")
    print(f"coefficient_checks={coefficient_checks}")

if __name__=="__main__":
    run()
