"""Exact small-field checks for finite-field modular monoid rigidity.

Uses only Python's standard library. Theorems for arbitrary q,n rely on the proof,
not on these finite enumerations.
"""
from itertools import permutations, product
from math import factorial, gcd, prod

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5, 7)
        self.q = q
        self.p = 2 if q == 4 else q
        self.degree = 2 if q == 4 else 1
    def add(self, a, b):
        if self.q == 4:
            return a ^ b
        return (a+b)%self.q
    def neg(self, a):
        if self.q == 4: return a
        return -a%self.q
    def mul(self, a, b):
        if self.q != 4: return a*b%self.q
        aa=(a&1)*b
        bb=(a>>1)*(b<<1)
        v=aa^bb
        if v&8: v^=0b1100   # x^3 = x^2 + x (in GF(4))
        if v&4: v^=0b111    # x^2 = x + 1
        return v
    def power(self, a,n):
        z=1
        for _ in range(n): z=self.mul(z,a)
        return z
    def primitive(self):
        for a in range(1,self.q):
            if len({self.power(a,i) for i in range(self.q-1)})==self.q-1:return a
        raise AssertionError('no primitive scalar')

def vec_add(F,a,b): return tuple(F.add(x,y) for x,y in zip(a,b))
def vec_scale(F,c,a): return tuple(F.mul(c,x) for x in a)

def monoid_case(q,d):
    F=Field(q); V=list(product(range(q),repeat=d)); vid={v:i for i,v in enumerate(V)}
    Q=len(V)
    elements=list(product(range(q),V)) # (z,v) corresponds to (a,v) with a=z-1
    def multiply(x,y):
        a,v=x; b,w=y
        return F.mul(a,b),vec_add(F,v,vec_scale(F,a,w))
    for x in elements:
        for y in elements:
            # Original paper's law for m=(z-1,v)
            z,v=x; w,u=y
            a=F.add(z,F.neg(1)); b=F.add(w,F.neg(1))
            lhs=F.add(a,F.mul(z,b)),vec_add(F,v,vec_scale(F,z,u))
            c,delta=multiply(x,y)
            rhs=(F.add(c,F.neg(1)),delta)
            assert lhs==rhs
    left_zeros=[x for x in elements if all(multiply(x,y)==x for y in elements)]
    assert set(left_zeros)=={(0,v) for v in V}
    assert len([x for x in elements if x[0]!=0])==(q-1)*Q
    def transform(z,v):
        return tuple(vid[vec_add(F,vec_scale(F,z,x),v)] for x in V)
    Ts={transform(z,v) for z,v in elements}
    # Enumerate normalizer permutations fixing the zero vector; translations then
    # recover all normalizer elements. Testing a generating family is sufficient.
    unit_gens=[]
    zero=tuple([0]*d)
    for j in range(d):
        ej=tuple(1 if i==j else 0 for i in range(d))
        unit_gens.append(transform(1,ej))
    unit_gens.append(transform(F.primitive(),zero))
    ok=0
    observed=set()
    for tail in permutations(range(1,Q)):
        sigma=(0,)+tail
        inverse=[None]*Q
        for idx,output in enumerate(sigma):inverse[output]=idx
        if all(tuple(sigma[g[inverse[i]]] for i in range(Q)) in Ts for g in unit_gens):
            ok+=1
            observed.add(sigma)
    expected_gl=prod(q**d-q**j for j in range(d))
    expected_origin=expected_gl*F.degree
    assert ok==expected_origin,(q,d,ok,expected_origin)
    print(f'FIELD q={q} d={d}: monoid_size={len(elements)} left_zeros={Q} origin_normalizer={ok} aut={Q*ok} PASS')


def rank_one_case(q):
    F=Field(q); universe=list(range(q))
    # In scalar z coordinates the monoid is (F_q,multiplication), with 0 fixed.
    count=0
    for tail in permutations(range(1,q)):
        permutation=(0,)+tail
        if all(permutation[F.mul(a,b)]==F.mul(permutation[a],permutation[b]) for a in universe for b in universe):
            count+=1
    expected=sum(1 for j in range(1,q) if gcd(j,q-1)==1) if q>2 else 1
    assert count==expected,(q,count,expected)
    print(f'RANK_ONE q={q}: monoid_automorphisms={count} phi(q-1)={expected} PASS')

for q,d in [(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]:
    monoid_case(q,d)
for q in [2,3,4,5,7]:rank_one_case(q)
print('VERIFY_OK')
