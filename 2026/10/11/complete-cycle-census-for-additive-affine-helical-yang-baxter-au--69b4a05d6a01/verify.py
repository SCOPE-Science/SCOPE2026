"""Exact finite checks for affine binary helical dynamics.
Run: python3 verify.py. This program uses only the Python standard library.
Universal conclusions rely on the analytical argument in RESULT.md, not finite tests.
"""
from itertools import product
from math import prod

def linear(cols,x):
    y=0
    for i,col in enumerate(cols):
        if x>>i & 1:y^=col
    return y

def rank(cols,m):
    basis=[0]*m;r=0
    for col in cols:
        v=col
        while v:
            i=v.bit_length()-1
            if basis[i]:v^=basis[i]
            else:
                basis[i]=v;r+=1;break
    return r

def YBfunctional(f,q):
    for x in range(q):
        for y in range(q):
            if f[x]^f[x^f[y]]!=f[x^f[y^f[x]]]:return False
    return True

def update(state,f):
    *xx,carrier=state
    out=[]
    for x in xx:
        a=f[x^carrier]
        out.append(carrier^a)
        carrier=x^a
    return tuple(out+[carrier])

def gaussian(n,r):
    num=prod(2**(n-j)-1 for j in range(r))
    den=prod(2**(r-j)-1 for j in range(r))
    return num//den

def gl(r):return prod(2**r-2**j for j in range(r))

checks=0
for m in (2,3):
    q=2**m
    admissible=[]
    for A in product(range(q),repeat=m):
        if rank(A,m)!=m:continue
        D=tuple(A[i]^(1<<i) for i in range(m))
        squarezero=all(linear(D,linear(D,x))==0 for x in range(q))
        r=rank(D,m)
        for c in range(q):
            f=[linear(A,x)^c for x in range(q)]
            valid=YBfunctional(f,q)
            assert valid==squarezero,(m,A,c)
            checks+=1
            if valid:admissible.append((A,D,c,r,f))
    predicted=q*sum(gaussian(m,r)*gaussian(m-r,r)*gl(r) for r in range(m//2+1))
    assert len(admissible)==predicted,(m,len(admissible),predicted)
    checks+=1
    for A,D,c,r,f in admissible:
        v=linear(D,c)
        im={linear(D,x) for x in range(q)}
        for N in (1,2,3) if m==3 else (1,2,3,4):
            expect_fix= q*(q//(2**r))**N if c in im else 0
            fixed=0
            four=0
            for s in product(range(q),repeat=N+1):
                s1=update(s,f)
                s2=update(s1,f)
                expected=tuple(x^(v if N%2==0 else 0) for x in s[:-1])+(s[-1],)
                assert s2==expected,(m,A,c,N,s,s2,expected)
                checks+=1
                if s1==s:fixed+=1
                if s2!=s:four+=1
            assert fixed==expect_fix,(m,A,c,N,fixed,expect_fix)
            assert four==(q**(N+1) if N%2==0 and v else 0)
            checks+=2
    print('dimension',m,'admissible_affine_maps',len(admissible),'exact_assertions_so_far',checks)
# Independent square-zero rank census in dimension four (all 65,536 operators).
m=4;q=2**m
hist={}
for D in product(range(q),repeat=m):
    if all(linear(D,linear(D,x))==0 for x in range(q)):
        r=rank(D,m)
        hist[r]=hist.get(r,0)+1
        checks+=1
expected={r:gaussian(m,r)*gaussian(m-r,r)*gl(r) for r in range(m//2+1)}
assert hist==expected,(hist,expected)
assert hist=={0:1,1:105,2:210}
assert sum(hist.values())*q==5056
assert sum(count*(q-q//(2**r)) for r,count in hist.items())==3360
checks+=4
print('dimension 4 rank census',hist,'affine_rules',5056,'four_cycle_only_rules_for_even_length',3360)
print('VERIFY_OK',checks)
