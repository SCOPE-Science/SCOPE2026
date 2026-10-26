"""Independent finite-field check of the diagonal quartic bitangent classification.

The square-on-a-line test is independent of the predicted fourth-root
count formula.  All computations use exact arithmetic modulo p.
"""
from collections import Counter
from math import gcd


def binary_quartic_square_up_to_scalar(coeff, p):
    """Geometric square criterion for a binary quartic with F_p coefficients."""
    a, b, c, d, e = [x % p for x in coeff]
    if a:
        v = b * pow(2*a, -1, p) % p
        w = (c*pow(a, -1, p) - v*v) * pow(2, -1, p) % p
        return d*pow(a, -1, p)%p == (2*v*w)%p and e*pow(a, -1, p)%p == w*w%p
    if b:
        return False
    if c:
        return (d*d - 4*c*e) % p == 0
    return d==0  # e*y^4, including zero; smooth quartic prevents zero restriction


def geometric_rational_bitangents(p, a, b, c):
    count=0
    for A in range(p):
        for B in range(p):
            # normalized C=1; substitute z=-A*x-B*y
            ff=[a+c*A**4,4*c*A**3*B,6*c*A**2*B**2,4*c*A*B**3,b+c*B**4]
            count += binary_quartic_square_up_to_scalar(ff,p)
    for A in range(p):
        # C=0, normalized B=1; y=-A*x
        ff=[a+b*A**4,0,0,0,c]
        count += binary_quartic_square_up_to_scalar(ff,p)
    # B=C=0: line x=0
    count += binary_quartic_square_up_to_scalar([b,0,0,0,c],p)
    return count


def predicted_rational_bitangents(p,a,b,c):
    def count_roots(z):
        return sum(pow(t,4,p)==z%p for t in range(1,p))
    inv=lambda z:pow(z,-1,p)
    return (count_roots(-b*inv(a)) + count_roots(-c*inv(a))
            + count_roots(-c*inv(b))
            + count_roots(b*inv(a))*count_roots(c*inv(a)))


def representative_generator(p):
    factors=[d for d in range(1,p-1) if (p-1)%d==0]
    return next(g for g in range(2,p) if all(pow(g,d,p)!=1 for d in factors))


def check_prime(p):
    g=representative_generator(p)
    reps=sorted(set(pow(g,j,p) for j in range(4)))
    observed=Counter()
    for a in reps:
        for b in reps:
            for c in reps:
                observed[(geometric_rational_bitangents(p,a,b,c),)] += 1
                predicted=predicted_rational_bitangents(p,a,b,c)
                assert geometric_rational_bitangents(p,a,b,c)==predicted,(p,a,b,c,predicted)
    expected=({4} if p%4==3 else ({0,4,28} if p%8==1 else {0,4,8,16}))
    assert {x[0] for x in observed} == expected,(p, observed, expected)
    print('p=',p, 'coefficient samples=',len(reps)**3, 'rational bitangent counts=',dict(observed))


def theoretical_profiles():
    from collections import defaultdict
    d={}
    for eps in [0,2]:
        out=defaultdict(list)
        for r in range(4):
            for s in range(4):
                L=lambda k:4//gcd(4,k%4)
                cc=Counter()
                for k in [r+eps,s+eps,s-r+eps]:
                    z=L(k);cc[z]+=4//z
                z=max(L(r),L(s));cc[z]+=16//z
                assert sum(k*v for k,v in cc.items())==28
                out[tuple(sorted(cc.items()))].append((r,s))
        d[eps]=out
    assert set(d[0])=={((1,28),),((1,4),(2,12)),((1,4),(4,6)),((2,2),(4,6))}
    assert set(d[2])=={((1,16),(2,6)),((1,8),(2,10)),((1,4),(4,6)),((2,2),(4,6))}
    print('q congruent 1 mod 8:',dict(d[0]))
    print('q congruent 5 mod 8:',dict(d[2]))
    print('q congruent 3 mod 4: one invariant profile 1^4 2^12')

if __name__=='__main__':
    for p in [3,5,7,11,13,17,19,23,29,31,37]:
        check_prime(p)
    theoretical_profiles()
    print('VERIFY_OK: explicit binary-square enumeration agrees with fourth-root theorem for all 11 prime fields and all coefficient fourth-power class triples')

# Secondary check over the genuinely non-prime field F9 (adjoin i^2=-1 to F3).
def f9add(x,y): return (x%3+y%3)%3+3*((x//3+y//3)%3)
def f9neg(x):return (-(x%3))%3+3*((-(x//3))%3)
def f9mul(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
def f9pow(a,k):
    v=1
    while k:
        if k&1:v=f9mul(v,a)
        a=f9mul(a,a);k//=2
    return v
def f9sum(*xs):
    v=0
    for x in xs:v=f9add(v,x)
    return v
def f9inv(x):return f9pow(x,7)
def f9square_quartic(v):
    a,b,c,d,e=v
    if a:
        rat=lambda x:f9mul(x,f9inv(a))
        vv=f9mul(rat(b),2)
        ww=f9mul(f9add(rat(c),f9neg(f9mul(vv,vv))),2)
        return rat(d)==f9mul(2,f9mul(vv,ww)) and rat(e)==f9mul(ww,ww)
    if b:return False
    if c:return f9mul(d,d)==f9mul(4,f9mul(c,e))
    return d==0

def check_f9():
    g=next(x for x in range(2,9) if len({f9pow(x,j) for j in range(8)})==8)
    classes=[f9pow(g,j) for j in range(4)]
    counts=Counter()
    for a in classes:
      for b in classes:
       for c in classes:
        n=0
        for A in range(9):
         for B in range(9):
          n+=f9square_quartic([
           f9sum(a,f9mul(c,f9pow(A,4))),
           f9mul(f9mul(c,f9pow(A,3)),B),  # 4=1 in characteristic 3
           0,                               # 6=0 in characteristic 3
           f9mul(f9mul(c,A),f9pow(B,3)),
           f9sum(b,f9mul(c,f9pow(B,4)))
          ])
        for A in range(9):
         n+=f9square_quartic([f9sum(a,f9mul(b,f9pow(A,4))),0,0,0,c])
        n+=f9square_quartic([b,0,0,0,c])
        counts[n]+=1
    assert counts==Counter({28:4,4:36,0:24}),counts
    print('GF9: 64 coefficient representatives, independent line-square counts',dict(counts))
    print('GF9_VERIFY_OK')
if __name__ == '__main__':
    check_f9()
