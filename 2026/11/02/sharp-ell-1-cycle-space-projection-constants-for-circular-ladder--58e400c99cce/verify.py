"""Exact-rational consistency checks for minimum cycle-space projections of prism graphs.

Execute with Python 3. No third-party dependencies. This checks constructed
projections and finitely many test cases; the uniform lower bound is proved in
RESULT.md by inequalities valid for every real equivariant projection.
"""
from fractions import Fraction as F
from random import Random


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def scale(c, x):
    return [c * t for t in x]


def data(n):
    assert n >= 10
    u = F(3*n-9, 10*n)
    v = F(1,n)
    b = [F(0)] * n
    b[0], b[1], b[n-2], b[n-1] = -u, -v, v, u
    a = [(F(i == 0) + b[i] - b[(i-1) % n])/2 for i in range(n)]
    assert a[0] >= a[1] >= a[2] == F(1,2*n)
    assert all(a[i] == 0 for i in range(3,n-2))
    return a,b,u,v


def square(n, j):
    s = [F(0)] * (3*n)
    s[j % n] = F(1)
    s[n+j % n] = F(-1)
    s[2*n+(j+1)%n] = F(1)
    s[2*n+j % n] = F(-1)
    return s


def column(n,typ,j,a,b):
    t = [F(1)]*(2*n)+[F(0)]*n
    if typ == 'top':
        out = scale(F(1,2*n),t)
        for i in range(n):
            if a[i]: out=add(out,scale(a[i],square(n,j+i)))
    elif typ == 'bottom':
        out = scale(F(1,2*n),t)
        for i in range(n):
            if a[i]: out=add(out,scale(-a[i],square(n,j+i)))
    else:
        out = [F(0)]*(3*n)
        for i in range(n):
            if b[i]: out=add(out,scale(b[i],square(n,j+i)))
    return out


def divergence(n,coeff):
    out=[F(0)]*(2*n)
    for layer in range(2):
        for i in range(n):
            weight=coeff[layer*n+i]
            out[layer*n+i]+=weight
            out[layer*n+(i+1)%n]-=weight
    for i in range(n):
        weight=coeff[2*n+i]
        out[i]+=weight
        out[n+i]-=weight
    return out


def run():
    checks=0
    for n in range(10,31):
        a,b,u,v=data(n)
        goal=F(12,5)-F(16,5*n)
        # Every column is a divergence-free circulation, with the sharp norm.
        cols=[]
        for typ in ('top','bottom','vertical'):
            for j in range(n):
                c=column(n,typ,j,a,b)
                assert all(x==0 for x in divergence(n,c))
                assert sum(map(abs,c)) == goal
                cols.append(c)
                checks+=1
        # P fixes every square circulation; also fixes the horizontal sum t.
        for j in range(n):
            sj=square(n,j)
            projected=[sum(cols[k][i]*sj[k] for k in range(3*n)) for i in range(3*n)]
            assert projected == sj
            checks+=1
        t=[F(1)]*(2*n)+[F(0)]*n
        projected=[sum(cols[k][i]*t[k] for k in range(3*n)) for i in range(3*n)]
        assert projected == t
        checks+=1
        # Universal lower-bound algebra at the prescribed coefficient vectors.
        h=2*sum(max(abs(x),F(1,2*n)) for x in a) + sum(abs(a[i]-a[i-1]) for i in range(n))
        vv=2*sum(abs(x) for x in b) + sum(abs(b[i]-b[i-1]) for i in range(n))
        assert h == vv == goal
        checks+=1
    # Additional finite shape-check samples; not exhaustive evidence.
    rg=Random(15037)
    for n in (10,11,12,18):
        for repeat in range(100):
            b=[F(0)]*n
            for i in range(n//2):
                k=rg.randrange(-6,7)
                b[i]=F(k,11)
                b[n-1-i]=-b[i]
            if n%2: b[n//2]=F(0)
            a=[(F(i==0)+b[i]-b[i-1])/2 for i in range(n)]
            H=2*sum(max(abs(x),F(1,2*n)) for x in a)+sum(abs(a[i]-a[i-1]) for i in range(n))
            V=2*sum(map(abs,b))+sum(abs(b[i]-b[i-1]) for i in range(n))
            assert max(H,V) >= F(12,5)-F(16,5*n)
            checks+=1
    print('CHECK_OK exact_projection_and_norm_assertions=',checks,'dimensions=10..30','random_lower_inequality_samples=400')

if __name__=='__main__':run()
