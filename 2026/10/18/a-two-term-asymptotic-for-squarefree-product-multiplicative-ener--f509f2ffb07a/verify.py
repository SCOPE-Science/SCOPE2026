"""Finite checks for squarefree fixed-degree product collisions over finite fields.

All calculations use integer arithmetic. They do not establish the infinite asymptotic theorem.
"""
from collections import Counter, defaultdict
from math import gcd


def mobius(n):
    p=2
    sign=1
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:
                return 0
            sign=-sign
        p+=1
    if n>1:
        sign=-sign
    return sign


def irreducible_count(q,d):
    return sum(mobius(k)*q**(d//k) for k in range(1,d+1) if d%k==0)//d


def four_component_count(q,n):
    """Compute exact coefficient from product_P (1 + x1^deg P + ...+ x4^deg P)."""
    states={(0,0,0,0):1}
    for d in range(1,n+1):
        for _ in range(irreducible_count(q,d)):
            nxt=dict(states)
            for exps,c in states.items():
                for i in range(4):
                    if exps[i]+d<=n:
                        z=list(exps)
                        z[i]+=d
                        z=tuple(z)
                        nxt[z]=nxt.get(z,0)+c
            states=nxt
    return sum(states.get((k,k,n-k,n-k),0) for k in range(n+1))


def gf_mult(f,g,q):
    out=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            out[i+j]=(out[i+j]+a*b)%q
    return tuple(out)


def gf_rem(f,g,q):
    f=list(f)
    while len(f)>=len(g):
        c=f[-1]*pow(g[-1],-1,q)%q
        j=len(f)-len(g)
        for i,a in enumerate(g):
            f[i+j]=(f[i+j]-c*a)%q
        while f and f[-1]==0:
            f.pop()
    return tuple(f)


def gf_gcd(f,g,q):
    while g:
        f,g=g,gf_rem(f,g,q)
    return f


def squarefree(f,q):
    derivative=tuple((i*f[i])%q for i in range(1,len(f)))
    while derivative and derivative[-1]==0:
        derivative=derivative[:-1]
    return len(gf_gcd(f,derivative,q))==1


def monics(q,n):
    for idx in range(q**n):
        z=[]
        v=idx
        for i in range(n):
            z.append(v%q)
            v//=q
        yield tuple(z+[1])


def direct_collisions(q,n):
    pair_products=Counter()
    poly=list(monics(q,n))
    for a in poly:
        for b in poly:
            prod=gf_mult(a,b,q)
            if squarefree(prod,q):
                pair_products[prod]+=1
    return sum(c*c for c in pair_products.values())


def run():
    # Different arithmetic constructions: one prime-allocation four-variable
    # count and one direct enumeration of products and their representations.
    for q,hi in ((2,7),(3,3),(5,2)):
        for n in range(hi+1):
            a=four_component_count(q,n)
            b=direct_collisions(q,n)
            assert a==b,(q,n,a,b)
            print(f'q={q} n={n} collision_energy={a}')
    # Verify the 4-variable exact identity for all low degrees using an
    # Euler-product truncation up to degree n independently above.
    print('VERIFY_OK')


if __name__=='__main__':
    run()
