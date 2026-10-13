from fractions import Fraction
from itertools import permutations

def weight_systems(n):
    return [
        {(a,b): a + 2*b for a in range(1,n+1) for b in range(a+1,n+1)},
        {(a,b): (b-a)**2 - a for a in range(1,n+1) for b in range(a+1,n+1)},
        {(a,b): (-1)**(a+b) * (a*b + b) for a in range(1,n+1) for b in range(a+1,n+1)},
    ]

def score(p,w):
    n=len(p)
    return sum(w[(a,b)] for a in range(1,n+1) for b in range(a+1,n+1)
               if p[a-1] > p[b-1])

def inv(p):
    n=len(p)
    return sum(1 for a in range(n) for b in range(a+1,n) if p[a] > p[b])

def run():
    perm_count=0
    ordinary_local_checks=0
    conditional_checks=0
    weighted_checks=0
    aggregate_checks=0
    for n in range(2,10):
        ps=list(permutations(range(1,n+1)))
        N=len(ps)
        perm_count += N
        invs=[inv(p) for p in ps]
        mean_inv=Fraction(sum(invs),N)
        assert mean_inv == Fraction(n*(n-1),4)

        fixed=[[1 if p[i-1]==i else 0 for i in range(1,n+1)] for p in ps]
        for i in range(1,n+1):
            sfi=sum(f[i-1] for f in fixed)
            assert sfi* n == N
            sfI=sum(f[i-1]*x for f,x in zip(fixed,invs))
            cov=Fraction(sfI,N)-Fraction(sfi,N)*mean_inv
            want=-Fraction((n+1-2*i)**2,2*n*(n-1))
            assert cov == want
            ordinary_local_checks += 1

            cond=Fraction(sfI,sfi)
            want_cond=Fraction(n*(n-1),4)-Fraction((n+1-2*i)**2,2*(n-1))
            assert cond == want_cond
            conditional_checks += 1

        Ftot=[sum(f) for f in fixed]
        covtot=Fraction(sum(a*b for a,b in zip(Ftot,invs)),N)-Fraction(sum(Ftot),N)*mean_inv
        assert covtot == -Fraction(n+1,6)
        aggregate_checks += 1

        for w in weight_systems(n):
            vals=[score(p,w) for p in ps]
            mean=Fraction(sum(vals),N)
            for i in range(1,n+1):
                sf=sum(f[i-1] for f in fixed)
                cross=sum(f[i-1]*x for f,x in zip(fixed,vals))
                cov=Fraction(cross,N)-Fraction(sf,N)*mean
                L=sum(w[(a,i)] for a in range(1,i))
                R=sum(w[(i,b)] for b in range(i+1,n+1))
                want=Fraction((n+1-2*i)*(L-R),2*n*(n-1))
                assert cov == want
                weighted_checks += 1

    print("VERIFY_OK")
    print(f"permutations_enumerated={perm_count}")
    print(f"ordinary_local_checks={ordinary_local_checks}")
    print(f"conditional_mean_checks={conditional_checks}")
    print(f"weighted_local_checks={weighted_checks}")
    print(f"aggregate_checks={aggregate_checks}")
    print("max_n=9")

if __name__=="__main__":
    run()
