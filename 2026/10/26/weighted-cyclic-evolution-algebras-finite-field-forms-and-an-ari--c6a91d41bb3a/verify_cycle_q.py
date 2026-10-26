"""Exact modular-exponent verification of weighted cycle classification.

No external packages; coefficients are exponents of a fixed primitive element.
The program checks every weight tuple for modest groups and dimensions,
then checks every predicted rotation and the splitting condition by enumeration.
"""
from math import gcd, lcm
from itertools import product

def check(Q,n):
    N=2**n-1
    g=gcd(Q,N)
    classes={}
    for A in product(range(Q),repeat=n):
        a=sum((2**(n-1-j))*A[j] for j in range(n))%g
        orb=tuple(sorted({(2**k*a)%g for k in range(n)}))
        classes[orb]=classes.get(orb,0)+1
    predicted=set()
    for a in range(g):
        predicted.add(tuple(sorted({(2**k*a)%g for k in range(n)})))
    assert set(classes)==predicted
    # Independent orbit census from the actual generators of natural-basis changes.
    if Q**n<=3000:
        all_weights=set(product(range(Q),repeat=n))
        components=[]
        while all_weights:
            seed=all_weights.pop()
            visited={seed}
            todo=[seed]
            while todo:
                A=todo.pop()
                moves=[A[1:]+A[:1]]
                for j in range(n):
                    B=list(A)
                    B[j]=(B[j]+2)%Q
                    B[(j-1)%n]=(B[(j-1)%n]-1)%Q
                    moves.append(tuple(B))
                for B in moves:
                    if B not in visited:
                        visited.add(B)
                        all_weights.discard(B)
                        todo.append(B)
            orbitkeys={tuple(sorted({(2**k*sum(2**(n-1-i)*B[i] for i in range(n)))%g for k in range(n)})) for B in visited}
            assert len(orbitkeys)==1,(Q,n,seed,orbitkeys)
            components.append(next(iter(orbitkeys)))
        assert set(components)==predicted and len(components)==len(predicted)
    for a in range(g):
        d=g//gcd(g,a)
        h=1
        while pow(2,h,d if d>1 else 1)!=1%(d if d>1 else 1):
            h+=1
        assert n%h==0
        lifts=[]
        for k in range(n):
            actual=[u for u in range(Q) if (N*u-a*(1-2**k))%Q==0]
            expect=(g if k%h==0 else 0)
            assert len(actual)==expect,(Q,n,a,k,actual,expect)
            if k==h and h<n:
                lifts=actual
        m=n//h
        S=N//(2**h-1)
        predicted_split=(a%gcd(Q,S)==0)
        brute_split=True if m==1 else any((S*u+a)%Q==0 for u in lifts)
        assert predicted_split==brute_split,(Q,n,a,d,h,lifts,S)
    return len(classes)

def main():
    cases=[(Q,n) for Q in [1,2,3,4,6,7,8,10,12,15,18,24,63] for n in range(2,7) if Q**n<=16000]
    for Q,n in cases:
        check(Q,n)
    # Larger examples: direct congruence and class arithmetic, no tuple census.
    for Q,n in [(63,6),(18,6),(15,4),(6,6),(48,6),(255,8)]:
        N=2**n-1;g=gcd(Q,N)
        for a in range(g):
            d=g//gcd(g,a)
            h=next(h for h in range(1,n+1) if (2**h-1)%d==0)
            S=N//(2**h-1)
            predicted=(a%gcd(Q,S)==0)
            matches=([u for u in range(Q) if (S*u+a)%Q==0])
            assert bool(matches)==predicted
    print('VERIFY_OK',len(cases),'complete weight censuses, direct change-of-basis orbit checks for small cases, and six larger congruence sweeps')

if __name__=='__main__':main()
