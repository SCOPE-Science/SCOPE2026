"""Independent finite checks for the weight-two cyclic zero-padding theorem.

Run with Python 3.9+ and no third-party modules:
    python VERIFY.py
All checks use integer arithmetic and explicit binary words.
"""
from itertools import combinations
from random import Random


def arc(start, end, n):
    out = set()
    i = start
    while i != end:
        out.add(i)
        i = (i + 1) % n
    return out


def oriented_cost(a, b):
    left = len(a - b)
    right = len(b - a)
    if left == right == 0:
        return 0
    if left == 0 or right == 0:
        return None
    return abs(left - right)


def edge_formula(p, q, n):
    a = arc(p[0], p[1], n)
    b = arc(q[0], q[1], n)
    vals = (oriented_cost(a,b), oriented_cost(a, set(range(n))-b))
    return min(x for x in vals if x is not None)


def endpoint_formula(p, q, n):
    if p == q:
        return 0
    common = set(p) & set(q)
    if len(common) == 1:
        a = next(iter(common))
        b = next(iter(set(p)-common))
        c = next(iter(set(q)-common))
        return abs(((b-a) % n) + ((c-a) % n) - n)
    pts = sorted(set(p) | set(q))
    gaps = [((pts[(i+1)%4] - pts[i]) % n) for i in range(4)]
    colors = ['P' if x in p else 'Q' for x in pts]
    if colors[0] != colors[1] and colors[1] != colors[2]:
        return min(abs(gaps[0]-gaps[2]), abs(gaps[1]-gaps[3]))
    for shift in range(4):
        cc = colors[shift:] + colors[:shift]
        if cc == ['P','P','Q','Q']:
            gg = gaps[shift:] + gaps[:shift]
            return abs(gg[0]-gg[2])
        if cc == ['Q','Q','P','P']:
            gg = gaps[shift:] + gaps[:shift]
            return abs(gg[0]-gg[2])
    raise AssertionError((p,q,n))


def pad_words(p,q,n,z):
    pp=set(p); qq=set(q)
    a=''.join(('1' if i in pp else '0') + '0'*z[i] for i in range(n))
    b=''.join(('1' if i in qq else '0') + '0'*z[i] for i in range(n))
    return a,b


def cyclic_equiv(a,b):
    return len(a)==len(b) and b in a+a


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for i in range(total+1):
            for suffix in compositions(total-i,slots-1):
                yield (i,)+suffix


def brute_min(p,q,n,upper):
    for t in range(upper+1):
        for z in compositions(t,n):
            a,b=pad_words(p,q,n,z)
            if cyclic_equiv(a,b):
                return t
    raise AssertionError((p,q,n,upper))


def construct_min(p,q,n):
    a=arc(p[0],p[1],n)
    b=arc(q[0],q[1],n)
    alternatives=[]
    for bb in (b, set(range(n))-b):
        d1=a-bb; d2=bb-a
        c=oriented_cost(a,bb)
        if c is None:
            continue
        z=[0]*n
        if c:
            if len(d1) < len(d2):
                z[min(d1)] = c
            else:
                z[min(d2)] = c
        alternatives.append((c,z))
    assert alternatives
    t,z=min(alternatives,key=lambda x:x[0])
    u,v=pad_words(p,q,n,z)
    assert cyclic_equiv(u,v)
    return t,z,u,v


def run():
    checks=0
    by_n={}
    for n in range(3,19):
        pairs=list(combinations(range(n),2))
        maxi=-1; maxima=0
        for p in pairs:
            for q in pairs:
                a=edge_formula(p,q,n)
                b=endpoint_formula(p,q,n)
                assert a==b,(n,p,q,a,b)
                t,z,u,v=construct_min(p,q,n)
                assert t==a and len(u)==len(v)==n+t and cyclic_equiv(u,v)
                assert sum(x>0 for x in z) <= 1
                if n >= 4:
                    common=set(p)&set(q)
                    extreme_form=False
                    if len(common)==1:
                        h=next(iter(common))
                        other={(x-h)%n for x in (set(p)|set(q))-common}
                        extreme_form=(other=={1,2} or other=={n-2,n-1})
                    assert (t==n-3)==extreme_form,(n,p,q,t)
                maxi=max(maxi,t)
                maxima += t==n-3
                checks+=1
        assert maxi==max(n-3,0)
        if n>=4:
            assert maxima==4*n,(n,maxima)
        by_n[n]=(len(pairs)**2,maxi,maxima)
    print('All edge/endpoint formulas and constructive solutions verified:', checks)
    for n, (pairs,maximum,extremizers) in by_n.items():
        print(f'n={n:2} ordered_pairs={pairs:6} maximum={maximum:2} extremizers={extremizers:3}')
    brute_checks=0
    for n in range(3,9):
        pairs=list(combinations(range(n),2))
        for p in pairs:
            for q in pairs:
                exp=endpoint_formula(p,q,n)
                actual=brute_min(p,q,n,exp)
                assert exp==actual,(n,p,q,exp,actual)
                brute_checks+=1
    print('Independent exhaustive padding search agrees:',brute_checks,'pairs through n=8')
    rng=Random(12062026)
    for _ in range(10000):
        n=rng.randrange(4,200)
        p=tuple(sorted(rng.sample(range(n),2)))
        q=tuple(sorted(rng.sample(range(n),2)))
        assert edge_formula(p,q,n)==endpoint_formula(p,q,n)
        t,z,u,v=construct_min(p,q,n)
        assert t==endpoint_formula(p,q,n) and cyclic_equiv(u,v)
    print('Random larger-parameter edge and construction tests: 10000')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    run()
