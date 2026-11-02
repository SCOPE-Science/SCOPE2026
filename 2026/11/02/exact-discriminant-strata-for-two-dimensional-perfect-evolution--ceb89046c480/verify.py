"""Exhaustive arithmetic checks of the discriminant strata over small finite fields."""
from collections import Counter
from itertools import product


def mul(a,b,q):
    if q!=4:
        return (a*b)%q
    p=0
    while b:
        if b&1:p^=a
        b>>=1
        a<<=1
        if a&4:a^=7
    return p


def add(a,b,q):
    return a^b if q==4 or q==2 else (a+b)%q


def neg(a,q):
    return a if q in (2,4) else (-a)%q


def powq(a,k,q):
    p=1
    for _ in range(k):p=mul(p,a,q)
    return p


def det(a,b,c,d,q):
    return add(mul(a,d,q),neg(mul(b,c,q),q),q)


def disc(a,b,c,d,q):
    # Homogeneous cubic c X^3 - a X^2Y + d XY^2 - b Y^3
    A=c;B=neg(a,q);C=d;D=neg(b,q)
    terms=[(1,mul(powq(B,2,q),powq(C,2,q),q)),(-4,mul(A,powq(C,3,q),q)),(-4,mul(powq(B,3,q),D,q)),(-27,mul(powq(A,2,q),powq(D,2,q),q)),(18,mul(mul(mul(A,B,q),C,q),D,q))]
    acc=0
    for k,t in terms:
        if q==4:
            kt=k&1
        else:
            kt=k%q
        tt=mul(kt,t%q if q!=4 else t,q)
        acc=add(acc,tt,q)
    return acc


def is_triple(a,b,c,d,q):
    if q%2==0:return False
    for r in range(1,q):
        if a==mul(3%q,mul(c,r,q),q) and d==mul(3%q,mul(c,powq(r,2,q),q),q) and b==mul(c,powq(r,3,q),q) and c!=0:
            return True
    return False


def check(q):
    groups=Counter()
    for a,b,c,d in product(range(q),repeat=4):
        if det(a,b,c,d,q)==0:continue
        Delta=disc(a,b,c,d,q)
        if not Delta:groups['triple' if is_triple(a,b,c,d,q) else 'double']+=1
        else:groups['reduced']+=1
    G=(q*q-1)*(q*q-q)
    assert sum(groups.values())==G
    if q%2==0:
        expected={'reduced':G}
    else:
        expected={'triple':(q-1)**2,'double':(q-1)**3,'reduced':G-q*(q-1)**2}
    assert dict(groups)==expected,(q,groups,expected)
    print('q=',q,'|GL2|=',G,'strata=',dict(groups),'VERIFY_OK')

if __name__=='__main__':
    for q in (2,3,4,5,7):check(q)
