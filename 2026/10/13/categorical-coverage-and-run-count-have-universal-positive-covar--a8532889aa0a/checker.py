from fractions import Fraction
from itertools import product

def stats(word):
    k=len(set(word))
    t=sum(word[i]!=word[i+1] for i in range(len(word)-1))
    return k,t

def formula(ps,n):
    s2=sum(p*p for p in ps)
    return (n-1)*sum(
        p*(1-p)**(n-2)*(2*s2-(1+s2)*p)
        for p in ps
    )

def exact_enum(weights,n):
    total=sum(weights)
    ps=[Fraction(w,total) for w in weights]
    EK=Fraction(0)
    ET=Fraction(0)
    EKT=Fraction(0)
    for word in product(range(len(weights)), repeat=n):
        prob=Fraction(1)
        for x in word:
            prob*=ps[x]
        k,t=stats(word)
        EK+=prob*k
        ET+=prob*t
        EKT+=prob*k*t
    return ps,EKT-EK*ET

def conditional_uniform(m,n):
    num_diff=0
    sum_diff=0
    num_same=0
    sum_same=0
    for word in product(range(m),repeat=n):
        k=len(set(word))
        if word[0]!=word[1]:
            num_diff+=1
            sum_diff+=k
        else:
            num_same+=1
            sum_same+=k
    return Fraction(sum_diff,num_diff)-Fraction(sum_same,num_same)

def check_tilt(weights,max_t=30):
    total=sum(weights)
    ps=[Fraction(w,total) for w in weights]
    s2=sum(p*p for p in ps)
    prev=None
    checks=0
    for t in range(max_t+1):
        U=sum(p*(1-p)**t for p in ps)
        V=sum(p*p*(1-p)**t for p in ps)
        W=sum(p*p*p*(1-p)**t for p in ps)
        rho=V/U
        assert V*V <= U*W
        assert rho <= s2
        if prev is not None:
            assert rho <= prev
        prev=rho
        checks+=2
    return checks

def compositions(total,m,prefix=()):
    if m==1:
        yield prefix+(total,)
        return
    for x in range(1,total-m+2):
        yield from compositions(total-x,m-1,prefix+(x,))

def run():
    profiles=[
        (1,1),(2,1),(3,1),(1,1,1),(3,2,1),(5,2,1),(2,3,4),(5,3,2,1)
    ]
    enumeration_checks=0
    words_weighted=0
    for weights in profiles:
        m=len(weights)
        max_n=6 if m<=3 else 5
        for n in range(2,max_n+1):
            ps,cov=exact_enum(weights,n)
            assert cov==formula(ps,n)
            assert cov>0
            enumeration_checks+=2
            words_weighted+=m**n

    uniform_checks=0
    conditional_checks=0
    for m in range(2,8):
        ps=[Fraction(1,m)]*m
        for n in range(2,10):
            cov=formula(ps,n)
            target=Fraction((n-1)*(m-1),m*m)*Fraction(m-1,m)**(n-2)
            assert cov==target
            assert cov>0
            uniform_checks+=2
            if m**n <= 200000:
                gap=conditional_uniform(m,n)
                assert gap==Fraction(m-1,m)**(n-2)
                conditional_checks+=1

    tilt_checks=0
    profile_count=0
    for m in range(2,6):
        for total in range(m,13):
            for weights in compositions(total,m):
                tilt_checks += check_tilt(weights,20)
                profile_count+=1

    print("VERIFY_OK")
    print(f"weighted_words_enumerated={words_weighted}")
    print(f"enumeration_formula_and_sign_checks={enumeration_checks}")
    print(f"uniform_formula_and_sign_checks={uniform_checks}")
    print(f"conditional_gap_checks={conditional_checks}")
    print(f"tilted_ratio_profiles={profile_count}")
    print(f"tilted_ratio_checks={tilt_checks}")

if __name__=="__main__":
    run()
