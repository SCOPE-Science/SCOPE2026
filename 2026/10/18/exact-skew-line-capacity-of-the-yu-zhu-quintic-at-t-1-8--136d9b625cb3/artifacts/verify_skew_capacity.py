#!/usr/bin/env python3
"""Exact arithmetic certificate for the maximum mutually skew subset of Yu--Zhu's 85 lines.
Only the line formulae in arXiv:2609.26862v1 section 3.2 are input; no precomputed incidence table.
K=Q(i,a,b), i^2=-1, a^4=2, b^4=3. Coefficient basis i^e*a^j*b^k.
The 85x85 incidence matrix is calculated by symbolic 4x4 determinants.
The recursive coloring bound certifies nonexistence of a 19-vertex independent set.
"""
from itertools import product

class K:
    __slots__=('d',)
    def __init__(self, d=0):
        if isinstance(d,K): self.d=dict(d.d)
        elif isinstance(d,int): self.d={0:d} if d else {}
        elif isinstance(d,dict): self.d={k:int(v) for k,v in d.items() if v}
        else: raise TypeError(type(d))
    def __add__(self,o):
        o=K(o); c=dict(self.d)
        for k,v in o.d.items():
            c[k]=c.get(k,0)+v
            if not c[k]:del c[k]
        return K(c)
    __radd__=__add__
    def __neg__(self): return K({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+-K(o)
    def __rsub__(self,o):return K(o)+-self
    def __mul__(self,o):
        o=K(o);c={}
        for k,v in self.d.items():
            i,a,b=k//16,(k//4)%4,k%4
            for k1,v1 in o.d.items():
                i1,a1,b1=k1//16,(k1//4)%4,k1%4
                ii=i+i1;aa=a+a1;bb=b+b1
                idx=(ii%2)*16+(aa%4)*4+(bb%4)
                val=v*v1*(-1 if ii>1 else 1)*(2 if aa>=4 else 1)*(3 if bb>=4 else 1)
                c[idx]=c.get(idx,0)+val
        return K(c)
    __rmul__=__mul__
    def __pow__(self,p):
        if p<0:raise ValueError('negative powers not needed')
        res=K(1);x=self
        while p:
            if p&1:res=res*x
            x=x*x;p>>=1
        return res
    def __bool__(self):return bool(self.d)
    def __eq__(self,o):return self.d==K(o).d
    def __repr__(self):return repr(self.d)

I=K({16:1});A=K({4:1});B=K({1:1})
s3=B*B;r12=A*A*B;r6=A*B;r18=A*B*B
zero=K(0); one=K(1)

def mk(*args):return [K(a) for a in args]
lines={1:[mk(0,0,1,0),mk(0,0,0,1)]}
def put(k,u,v):
    assert k not in lines,k
    lines[k]=[u,v]
for j1,j2,j3 in product(range(2),repeat=3):
    k=2+4*j1+2*j2+j3
    w=mk(0,0,0,0);w[3-j1]=one
    put(k,mk(s3-(-1)**(j1+j2),-(-1)**(j1+j3)*I**j2*r12,0,0),w)
for j1,j2 in product(range(2),repeat=2):
    k=10+2*j2+j1
    put(k,mk(1,-(-1)**j1*I*(I*s3)**j2,0,0),mk(0,0,1,2))
for j1,j3 in product(range(2),repeat=2):
    k=14+2*j1+j3
    put(k,mk(r12+(-1)**j3*(1-I),-(-1)**j1*((-1)**j3*r12-(1+I)*s3),0,0),mk(0,0,-(1-I*s3),4))
    k=18+2*j1+j3
    put(k,mk(r12-(-1)**(j1+j3)*(1+I),(-1)**j3*r12+(-1)**j1*(1-I)*s3,0,0),mk(0,0,-(1+I*s3),4))
for j1,j2,j3 in product(range(2),repeat=3):
    for k0 in range(4):
        k=22+16*j1+40*j2+4*j3+k0
        c=I**(k0+(1-j2)*(1-j3))*(I-1)
        e=(-1)**j2*r12+(-1)**j3*I**(1-j2)*(s3-(-1)**j2)
        put(k,mk(2*r18*(-1)**j1,-2*r18*(-1)**(j2+j3)*I,-c,-2*c),
              mk(4*(-1)**j1*(s3+(-1)**j2),4*I**j2*r12,-c*r6*e,0))
        k=30+16*j1+24*j2+4*j3+k0
        c=I**(k0+j2*(1-j3))*r6
        put(k,mk(2*(-1)**(j1+j3)*s3,6*(-1)**j2,-c,-2*c),
              mk((-1)**j1*((-I)**j2*r12+(-1)**j3*(1+(-1)**j2*s3)),
                 (-1)**j3*(-I)**j2*r12+3-(-1)**j2*s3,
                 -I**(k0+j2*(3-j3))*r6,0))
assert sorted(lines)==list(range(1,86))
# 2x2 row minors of planes; wedge identifies intersection of two projective lines.
pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def minors(L):
    u,v=L;return tuple(u[a]*v[b]-u[b]*v[a] for a,b in pairs)
W=[minors(lines[k]) for k in range(1,86)]
def meet(p,q):
    return not (p[0]*q[5]-p[1]*q[4]+p[2]*q[3]+p[3]*q[2]-p[4]*q[1]+p[5]*q[0])
meet_mask=[0]*85
for j in range(85):
 for k in range(j+1,85):
    if meet(W[j],W[k]):
        meet_mask[j] |= 1<<k
        meet_mask[k] |= 1<<j
assert all(m.bit_count()==20 for m in meet_mask),[m.bit_count() for m in meet_mask]
assert sum(m.bit_count() for m in meet_mask)==1700
# Cross-check the published edge/common-neighbor census of the same graph.
common_3=common_0=0
for a in range(85):
    for b in range(a+1,85):
        if (meet_mask[a]>>b)&1:
            common=(meet_mask[a]&meet_mask[b]).bit_count()
            assert common in (0,3)
            if common==3:common_3+=1
            else:common_0+=1
assert (common_3,common_0)==(530,320)
# An explicit 18-vertex independent set, in 1-based Yu--Zhu labels.
witness=[2,6,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]
assert len(witness)==len(set(witness))==18
assert all(not ((meet_mask[a-1]>>(b-1))&1) for i,a in enumerate(witness) for b in witness[i+1:])
# Finite structural certificate: 19 cliques of meeting lines cover all 85 lines.
# If 19 mutually skew lines existed, exactly one vertex from each clique would
# be selected, and no selected vertex could occur in two covering cliques.
cover19=[
 [1,2,3,4,5], [1,6,7,8,9], [18,22,50,64,75],
 [14,23,48,59,85], [18,24,52,62,77], [10,25,44,66,80],
 [19,26,49,67,73], [15,27,51,57,80], [19,28,47,69,71],
 [11,29,38,65,83], [20,30,43,54,84], [16,31,38,68,74],
 [20,32,45,56,82], [12,33,53,59,70], [17,34,42,63,72],
 [13,34,46,55,76], [21,35,39,60,81], [21,36,40,61,78],
 [21,37,41,58,79]]
assert {x for C in cover19 for x in C}==set(range(1,86))
assert all(len(C)==5 and all((meet_mask[a-1]>>(b-1))&1 for i,a in enumerate(C)
                             for b in C[i+1:]) for C in cover19)
from collections import Counter
freq=Counter(x for C in cover19 for x in C)
# These eight of the nineteen cliques have no mutually skew transversal
# after removing vertices that occur in another covering clique.
selected=[3,7,9,11,13,14,15,17]  # zero-based indices
blocks=[[x for x in cover19[j] if freq[x]==1] for j in selected]
assert blocks==[[14,23,48,85],[15,27,51,57],[11,29,65,83],
                [16,31,68,74],[12,33,53,70],[17,42,63,72],
                [13,46,55,76],[36,40,61,78]]
for choice in product(*blocks):
    assert any((meet_mask[a-1]>>(b-1))&1 for ix,a in enumerate(choice)
               for b in choice[ix+1:]),choice
# Therefore no 19 pairwise-skew lines exist. The general exhaustive search
# below is a second independent combinatorial bound, beyond the 8-block test.
# Recursive exhaustive clique bound in complementary (skew) graph.
full=(1<<85)-1
skew=[full&~(meet_mask[j]|(1<<j)) for j in range(85)]
calls=0

def greedy_coloring(mask):
    """Proper greedy coloring of induced skew graph; equal colors are mutually nonadjacent.
    Every clique in the prefix of returned order has size <= last corresponding color.
    """
    order=[]; color_bound=[];remaining=mask;color=0
    while remaining:
        color+=1
        avail=remaining
        while avail:
            bit=avail&-avail
            v=bit.bit_length()-1
            order.append(v);color_bound.append(color)
            remaining &= ~bit
            avail &= ~(bit|skew[v])
    return order,color_bound

def exists_skew_19(mask,depth=0):
    """Search ALL skew cliques of size 19: include each pivot, then exclude.
    Prune a branch only if a proper coloring proves fewer than 19-depth candidates.
    """
    global calls
    calls+=1
    if depth==19: return True
    if depth+mask.bit_count()<19:return False
    order,bounds=greedy_coloring(mask)
    for ix in range(len(order)-1,-1,-1):
        if depth+bounds[ix]<19:return False
        v=order[ix];bit=1<<v
        if exists_skew_19(mask&skew[v],depth+1):return True
        mask &= ~bit
    return False
assert not exists_skew_19(full)
print('YU_ZHU_85_SKEW_MAXIMUM_EXACT_OK')
print('intersection edges:',sum(m.bit_count() for m in meet_mask)//2,'degree:',meet_mask[0].bit_count())
print('maximal skew size:',len(witness),'witness:',witness,'8-block test:',4**8,'exhaustive nodes:',calls)
