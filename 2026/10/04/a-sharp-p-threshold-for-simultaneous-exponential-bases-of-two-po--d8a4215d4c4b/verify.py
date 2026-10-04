import cmath
import itertools
import math


def elems(mods):
    return list(itertools.product(*[range(n) for n in mods]))


def add(a,b,mods):
    return tuple((x+y)%n for x,y,n in zip(a,b,mods))


def sub(a,b,mods):
    return tuple((x-y)%n for x,y,n in zip(a,b,mods))


def char(k,x,mods):
    phase=sum(ki*xi/n for ki,xi,n in zip(k,x,mods))
    return cmath.exp(2j*math.pi*phase)


def det_nonzero(E,B,mods,tol=1e-9):
    x,y=E
    a,b=B
    det=char(a,x,mods)*char(b,y,mods)-char(b,x,mods)*char(a,y,mods)
    return abs(det)>tol


def quotient(b,a,mods):
    return tuple((bi-ai)%n for ai,bi,n in zip(a,b,mods))


def annihilates(k,d,mods,tol=1e-9):
    return abs(char(k,d,mods)-1)<tol


def least_prime_divisor(n):
    for p in range(2,n+1):
        if n%p==0 and all(p%q for q in range(2,int(p**0.5)+1)):
            return p
    raise AssertionError


def check_group(mods):
    G=elems(mods)
    dual=G
    twos=list(itertools.combinations(G,2))
    # Exact determinant criterion for every two-point set and every ordered distinct character pair.
    for E in twos:
        d=sub(E[1],E[0],mods)
        for a,b in itertools.permutations(dual,2):
            psi=quotient(b,a,mods)
            assert det_nonzero(E,(a,b),mods)==(not annihilates(psi,d,mods))
    # Every pair of two-point subsets has a common basis.
    for E1,E2 in itertools.combinations_with_replacement(twos,2):
        found=False
        for a,b in itertools.combinations(dual,2):
            if det_nonzero(E1,(a,b),mods) and det_nonzero(E2,(a,b),mods):
                found=True
                break
        assert found, (mods,E1,E2)
    # For groups small enough, directly check every family up to the least-prime threshold.
    p=least_prime_divisor(math.prod(mods))
    if len(twos)<=28:
        for m in range(1,p+1):
            for fam in itertools.combinations(twos,m):
                diffs=[sub(E[1],E[0],mods) for E in fam]
                assert any(all(not annihilates(k,d,mods) for d in diffs) for k in dual)


def sharp_prime(p):
    mods=(p,p)
    G=elems(mods)
    # Representatives (1,t), plus the vertical direction (0,1).
    ds=[(1,t) for t in range(p)]+[(0,1)]
    assert len(ds)==p+1
    dual=G
    union=set()
    kernels=[]
    for d in ds:
        ker={k for k in dual if annihilates(k,d,mods)}
        assert len(ker)==p
        kernels.append(ker)
        union |= ker
    assert len({frozenset(k) for k in kernels})==p+1
    assert union==set(dual)
    # Hence no two-character basis works for E_d={0,d} simultaneously.
    zero=(0,0)
    fam=[(zero,d) for d in ds]
    assert not any(all(det_nonzero(E,(a,b),mods) for E in fam) for a,b in itertools.combinations(dual,2))


for mods in [(2,2),(3,),(4,),(2,3),(2,4),(3,3)]:
    check_group(mods)
for p in [2,3,5,7]:
    sharp_prime(p)
print('VERIFY_OK')
