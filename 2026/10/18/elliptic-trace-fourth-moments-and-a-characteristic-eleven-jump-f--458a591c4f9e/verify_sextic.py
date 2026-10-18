#!/usr/bin/env python3
"""Exact finite-field checks for the sixth-power graph energy formula.
Only Python's standard library is used. This finite test does not replace the proof.
"""
from collections import Counter
from math import gcd


class Field:
    def __init__(self, p, r=1):
        assert p in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
        assert r in (1, 2)
        self.p = p
        self.r = r
        self.q = p**r
        if r == 2:
            self.d = next(d for d in range(2, p) if pow(d, (p-1)//2, p) == p-1)

    def elt(self, n):
        return n % self.p

    def add(self, x, y):
        p = self.p
        if self.r == 1:
            return (x+y) % p
        return (x%p+y%p)%p + p*((x//p+y//p)%p)

    def neg(self, x):
        return self.add(0, -x) if self.r == 1 else ((-x%self.p)%self.p + self.p*((-(x//self.p))%self.p))

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        p = self.p
        if self.r == 1:
            return (x*y) % p
        a,b=x%p,x//p
        c,d=y%p,y//p
        return (a*c+self.d*b*d)%p + p*((a*d+b*c)%p)

    def pow(self, x, e):
        z = 1
        while e:
            if e & 1:
                z = self.mul(z,x)
            x = self.mul(x,x)
            e //= 2
        return z

    def chi(self, x):
        return 0 if x == 0 else (1 if self.pow(x,(self.q-1)//2)==1 else -1)

    def poly(self, x, coeff):
        z = 0
        for a in reversed(coeff):
            z = self.add(self.mul(z,x), self.elt(a))
        return z


def verify_field(p, r):
    F=Field(p,r)
    q=F.q
    mul=F.mul
    add=F.add
    chi=F.chi
    pol=F.poly
    # Formula ingredients: two elliptic character sums, singular-prime branch,
    # and the exceptional diagonal intersection.
    delta=chi(F.elt(-3))
    epsilon=chi(F.elt(-1))
    cubic_sum=sum(chi(pol(u,[0,-55,10,1])) for u in range(q))
    quartic_sum=sum(chi(mul(pol(u,[15,15,1]),pol(u,[20,20,1]))) for u in range(q))
    bad_diagonal=2*sum(pol(z,[5,0,10,0,1])==0 for z in range(q))
    if p != 11:
        a=-cubic_sum
        b=-quartic_sum-1
        n_pred=q-1-2*delta-delta*(2*a+b)
        assert abs(a) <= 2*q**0.5+1e-12, (p,r,a)
        assert abs(b) <= 2*q**0.5+1e-12, (p,r,b)
        e_pred=1+(q-1)*(3*q-2+gcd(6,q-1)-bad_diagonal-2*delta-delta*(2*a+b))
    else:
        assert bad_diagonal==8
        n_pred=2*q-4-2*epsilon
        e_pred=1+(q-1)*(4*q-13+gcd(6,q-1)-2*epsilon)
    n_direct=0
    for z in range(q):
        z2=mul(z,z)
        z4=mul(z2,z2)
        for w in range(q):
            w2=mul(w,w)
            w4=mul(w2,w2)
            total=add(add(z4,mul(z2,w2)),w4)
            total=add(total,mul(F.elt(15),add(z2,w2)))
            total=add(total,F.elt(15))
            n_direct += (total==0)
    assert n_direct==n_pred, (p,r,n_direct,n_pred)
    if p==11:
        # Independent check of the characteristic-11 conic factorization.
        for z in range(q):
            z2=mul(z,z)
            for w in range(q):
                w2=mul(w,w)
                first=add(add(z2,mul(z,w)),add(w2,F.elt(2)))
                second=add(F.sub(add(z2,w2),mul(z,w)),F.elt(2))
                left=F.poly(z,[0,0,0,0,1])
                left=add(left,mul(z2,w2))
                left=add(left,F.poly(w,[0,0,0,0,1]))
                left=add(left,mul(F.elt(15),add(z2,w2)))
                left=add(left,F.elt(15))
                assert mul(first,second)==left
    freq=Counter()
    for x in range(q):
        x6=F.pow(x,6)
        for y in range(q):
            freq[(add(x,y),add(x6,F.pow(y,6)))]+=1
    e_direct=sum(t*t for t in freq.values())
    assert e_direct==e_pred, (p,r,e_direct,e_pred)
    # The moment is E/q^2 by character orthogonality, not a sharp extension norm.
    return q,e_direct,n_direct,bad_diagonal


def main():
    cases=[(p,1) for p in (7,11,13,17,19,23,29,31,37,41,43,47)]
    cases.extend([(7,2),(11,2),(13,2)])
    checked=[]
    for p,r in cases:
        result=verify_field(p,r)
        checked.append(result)
        print('FIELD_OK',f'{p}^{r}', 'q,E,N,B=',result)
    print('VERIFY_OK', 'fields='+str(len(cases)),
          'total_ordered_pairs='+str(sum(q*q for q,*_ in checked)),
          'exceptional_characteristic_11=2',
          'elliptic_trace_checks=13',
          'collision_energy=PASS')

if __name__=='__main__':
    main()
