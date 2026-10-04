#!/usr/bin/env python3
"""Exact stdlib verifier for the eight local Cayley hyperdeterminants."""
from itertools import product

BITS = [''.join(map(str,b)) for b in product((0,1), repeat=4)]
VARS = [b for b in BITS if b != '0000']
POS = {b:i for i,b in enumerate(VARS)}
N = len(VARS)
ZERO = (0,)*N

def add(p,q):
    r = dict(p)
    for m,c in q.items():
        r[m] = r.get(m,0)+c
        if r[m] == 0: del r[m]
    return r

def scale(p,c):
    return {m:c*a for m,a in p.items() if c*a}

def mul(p,q):
    r = {}
    for m,a in p.items():
        for n,b in q.items():
            k = tuple(x+y for x,y in zip(m,n))
            r[k] = r.get(k,0)+a*b
    return {m:c for m,c in r.items() if c}

def powp(p,n):
    r={ZERO:1}
    for _ in range(n): r=mul(r,p)
    return r

def y(b):
    m=[0]*N; m[POS[b]]=1
    return {tuple(m):1}

def x(b):
    if b=='0000': return {ZERO:1}
    if b=='1111': return add({ZERO:1}, y(b))
    return y(b)

def cayley(a):
    # a maps 000,...,111 to sparse polynomials.
    terms=[]
    def P(*fs):
        r={ZERO:1}
        for f in fs: r=mul(r,f)
        return r
    terms.append(P(powp(a['000'],2),powp(a['111'],2)))
    terms.append(P(powp(a['001'],2),powp(a['110'],2)))
    terms.append(P(powp(a['010'],2),powp(a['101'],2)))
    terms.append(P(powp(a['011'],2),powp(a['100'],2)))
    terms.append(scale(P(a['000'],a['011'],a['101'],a['110']),4))
    terms.append(scale(P(a['001'],a['010'],a['100'],a['111']),4))
    terms.append(scale(P(a['000'],a['001'],a['110'],a['111']),-2))
    terms.append(scale(P(a['000'],a['010'],a['101'],a['111']),-2))
    terms.append(scale(P(a['000'],a['011'],a['100'],a['111']),-2))
    terms.append(scale(P(a['001'],a['010'],a['101'],a['110']),-2))
    terms.append(scale(P(a['001'],a['011'],a['100'],a['110']),-2))
    terms.append(scale(P(a['010'],a['011'],a['100'],a['101']),-2))
    r={}
    for t in terms: r=add(r,t)
    return r

def degree(m): return sum(m)

def monomial_square(b):
    m=[0]*N; m[POS[b]]=2
    return {tuple(m):1}

expected = {
 (0,0):'0111', (0,1):'1000',
 (1,0):'1011', (1,1):'0100',
 (2,0):'1101', (2,1):'0010',
 (3,0):'1110', (3,1):'0001',
}
seen=[]
for mode in range(4):
    remaining=[i for i in range(4) if i!=mode]
    for eps in (0,1):
        a={}
        for tri in product((0,1),repeat=3):
            full=['0']*4; full[mode]=str(eps)
            for j,idx in enumerate(remaining): full[idx]=str(tri[j])
            a[''.join(map(str,tri))]=x(''.join(full))
        f=cayley(a)
        mind=min(degree(m) for m in f)
        q={m:c for m,c in f.items() if degree(m)==2}
        b=expected[(mode,eps)]
        assert mind==2, (mode,eps,mind)
        assert q==monomial_square(b), (mode,eps,q,b)
        seen.append(b)
        print(f"mode={mode} fixed={eps}: initial=y_{b}^2")
assert len(set(seen))==8
assert set(seen)=={b for b in VARS if b.count('1') in (1,3)}
# Eight independent square initial forms are a regular sequence in a 15-variable polynomial ring.
codim=8
dim=N-codim
multiplicity=2**8
assert N==15 and dim==7 and multiplicity==256
print("initial_forms_regular_sequence=YES")
print("tangent_cone_hilbert_series=(1+t)^8/(1-t)^7")
print("local_dimension=7")
print("multiplicity=256")
print("VERIFY_OK")
