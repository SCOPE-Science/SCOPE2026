"""Standalone exhaustive verification of subalgebra counts in quadratic socle-degree-two algebras.

No external libraries are used. Executable with Python 3.10 or newer.
The field arithmetic below is deliberately restricted to prime fields for exhaustive tests;
the proven counting identity applies to every odd prime power.
"""
from itertools import combinations, product
from collections import Counter


def gaussian(n,k,q):
    if k<0 or k>n: return 0
    num=1;den=1
    for i in range(k):
        num*=q**(n-i)-1
        den*=q**(k-i)-1
    return num//den


def iso_counts(d,q,sign):
    if d%2:
        m=d//2
        return [gaussian(m,k,q)*prod(q**(m-i)+1 for i in range(k)) for k in range(m+1)]
    m=d//2
    if sign=='+':
        return [gaussian(m,k,q)*prod(q**(m-1-i)+1 for i in range(k)) for k in range(m+1)]
    return [gaussian(m-1,k,q)*prod(q**(m-i)+1 for i in range(k)) for k in range(m)]


def prod(seq):
    x=1
    for v in seq:x*=v
    return x


def predicted(d,q,sign):
    c=Counter()
    for k in range(d+1):
        c[k+2]+=gaussian(d,k,q)
    for k,num in enumerate(iso_counts(d,q,sign)):
        c[k+1]+=num*q**k
    return c


def rref_subspaces(n,q):
    """Generate RREF bases for every subspace of F_q^n exactly once."""
    yield ()
    for k in range(1,n+1):
        for piv in combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
            for vals in product(range(q),repeat=len(free)):
                rows=[[int(j==p) for j in range(n)] for p in piv]
                for (i,j),v in zip(free,vals):rows[i][j]=v
                yield tuple(tuple(row) for row in rows)


def member(v,rows,q):
    w=list(v)
    for row in rows:
        p=next(i for i,x in enumerate(row) if x)
        a=w[p]
        if a:
            w=[(x-a*y)%q for x,y in zip(w,row)]
    return not any(w)


def forms(d,q,sign):
    # Orthogonal sum of hyperbolic planes and, when appropriate, an anisotropic plane.
    B=[[0]*d for _ in range(d)]
    h=d//2 if (d%2 or sign=='+') else d//2-1
    for i in range(h):
        B[2*i][2*i+1]=1
        B[2*i+1][2*i]=1
    if d%2:B[-1][-1]=1
    elif sign=='-':
        # Choose a 2x2 diagonal anisotropic form x^2+a*y^2: -a nonsquare.
        a=next(a for a in range(1,q) if (-a)%q not in {z*z%q for z in range(q)})
        B[-2][-2]=1
        B[-1][-1]=a
    return B


def direct(d,q,sign):
    B=forms(d,q,sign)
    counts=Counter()
    count_iso=Counter()
    for U in rref_subspaces(d,q):
        isotropic=all(sum(x[i]*B[i][j]*y[j] for i in range(d) for j in range(d))%q==0
                      for x in U for y in U)
        if isotropic: count_iso[len(U)]+=1
    Z=[0]*d+[1]
    for W in rref_subspaces(d+1,q):
        # Actual pairwise products of the nilpotent basis elements; no use of the theorem's classification.
        closed=True
        for x in W:
            for y in W:
                scalar=sum(x[i]*B[i][j]*y[j] for i in range(d) for j in range(d))%q
                if scalar and not member([0]*d+[scalar],W,q):
                    closed=False
                    break
            if not closed:break
        if closed:counts[len(W)+1]+=1
    return counts,count_iso


def run():
    tests=[(3,2,'+'),(3,2,'-'),(3,3,'o'),(3,4,'+'),(3,4,'-'),(3,5,'o'),
           (5,2,'+'),(5,2,'-'),(5,3,'o'),(5,4,'+')]
    for q,d,sign in tests:
        count,iso=direct(d,q,sign)
        expected=predicted(d,q,sign)
        exact_iso={k:c for k,c in enumerate(iso_counts(d,q,sign))}
        assert count==expected,(q,d,sign,count,expected)
        assert dict(iso)==exact_iso,(q,d,sign,iso,exact_iso)
        print(f'EXHAUSTIVE_OK q={q} d={d} type={sign} total={sum(count.values())} ranks='+str(sorted(count.items())))
    for q in (3,5,7,11):
        for d in (2,4,6,8):
            a=predicted(d,q,'+')[2]
            b=predicted(d,q,'-')[2]
            assert a-b==2*q**(d//2)
    print('WITT_GAP_OK')
    print('VERIFY_OK')


if __name__=='__main__':run()
