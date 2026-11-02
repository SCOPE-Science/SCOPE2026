#!/usr/bin/env python3
"""Standalone exact arithmetic checks for complex-structure joint-Lee constructions."""
from itertools import product

def jmap(v, p):
    out=[]
    for i in range(0,len(v),2):
        out.extend(((-v[i+1])%p,v[i]))
    return tuple(out)

def add(a,b,p): return tuple((x+y)%p for x,y in zip(a,b))
def neg(a,p): return tuple((-x)%p for x in a)
def mul(a,k,p): return tuple((k*x)%p for x in a)
def dot(a,b,p): return sum(x*y for x,y in zip(a,b))%p

def make(p,r):
    vectors=set(product(range(p),repeat=r)); vectors.remove((0,)*r)
    coords=[]
    while vectors:
        v=min(vectors); j=jmap(v,p)
        orbit={v,j,neg(v,p),neg(j,p)}
        assert len(orbit)==4 and orbit <= vectors
        vectors.difference_update(orbit)
        coords.append((v,j))
    return coords

def rank(rows,p):
    a=[list(row) for row in rows]; i=0
    for c in range(len(a[0])):
        piv=next((j for j in range(i,len(a)) if a[j][c]),None)
        if piv is None:continue
        a[i],a[piv]=a[piv],a[i]
        t=pow(a[i][c],-1,p)
        a[i]=[(x*t)%p for x in a[i]]
        for j in range(len(a)):
            if j!=i and a[j][c]:
                b=a[j][c]
                a[j]=[(x-b*y)%p for x,y in zip(a[j],a[i])]
        i+=1
        if i==len(a):break
    return i

def verify(p,r):
    coords=make(p,r)
    n=len(coords)
    assert 4*n==p**r-1
    # For each pair (v,Jv), row matrix is (H_X | H_Z)=(Jv | -v).
    hx=[[j[t] for v,j in coords] for t in range(r)]
    hz=[[(-v[t])%p for v,j in coords] for t in range(r)]
    H=[a+b for a,b in zip(hx,hz)]
    assert rank(H,p)==r
    for i in range(r):
        for j in range(r):
            comm=(sum(hx[i][k]*hz[j][k]-hz[i][k]*hx[j][k] for k in range(n)))%p
            assert comm==0,(p,r,i,j,comm)
    elementary={}
    for k,(v,j) in enumerate(coords):
        for kind,t in [('X',v),('Z',j)]:
            for sg in [1,-1]:
                syndrome=mul(t,sg,p)
                assert syndrome not in elementary
                elementary[syndrome]=(k,kind,sg)
    assert len(elementary)==p**r-1
    v,j=coords[0]
    target=add(v,j,p)
    assert target!=v and target!=j
    k,kind,sg=elementary[neg(target,p)]
    assert k!=0
    # The weight-three zero-syndrome witness acts in two physical qudits.
    minimum_support_bound=((p-1)*p**(r-1)+3)//4
    assert (p,r)==(3,2) or minimum_support_bound>2
    # Independently check that the weight-three witness cannot belong
    # to the row-span; test every stabilizer vector for the smaller cases.
    for coeff in product(range(p), repeat=r):
        if all(x==0 for x in coeff): continue
        active=sum(1 for z in range(n) if dot(coeff,[hx[t][z] for t in range(r)],p) or dot(coeff,[hz[t][z] for t in range(r)],p))
        assert active>=minimum_support_bound
        if (p,r)!=(3,2):assert active>2
    print(f'VERIFY_OK p={p} r={r} n={n} k={n-r} commutators={r*r} single_syndromes={p**r-1} stabilizers={p**r-1} witness=qudit_0_XZ_and_{k}_{kind}_{sg} support_lower_bound={minimum_support_bound}')

for pair in [(3,2),(3,4),(3,6),(7,2),(11,2),(19,2)]:
    verify(*pair)
print('COMPLEX_STRUCTURE_LEE_VERIFY_OK')
