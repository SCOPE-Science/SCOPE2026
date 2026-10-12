from itertools import product
from math import comb, factorial
from collections import Counter

# Finite fields needed only for brute-force low-size replay.
def field_ops(q):
    if q in (2,3,5):
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
        inv=lambda a:pow(a,-1,q)
        return add,mul,inv
    if q==4:
        # GF(4)=F2[a]/(a^2+a+1), encoded 0,1,a,a+1 as 0,1,2,3.
        def add(a,b): return a^b
        mt=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
        def mul(a,b): return mt[a][b]
        invt={1:1,2:3,3:2}
        def inv(a): return invt[a]
        return add,mul,inv
    raise ValueError(q)

def normalize(v,q):
    _,mul,inv=field_ops(q)
    for x in v:
        if x:
            c=inv(x)
            return tuple(mul(c,y) for y in v)
    raise ValueError('zero')

def proj_points(n,q):
    seen=set()
    for v in product(range(q), repeat=n):
        if not any(v): continue
        seen.add(normalize(v,q))
    return sorted(seen)

def angle(u,v,q):
    _,mul,_=field_ops(q)
    best=len(u)+1
    for c in range(1,q):
        d=sum(a!=mul(c,b) for a,b in zip(u,v))
        best=min(best,d)
    return best

def compositions(total, parts):
    if parts==1:
        yield (total,); return
    for x in range(total+1):
        for tail in compositions(total-x,parts-1):
            yield (x,)+tail

def multinomial(a):
    z=factorial(sum(a))
    for x in a: z//=factorial(x)
    return z

def formula_shells(n,q,w):
    Q=q-1
    raw=Counter()
    for b in range(n-w+1):
        outside=comb(n-w,b)*(Q**b)
        for a in compositions(w,q): # a0 plus q-1 nonzero multiplicities
            m=max(a[1:]) if Q else 0
            r=b+w-m
            raw[r]+=outside*multinomial(a)
    raw[w]-=1 # remove v=0
    assert all(v%Q==0 for v in raw.values())
    return {r:v//Q for r,v in raw.items() if v}

def brute_shells(n,q,w):
    u=(1,)*w+(0,)*(n-w)
    return dict(sorted(Counter(angle(u,v,q) for v in proj_points(n,q)).items()))

def expected_radius_one(n,q,w):
    Q=q-1
    if w==1: return (n-1)*Q
    if w==2: return q+(n-2)*Q
    return n*Q

def expected_max_shell(n,q,w):
    Q=q-1
    if w==n: return 0
    return Q**(n-w-1)

for q in (2,3,4,5):
    for n in range(1,5):
        pts=proj_points(n,q)
        assert len(pts)==(q**n-1)//(q-1)
        for w in range(1,n+1):
            f=dict(sorted(formula_shells(n,q,w).items()))
            b=brute_shells(n,q,w)
            assert f==b,(q,n,w,f,b)
            assert sum(f.values())==len(pts)
            assert f.get(0,0)==1
            if n>=2:
                assert f.get(1,0)==expected_radius_one(n,q,w),(q,n,w,f)
            assert f.get(n,0)==expected_max_shell(n,q,w),(q,n,w,f)

# Representative nonbinary profiles.
assert formula_shells(3,3,1)=={0:1,1:4,2:6,3:2}
assert formula_shells(3,3,2)=={0:1,1:5,2:6,3:1}
assert formula_shells(3,3,3)=={0:1,1:6,2:6}
assert formula_shells(4,4,1)!=formula_shells(4,4,2)!=formula_shells(4,4,3)
print('VERIFY_OK')
