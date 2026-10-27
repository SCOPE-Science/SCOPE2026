"""Exact, standalone checks of the finite-gap broadcast scheduling identities.

Requires Python 3 standard library only. Run `python verify.py`.
Finite checks corroborate, but do not replace, the general analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def product2(A, x):
    return (A[0][0] * x[0] + A[0][1] * x[1],
            A[1][0] * x[0] + A[1][1] * x[1])


def direct(gaps, p, b1, b2):
    W = ((1-p,p),(p,1-p))
    D = (1-b1,1-b2)
    e = (F(1), F(1))
    e = tuple(D[i]*product2(W,e)[i] for i in (0,1))
    for g in gaps:
        for _ in range(g):
            e = product2(W,e)
        e = tuple(D[i]*product2(W,e)[i] for i in (0,1))
    return sum(e)/2


def closed(gaps, p, b1, b2):
    lam = 1-2*p
    a = 1-(b1+b2)/2
    c = (b2-b1)/2
    if len(gaps) == 2:
        x,y = (lam**(g+1) for g in gaps)
        return a**3+a*c*c*(x+y+x*y)
    if len(gaps) == 3:
        x,y,z = (lam**(g+1) for g in gaps)
        return a**4+a*a*c*c*(x*y*z+y+(1+y)*(x+z))+c**4*x*z
    raise ValueError('Exactly three or four broadcasts required')


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, slots-1):
                yield (first,)+rest


def reduced_four(total, p, b1, b2):
    # Exact finite family obtained by balancing the two outside gaps.
    options=[]
    for m in range(total+1):
        h=total-m
        options.append((h//2,m,h-h//2))
    return min(closed(g,p,b1,b2) for g in options)


def run():
    count=0
    for p in (F(1,100),F(1,10),F(1,4)):
        for b1,b2 in ((F(1,5),F(4,5)),(F(1,3),F(1,2)),(F(3,4),F(1,10))):
            for G in range(11):
                for K in (3,4):
                    es=[]
                    for gaps in compositions(G,K-1):
                        assert direct(gaps,p,b1,b2)==closed(gaps,p,b1,b2)
                        es.append((closed(gaps,p,b1,b2),gaps))
                        count+=1
                    if K==3:
                        mins={g for e,g in es if e==min(z[0] for z in es)}
                        assert mins=={g for g in compositions(G,2) if abs(g[0]-g[1])<=1}
                    else:
                        assert min(e for e,g in es)==reduced_four(G,p,b1,b2)
                        assert all(abs(g[0]-g[2])<=1 for e,g in es if e==min(z[0] for z in es))
    p=F(1,100); b1=F(4,5); b2=F(1,5); lam=1-2*p
    a=1-(b1+b2)/2; c=(b2-b1)/2; G=10
    assert lam**G*(1+lam)>1+(c/a)**2*lam
    best=min((closed(g,p,b1,b2),g) for g in compositions(G,3))
    assert best[1]==(0,10,0)
    assert best[0]==F(903373787686956792814241,4882812500000000000000000)
    assert closed((3,4,3),p,b1,b2)-best[0]==F(25553392256660104683,24414062500000000000000)
    print('CHECK_OK exact_schedules=',count,'optimal=',best[1], 'error=',best[0])

if __name__=='__main__':
    run()
