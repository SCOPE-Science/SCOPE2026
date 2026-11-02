#!/usr/bin/env python3
"""Direct finite-algebra generation checks for the finite product formula.
Uses multiplication and linear-span closure, not the residue/tangent criterion.
Only the prime field F_2 and residue fields F_2/F_4 are tested exhaustively.
"""
import itertools
import math


def f4_mul(x, y):
    t = 0
    for i in range(2):
        for j in range(2):
            if (x >> i) & 1 and (y >> j) & 1:
                t ^= 1 << (i+j)
    if t & 4:  # alpha^2 = alpha + 1
        t ^= 7
    return t


class Algebra:
    def __init__(self, field_degree, d, r):
        assert field_degree in (1, 2)
        self.f = field_degree
        self.d = d
        self.r = r
        self.width = field_degree*(d+1)
        self.dim = self.width*r
        self.size = 1 << self.dim
        self.cell_mask = (1 << self.width)-1
        self.field_mask = (1 << self.f)-1
        self.one = sum(1 << (i*self.width) for i in range(r))
        self.cellmul = self.precompute()

    def mult_field(self, x, y):
        return x & y if self.f == 1 else f4_mul(x, y)

    def precompute(self):
        result = [[0]*(1 << self.width) for _ in range(1 << self.width)]
        for a in range(1 << self.width):
            for b in range(1 << self.width):
                a0 = a & self.field_mask
                b0 = b & self.field_mask
                c = self.mult_field(a0, b0)
                for i in range(self.d):
                    ai = (a >> ((i+1)*self.f)) & self.field_mask
                    bi = (b >> ((i+1)*self.f)) & self.field_mask
                    ci = self.mult_field(a0, bi) ^ self.mult_field(ai, b0)
                    c |= ci << ((i+1)*self.f)
                result[a][b] = c
        return result

    def mul(self, a, b):
        c = 0
        for i in range(self.r):
            shift = i*self.width
            aa = (a >> shift) & self.cell_mask
            bb = (b >> shift) & self.cell_mask
            c |= self.cellmul[aa][bb] << shift
        return c

    def generated(self, gens):
        pivots = [0]*self.dim
        todo = []
        rank = 0
        def add(x):
            nonlocal rank
            while x:
                bit = x.bit_length()-1
                if pivots[bit]:
                    x ^= pivots[bit]
                else:
                    pivots[bit] = x
                    todo.append(x)
                    rank += 1
                    return
        add(self.one)
        for g in gens:
            add(g)
        while todo and rank < self.dim:
            a = todo.pop()
            for g in gens:
                add(self.mul(a, g))
        return rank == self.dim


def mobius(n):
    p = 2
    count = 0
    while p*p <= n:
        if n % p == 0:
            n //= p
            count += 1
            if n % p == 0:
                return 0
        else:
            p += 1
    if n > 1:
        count += 1
    return -1 if count % 2 else 1


def expected(q, f, d, r, k):
    Q = q**f
    t = sum(mobius(e)*q**(k*f//e) for e in range(1,f+1) if f % e == 0)
    assert t % f == 0
    n_orbits = t//f
    if k < d or r > n_orbits:
        return 0
    residues = 1
    for j in range(r):
        residues *= (t - f*j)
    tangent = 1
    for j in range(d):
        tangent *= (Q**k-Q**j)
    # count of generator tuples = residue assignments * full-rank tangent
    # assignments * unrestricted higher nilpotent coordinates.
    # For R=F_Q[x_1,...,x_d]/m^2, no higher nilpotents.
    return residues * tangent**r


def check(q,f,d,r,k):
    assert q == 2
    A = Algebra(f,d,r)
    count = sum(A.generated(gens) for gens in itertools.product(range(A.size),repeat=k))
    ex = expected(q,f,d,r,k)
    print('EXHAUSTIVE_OK q=%d f=%d d=%d r=%d k=%d total=%d success=%d'%(q,f,d,r,k,A.size**k,count))
    assert count == ex, (count,ex)




def verify_higher_truncation():
    # An independent length-three algebra: F_2[x]/(x^3), encoded by 3 bits.
    def mul3(a,b):
        x=0
        for i in range(3):
            for j in range(3-i):
                if (a>>i)&1 and (b>>j)&1:
                    x^=1<<(i+j)
        return x
    def rank3(gens):
        pivots=[0]*3
        span=[]
        def add(v):
            while v:
                j=v.bit_length()-1
                if pivots[j]:v^=pivots[j]
                else:
                    pivots[j]=v
                    span.append(v)
                    return
        add(1)
        for g in gens:add(g)
        idx=0
        while idx <len(span):
            a=span[idx];idx+=1
            for g in gens:add(mul3(a,g))
        return len(span)==3
    for k in (1,2):
        actual=sum(rank3(g) for g in itertools.product(range(8),repeat=k))
        predicted=expected(2,1,1,1,k)*2**k
        assert actual==predicted,(actual,predicted)
        print('HIGHER_LENGTH_OK h=3 k=%d total=%d success=%d'%(k,8**k,actual))




def verify_mixed_local_types():
    # Algebra F_2[x]/(x^2) times F_2[y,z]/(y,z)^2, 5-dimensional.
    # The two factors have the same residue field but tangent ranks 1 and 2.
    def local_product(a,b,d):
        c=(a&1)&(b&1)
        for j in range(d):
            bit=((a&1)*((b>>(j+1))&1)) ^ (((a>>(j+1))&1)*(b&1))
            c |= bit << (j+1)
        return c
    def mul(a,b):
        return local_product(a&3,b&3,1) | (local_product((a>>2)&7,(b>>2)&7,2)<<2)
    def generated(gens):
        piv=[0]*5;basis=[]
        def add(x):
            while x:
                j=x.bit_length()-1
                if piv[j]:x^=piv[j]
                else:piv[j]=x;basis.append(x);return
        add(1 | (1<<2))
        for g in gens:add(g)
        at=0
        while at <len(basis):
            v=basis[at];at+=1
            for g in gens:add(mul(v,g))
        return len(basis)==5
    got=sum(generated(g) for g in itertools.product(range(32),repeat=2))
    predicted=(4*3)*(4-1)*((4-1)*(4-2))
    assert got==predicted,(got,predicted)
    print('MIXED_LOCAL_OK q=2 d=(1,2) k=2 total=1024 success=%d'%got)


def run():
    cases = [(2,1,1,1,1), (2,1,1,1,2), (2,1,1,2,1),
             (2,1,1,2,2),(2,1,1,3,2),(2,1,1,4,2),
             (2,2,1,1,1),(2,2,1,1,2),(2,2,1,2,2),
             (2,2,2,1,2)]
    for args in cases:
        check(*args)
    # First nontrivial extension-field + two tangent directions: q=2,f=d=k=2.
    # Here the maximal r permitting 2 generators is six.
    assert sum(mobius(e)*2**(2*2//e) for e in (1,2))//2 == 6
    assert expected(2,2,2,1,2) == 2160
    verify_higher_truncation()
    verify_mixed_local_types()
    print('VERIFY_OK')


if __name__=='__main__':
    run()
