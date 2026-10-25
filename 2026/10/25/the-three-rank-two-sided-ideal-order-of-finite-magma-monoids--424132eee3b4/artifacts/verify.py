"""Reproducible finite checks for Green J-preorder of equivariant binary-operation monoids.

Only finite sizes are enumerated; the general result rests on a separate proof.
"""
import itertools
import random
from collections import Counter

def orbit_count(n):
    return n*(n-1)//2

def compose(f,g,n):
    """g after f, fixed labels <n and free labels n+2*j+sign."""
    N=orbit_count(n)
    out=[g[f[i]] for i in range(n)]
    for t in f[n:]:
        if t<n: out.append(g[t])
        else:
            j,sign=divmod(t-n,2)
            image=g[n+j]
            out.append(image if image<n else n+((image-n)^sign))
    return tuple(out)

def kind(f,n):
    c=len(set(f[:n]))
    d=len({x for x in f if x<n})
    a=len({(x-n)//2 for x in f[n:] if x>=n})
    return (c,d,a)

def dominates(f,h,n):
    c,d,a=kind(f,n)
    C,D,A=kind(h,n)
    return C<=c and A<=a and D+A<=d+a

def factor(f,h,n):
    """If kind(h) is below kind(f), return v,u with h=u ∘ f ∘ v.

    First choose distinct intermediate image orbits for each target image orbit,
    reserving f(F) for those hit from h(F), then lift through f.
    """
    N=orbit_count(n)
    assert dominates(f,h,n)
    mf=sorted(set(f[:n]))
    fixed=sorted({x for x in f if x<n})
    free=sorted({(x-n)//2 for x in f[n:] if x>=n})
    marked=sorted(set(h[:n]))
    allfixed=sorted({x for x in h if x<n})
    allfree=sorted({(x-n)//2 for x in h[n:] if x>=n})
    resources={}
    used=set()
    for target,res in zip(marked,mf):
        resources[('F',target)]=('F',res)
        used.add(('F',res))
    for target,res in zip(allfree,free):
        resources[('P',target)]=('P',res)
        used.add(('P',res))
    remaining=[('F',i) for i in fixed if ('F',i) not in used]
    remaining += [('P',i) for i in free if ('P',i) not in used]
    unmet=[x for x in allfixed if x not in marked]
    assert len(unmet)<=len(remaining)
    for target,res in zip(unmet,remaining):
        resources[('F',target)]=res
    u=[0]*(n+N)
    for (k,target),(rk,res) in resources.items():
        if rk=='F':
            assert k=='F'
            u[res]=target
        elif k=='F':
            u[n+res]=target
        else:
            u[n+res]=n+2*target
    # Select v to lift f values selected by resources.
    v=[]
    for target in h[:n]:
        rk,res=resources[('F',target)]
        assert rk=='F'
        v.append(next(i for i,x in enumerate(f[:n]) if x==res))
    for q in h[n:]:
        if q<n: rk,res=resources[('F',q)]
        else:
            j,sign=divmod(q-n,2)
            rk,res=resources[('P',j)]
        if rk=='F':
            v.append(next((i for i,x in enumerate(f[:n]) if x==res),None))
            if v[-1] is None:
                v[-1]=n+2*next(i for i,x in enumerate(f[n:]) if x==res)
        else:
            k=next(i for i,x in enumerate(f[n:]) if x>=n and (x-n)//2==res)
            input_sign=(0 if q<n else (q-n)%2) ^ ((f[n+k]-n)%2)
            v.append(n+2*k+input_sign)
    assert compose(compose(tuple(v),f,n),tuple(u),n)==h, (f,h,u,v)
    return tuple(v),tuple(u)

def allmaps(n):
    N=orbit_count(n)
    yield from (p+q for p in itertools.product(range(n),repeat=n)
                         for q in itertools.product(range(n+2*N),repeat=N))

def test(n,seed,count):
    rng=random.Random(seed)
    N=orbit_count(n)
    def sample():
        return tuple([rng.randrange(n) for _ in range(n)]
                     +[rng.randrange(n+2*N) for _ in range(N)])
    hits=0
    for _ in range(count):
        f,h=sample(),sample()
        if dominates(f,h,n):
            factor(f,h,n);hits+=1
    assert hits>0
    print(f'RANDOM_FACTORIZATIONS_n={n}_tested={hits}')

if __name__=='__main__':
    for n in (1,2):
        elems=list(allmaps(n))
        keys={x:i for i,x in enumerate(elems)}
        for f in elems:
            actual={keys[compose(compose(v,f,n),u,n)] for v in elems for u in elems}
            predicted={keys[h] for h in elems if dominates(f,h,n)}
            assert actual==predicted, (n,f,actual^predicted)
        unique={kind(x,n) for x in elems}
        N=orbit_count(n)
        expected=n*(n+1)*(3*n*n-5*n+8)//12
        assert len(unique)==expected
        print(f'EXHAUSTIVE_n={n}_elements={len(elems)}_Jclasses={len(unique)}')
    n=3
    all3=list(allmaps(n))
    assert len(all3)==19683
    types={kind(x,3) for x in all3}
    assert len(types)==20
    print('EXHAUSTIVE_TYPES_n=3_Jclasses=20')
    representatives={}
    for x in all3:
        representatives.setdefault(kind(x,3),x)
    factorizations=0
    for f in representatives.values():
        for h in all3:
            if dominates(f,h,3):
                factor(f,h,3)
                factorizations+=1
    print(f'REPRESENTATIVE_EXHAUSTIVE_FACTORIZATIONS_n=3_count={factorizations}')
    test(3,12345,10000)
    test(4,54321,10000)
    test(5,19191,10000)
    print('VERIFY_OK')
