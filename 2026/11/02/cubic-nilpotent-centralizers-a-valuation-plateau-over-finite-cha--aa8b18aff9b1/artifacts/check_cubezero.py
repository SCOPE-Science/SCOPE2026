"""Independent exhaustive checks of cube-zero 2-by-2 matrix counts.

Requires Python 3 standard library only. All rings are represented by explicit
arithmetic tables; neither the trace/determinant proof nor its stratum formula
is used to decide whether a matrix is cube-zero.
"""
from itertools import product
from math import ceil


def gf4_mul(a, b):
    out = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                out ^= 1 << (i + j)
    if out & 8:
        out ^= 0b1110
    if out & 4:
        out ^= 0b111
    return out


class Ring:
    def __init__(self, q, s, kind):
        self.q, self.s, self.kind = q, s, kind
        self.order = q**s
        self.digits = [self._unpack(x) for x in range(self.order)]
        self.zero = 0
        self.addition = [[self._add(x, y) for y in range(self.order)] for x in range(self.order)]
        self.multiplication = [[self._mul(x, y) for y in range(self.order)] for x in range(self.order)]

    def _unpack(self, x):
        return tuple((x // self.q**i) % self.q for i in range(self.s))

    def _add(self, a, b):
        if self.kind == 'integers':
            return (a+b) % self.order
        ad, bd = self.digits[a], self.digits[b]
        return sum(((ad[i]^bd[i]) if self.q==4 else (ad[i]+bd[i]) % self.q)*self.q**i for i in range(self.s))

    def _mul(self, a, b):
        if self.kind == 'integers':
            return (a*b) % self.order
        ad, bd = self.digits[a], self.digits[b]
        out = [0]*self.s
        for i in range(self.s):
            for j in range(self.s-i):
                v = gf4_mul(ad[i],bd[j]) if self.q==4 else (ad[i]*bd[j])%self.q
                out[i+j] = out[i+j]^v if self.q==4 else (out[i+j]+v)%self.q
        return sum(out[i]*self.q**i for i in range(self.s))

    def valuation(self, x):
        if not x:return self.s
        if self.kind=='integers':
            v=0
            while x%self.q==0:
                x//=self.q;v+=1
            return v
        return next(i for i,a in enumerate(self.digits[x]) if a)


def cube_zero(A,R):
    a,b,c,d=A
    add,mul=R.addition,R.multiplication
    aa=add[mul[a][a]][mul[b][c]]
    ab=add[mul[a][b]][mul[b][d]]
    ca=add[mul[c][a]][mul[d][c]]
    dd=add[mul[c][b]][mul[d][d]]
    return all((
        add[mul[aa][a]][mul[ab][c]]==0,
        add[mul[aa][b]][mul[ab][d]]==0,
        add[mul[ca][a]][mul[dd][c]]==0,
        add[mul[ca][b]][mul[dd][d]]==0,
    ))


def prediction(q,s):
    c=(s+2)//3
    per=(q*q-1)*q**(3*s-2-c)
    total=q**(4*(s-c))+c*per
    layers={v:(per if v<c else (q**4-1)*q**(4*(s-v-1))) for v in range(s)}
    return total,layers


def check(q,s,kind):
    R=Ring(q,s,kind)
    layers={v:0 for v in range(s)}
    total=1 # zero matrix
    for A in product(range(R.order),repeat=4):
        if all(x==0 for x in A):continue
        if cube_zero(A,R):
            v=min(R.valuation(x) for x in A)
            layers[v]+=1
            total+=1
    expected, strata = prediction(q,s)
    assert total==expected and layers==strata, (kind,q,s,total,expected,layers,strata)
    print(f'{kind} q={q} length={s} cube_zero={total} strata={list(layers.values())}')


def main():
    cases=[(2,1,'polynomial'),(2,2,'polynomial'),(2,3,'polynomial'),(2,4,'polynomial'),
           (3,1,'polynomial'),(3,2,'polynomial'),(4,1,'polynomial'),(4,2,'polynomial'),
           (2,2,'integers'),(2,3,'integers'),(2,4,'integers'),(3,2,'integers'),
           (3,3,'integers'),(3,3,'polynomial')]
    for args in cases:check(*args)
    print('CUBE_ZERO_CHAIN_RING_CENSUS_OK',len(cases))


if __name__=='__main__':main()
