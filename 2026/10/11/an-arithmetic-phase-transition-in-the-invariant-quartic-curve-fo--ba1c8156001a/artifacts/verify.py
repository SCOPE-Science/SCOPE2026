"""Exact finite-field collision tests for a multiplicatively invariant quartic Fourier family."""
from collections import defaultdict


def least_nonsquare(p):
    squares = {x*x % p for x in range(p)}
    return next(x for x in range(2, p) if x not in squares)


class Field:
    def __init__(self, p, degree=1):
        self.p, self.degree = p, degree
        self.d = least_nonsquare(p) if degree == 2 else None
        self.elements = tuple(range(p**degree))
        self.zero, self.one = 0, 1

    def split(self, x):
        return x % self.p, x // self.p

    def add(self, x, y):
        if self.degree == 1:
            return (x+y) % self.p
        a,b = self.split(x)
        c,d = self.split(y)
        return (a+c) % self.p + self.p*((b+d) % self.p)

    def mul(self, x, y):
        if self.degree == 1:
            return x*y % self.p
        a,b = self.split(x)
        c,d = self.split(y)
        return (a*c + self.d*b*d) % self.p + self.p*((a*d+b*c) % self.p)

    def power(self, x, n):
        result = self.one
        while n:
            if n & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            n //= 2
        return result

    def signed_int(self, t):
        return t % self.p

    def minus_int(self, t):
        return self.signed_int(-t)

    def quadchar(self, x):
        if x == 0:
            return 0
        return 1 if self.power(x, (len(self.elements)-1)//2) == self.one else -1


def gauss_mul(a,b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def check_field(p, degree):
    F = Field(p,degree)
    q=len(F.elements)
    h=F.quadchar(F.minus_int(7))
    k=F.quadchar(F.minus_int(3))
    graph = {t:F.power(t,4) for t in F.elements}
    pair_sums = defaultdict(list)
    for a in F.elements:
        for b in F.elements:
            pair_sums[(F.add(a,b),F.add(graph[a],graph[b]))].append((a,b))
    w=[0]*q
    energy=0
    for pairs in pair_sums.values():
        energy+=len(pairs)**2
        for a,b in pairs:
            w[a]+=len(pairs)
    assert w[0] == 3*q-2+(q-1)*h, (q,'zero',w[0],h)
    assert all(w[t]==3*q-3-h-2*k for t in F.elements if t), (q,'nonzero',w,h,k)
    assert energy==3*q*q-3*q+1-2*(q-1)*k
    sample_z=[(0,0),(1,0),(2,0),(-1,0),(1,2),(-2,3)]
    for z in sample_z:
        conv=defaultdict(lambda:(0,0))
        for y,pairs in pair_sums.items():
            real=imag=0
            for a,b in pairs:
                v=gauss_mul(z if not a else (1,0),z if not b else (1,0))
                real+=v[0]
                imag+=v[1]
            conv[y]=(real,imag)
        direct=sum(re*re+im*im for re,im in conv.values())
        zr,zi=z
        mod2=zr*zr+zi*zi
        predicted=mod2*mod2+4*(q-1)*mod2+4*(q-1)*(1+h)*zr+(q-1)*(3*q-8-4*h-2*k)
        assert direct==predicted,(q,z,direct,predicted)
    return q,len(pair_sums),h,k


def main():
    qs=[]
    for p in (5,7,11,13,17,19,23,29,31,37,41):
        qs.append(check_field(p,1))
    for p in (5,7,11):
        qs.append(check_field(p,2))
    assert {h for q,_,h,_ in qs}=={-1,0,1}
    assert {k for q,_,_,k in qs}=={-1,1}
    print('VERIFY_OK fields=%d Gaussian_integer_fourth_moments=%d local_representation_profiles=%d quadratic_characters=PASS'%(len(qs),6*len(qs),len(qs)))


if __name__=='__main__':
    main()
