#!/usr/bin/env python3
"""Self-contained finite checks for the mean intrinsic distance of a metric theta graph.

These checks supplement, but do not replace, the analytic integration proof.
"""
from fractions import Fraction as F
from random import Random
import math


def cubic(a, b, c):
    a, b, c = sorted((F(a), F(b), F(c)))
    return (2*a**3+a*a*(b+c)+3*a*(b*b+c*c)+4*a*b*c
            +b**3+2*b*b*c+2*b*c*c+c**3)/4


def formula(a, b, c):
    return cubic(a,b,c)/(F(a)+F(b)+F(c))**2


def same_integral(L, s):
    return L**3/3-max(L-s, F(0))**3/12


def pair_baseline(r, s):
    r, s = sorted((r, s))
    return r*r*s/2+r*s*s/4-r**3/12


def corner_correction(a, b, c):
    return (c-a)*(b-a)**2/4-(b-a)**3/12


def pairwise_integral(a,b,c):
    a,b,c=sorted((F(a),F(b),F(c)))
    self_sum=(same_integral(a,b)+same_integral(b,a)+same_integral(c,a))
    cross=pair_baseline(a,b)+pair_baseline(a,c)+pair_baseline(b,c)-corner_correction(a,b,c)
    return self_sum+2*cross


def distance(x, i, y, j, lengths):
    if i == j:
        L=lengths[i]
        s=min(lengths[k] for k in range(3) if k!=i)
        return min(abs(x-y),L+s-abs(x-y))
    li, lj=lengths[i], lengths[j]
    k=3-i-j
    lk=lengths[k]
    return min(x+y, li+lj-x-y, x+lk+lj-y, li-x+lk+y)


def sampled_average(lengths, count=150000, seed=137):
    rng=Random(seed)
    total=sum(lengths)
    accum=0.0
    for _ in range(count):
        px=rng.random()*total
        py=rng.random()*total
        i=next((i for i in range(3) if px<sum(lengths[:i+1])),2)
        j=next((j for j in range(3) if py<sum(lengths[:j+1])),2)
        x=px-sum(lengths[:i])
        y=py-sum(lengths[:j])
        accum+=distance(x,i,y,j,lengths)
    return accum/count



def verify_symbolic_polynomials():
    """Exact coefficient-wise polynomial certificates in Q[a,u,v], no CAS."""
    zero = (0, 0, 0)
    def C(q):
        q=F(q)
        return {} if q==0 else {zero:q}
    def X(index):
        m=[0,0,0]
        m[index]=1
        return {tuple(m):F(1)}
    def add(*terms):
        out={}
        for p in terms:
            for m,v in p.items():
                out[m]=out.get(m,F(0))+v
        return {m:v for m,v in out.items() if v}
    def mult(*terms):
        out=C(1)
        for p in terms:
            nxt={}
            for k,v in out.items():
                for j,w in p.items():
                    m=tuple(k[i]+j[i] for i in range(3))
                    nxt[m]=nxt.get(m,F(0))+v*w
            out={m:v for m,v in nxt.items() if v}
        return out
    def sc(q,p):
        return {m:F(q)*v for m,v in p.items() if F(q)*v}
    def pw(p,n):
        return mult(*([p]*n))
    a=X(0)
    u=X(1)
    v=X(2)
    b=add(a,u)
    c=add(a,u,v)
    T=add(a,b,c)
    N=sc(F(1,4),add(sc(2,pw(a,3)),mult(pw(a,2),add(b,c)),
       sc(3,mult(a,add(pw(b,2),pw(c,2)))),sc(4,mult(a,b,c)),
       pw(b,3),sc(2,mult(pw(b,2),c)),sc(2,mult(b,pw(c,2))),pw(c,3)))
    self_sum=add(sc(F(1,3),add(pw(a,3),pw(b,3),pw(c,3))),
        sc(F(-1,12),add(pw(u,3),pw(add(u,v),3))))
    def J0(r,s):
        return add(sc(F(1,2),mult(pw(r,2),s)),
           sc(F(1,4),mult(r,pw(s,2))), sc(F(-1,12),pw(r,3)))
    corr=add(sc(F(1,4),mult(add(u,v),pw(u,2))),sc(F(-1,12),pw(u,3)))
    N2=add(self_sum,sc(2,add(J0(a,b),J0(a,c),J0(b,c),sc(-1,corr))))
    assert N==N2, (N,N2)
    gap=add(sc(36,mult(a,pw(u,2))),sc(36,mult(a,u,v)),sc(36,mult(a,pw(v,2))),
            sc(2,pw(u,3)),sc(3,mult(pw(u,2),v)),sc(15,mult(u,pw(v,2))),sc(7,pw(v,3)))
    assert add(sc(108,N),sc(-20,pw(T,3)))==gap
    return 2

def main():
    count=verify_symbolic_polynomials()
    for a in (F(1,5),F(1,2),F(1),F(2)):
        for u in (F(0),F(1,7),F(1),F(3)):
            for v in (F(0),F(1,7),F(1),F(2)):
                b,c=a+u,a+u+v
                n=cubic(a,b,c)
                assert n==pairwise_integral(a,b,c)
                assert 108*(n-F(5,27)*(a+b+c)**3)==(36*a*u*u+36*a*u*v+36*a*v*v+2*u**3+3*u*u*v+15*u*v*v+7*v**3)
                assert n>=F(5,27)*(a+b+c)**3
                assert (n==F(5,27)*(a+b+c)**3)==(u==v==0)
                assert n<((a+b+c)**3)/4
                count+=5
    assert formula(1,1,1)==F(5,9)
    assert formula(F(3,11),F(15,11),F(15,11))==F(5,9)+F(16,1089)
    assert formula(F(1,100),F(299,200),F(299,200))<formula(F(3,11),F(15,11),F(15,11))
    count+=3
    # Pairwise formula and the direct shortest-path definition are independent calculations.
    for l in ((1.,1.,1.),(.5,.5,2.),(.2,1.3,1.5),(1.,2.,3.),(.03,.12,2.85)):
        approx=sampled_average(l)
        exact=float(formula(*[F(str(x)) for x in l]))
        assert abs(approx-exact)<.008, (l,approx,exact)
        print('Monte Carlo cross-check:',l, 'sample',round(approx,6), 'formula',round(exact,6))
        count+=1
    print('PASS:',count,'exact assertions and 750000 independently sampled point-pairs')

if __name__=='__main__':
    main()
