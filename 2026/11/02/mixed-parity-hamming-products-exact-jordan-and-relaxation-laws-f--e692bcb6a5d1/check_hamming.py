#!/usr/bin/env python3
"""Separate GF(2) matrix and finite-state checks for mixed-coordinate Hamming parity dynamics."""
import itertools, math, collections

def mul(M,N):
    nr=len(M); nc=len(N[0]); out=[[0]*nc for _ in range(nr)]
    for i in range(nr):
        for k,c in enumerate(M[i]):
            if c:
                for j,v in enumerate(N[k]): out[i][j]^=v
    return out

def rank(M):
    rows=[]
    for row in M:
        bits=sum((b&1)<<i for i,b in enumerate(row))
        for x in rows: bits=min(bits,bits^x)
        if bits:
            rows.append(bits)
            rows.sort(reverse=True)
    return len(rows)

def form(dims):
    verts=list(itertools.product(*(range(x) for x in dims)))
    return [[int(sum(x!=y for x,y in zip(u,v))==1) for v in verts] for u in verts]

def pred(dims):
    odds=[a for a in dims if a&1]; evens=[a for a in dims if not a&1]
    O=math.prod(odds); E=math.prod(evens); delta=math.prod(a-2 for a in odds); H=math.prod(a-2 for a in evens)
    P=((O+delta)//2,(O-delta)//2); b=(E-H)//2
    e=len(dims)%2
    z=P[e]*E; w=P[1-e]*E
    B0=P[e]*b;B1=P[1-e]*b
    S0=P[e]*H;S1=P[1-e]*H
    return z,w,B0,B1,S0,S1

def analyze(dims):
    A=form(dims); n=len(A); I=[[int(i==j) for j in range(n)] for i in range(n)];
    A2=mul(A,A);Ap=[[A[i][j]^I[i][j] for j in range(n)]for i in range(n)]; Ap2=mul(Ap,Ap)
    z,w,b0,b1,s0,s1=pred(dims)
    # Generalized eigenvalues 0 and 1 are separated by A^2 and (A+I)^2.
    # A^2 is identity on generalized lambda 1 and zero on lambda 0.
    assert rank(A2)==w,(dims,'rankA2',rank(A2),w)
    assert rank(Ap2)==z,(dims,'rankAp2',rank(Ap2),z)
    assert rank(A)==w+b0,(dims,'rankA',rank(A),w+b0)
    assert rank(Ap)==z+b1,(dims,'rankAp',rank(Ap),z+b1)
    assert s0+2*b0==z and s1+2*b1==w and z+w==n
    A3=mul(A2,A);A4=mul(A2,A2)
    assert A4==A2,(dims,'A4 != A2')

def state_checks(dims,q):
    n=math.prod(dims); A=form(dims)
    z,w,b0,b1,s0,s1=pred(dims)
    want_entry=[q**w,q**w*(q**(s0+b0)-1),q**w*(q**z-q**(s0+b0))]
    want_fixed=q**(w-b1)
    actual_entry=[0,0,0];fixed=0
    # Each GF(2^f) addition is bitwise xor in a polynomial basis, even if multiplication unused.
    def apply(v):
        return tuple(__import__('functools').reduce(int.__xor__,(v[j] for j in range(n) if A[i][j]),0) for i in range(n))
    for x in itertools.product(range(q),repeat=n):
        a=apply(x);b=apply(a);c=apply(b);d=apply(c)
        t=(0 if x==b and a==c else (1 if a==c else 2))
        assert b==d or c==d,(dims,q,x,'not eventually periodic by 2?')
        actual_entry[t]+=1
        if x==a:fixed+=1
    assert actual_entry==want_entry,(dims,q,actual_entry,want_entry)
    assert fixed==want_fixed,(dims,q,fixed,want_fixed)

counter=0
for d in range(1,5):
    for dims in itertools.product(range(2,7),repeat=d):
        if math.prod(dims)>140:continue
        analyze(dims);counter+=1
print('RANK_JORDAN_CASES_PASSED',counter)
finite=0; states=0
for d in range(1,4):
    for dims in itertools.product(range(2,6),repeat=d):
        n=math.prod(dims)
        if n>10:continue
        state_checks(dims,2);finite+=1;states+=2**n
for dims in [(2,2),(2,3),(2,4),(3,3)]:
    state_checks(dims,4);finite+=1;states+=4**math.prod(dims)
print('EXHAUSTIVE_FINITE_STATE_CASES_PASSED',finite,'TOTAL_CONFIGURATIONS',states)
print('MIXED_HAMMING_JORDAN_ALL_CHECKS_PASSED')
