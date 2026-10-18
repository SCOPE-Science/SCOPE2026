"""Direct arithmetic checks of a modular dihedral-quandle idempotent theorem.
Run: python check_idempotents.py
Uses Python's standard library only. Finite tests corroborate the written proof.
"""
from itertools import product
from math import comb, factorial
from random import Random


def mul_trunc(a,b,p):
    c=[0]*p
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b[:p-i]):
            c[i+j]=(c[i+j]+x*y)%p
    return c


def power_trunc(a,e,p):
    r=[1]+[0]*(p-1)
    for _ in range(e): r=mul_trunc(r,a,p)
    return r


def exp_trunc(g,p):
    out=[1]+[0]*(p-1)
    term=[1]+[0]*(p-1)
    for j in range(1,p):
        term=mul_trunc(term,g,p)
        invfac=pow(factorial(j),-1,p)
        for i in range(p):out[i]=(out[i]+term[i]*invfac)%p
    return out


def log_t(p):
    x=[0]*p
    for j in range(1,p):x[j]=(-1 if j%2==0 else 1)*pow(j,-1,p)%p
    return x


def to_t_basis(g,p):
    return [sum(g[j]*comb(j,i)*(-1)**(j-i) for j in range(i,p))%p
            for i in range(p)]


def star(a,b,p):
    ans=[0]*p
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[(2*j-i)%p]=(ans[(2*j-i)%p]+x*y)%p
    return tuple(ans)


def resonance_degrees(p):
    return [m for m in range(1,p) if ((-1)**m+pow(2,m,p)-1)%p==0]


def element(p, coeffs):
    degrees=resonance_degrees(p)
    x=log_t(p)
    g=[0]*p
    for m,c in zip(degrees,coeffs):
        xm=power_trunc(x,m,p)
        for j in range(p):g[j]=(g[j]+c*xm[j])%p
    return tuple(to_t_basis(exp_trunc(g,p),p))


def check_prime(p):
    dims=resonance_degrees(p)
    order=1;t=2%p
    while t!=1: t=(2*t)%p;order+=1
    L=order if order%2==0 else 2*order
    assert dims==list(range(1,p,L)),(p,dims,L)
    vectors=[element(p, tuple(1 if i==j else 0 for i in range(len(dims))))
             for j in range(len(dims))]
    for a in vectors:assert star(a,a,p)==a
    z=tuple([0]*p)
    e=element(p,[0]*len(dims))
    assert e==(1,)+tuple([0]*(p-1))
    assert all(sum(a)%p==1 for a in vectors)
    rng=Random(p*7907)
    for _ in range(24):
        ca=[rng.randrange(p) for _ in dims]; cb=[rng.randrange(p) for _ in dims]
        a=element(p,ca);b=element(p,cb)
        assert star(a,a,p)==a,(p,ca,a)
        assert star(a,b,p)==element(p,[(-v+2*w)%p for v,w in zip(ca,cb)]),(p,ca,cb)
        assert star(a,z,p)==z and star(z,b,p)==z
    # Exhaustive enumeration of ALL algebra elements in small characteristics.
    if p<=5:
        brute={a for a in product(range(p),repeat=p) if star(a,a,p)==a}
        constructed={z}|{element(p,c) for c in product(range(p),repeat=len(dims))}
        assert brute==constructed,(p,len(brute),len(constructed))
    print('p=',p,'ord_p(2)=',order,'degrees=',dims,'predicted count over F_p=',p**len(dims)+1,'OK')


def check_f9():
    # F_9 = F_3[alpha]/(alpha^2+1), elements a+3*b.
    def madd(x,y):return (x%3+y%3)%3 + 3*((x//3+y//3)%3)
    def mmul(x,y):
        a,b=x%3,x//3;c,d=y%3,y//3
        return (a*c-b*d)%3 + 3*((a*d+b*c)%3)
    def sq(a):
        out=[0,0,0]
        for i,x in enumerate(a):
            for j,y in enumerate(a):
                k=(2*j-i)%3
                out[k]=madd(out[k],mmul(x,y))
        return tuple(out)
    ids=[a for a in product(range(9),repeat=3) if sq(a)==a]
    assert len(ids)==10,len(ids)
    print('F_9[R_3]: exactly 10 idempotents (including zero), exhaustive OK')


if __name__=='__main__':
    check_f9()
    for p in (3,5,7,11,13,17,19,23,31,41):check_prime(p)
    # p=17 first prime with a second resonance; witness exp((log t)^9).
    e17=element(17,[0,1])
    assert e17 not in {tuple(1 if j==i else 0 for j in range(17)) for i in range(17)}
    assert star(e17,e17,17)==e17
    print('p=17 nontrivial witness coefficients (in the t basis):',list(e17))
    print('ALL_EXACT_CHECKS_PASSED')
