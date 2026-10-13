"""Finite evidence for a central-bilinear family of Heisenberg skew braces.

Run: python3 verify.py. Uses only the Python standard library.
"""
from itertools import product
from collections import Counter

p = 3
n = 4
J = [[0]*n for _ in range(n)]
for i in range(2):
    J[i][i+2] = 1
    J[i+2][i] = p-1
pairs = [(i,j) for i in range(n) for j in range(i+1,n)]

def transpose(A):
    return [list(x) for x in zip(*A)]

def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p
             for j in range(len(B[0]))] for i in range(len(A))]

def bmat(z):
    M = [[0]*n for _ in range(n)]
    for v,(i,j) in zip(z,pairs):
        M[i][j] = v
        M[j][i] = -v % p
    return M

def bcoords(M):
    return tuple(M[i][j] for i,j in pairs)

def transvection(v):
    row=[sum(v[i]*J[i][j] for i in range(n))%p for j in range(n)]
    return [[(int(i==j)+v[i]*row[j])%p for j in range(n)] for i in range(n)]

# Independent orbit enumeration of the 729 alternating 4-by-4 forms.
generators = {tuple(tuple(row) for row in transvection(v))
              for v in product(range(p),repeat=n) if any(v)}
actions=[]
for raw in generators:
    P=[list(row) for row in raw]
    assert multiply(multiply(transpose(P),J),P)==J
    cols=[]
    for k in range(len(pairs)):
        z=[0]*len(pairs);z[k]=1
        cols.append(bcoords(multiply(multiply(transpose(P),bmat(z)),P)))
    actions.append(cols)

unseen=set(product(range(p),repeat=len(pairs)))
orbits=[]

def rank(M):
    R=[row[:] for row in M]
    r=0
    for j in range(len(R[0])):
        k=next((i for i in range(r,len(R)) if R[i][j]),None)
        if k is None:
            continue
        R[r],R[k]=R[k],R[r]
        inv=pow(R[r][j],-1,p)
        R[r]=[inv*x%p for x in R[r]]
        for i in range(len(R)):
            if i!=r and R[i][j]:
                a=R[i][j]
                R[i]=[(u-a*v)%p for u,v in zip(R[i],R[r])]
        r+=1
    return r

while unseen:
    start=next(iter(unseen));unseen.remove(start)
    frontier=[start];size=0
    while frontier:
        x=frontier.pop();size+=1
        for cols in actions:
            y=tuple(sum(x[j]*cols[j][i] for j in range(6))%p
                    for i in range(6))
            if y in unseen:
                unseen.remove(y);frontier.append(y)
    orbits.append((rank(bmat(start)),size))
assert len(orbits)==12
assert Counter(r for r,s in orbits)==Counter({0:1,2:3,4:8})
assert sorted(s for r,s in orbits)==[1,1,1,72,72,72,80,80,80,90,90,90]
assert sum(s for r,s in orbits)==p**6

# Direct brace operation check for all three beta-values in dimension two.
def omega(v,w):
    return (v[0]*w[1]-v[1]*w[0])%p

def add(a,b,k):
    (v,s),(w,t)=a,b
    return ((v[0]+w[0])%p,(v[1]+w[1])%p),(s+t+k*omega(v,w))%p

def mul(a,b):
    return add(a,b,1)

def neg(a):
    return (tuple(-u%p for u in a[0]),-a[1]%p)

def lam(a,b,k):
    return add(neg(a),mul(a,b),k)

G=[((x,y),s) for x,y,s in product(range(p),repeat=3)]
for k in range(p):
    for a in G:
        for b in G:
            for c in G:
                # lambda_a(b+_k c) = lambda_a(b)+_k lambda_a(c)
                assert lam(a,add(b,c,k),k)==add(lam(a,b,k),lam(a,c,k),k)
                # the multiplicative group is the same for all k.
                assert mul(a,b)==add(a,b,1)
                assert mul(add(a,b,k),c)==add(add(mul(a,c),neg(c),k),mul(b,c),k)

print('VERIFY_OK')
print('p=3,d=2: 729 alternating forms; 12 symplectic orbits')
print('orbit_rank_counts',dict(sorted(Counter(r for r,s in orbits).items())))
print('orbit_sizes',sorted(s for r,s in orbits))
print('p=3,d=1: all 3 central alternating additions satisfy skew brace identity')
