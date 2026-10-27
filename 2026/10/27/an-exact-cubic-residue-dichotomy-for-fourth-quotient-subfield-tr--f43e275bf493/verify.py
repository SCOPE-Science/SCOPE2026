#!/usr/bin/env python3
"""Exact checks for the quadratic-extension fourth-quotient cubic-coset theorem.

No third-party packages. Every tested field is a PRIME quadratic field.
The theorem itself also covers nonprime odd prime-power base fields.
"""
from collections import Counter


def factor_primes(n):
    ans=[]; d=2
    while d*d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0: n//=d
        d += 1
    if n>1: ans.append(n)
    return ans


def check(p):
    assert p%12==7
    nonres=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    one=(1,0)
    def mul(a,b):
        return ((a[0]*b[0]+nonres*a[1]*b[1])%p,
                (a[0]*b[1]+a[1]*b[0])%p)
    def power(a,n):
        y=one
        while n:
            if n&1: y=mul(y,a)
            a=mul(a,a); n>>=1
        return y
    divs=factor_primes(p*p-1)
    generator=None
    for aa in range(p):
        for bb in range(p):
            g=(aa,bb)
            if g!=(0,0) and all(power(g,(p*p-1)//prime)!=one for prime in divs):
                generator=g; break
        if generator: break
    assert generator is not None
    d=3*(p+1)//4
    assert d*(4*(p-1)//3)==p*p-1
    h=power(generator,d)
    H=set(); z=one
    for _ in range(4*(p-1)//3):
        assert z not in H
        H.add(z); z=mul(z,h)
    assert z==one
    assert len([z for z in H if z[1]==0])==(p-1)//3
    # Fibers over the base-field translate set.
    R=Counter()
    for z in H | {(0,0)}:
        for a in range(p):
            R[((z[0]+a)%p,z[1])]+=1
    assert sum(R.values())==p*(len(H)+1)
    cube2=pow(2,(p-1)//3,p)==1
    base=(p+2)//3
    assert all(R[(a,0)]==base for a in range(p))
    # The entire affine base-field fiber has one representation count.
    assert all(R[(a,b)] == R[(0,b)] for b in range(1,p) for a in range(p))
    counts=Counter(R[(0,b)] for b in range(1,p))
    expected=(Counter({3:(p-1)//3, 0:2*(p-1)//3}) if cube2 else
              Counter({2:(p-1)//3,1:(p-1)//3,0:(p-1)//3}))
    assert counts==expected,(p,counts,expected)
    distinct=sum(1 for a in range(p) for b in range(p) if R[(a,b)]>0)
    expected_card=(p*(p+2)//3 if cube2 else p*(2*p+1)//3)
    assert distinct==expected_card
    # Primitive fourth-quotient generator and trace/norm identities.
    assert power(h,4)[1]==0
    assert power(h,2)[1]!=0
    tr=(2*h[0])%p
    norm=(h[0]**2-nonres*h[1]**2)%p
    assert tr!=0
    assert (tr*tr-2*norm)%p==0
    print('CHECK_OK',f'p={p}',f'd={d}',f'2_cube={cube2}',
          f'base_representations={base}',f'covered={distinct}',
          f'missing={p*p-distinct}',f'generator={generator}',f'nonresidue={nonres}')

if __name__=='__main__':
    for p in (7,19,31,43,67,79,103): check(p)
    print('CERTIFICATE_OK 7 complete quadratic-prime-field enumerations')
