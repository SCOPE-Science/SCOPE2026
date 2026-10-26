#!/usr/bin/env python3
"""Exact finite checks for the 2-adic Narayana zero-class theorem."""
M = ((1, 0, 1), (1, 0, 0), (0, 1, 0))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

def mul(A, B, mod=None):
    C = tuple(tuple(sum(A[i][h] * B[h][j] for h in range(3)) for j in range(3)) for i in range(3))
    if mod: C = tuple(tuple(t % mod for t in row) for row in C)
    return C

def power(A, n, mod=None):
    B = I
    while n:
        if n & 1: B = mul(B, A, mod)
        A = mul(A, A, mod)
        n //= 2
    return B

def narayana_mod_zeros(k):
    modulus = 1 << k
    period = 7 << (k-1)
    a, b, c = 0, 1, 1
    roots = []
    for n in range(period):
        if a % modulus == 0: roots.append(n)
        a, b, c = b, c, (c+a) % modulus
    assert (a,b,c) == (0,1,1), (k,a,b,c)
    return roots

M7=power(M,7)
M28=power(M,28)
E=tuple(tuple((M28[i][j]-I[i][j]) // 8 for j in range(3)) for i in range(3))
assert M7 == ((9,4,6),(6,3,4),(4,2,3))
assert M28 == ((27201,12664,18560),(18560,8641,12664),(12664,5896,8641))
assert all((M28[i][j]-I[i][j])%8==0 for i in range(3) for j in range(3))
assert tuple(tuple(e%2 for e in row) for row in E) == ((0,1,0),(0,0,1),(1,1,0))
X = (1,1,0)
assert sum(E[2][j]*X[j] for j in range(3)) %16 == 0
E2=mul(E,E)
assert sum(E2[2][j]*X[j] for j in range(3))%2 == 1
assert all(sum(M7[i][j]*X[j] for j in range(3))%2==X[i]%2 for i in range(3))
assert [i for i in range(7) if (lambda n: n%2==0)([0,1,1,1,2,3,4][i])] == [0,4,6]
for k in range(3,14):
    modulus=1<<k
    period=7<<(k-1)
    assert power(M,period,modulus)==I
    assert power(M,period//2,modulus)!=I
base=narayana_mod_zeros(6)
assert base == [0,28,56,84,112,140,168,196,216,221,223]
for k in range(6,14):
    roots=narayana_mod_zeros(k)
    assert len(roots)==11,(k,len(roots))
    assert sum(n%7==0 for n in roots)==8
    assert sum(n%7==4 for n in roots)==1
    assert sum(n%7==6 for n in roots)==2
    assert all(n%28==0 for n in roots if n%7==0)
    assert all(n%7 in (4,6) for n in roots if n%28!=0)
    assert sum(n %7 in (4,6) for n in roots)==3
# Independent finite determination of the second 2-adic root alpha modulo 2^j:
for j in range(1,9):
    modulus=1 << (5+j)
    nmax=28*(1<<j)
    a,b,c=0,1,1
    special=[]
    for n in range(nmax):
        if n and n%28==0 and (n//28)%2 and a%modulus==0:
            special.append(n//28)
        a,b,c=b,c,(c+a)%modulus
    assert len(special)==1,(j,special)
    if j>=3:assert special[0]%8==5
    if j>=4:assert special[0]%16==13
    print('alpha modulo',1<<j,':',special[0])
print('VERIFY_OK: exact companion identities, 11-root periods k=6..13, two-adic root lifts j=1..8')
