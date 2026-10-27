#!/usr/bin/env python3
"""Exact SU(3) character-ring / Haar-moment checks for the (3, 3bar, 8) packet.

Requires only the Python standard library. Polynomial dictionaries use exponent tuples.
The analytic optimization and phase equality conditions are proved in RESULT.md.
"""
from itertools import product
from collections import defaultdict


def ladd(a,b):
    r=a.copy()
    for k,v in b.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}


def lmul(a,b):
    r=defaultdict(int)
    for (i,j),v in a.items():
        for (k,l),w in b.items(): r[i+k,j+l]+=v*w
    return {k:v for k,v in r.items() if v}


def lstar(a): return {(-i,-j):v for (i,j),v in a.items()}


def schur(p,q):
    """SU(3) character as a Laurent polynomial by semistandard tableaux."""
    rows=[p+q,q]
    cells=[(r,c) for r in range(2) for c in range(rows[r])]
    out=defaultdict(int)
    for word in product(range(1,4),repeat=len(cells)):
        tab=dict(zip(cells,word))
        if any(tab[r,c]>tab[r,c+1] for r,c in cells if (r,c+1) in tab): continue
        if any(tab[r,c]>=tab[r+1,c] for r,c in cells if (r+1,c) in tab): continue
        u,v,w=(word.count(i) for i in (1,2,3))
        out[u-w,v-w]+=1
    return dict(out)


I={(0,0):1}
weights=[(1,0),(0,1),(-1,-1)]
weyl=I
for i in range(3):
    for j in range(3):
        if i==j: continue
        di,dj=(weights[i][k]-weights[j][k] for k in range(2))
        weyl=lmul(weyl,{(0,0):1,(di,dj):-1})
assert weyl.get((0,0))==6


def haar(a):
    numerator=lmul(a,weyl).get((0,0),0)
    assert numerator%6==0
    return numerator//6

reps={r:schur(*r) for r in [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),
                            (3,0),(0,3),(2,1),(1,2),(2,2)]}
products=[
    ((1,0),(1,0),[(2,0),(0,1)]),
    ((0,1),(0,1),[(0,2),(1,0)]),
    ((1,0),(0,1),[(0,0),(1,1)]),
    ((1,0),(1,1),[(1,0),(0,2),(2,1)]),
    ((0,1),(1,1),[(0,1),(2,0),(1,2)]),
    ((1,1),(1,1),[(0,0),(1,1),(1,1),(3,0),(0,3),(2,2)]),
]
for r,s,members in products:
    rhs={}
    for u in members: rhs=ladd(rhs,reps[u])
    assert lmul(reps[r],reps[s])==rhs,(r,s)
print('Six tensor product identities verified exactly by independent tableau enumeration.')

chars=[reps[(1,0)],reps[(0,1)],reps[(1,1)]]
assert all(haar(lmul(chars[i],lstar(chars[j])))==int(i==j)
           for i in range(3) for j in range(3))


def varpair(idx,conjugate=False):
    e=[0]*6
    for j in idx:e[j+(3 if conjugate else 0)]+=1
    return tuple(e)

# Expand all 81 fourth-moment contributions via Weyl's exact constant term.
lhs=defaultdict(int)
for i,j,k,l in product(range(3),repeat=4):
    x=lmul(lmul(chars[i],chars[j]),lmul(lstar(chars[k]),lstar(chars[l])))
    e=[0]*6
    for m in [i,j]:e[m]+=1
    for m in [k,l]:e[3+m]+=1
    lhs[tuple(e)]+=haar(x)
lhs={k:v for k,v in lhs.items() if v}

# Independently expand the asserted character product-sum formula.
terms=[
    (1,{(2,2):1,(0,1):2}),
    (1,{(2,2):2,(0,1):2}),
    (2,{(0,0):1,(1,2):2}),
    (2,{(1,1):1,(0,2):2}),
    (3,{(2,2):1}),
    (4,{(0,2):1}),
    (4,{(1,2):1}),
]
rhs=defaultdict(int)
for weight,terms2 in terms:
    for p,v in terms2.items():
        for q,w in terms2.items():
            e=tuple(x+y for x,y in zip(varpair(p),varpair(q,True)))
            rhs[e]+=weight*v*w
rhs={k:v for k,v in rhs.items() if v}
assert lhs==rhs,('coefficient mismatch',set(lhs.items())^set(rhs.items()))
print('Exact six-variable fourth-moment polynomial:',len(lhs),'nonzero coefficients verified.')

# Check the one-variable derivative identity without symbolic dependencies.
N=[12,16,36,0,8] # 12+16r+36r^2+8r^4
D=[2,0,1]

def mul1(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o

def sub1(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n)]

def deriv(a):return [i*a[i] for i in range(1,len(a))]
left=sub1(mul1(deriv(N),D),mul1([0,4],N))
assert left[:5]==[32,96,-48,-8,0] and all(x==0 for x in left[5:])
# This is -8*(r^3+6*r^2-12*r-4).
def g(r):return r**3+6*r*r-12*r-4
lo,hi=1.0,3.0
for _ in range(80):
    mid=(lo+hi)/2
    if g(mid)>0:hi=mid
    else:lo=mid
r=(lo+hi)/2
K=(8*r**4+36*r*r+16*r+12)/(r*r+2)**2
assert 1.8168<r<1.8169 and 8.7926<K<8.7927
print('Unique positive optimizer root (Descartes + derivative):',format(r,'.15f'))
print('Fourth-power sharp constant:',format(K,'.15f'))
print('All exact algebraic checks passed; root decimals are auxiliary.')
