#!/usr/bin/env python3
"""Exact checks for the local normal form of constant-rank quadratic pencils.

Python 3 standard library only. Polynomial arithmetic has integer coefficients;
finite-field checks are exhaustive for the listed small canonical pencils.
No finite check is used to assert the infinite-family theorem.
"""
from collections import defaultdict
from itertools import product

class Poly:
    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v}

    @staticmethod
    def var(s):
        return Poly({(s,): 1})

    @staticmethod
    def scalar(a):
        return Poly({(): a})

    def __add__(self, other):
        if isinstance(other, int):
            other = Poly.scalar(other)
        d = dict(self.d)
        for k, v in other.d.items():
            d[k] = d.get(k, 0) + v
        return Poly(d)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + (-other if not isinstance(other, int) else -other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Poly({k: v * other for k, v in self.d.items()})
        d = defaultdict(int)
        for a, x in self.d.items():
            for b, y in other.d.items():
                d[tuple(sorted(a + b))] += x*y
        return Poly(d)

    __rmul__ = __mul__

    def __eq__(self, other):
        if isinstance(other, int):
            other = Poly.scalar(other)
        return self.d == other.d

ONE = Poly.scalar(1)
ZERO = Poly()

def partitions(n, least=1):
    if n == 0:
        yield ()
    else:
        for k in range(least, n+1):
            for rest in partitions(n-k, k):
                yield (k,) + rest

def algebraic_test(partition, chosen):
    h = len(partition)
    u = {}
    v = {}
    pivot = (chosen, partition[chosen]-1)
    for i, size in enumerate(partition):
        for j in range(size):
            u[i,j] = Poly.var('u_%d_%d' % (i,j))
        for j in range(size+1):
            v[i,j] = ONE if (i,j) == (chosen,size) else Poly.var('v_%d_%d' % (i,j))
    alpha = v[chosen, partition[chosen]-1]
    q0 = ZERO
    q1_rest = ZERO
    for i, size in enumerate(partition):
        for j in range(size):
            if (i,j) != pivot:
                q0 += u[i,j] * v[i,j]
                q1_rest += u[i,j] * v[i,j+1]
    q0 += (-q1_rest)*alpha
    predicted = ZERO
    for i, size in enumerate(partition):
        for j in range(size):
            if (i,j) != pivot:
                predicted += u[i,j] * (v[i,j] - alpha*v[i,j+1])
    assert q0 == predicted, (partition,chosen,'local equation')

    # Invert the change of variables in the v-coordinates using recursion.
    a = Poly.var('a')
    recon = {}
    for i, size in enumerate(partition):
        recon[i,size] = ONE if i==chosen else Poly.var('w_%d' % i)
        for j in reversed(range(size)):
            if (i,j) == pivot:
                recon[i,j] = a
            else:
                z = Poly.var('z_%d_%d' % (i,j))
                recon[i,j] = z + a*recon[i,j+1]
    assert recon[chosen,partition[chosen]-1] == a
    for i,size in enumerate(partition):
        for j in range(size):
            if (i,j) != pivot:
                assert recon[i,j] - a*recon[i,j+1] == Poly.var('z_%d_%d' % (i,j))
    assert sum(1 for i,s in enumerate(partition) for j in range(s) if (i,j)!=pivot)==sum(partition)-1
    return True



def algebraic_test_front(partition, chosen):
    """Second affine atlas: normalize the first v coordinate, eliminate q0."""
    u = {}
    v = {}
    pivot = (chosen, 0)
    for i, size in enumerate(partition):
        for j in range(size):
            u[i,j] = Poly.var('u_%d_%d' % (i,j))
        for j in range(size+1):
            v[i,j] = ONE if (i,j) == pivot else Poly.var('v_%d_%d' % (i,j))
    alpha = v[chosen,1]
    q0_rest = ZERO
    q1 = ZERO
    for i, size in enumerate(partition):
        for j in range(size):
            if (i,j) != pivot:
                q0_rest += u[i,j] * v[i,j]
                q1 += u[i,j] * v[i,j+1]
    q1 += -q0_rest * alpha
    predicted = ZERO
    for i, size in enumerate(partition):
        for j in range(size):
            if (i,j) != pivot:
                predicted += u[i,j] * (v[i,j+1]-alpha*v[i,j])
    assert q1 == predicted, (partition,chosen,'front chart equation')
    a = Poly.var('a')
    recon = {}
    for i, size in enumerate(partition):
        recon[i,0] = ONE if i==chosen else Poly.var('w_%d' % i)
        for j in range(size):
            if (i,j) == pivot:
                recon[i,j+1] = a
            else:
                z = Poly.var('z_%d_%d' % (i,j))
                recon[i,j+1] = z + a*recon[i,j]
    assert recon[chosen,1] == a
    for i,size in enumerate(partition):
        for j in range(size):
            if (i,j) != pivot:
                assert recon[i,j+1]-a*recon[i,j] == Poly.var('z_%d_%d' % (i,j))
    return True

def projective_vectors(q,n):
    for first in range(n):
        for tail in product(range(q), repeat=n-first-1):
            yield (0,)*first + (1,) + tail

def is_dep(a,b,q):
    # rank of the two rows <2
    return all((a[i]*b[j] - a[j]*b[i])%q == 0 for i in range(len(a)) for j in range(i+1,len(a)))

def finite_test(partition,q=3):
    h=len(partition)
    r=sum(partition)
    uj=[]; vj=[]
    for i,size in enumerate(partition):
        uj += [(i,j) for j in range(size)]
        vj += [(i,j) for j in range(size+1)]
    U={a:i for i,a in enumerate(uj)}
    V={a:i+r for i,a in enumerate(vj)}
    n=len(uj)+len(vj)
    Xcount=0
    actual_sing=set()
    for vec in projective_vectors(q,n):
        q0=sum(vec[U[i,j]]*vec[V[i,j]] for i,s in enumerate(partition) for j in range(s))%q
        q1=sum(vec[U[i,j]]*vec[V[i,j+1]] for i,s in enumerate(partition) for j in range(s))%q
        if q0 or q1:
            continue
        Xcount+=1
        gr0=[0]*n; gr1=[0]*n
        for i,s in enumerate(partition):
            for j in range(s):
                a=U[i,j]
                b=V[i,j]
                c=V[i,j+1]
                gr0[a]=vec[b]
                gr1[a]=vec[c]
                gr0[b]=vec[a]
                gr1[c]=vec[a]
        if is_dep(gr0,gr1,q):
            actual_sing.add(vec)
    scroll=set()
    for a,b in projective_vectors(q,2):
        for weights in projective_vectors(q,h):
            v=[]
            for i,size in enumerate(partition):
                v += [(weights[i] * pow(-b,size-j,q)*pow(a,j,q))%q for j in range(size+1)]
            # normalize projective coordinates
            w=(0,)*r + tuple(v)
            k=next(x for x in w if x)
            w=tuple(x*pow(k,-1,q)%q for x in w)
            scroll.add(w)
    assert actual_sing==scroll, (partition,q,'singular support',len(actual_sing),len(scroll))
    affine_cone_size = q**(r+h)+(q**r-1)*q**(r+h-2)
    expected_base=(affine_cone_size-1)//(q-1)
    assert Xcount==expected_base,(partition,q,'base count',Xcount,expected_base)
    expected_scroll=(q+1)*(q**h-1)//(q-1)
    assert len(scroll)==expected_scroll,(partition,q,len(scroll),expected_scroll)
    return Xcount,len(actual_sing)


def main():
    checked=0
    for r in range(2,9):
        for part in partitions(r):
            for chosen in range(len(part)):
                algebraic_test(part,chosen)
                algebraic_test_front(part,chosen)
                checked += 2
    print('EXACT_NORMAL_FORM_AND_INVERSE_IDENTITIES_PASS',checked)
    for part in [(2,),(1,1),(3,),(1,2),(1,1,1),(4,),(2,2)]:
        base,sing=finite_test(part,3)
        print('FINITE_FIELD_F3_EXHAUSTIVE',part,'base',base,'singular',sing)
    print('ALL_CANONICAL_PENCIL_TESTS_PASS')

if __name__=='__main__':
    main()
