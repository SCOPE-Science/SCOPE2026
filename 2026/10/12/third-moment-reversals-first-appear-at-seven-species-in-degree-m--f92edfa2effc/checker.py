"""Exact self-contained checks for a three-plant coextinction-moment comparison.
Standard-library-only; run `python checker.py`.
"""
from itertools import combinations
from collections import defaultdict
from fractions import Fraction
from math import comb

def connected(rows,n):
    m=len(rows)
    adj=[set() for _ in range(m+n)]
    for i,row in enumerate(rows):
        for j in range(n):
            if row>>j&1:
                adj[i].add(m+j)
                adj[m+j].add(i)
    seen={0}
    while True:
        nxt=seen | set().union(*(adj[v] for v in seen))
        if nxt==seen:return len(seen)==m+n
        seen=nxt

def hist(rows,n,k):
    a=[0]*(len(rows)+1)
    for deleted in combinations(range(n),k):
        mask=sum(1<<j for j in deleted)
        a[sum((row & mask)==row for row in rows)]+=1
    assert sum(a)==comb(n,k)
    return tuple(a)

def lawprofile(rows,n):return tuple(hist(rows,n,k) for k in range(n+1))

def moment_distribution(rows,n,q):
    m=len(rows)
    p=[Fraction(0) for _ in range(m+1)]
    for mask in range(1<<n):
        extinct=mask.bit_count()
        count=sum((r&mask)==r for r in rows)
        p[count]+=q**extinct*(1-q)**(n-extinct)
    return p

def moments(p):
    mean=sum(i*z for i,z in enumerate(p))
    v=sum((i-mean)**2*z for i,z in enumerate(p))
    mu3=sum((i-mean)**3*z for i,z in enumerate(p))
    return mean,v,mu3

total=0;groups=0
for m in range(1,6):
    for n in range(1,6):
        if m+n>6:continue
        seen={}
        for packed in range(1<<(m*n)):
            rows=tuple((packed>>(i*n))&((1<<n)-1) for i in range(m))
            if 0 in rows or not connected(rows,n):continue
            total+=1
            rd=tuple(sorted(row.bit_count() for row in rows))
            cd=tuple(sorted(sum((row>>j)&1 for row in rows) for j in range(n)))
            signature=(rd,cd)
            profile=lawprofile(rows,n)
            if signature in seen:
                assert seen[signature]==profile,(m,n,signature,rows)
            else:seen[signature]=profile
        groups+=len(seen)
assert total==387,(total,groups)
assert groups==44,(total,groups)

# Connected seven-species tree pairs with the same two guild degree sequences.
# Column masks: bit 0/1/2 indicates adjacency to each of three plants.
Gcols=(1,1,3,6)
Hcols=(1,2,3,5)
def rows_from_cols(cols):
    return tuple(sum(1<<j for j,c in enumerate(cols) if c>>i&1) for i in range(3))
G,H=rows_from_cols(Gcols),rows_from_cols(Hcols)
assert G==(7,12,8),G
assert H==(13,6,8),H
assert connected(G,4) and connected(H,4)
assert tuple(sorted(r.bit_count() for r in G))==tuple(sorted(r.bit_count() for r in H))==(1,2,3)
assert tuple(sorted(c.bit_count() for c in Gcols))==tuple(sorted(c.bit_count() for c in Hcols))==(1,1,2,2)
assert lawprofile(G,4)!=lawprofile(H,4)

# Polynomial arithmetic over the rationals: low-order coefficient first.
def add(a,b):
    m=max(len(a),len(b))
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(m))
def neg(a):return tuple(-z for z in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)
def power(a,j):
    out=(1,)
    for _ in range(j):out=mul(out,a)
    return out
def normalize(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return tuple(a)

def probpoly(rows,n):
    m=len(rows)
    ans=[(0,) for _ in range(m+1)]
    for mask in range(1<<n):
        k=mask.bit_count()
        count=sum((r&mask)==r for r in rows)
        ans[count]=add(ans[count],mul(power((0,1),k),power((1,-1),n-k)))
    return tuple(normalize(x) for x in ans)

def mompolys(polys):
    # Raw moments built directly from complete probability-generating polynomials.
    out=[]
    for r in (1,2,3):
        t=(0,)
        for j,p in enumerate(polys):t=add(t,tuple(j**r*x for x in p))
        out.append(t)
    mu,r2,r3=out
    variance=sub(r2,mul(mu,mu))
    third=add(sub(r3,mul((3,),mul(mu,r2))),mul((2,),power(mu,3)))
    return tuple(map(normalize,(mu,variance,third)))
pG,pH=probpoly(G,4),probpoly(H,4)
mG,vG,cG=mompolys(pG)
mH,vH,cH=mompolys(pH)
assert mG==mH==(0,1,1,1)
assert normalize(sub(vG,vH))==(0,0,2,-4,2)
assert normalize(sub(cG,cH))==normalize(mul((6,),mul((0,0,1,-2,1),(1,-1,-1,-1))))
for q in (Fraction(1,4),Fraction(1,2),Fraction(3,5),Fraction(3,4)):
    a,b=moments(moment_distribution(G,4,q)),moments(moment_distribution(H,4,q))
    assert a[0]==b[0]==q+q*q+q**3
    assert a[1]-b[1]==2*q*q*(1-q)**2
    assert a[2]-b[2]==6*q*q*(1-q)**2*(1-q-q*q-q**3)
assert Fraction(1,2)+Fraction(1,2)**2+Fraction(1,2)**3<1
assert Fraction(3,5)+Fraction(3,5)**2+Fraction(3,5)**3>1
print(f'VERIFY_OK labeled_connected_small={total} matched_degree_profiles={groups} seven_species_trees=2 moment_polynomial_identities=3 exact_probability_tests=4')
