#!/usr/bin/env python3
"""Exact checks of cyclic weighted evolution-algebra isomorphism classes.
Standard library only; prime fields and binary extension fields.
"""
import itertools, math
from collections import Counter


def mul(a,b,q):
    if q in (2,3,5,7,11):return a*b%q
    if q in (4,8):
        mod={4:0b111,8:0b1011}[q]
        h={4:2,8:3}[q]
        result=0
        while b:
            if b&1:result^=a
            b>>=1
            a<<=1
            if a&(1<<h):a^=mod
        return result
    raise ValueError(q)


def powf(x,e,q):
    value=1
    while e:
        if e&1:value=mul(value,x,q)
        x=mul(x,x,q)
        e>>=1
    return value


def inv(x,q):
    assert x
    return powf(x,q-2,q)


def primitive(q):
    for x in range(1,q):
        if len({powf(x,i,q) for i in range(q-1)})==q-1:return x
    raise AssertionError(q)


def order_two(d):
    if d==1:return 1
    r=1
    while pow(2,r,d)!=1:r+=1
    return r


def totient(d):
    return sum(math.gcd(d,i)==1 for i in range(1,d+1))


def cycle_exponent(a,q,logs):
    n=len(a)
    g=math.gcd(2**n-1,q-1)
    return sum((2**(n-1-i))*logs[c] for i,c in enumerate(a))%g


def iso_key(a,q,logs):
    n=len(a)
    g=math.gcd(2**n-1,q-1)
    x=cycle_exponent(a,q,logs)
    return min(x*pow(2,j,g)%g for j in range(n))


def lift_exists(a,b,j,q):
    n=len(a)
    for t0 in range(1,q):
        t=t0
        for i in range(n):
            t=mul(mul(t,t,q),mul(b[(i+j)%n],inv(a[i],q),q),q)
        if t==t0:return True
    return False


def direct_aut_order(a,q):
    n=len(a)
    ans=0
    for shift in range(n):
        for t0 in range(1,q):
            t=t0
            for i in range(n):
                t=mul(mul(t,t,q),mul(a[(i+shift)%n],inv(a[i],q),q),q)
            if t==t0:ans+=1
    return ans


def direct_idempotents(a,q):
    n=len(a)
    ans=0
    for vec in itertools.product(range(q),repeat=n):
        value=[0]*n
        for i in range(n):value[(i+1)%n]=mul(a[i],mul(vec[i],vec[i],q),q)
        if tuple(value)==vec:ans+=1
    return ans


def run_case(q,n):
    gen=primitive(q)
    logs={powf(gen,i,q):i for i in range(q-1)}
    g=math.gcd(2**n-1,q-1)
    all_a=list(itertools.product(range(1,q),repeat=n))
    keys=Counter()
    by_order=Counter()
    for a in all_a:
        c=cycle_exponent(a,q,logs)
        d=g//math.gcd(g,c)
        o=order_two(d)
        predicted_aut=g*n//o
        predicted_idem=1+g if c==0 else 1
        assert direct_aut_order(a,q)==predicted_aut,(q,n,a,'aut')
        assert direct_idempotents(a,q)==predicted_idem,(q,n,a,'idem')
        by_order[d]+=1
        keys[iso_key(a,q,logs)]+=1
    expected_classes=sum(totient(d)//order_two(d) for d in range(1,g+1) if g%d==0)
    assert len(keys)==expected_classes,(q,n,len(keys),expected_classes)
    for d in range(1,g+1):
        if g%d==0:
            assert by_order[d]==(q-1)**n*totient(d)//g,(q,n,d,by_order)
    # Independent isomorphism searches, exhaustive for small families.
    if len(all_a)<=80:
        for a in all_a:
            for b in all_a:
                actual=any(lift_exists(a,b,j,q) for j in range(n))
                assert actual==(iso_key(a,q,logs)==iso_key(b,q,logs)),(q,n,a,b)
    else:
        # Repeatable deterministic representatives exercise every predicted orbit.
        reps={}
        for a in all_a:reps.setdefault(iso_key(a,q,logs),a)
        for a in list(reps.values()):
            for b in list(reps.values()):
                actual=any(lift_exists(a,b,j,q) for j in range(n))
                assert actual==(iso_key(a,q,logs)==iso_key(b,q,logs)),(q,n,a,b)
        for a in all_a[::max(1,len(all_a)//70)]:
            b=reps[iso_key(a,q,logs)]
            assert any(lift_exists(a,b,j,q) for j in range(n)),(q,n,a,b)
    return len(all_a),len(keys)


def main():
    cases=[(q,n) for q in (2,3,4,5,7,8,11) for n in (1,2,3)]
    cases += [(2,4),(3,4),(4,4),(5,4),(7,4)]
    matrices=classes=0
    for q,n in cases:
        count,cl=run_case(q,n)
        matrices+=count
        classes+=cl
    print('ALL_CYCLIC_EVOLUTION_ARITHMETIC_CHECKS_PASSED',len(cases),matrices,classes)

if __name__=='__main__':main()
