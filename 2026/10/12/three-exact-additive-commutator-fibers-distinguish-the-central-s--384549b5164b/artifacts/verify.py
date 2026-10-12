#!/usr/bin/env python3
"""Self-contained finite-field census for the additive commutator fibers of N_4(F_q)."""
from collections import Counter
from itertools import product


def operations(q):
    if q in (2, 3, 5):
        return lambda a,b:(a+b)%q, lambda a,b:(a-b)%q, lambda a,b:(a*b)%q
    if q == 4:
        def mul(x,y):
            z=0
            while y:
                if y&1: z ^= x
                y >>= 1
                x <<= 1
                if x&4: x ^= 7  # t^2+t+1
            return z
        return lambda a,b:a^b, lambda a,b:a^b, mul
    raise ValueError('unsupported test field')


def predicted(q,z):
    r,s,t=z
    if r or s: return q**9-q**7
    if t: return 2*q**9-2*q**7
    return 2*q**9+q**8-2*q**7


def matrix(x):
    a,b,c,d,e,f=x
    return ((0,a,d,f),(0,0,b,e),(0,0,0,c),(0,0,0,0))


def brute(q):
    plus,minus,mul=operations(q)
    words=list(product(range(q),repeat=6))
    h=Counter()
    # Independently compute matrix products using two-summand matrix dots,
    # without calling the closed-form commutator identity.
    for x in words:
        X=matrix(x)
        for y in words:
            Y=matrix(y)
            z=[]
            for i,j in ((0,2),(1,3),(0,3)):
                xy=0; yx=0
                for k in range(4):
                    xy=plus(xy,mul(X[i][k],Y[k][j]))
                    yx=plus(yx,mul(Y[i][k],X[k][j]))
                z.append(minus(xy,yx))
            h[tuple(z)]+=1
    for z in product(range(q),repeat=3):
        assert h[z]==predicted(q,z), (q,z,h[z],predicted(q,z))
    assert sum(h.values())==q**12
    rank_profile=(q,q*(q*q-1),q**3*(q*q+q-2),q**3*(q-1)*(q*q-1))
    assert sum(rank_profile)==q**6
    print(f'q={q}: full matrix-product brute force; zero={h[0,0,0]}; min={min(h.values())}; image={len(h)}; rank_profile={rank_profile}',flush=True)


def exhaustive_linear_fibers(q):
    plus,minus,mul=operations(q)
    hist=Counter()
    ranks=Counter()
    for a,b,c,d,e,f in product(range(q),repeat=6):
        cols=((minus(0,b),0,minus(0,e)),(a,minus(0,c),0),(0,b,d),
              (0,0,minus(0,c)),(0,0,a),(0,0,0))
        image={(0,0,0)}
        for col in cols:
            if col==(0,0,0): continue
            image={tuple(plus(v[i],mul(t,col[i])) for i in range(3))
                   for v in image for t in range(q)}
        size=len(image)
        rank=0; t=size
        while t>1:
            assert t%q==0
            t//=q
            rank+=1
        ranks[rank]+=1
        for z in image: hist[z]+=q**(6-rank)
    for z in product(range(q),repeat=3):
        assert hist[z]==predicted(q,z),(q,z,hist[z],predicted(q,z))
    assert sum(hist.values())==q**12
    expected=(q,q*(q*q-1),q**3*(q*q+q-2),q**3*(q-1)*(q*q-1))
    assert tuple(ranks[i] for i in range(4))==expected,(q,ranks,expected)
    print(f'q={q}: all {q**6} coefficient matrices and their image spaces; zero={hist[0,0,0]}; rank_profile={expected}',flush=True)

if __name__=='__main__':
    for q in (2,3): brute(q)
    for q in (4,5): exhaustive_linear_fibers(q)
    print('VERIFY_OK')
