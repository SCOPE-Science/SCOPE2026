"""Reproduce the finite-ring Rule 22 fiber-mode theorem using exact integers."""
from itertools import product

A0=((1,0,0,0),(0,0,0,1),(0,1,0,0),(0,0,1,1))
A1=((0,1,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))

def mul(A,B):
    n=len(A); p=len(B); m=len(B[0]);
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(p)) for j in range(m)) for i in range(n))

def trace(A): return sum(A[i][i] for i in range(len(A)))

def matrix_count(bits):
    P=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
    for b in bits: P=mul(P,A1 if b else A0)
    return trace(P)

def envelope(m):
    result=[]
    for i in range(4):
        v=[int(i==j) for j in range(4)]
        for _ in range(m):
            a=[sum(v[k]*A0[k][j] for k in range(4)) for j in range(4)]
            b=[sum(v[k]*A1[k][j] for k in range(4)) for j in range(4)]
            v=[max(a[j],b[j]) for j in range(4)]
        result.append(tuple(v))
    return result

def output(x,n):
    return sum((( ((x>>((i-1)%n))&1)+((x>>i)&1)+((x>>((i+1)%n))&1))==1)<<i for i in range(n))

# Exact general envelope, closed form and matrix trace identities.
g=[3,1,1]
for n in range(3,101):g.append(g[n-1]+g[n-3])
U={3:3,4:3,5:4}
for n in range(6,101):U[n]=U[n-1]+U[n-3]
for m in range(2,50):
    E=envelope(m)
    assert len(set(E))==1, (m,E)
    x=E[0]
    if m>=3:
        assert x[0]==x[1] and 0<=x[0]<=x[2]<=x[3], (m,x)
    assert 2*x[0]+x[2]==U[m+1], (m,x,U[m+1])
for n in range(3,101):
    assert g[n]>U[n],(n,g[n],U[n])
    assert g[n]==g[n-1]+g[n-3] if n>=3 else True
    if n<=20: assert matrix_count((0,)*n)==1+g[n]

# Direct full preimage enumeration with independently computed local majority-of-one rule.
for n in range(3,17):
    N=1<<n
    counts=[0]*N
    for x in range(N):counts[output(x,n)]+=1
    assert counts[0]==1+g[n],(n,counts[0],1+g[n])
    assert max(counts[1:])<counts[0],n
    assert max(counts[1:])<=U[n],n
    if n<=11:
        for y in range(N):
            assert matrix_count(tuple((y>>i)&1 for i in range(n)))==counts[y],(n,y)
    print(n,counts[0],max(counts[1:]),U[n])
print('VERIFY_OK')
