"""Independent finite-horizon checks for balanced multicolour completion times.

Only verifies finite instances and asymptotic numerical consistency; the universal
inequalities and tail asymptotics are established analytically in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial, gamma, lgamma, exp
from itertools import product


def rise(x, n):
    ans = 1
    for j in range(n):
        ans *= x + j
    return ans


def compositions(k, q):
    if q == 1:
        yield (k,)
    else:
        for x in range(k + 1):
            for z in compositions(k - x, q - 1):
                yield (x,) + z


def formula(q, a, r, k, mode):
    if k < q*r:
        return Fraction(0)
    if mode == 'without' and k > q*a:
        return Fraction(1)
    v = Fraction(0)
    for c in compositions(k, q):
        if min(c) < r:
            continue
        if mode == 'without':
            if max(c) > a:
                continue
            num = 1
            for x in c:
                num *= comb(a,x)
            term = Fraction(num, comb(q*a,k))
        elif mode == 'iid':
            m = factorial(k)
            for x in c:
                m //= factorial(x)
            term = Fraction(m, q**k)
        else:
            m = factorial(k)
            for x in c:
                m //= factorial(x)
            h = 1
            for x in c:
                h *= rise(a,x)
            term = Fraction(m*h, rise(q*a,k))
        v += term
    return v


def dynamic(q,a,r,k,mode):
    if mode=='without' and k>q*a:
        return Fraction(1)
    d={(0,)*q:Fraction(1)}
    for t in range(k):
        nd={}
        for c,mass in d.items():
            for j in range(q):
                if mode=='without':
                    x=Fraction(a-c[j],q*a-t)
                elif mode=='iid':
                    x=Fraction(1,q)
                else:
                    x=Fraction(a+c[j],q*a+t)
                if x==0: continue
                z=list(c); z[j]+=1; z=tuple(z)
                nd[z]=nd.get(z,Fraction(0))+mass*x
        d=nd
    return sum((v for c,v in d.items() if min(c)>=r),Fraction(0))


def single_tail(q,a,r,n):
    # A specified category is seen fewer than r times, exactly.
    return sum((Fraction(comb(n,j)*rise(a,j)*rise((q-1)*a,n-j),rise(q*a,n))
                for j in range(min(r,n+1))),Fraction(0))


def double_tail(q,a,r,n):
    if q==2:
        return Fraction(0) if n>2*(r-1) else sum((Fraction(comb(n,j)*rise(a,j)*rise(a,n-j),rise(2*a,n))
                  for j in range(max(0,n-r+1),min(r,n+1))),Fraction(0))
    ans=Fraction(0)
    for j in range(min(r,n+1)):
        for l in range(min(r,n-j+1)):
            if n-j-l < 0:continue
            m=factorial(n)//(factorial(j)*factorial(l)*factorial(n-j-l))
            ans+=Fraction(m*rise(a,j)*rise(a,l)*rise((q-2)*a,n-j-l),rise(q*a,n))
    return ans


def tail_constant(q,a,r):
    return Fraction(q*factorial(q*a-1),factorial((q-1)*a-1))*sum(
        (Fraction(rise(a,j),factorial(j)) for j in range(r)),Fraction(0))


def run():
    checks=0; cases=0
    for q in (2,3,4):
        for a in (1,2,3):
            for r in range(1,a+1):
                for k in range(q*r, min(q*a+2,q*r+5)+1):
                    vals=[]
                    for mode in ('without','iid','polya'):
                        f=formula(q,a,r,k,mode)
                        d=dynamic(q,a,r,k,mode)
                        assert f==d,(q,a,r,k,mode,f,d)
                        vals.append(f);checks+=1
                    assert vals[0]>vals[1]>vals[2],(q,a,r,k,vals)
                    cases+=1
    # Single-category exact tail, pair correction and leading coefficient.
    asymptotic_checks=0
    for q,a,r in product((2,3,4),(1,2,3),(1,2)):
        if r>a:continue
        C=float(tail_constant(q,a,r))
        for n in (400,800,1600):
            P=float(single_tail(q,a,r,n))
            D=float(double_tail(q,a,r,n))
            assert D>=0 and D<=P
            assert abs((q*P)*(n**a)/C-1) < 1.100*(a+r+q)**2/n
            assert (D/P if P else 0) < 100*(a+r+q)**2/n**a,(q,a,r,n,D/P,100*(a+r+q)**2/n**a)
            asymptotic_checks+=1
    print('PASS',cases,'finite-horizon triples;',checks,'independent closed-form/recursion comparisons;',asymptotic_checks,'tail consistency checks')
    print('Example q=3 a=2 r=2: constant =',tail_constant(3,2,2))

if __name__=='__main__':
    run()
