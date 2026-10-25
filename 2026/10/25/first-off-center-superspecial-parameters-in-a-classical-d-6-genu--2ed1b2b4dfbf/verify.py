#!/usr/bin/env python3
"""Exact finite-field coefficient and gcd verification for the genus-three D6 pencil.
Only Python's standard library is required.
"""
from math import comb

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31)

def normalize(f, p):
    a = [int(x) % p for x in f]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def divmod_poly(f, g, p):
    f, g = normalize(f,p), normalize(g,p)
    assert g != [0]
    rem = f[:]
    quot = [0] * max(1, len(f) - len(g) + 1)
    inv = pow(g[-1], -1, p)
    while rem != [0] and len(rem) >= len(g):
        shift = len(rem) - len(g)
        c = rem[-1] * inv % p
        quot[shift] = c
        for j, gj in enumerate(g):
            rem[shift+j] = (rem[shift+j] - c*gj) % p
        rem = normalize(rem, p)
    return normalize(quot,p), rem

def gcd_poly(a,b,p):
    a,b=normalize(a,p),normalize(b,p)
    while b != [0]:
        _, r=divmod_poly(a,b,p)
        a,b=b,r
    if a == [0]: return a
    return normalize([(x*pow(a[-1], -1,p))%p for x in a],p)

def coeff_at_u(n,k,p):
    """Coefficient [u^k](u^2-tu+1)^n, as polynomial in t modulo p."""
    ans=[0]*(n+1)
    for b in range(n+1):
        if (k-b)%2: continue
        a=(k-b)//2
        c=n-a-b
        if a<0 or c<0: continue
        ans[b]=(ans[b]+(-1)**b*comb(n,b)*comb(n-b,a))%p
    return normalize(ans,p)

def get_ab(p):
    assert p>=5 and p%2==1 and p%3!=0
    n=(p-1)//2
    m=(p-(1 if p%6==1 else 5))//6
    return coeff_at_u(n,m,p),coeff_at_u(n,n,p)

EXPECTED={5:[1],7:[0,1],11:[0,1],13:[1],17:[1],
          19:[0,1],23:[0,1],29:[1],31:[0,11,0,1]}

def full_hasse_numeric(p,t):
    """Independent f(x)^((p-1)/2) convolution and [x^(pi-j)] extraction."""
    n=(p-1)//2
    f={1:1,4:(-t)%p,7:1}
    accum={0:1}
    for _ in range(n):
        nxt={}
        for d,c in accum.items():
            for e,ce in f.items():
                nxt[d+e]=(nxt.get(d+e,0)+c*ce)%p
        accum=nxt
    return [[accum.get(p*i-j,0) for j in (1,2,3)] for i in (1,2,3)]

def derived_hasse(p,t):
    a,b=get_ab(p)
    def ev(poly): return sum(v*pow(t,i,p) for i,v in enumerate(poly))%p
    A,B=ev(a),ev(b)
    return [[A,0,0],[0,B,0],[0,0,A]] if p%6==1 else [[0,0,A],[0,B,0],[A,0,0]]

if __name__ == '__main__':
    for p in PRIMES:
        a,b=get_ab(p)
        g=gcd_poly(a,b,p)
        assert g==EXPECTED[p],(p,g,EXPECTED[p])
        for t in range(p):
            assert derived_hasse(p,t)==full_hasse_numeric(p,t), (p,t)
        print('p',p,'gcd monic coefficients low-to-high',g,'Adeg',len(a)-1,'Bdeg',len(b)-1)
    a,b=get_ab(31)
    # The two polynomial equations have common zero scheme V(t(t^2-20)).
    assert gcd_poly(a,b,31)==[0,11,0,1] # t^3-20t
    assert [t for t in range(31) if all(z==0 for row in derived_hasse(31,t) for z in row)]==[0,12,19]
    # For p=31, t=0 and t=+/-12 are admissible smooth parameters.
    assert all((t*t-4)%31 != 0 for t in (0,12,19))
    # Explicit degree-five coefficient identity A_31(t)=4t(t^2-20)(t^2-12).
    assert a==normalize([0, 4*240, 0,-4*32,0,4],31),a
    # At p=31, t=+/-12 are not t=0 nor degenerations and are conjugate via t -> -t.
    print('p31 A_31 coeffs',a)
    print('p31 B_31 coeffs',b)
    print('superspecial parameters for p31: 0,12,19')
    print('VERIFY_OK')
