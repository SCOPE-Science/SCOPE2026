#!/usr/bin/env python3
"""Finite consistency tests for modal Abelian star hierarchy.
This code checks sample valuations, not the all-real quantified theorem.
No third-party packages required.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

# Star: root is 0; leaves have indices 1..r. Box at a leaf has value zero.
def value(term, xvalues, world=0):
    tag = term[0]
    if tag == 'x': return xvalues[world]
    if tag == 'c': return F(-1)
    if tag == 'zero': return F(0)
    if tag == 'add': return value(term[1],xvalues,world)+value(term[2],xvalues,world)
    if tag == 'neg': return -value(term[1],xvalues,world)
    if tag == 'max': return max(value(term[1],xvalues,world),value(term[2],xvalues,world))
    if tag == 'min': return min(value(term[1],xvalues,world),value(term[2],xvalues,world))
    if tag == 'box':
        return min(value(term[1],xvalues,j) for j in range(1,len(xvalues))) if world == 0 else F(0)
    raise AssertionError(tag)

def add(a,b): return ('add',a,b)
def neg(a):return ('neg',a)
def max2(a,b):return ('max',a,b)
def absolute(a):return max2(a,neg(a))
X=('x',); C=('c',)
def mult(n,t):
    ans=('zero',)
    for _ in range(n):ans=add(ans,t)
    return ans

def sep(m):
    # max_{0 <= i <= m} Box (abs(2m*x - 2i) - 1).
    parts=[('box',add(absolute(add(mult(2*m,X),mult(2*i,C))),C)) for i in range(m+1)]
    ans=parts[0]
    for v in parts[1:]:ans=max2(ans,v)
    return ans

def occurrence_count(t):
    if t[0] in ('x','c','zero'):return 0
    if t[0] == 'box':return 1+occurrence_count(t[1])
    if t[0]=='neg':return occurrence_count(t[1])
    return occurrence_count(t[1])+occurrence_count(t[2])

def root_witness_indices(t,xvalues):
    # Every modal occurrence evaluated at root needs one minimizer.
    def rec(u):
        tag=u[0]
        if tag=='box':
            return [min(range(1,len(xvalues)),key=lambda j:value(u[1],xvalues,j))]
        if tag in ('x','c','zero'):return []
        if tag=='neg':return rec(u[1])
        return rec(u[1])+rec(u[2])
    return root_witness_indices_rec(t,xvalues)

def root_witness_indices_rec(t,xvalues):
    if t[0]=='box':return [min(range(1,len(xvalues)),key=lambda j:value(t[1],xvalues,j))]
    if t[0] in ('x','c','zero'):return []
    if t[0]=='neg':return root_witness_indices_rec(t[1],xvalues)
    return root_witness_indices_rec(t[1],xvalues)+root_witness_indices_rec(t[2],xvalues)

rng=Random(428167)
checks=0
for m in range(1,7):
    phi=sep(m)
    assert occurrence_count(phi)==m+1
    bad=[F(0)]+[F(j,m) for j in range(m+1)]
    assert value(phi,bad,0)==F(-1), (m,value(phi,bad,0))
    assert all(value(phi,bad,j)==0 for j in range(1,len(bad)))
    checks+=len(bad)
    grid=[F(j,2) for j in range(-5,4*m+6)]
    samples=list(product(grid,repeat=m)) if m<=2 else [tuple(rng.choice(grid) for _ in range(m)) for _ in range(5000)]
    for tup in samples:
        w=[F(0)]+list(tup)
        assert value(phi,w,0)>=0, ('failure',m,tup,value(phi,w,0))
        checks+=1

# The bounded-occurrence witness lemma also holds for nested Box nodes.
def random_term(depth):
    if depth==0 or rng.random()<.18:return rng.choice([X,C,('zero',)])
    choice=rng.choice(['add','max','min','neg','box'])
    if choice in ('box','neg'):return (choice,random_term(depth-1))
    return (choice,random_term(depth-1),random_term(depth-1))

for num_leaves in range(1,7):
    for trial in range(3000):
        t=random_term(5)
        boxes=occurrence_count(t)
        if boxes==0 or boxes>=num_leaves:continue
        x=[F(rng.randrange(-30,31),3) for _ in range(num_leaves+1)]
        indices=list(dict.fromkeys(root_witness_indices_rec(t,x)))
        if not indices:indices=[1]
        assert len(indices)<=boxes
        padded=indices+next((j for j in range(1,num_leaves+1) if j not in indices),indices[0])*0 if False else indices
        y=[x[0]]+[x[j] for j in indices]
        assert value(t,x,0)==value(t,y,0),(t,boxes,x,y)
        checks+=1
print('PASS',checks,'finite sample/assertion groups')
