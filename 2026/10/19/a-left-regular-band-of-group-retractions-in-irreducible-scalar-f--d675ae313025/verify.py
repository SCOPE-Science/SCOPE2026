"""Exhaustive checks of group-endomorphism retractions and their commutation.
Uses generator images and independently tests group presentation relations.
No assumptions about the form of an idempotent endomorphism are used.
"""
from itertools import product
from math import comb

CASES = [
    (3, 1, None, 2), (5, 1, None, 4),
    (7, 1, None, 2), (7, 1, None, 3), (7, 1, None, 6),
    (11, 1, None, 10), (13, 1, None, 12),
    (2, 2, [1, 1, 1], 3),
    (2, 3, [1, 1, 0, 1], 7),
    (3, 2, [1, 0, 1], 4),
    (3, 2, [1, 0, 1], 8),
]

def count_prime_factors(n):
    ans = 0
    d = 2
    while d*d <= n:
        if n % d == 0:
            ans += 1
            while n % d == 0:
                n //= d
        d += 1
    return ans + (n > 1)

def check_case(p, d, modulus, m):
    q = p**d
    def digits(a):
        return [(a//p**i)%p for i in range(d)]
    def enc(ds):
        return sum(int(c)*p**i for i,c in enumerate(ds))
    def add(a,b):
        return enc([(x+y)%p for x,y in zip(digits(a),digits(b))])
    def neg(a):
        return enc([(-x)%p for x in digits(a)])
    def mul(a,b):
        if d==1: return a*b%p
        out = [0]*(2*d-1)
        for i,x in enumerate(digits(a)):
            for j,y in enumerate(digits(b)):
                out[i+j]=(out[i+j]+x*y)%p
        for i in range(2*d-2,d-1,-1):
            c=out[i]
            for j in range(d):
                out[i-d+j]=(out[i-d+j]-c*modulus[j])%p
        return enc(out[:d])
    def powfld(a,k):
        ans=1
        while k:
            if k&1: ans=mul(ans,a)
            a=mul(a,a);k//=2
        return ans
    alpha=next(a for a in range(1,q) if powfld(a,m)==1 and all(powfld(a,k)!=1 for k in range(1,m)))
    assert all(mul(a,powfld(a,q-2))==1 for a in range(1,q))
    apow=[powfld(alpha,j) for j in range(m)]
    def gmul(x,y):
        return (add(x[0],mul(apow[x[1]],y[0])),(x[1]+y[1])%m)
    def ginv(x):
        return (neg(mul(apow[(-x[1])%m],x[0])),(-x[1])%m)
    def gpow(x,k):
        ans=(0,0)
        for _ in range(k):ans=gmul(ans,x)
        return ans
    # Independent generator-relationship construction of all homomorphisms.
    homs=[]
    ts=list(product(range(q),repeat=d))
    hs=[(v,j) for v in range(q) for j in range(m) if gpow((v,j),m)==(0,0)]
    for images in ts:
        for h in hs:
            good=True
            for i,v in enumerate(images):
                conjugated=gmul(gmul(h,(v,0)),ginv(h))
                av=mul(alpha,p**i)
                target=0
                for z,coeff in zip(images,digits(av)):
                    for _ in range(coeff):target=add(target,z)
                if conjugated != (target,0):
                    good=False;break
            if not good:continue
            def f(x, images=images, h=h):
                y=(0,0)
                for v,e in zip(images,digits(x[0])):
                    for _ in range(e):y=gmul(y,(v,0))
                return gmul(y,gpow(h,x[1]))
            assert all(f(gmul(x,y))==gmul(f(x),f(y)) for x in ((0,1), (1,0), (0,0)) for y in ((0,1),(1,0),(0,0)))
            homs.append((images,h,f))
    # Check composition-idempotence on generating set, hence whole group.
    idem=[]
    gen=[(p**i,0) for i in range(d)]+[(0,1)]
    for images,h,f in homs:
        if all(f(f(x))==f(x) for x in gen):
            idem.append((images,h,f))
    nidem=len(idem)
    r=count_prime_factors(m)
    predicted=2+q*(2**r-1)
    assert nidem==predicted,(p,d,m,nidem,predicted)
    signatures = {tuple(f(x) for x in gen) for _,_,f in idem}
    assert len(signatures)==nidem
    for A in idem:
        for B in idem:
            # In the multiplication order A B = A after B.
            ab = tuple(A[2](B[2](x)) for x in gen)
            assert ab in signatures, (q,m,"not closed")
            aba=tuple(A[2](B[2](A[2](x))) for x in gen)
            assert aba == ab, (q,m,"not left regular")
    c=0
    deg=[]
    for A in idem:
        cnt=0
        for B in idem:
            if all(A[2](B[2](x))==B[2](A[2](x)) for x in gen):
                c+=1;cnt+=1
        deg.append(cnt)
    disjoint=(3**r-2**(r+1)+1)
    predicted_c=4+4*q*(2**r-1)+q*q*disjoint+q*(4**r-3**r)
    assert c==predicted_c,(p,d,m,c,predicted_c)
    expected_deg=[nidem,nidem]
    for s in range(1,r+1):
        centralizer=2+2**r-q+(q-1)*2**(r-s)
        expected_deg += [centralizer]*(q*comb(r,s))
    assert sorted(deg)==sorted(expected_deg),(p,d,m,sorted(deg),sorted(expected_deg))
    print('PASS',{'q':q,'m':m,'idempotents':nidem,'commuting_ordered_pairs':c,'all_homomorphisms':len(homs)})

if __name__=='__main__':
    for c in CASES:check_case(*c)
    print('ALL_EXACT_CHECKS_PASSED')
