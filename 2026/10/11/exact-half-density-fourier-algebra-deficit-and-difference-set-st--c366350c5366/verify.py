import cmath, itertools, math, random

def ft(p, A):
    return [sum(cmath.exp(-2j*math.pi*r*x/p) for x in A)/p for r in range(p)]

def normA(p, A):
    return sum(abs(z) for z in ft(p,A))

def stats(p,A):
    k=(p-1)//2
    c=math.sqrt(p+1)/(2*p)
    U=(p-1)*(1+math.sqrt(p+1))/(2*p)
    F=ft(p,A)
    deficit=U-sum(abs(z) for z in F)
    spectral=p/math.sqrt(p+1)*sum((abs(F[r])-c)**2 for r in range(1,p))
    lam=(p-3)/4
    V=sum((sum(1 for x in A if (x-t)%p in A)-lam)**2 for t in range(1,p))
    lo=4*V/(math.sqrt(p+1)*(p-1+math.sqrt(p+1))**2)
    hi=4*V/(p+1)**1.5
    return deficit,spectral,V,lo,hi

def isprime(n):
    if n<2:return False
    d=2
    while d*d<=n:
        if n%d==0:return False
        d+=1
    return True

maxerr=0.0; cases=0
for p in range(3,40,2):
    k=(p-1)//2
    for _ in range(40):
        A=set(random.sample(range(p),k))
        d,s,V,lo,hi=stats(p,A)
        maxerr=max(maxerr,abs(d-s))
        assert abs(d-s)<2e-11
        assert d+2e-11>=lo and d<=hi+2e-11
        cases+=1

for p in (7,11):
    k=(p-1)//2; U=(p-1)*(1+math.sqrt(p+1))/(2*p)
    for A in itertools.combinations(range(p),k):
        d,s,V,lo,hi=stats(p,set(A))
        assert normA(p,A)<=U+2e-11
        if abs(normA(p,A)-U)<2e-10:
            lam=(p-3)//4
            assert all(sum(1 for x in A if (x-t)%p in A)==lam for t in range(1,p))
        cases+=1

paley=0
for p in range(3,300):
    if p%4!=3 or not isprime(p): continue
    Q={x for x in range(1,p) if pow(x,(p-1)//2,p)==1}
    U=(p-1)*(1+math.sqrt(p+1))/(2*p)
    F=ft(p,Q); c=math.sqrt(p+1)/(2*p)
    assert abs(normA(p,Q)-U)<2e-10
    assert max(abs(abs(F[r])-c) for r in range(1,p))<2e-10
    lam=(p-3)//4
    assert all(sum(1 for x in Q if (x-t)%p in Q)==lam for t in range(1,p))
    paley+=1

print(f'VERIFY_OK random_and_exhaustive_cases={cases} paley_primes={paley} max_deficit_identity_err={maxerr:.3e}')
