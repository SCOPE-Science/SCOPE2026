#!/usr/bin/env python3
"""Exact finite-field checks for the arithmetic node strata of tetrahedral nodal quartics.
No external packages are needed. In particular, this script does not infer
geometric smoothness or infinite-field statements from a finite enumeration.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

EDGES = tuple(combinations(range(4), 2))

class Field:
    def __init__(self, m, reduction):
        self.m, self.q, self.poly = m, 1 << m, reduction
        self.mul_table = [[self._mul(a,b) for b in range(self.q)] for a in range(self.q)]
    def _mul(self, a, b):
        result = 0
        while b:
            if b & 1: result ^= a
            b >>= 1
            a <<= 1
            if a & self.q: a ^= self.poly
        return result
    def mul(self, a, b): return self.mul_table[a][b]
    def square(self, a): return self.mul(a,a)
    def inv(self, a):
        assert a != 0
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise AssertionError('not a field')
    def trace(self, a):
        u=a; z=0
        for _ in range(self.m):z^=u;u=self.square(u)
        assert z in (0,1)
        return z

def mask_profile(field, a, b):
    result=0
    for n,(i,j) in enumerate(EDGES):
        t=field.mul(field.mul(a[i],a[j]),field.inv(field.square(b[n])))
        if field.trace(t)==0:result|=1<<n
    return result

def direct_nodes(field,a,b):
    # Enumerate projective points once by fixing the first nonzero coordinate to 1.
    nodes=[]
    q=field.q
    for pivot in range(4):
        for tail in product(range(q),repeat=3-pivot):
            x=(0,)*pivot+(1,)+tail
            grad=tuple(field.mul(field.mul(x[(k+1)%4],x[(k+2)%4]),x[(k+3)%4]) for k in range(4))
            if any(grad):continue
            # Q(x) in characteristic two. F=product(x_i)+Q(x)^2.
            quad=0
            for i in range(4):quad ^= field.mul(a[i],field.square(x[i]))
            for n,(i,j) in enumerate(EDGES):quad ^= field.mul(b[n],field.mul(x[i],x[j]))
            f=field.mul(field.mul(x[0],x[1]),field.mul(x[2],x[3]))^field.square(quad)
            if f==0:nodes.append(x)
    return nodes

def check_small_fields():
    for m,poly in ((1,0b11),(2,0b111),(3,0b1011)):
        field=Field(m,poly)
        n0=sum(1 for t in range(1,field.q) if field.trace(t)==0)
        n1=sum(1 for t in range(1,field.q) if field.trace(t)==1)
        assert (n0,n1)==(field.q//2-1,field.q//2)
        # For all nonzero scalars, b -> a_i a_j/b^2 is a bijection.
        for c in range(1,field.q):
            images={field.mul(c,field.inv(field.square(b))) for b in range(1,field.q)}
            assert images==set(range(1,field.q))
        print(f'FIELD_CHECK q={field.q} nonzero_trace_classes={(n0,n1)}')

def exhaustive_F4():
    F=Field(2,0b111); values=tuple(range(1,F.q))
    histogram=Counter();representatives={}
    for coefficients in product(values,repeat=10):
        a=coefficients[:4];b=coefficients[4:]
        mask=mask_profile(F,a,b)
        histogram[mask]+=1
        representatives.setdefault(mask,(a,b))
    assert sum(histogram.values())==3**10
    assert len(histogram)==64
    for mask in range(64):
        s=mask.bit_count()
        assert histogram[mask]==(F.q-1)**4*(F.q//2-1)**s*(F.q//2)**(6-s)
        a,b=representatives[mask]
        nodes=direct_nodes(F,a,b)
        assert len(nodes)==2*s
        # Each rational node belongs to its predicted edge, exactly two per split edge.
        rational_edges=Counter(tuple(i for i in range(4) if p[i]) for p in nodes)
        for edge_num,edge in enumerate(EDGES):
            assert rational_edges[edge]==(2 if (mask>>edge_num)&1 else 0)
    print('EXHAUSTIVE_F4 all 59049 nonzero-coefficient quadrics, all 64 masks and direct singular-point counts OK')
    print('F4_BY_SPLIT_PAIR_COUNT', {s:sum(v for mask,v in histogram.items() if mask.bit_count()==s) for s in range(7)})

def check_F2_and_F8():
    F2=Field(1,0b11)
    assert len(direct_nodes(F2,(1,)*4,(1,)*6))==0
    assert mask_profile(F2,(1,)*4,(1,)*6)==0
    F8=Field(3,0b1011);vals=list(range(1,F8.q))
    # Construct profiles independently with diagonal coefficients all 1.
    by_split={0:[],1:[]}
    for b in vals:
        v=F8.trace(F8.inv(F8.square(b)))
        by_split[1-v].append(b)
    assert by_split[0] and by_split[1]
    for mask in range(64):
        b=tuple(by_split[(mask>>n)&1][0] for n in range(6))
        assert mask_profile(F8,(1,)*4,b)==mask
        assert len(direct_nodes(F8,(1,)*4,b))==2*mask.bit_count()
    print('F2_AND_F8 all 64 F8 profiles realized; direct F8 node counts OK')

if __name__=='__main__':
    check_small_fields()
    exhaustive_F4()
    check_F2_and_F8()
    print('VERIFY_OK')
