"""Independent exact finite-state checks for tandem-exclusion transport crossover.

Run: python3 verify.py
Only standard Python libraries are required.
"""
from fractions import Fraction
from itertools import combinations, product
from collections import defaultdict
from decimal import Decimal, localcontext
from math import comb


def enumerated_current(n, k, q):
    norm = Fraction(0)
    flux = Fraction(0)
    counts = defaultdict(Fraction)
    active = []
    for word in product((0, 1), repeat=n):
        if sum(word) != k:
            continue
        heads = sum(word[i] * word[(i+1)%n] * (1-word[(i+2)%n]) for i in range(n))
        tails = sum(word[i] * (1-word[(i+1)%n]) * word[(i+2)%n] for i in range(n))
        if heads + tails == 0:
            continue
        r = sum(word[i]*(1-word[(i+1)%n]) for i in range(n))
        weight = q**(k-r)
        norm += weight
        flux += weight*(heads+q*tails)
        counts[r] += weight
        active.append(word)
    return flux/(n*norm), {r:c/norm for r,c in counts.items()}, active


def run_current(n, k, q):
    z=n-k
    norm=Fraction(0)
    flux=Fraction(0)
    weights=defaultdict(Fraction)
    for r in range(1,min(k,z)+1):
        amount=Fraction(n,r)*comb(k-1,r-1)*comb(z-1,r-1)
        weight=amount*q**(k-r)
        norm+=weight
        flux+=weight*(Fraction(r*(k-r),k-1)+q*Fraction(r*(r-1),z-1))
        weights[r]+=weight
    frozen=Fraction(n,k)*comb(n-2*k-1,k-1) if n>=3*k else 0
    norm-=frozen
    weights[k]-=frozen
    return flux/(n*norm),{r:w/norm for r,w in weights.items() if w}


def generator_balance(n, k, q):
    states={}
    for ix in combinations(range(n), k):
        word=tuple(int(i in ix) for i in range(n))
        if any(tuple(word[(j+h)%n] for h in range(3)) in ((1,1,0),(1,0,1)) for j in range(n)):
            states[word]=q**sum(word[j]*word[(j+1)%n] for j in range(n))
    net=defaultdict(Fraction)
    for word,w in states.items():
        for j in range(n):
            triple=tuple(word[(j+h)%n] for h in range(3))
            if triple==(1,1,0):
                i,ii=(j+1)%n,(j+2)%n
                rate=Fraction(1)
            elif triple==(1,0,1):
                i,ii=j,(j+1)%n
                rate=q
            else:
                continue
            dest=list(word)
            dest[i],dest[ii]=dest[ii],dest[i]
            dest=tuple(dest)
            assert dest in states
            net[word]-=rate*w
            net[dest]+=rate*w
    assert all(x==0 for x in net.values())
    return len(states)


def scaled_deficit(n, k, c):
    z=n-k
    with localcontext() as ctx:
        ctx.prec=75
        q=Decimal(str(c))*n*n
        weights=[]
        w=Decimal(1)
        for r in range(1,min(k,z)+1):
            weights.append(w)
            w*=Decimal((k-r)*(z-r))/(Decimal(r*(r+1))*q)
        norm=sum(weights)
        d=sum(w*Decimal((r-1)*(k*(k-r-1)+z*r))/Decimal((k-1)*(z-1)) for r,w in enumerate(weights,1))
        return d/norm


def bessel_cluster_mean(t):
    with localcontext() as ctx:
        ctx.prec=75
        t=Decimal(str(t))
        denominator=Decimal(0)
        numerator=Decimal(0)
        term=Decimal(1)
        for s in range(200):
            denominator+=term
            numerator+=s*term
            term*=t/Decimal((s+1)*(s+2))
        assert term<Decimal('1e-60')
        return numerator/denominator


def main():
    triples=0
    generator_states=0
    for n in range(4,12):
        for k in range(2,n-1):
            for q in (Fraction(1,3),Fraction(1),Fraction(5),Fraction(17,2)):
                x,c1,_=enumerated_current(n,k,q)
                y,c2=run_current(n,k,q)
                assert x==y and c1==c2, (n,k,q,x,y,c1,c2)
                triples+=1
            for q in (Fraction(1,3),Fraction(3),Fraction(7,2)):
                generator_states+=generator_balance(n,k,q)
    print('PASS: exact current and run census,',triples,'parameter configurations')
    print('PASS: stationary weighted generator,',generator_states,'state-parameter pairs')
    for rho,c in ((.25,.2),(.4,1),(.5,.75),(.65,2.5),(.75,10)):
        t=rho*(1-rho)/c
        with localcontext() as ctx:
            ctx.prec=75
            limit=Decimal(str(rho))/Decimal(str(1-rho))*bessel_cluster_mean(t)
            errors=[]
            for n in (40,80,160,320,640):
                k=round(rho*n)
                # The ratio in this test uses K/n rather than the nominal rho.
                errors.append(abs(scaled_deficit(n,k,c)-limit))
            print('rho,c',rho,c,'predicted',float(limit),'absolute errors', [float(v) for v in errors])
            assert errors[-1]<errors[0] and errors[-1]<Decimal('.004')
    print('PASS: Bessel-series crossover checks')


if __name__=='__main__':
    main()
