#!/usr/bin/env python3
import cmath,itertools,math,random
omega=cmath.exp(2j*math.pi/3)

def enum_moment(a):
    n=len(a); total=0.0
    for x in itertools.product(range(3), repeat=n):
        z=sum(a[j]*(omega**x[j]) for j in range(n))
        total += abs(z)**6
    return total/(3**n)

def formula(a):
    S=sum(abs(z)**2 for z in a)
    Q=sum(abs(z)**4 for z in a)
    R=sum(abs(z)**6 for z in a)
    T=sum(z**3 for z in a)
    return 6*S**3-9*S*Q+3*R+abs(T)**2

def target6(n):
    return 6-8/n+3/(n*n)

rng=random.Random(314159)
identity=0
stress=0
extremizers=0
for n in range(2,7):
    for _ in range(14):
        a=[complex(rng.randint(-3,3),rng.randint(-3,3)) for _ in range(n)]
        if all(abs(z)==0 for z in a): a[0]=1
        e=enum_moment(a); f=formula(a)
        if not math.isclose(e,f,rel_tol=2e-11,abs_tol=2e-9):
            raise SystemExit(f'identity failure n={n} enum={e} formula={f}')
        identity+=1
    a=[omega**(j%3) for j in range(n)]
    ratio=enum_moment(a)/(sum(abs(z)**2 for z in a)**3)
    if not math.isclose(ratio,target6(n),rel_tol=2e-11,abs_tol=2e-10):
        raise SystemExit(f'extremizer failure n={n}: {ratio} vs {target6(n)}')
    extremizers+=1
    for _ in range(120):
        a=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(n)]
        S=sum(abs(z)**2 for z in a)
        v=formula(a)/(S**3)
        if v>target6(n)+1e-10:
            raise SystemExit(f'bound failure n={n}: {v} > {target6(n)}')
        stress+=1
print(f'VERIFY_OK identity_cases={identity} extremizers={extremizers} stress_cases={stress} n=2..6')
