#!/usr/bin/env python3
"""Exact, self-contained checks for a trace-quartic net and its arithmetic."""
from itertools import product
from math import comb

MODULI={1:(0,1),2:(1,0,1),3:(2,2,0,1)}

def digits(x,k):
    return tuple(x//(3**i)%3 for i in range(k))

def encode(v):
    return sum((a%3)*3**i for i,a in enumerate(v))

class Field:
    def __init__(self,k):
        self.k=k; self.q=3**k; self.mod=MODULI[k]
        self.rows=[digits(i,k) for i in range(self.q)]
        self.add=[[encode(tuple((a+b)%3 for a,b in zip(x,y))) for y in self.rows]
                  for x in self.rows]
        self.mul=[[self._multiply(x,y) for y in self.rows] for x in self.rows]

    def _multiply(self,u,v):
        k=self.k; acc=[0]*(2*k-1)
        for i,a in enumerate(u):
            for j,b in enumerate(v):
                acc[i+j]=(acc[i+j]+a*b)%3
        for i in range(2*k-2,k-1,-1):
            lead=acc[i]
            for j in range(k):
                acc[i-k+j]=(acc[i-k+j]-lead*self.mod[j])%3
        return encode(acc[:k])

    def power(self,x,n):
        z=1
        while n:
            if n%2: z=self.mul[z][x]
            n//=2; x=self.mul[x][x]
        return z

K=Field(3)
t=3  # t^3=t+1 in F_27
assert K.power(t,13)==1 and all(K.power(t,i)!=1 for i in range(1,13))
beta=K.power(t,2)
basis=[K.power(beta,3**i) for i in range(3)]
assert len({K.add[K.add[K.mul[a][basis[0]]][K.mul[b][basis[1]]]][K.mul[c][basis[2]]]
            for a,b,c in product(range(3),repeat=3)})==27

# Expand Trace((beta*x + beta^3*y + beta^9*z)^4) by exact field arithmetic.
coef={}
for i in range(5):
    for j in range(5-i):
        h=4-i-j; multinom=comb(4,i)*comb(4-i,j)%3
        v=multinom
        for b,power in zip(basis,(i,j,h)):
            v=K.mul[v][K.power(b,power)]
        tr=K.add[K.add[v][K.power(v,3)]][K.power(v,9)]
        assert tr in (0,1,2)
        coef[(i,j,h)]=tr

explicit={(4,0,0):1,(3,1,0):2,(3,0,1):1,
          (1,3,0):1,(1,0,3):2,(0,4,0):1,
          (0,3,1):2,(0,1,3):1,(0,0,4):1}
assert all(coef.get(mon,0)==explicit.get(mon,0) for mon in set(coef)|set(explicit))

def padd(a,b):
    c=dict(a)
    for mon,v in b.items():
        c[mon]=(c.get(mon,0)+v)%3
        if c[mon]==0:del c[mon]
    return c

def pmul(a,b):
    c={}
    for mon,v in a.items():
        for mon2,w in b.items():
            m=tuple(x+y for x,y in zip(mon,mon2))
            c[m]=(c.get(m,0)+v*w)%3
            if c[m]==0:del c[m]
    return c

def ppow(a,k):
    p={(0,0,0):1}
    for _ in range(k): p=pmul(p,a)
    return p

# The explicit projective F_3-coordinate change sends the trace quartic to Klein's.
M=((1,1,2),(2,1,1),(1,2,1))
det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
     -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
     +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))%3
assert det==1
L=[{tuple(int(j==v) for j in range(3)):M[i][v]}
   for i in range(3) for v in range(3)]
linear=[padd(padd(L[i*3],L[i*3+1]),L[i*3+2]) for i in range(3)]
transformed={}
for ex,c in explicit.items():
    one={(0,0,0):c}
    for a,k in zip(linear,ex):one=pmul(one,ppow(a,k))
    transformed=padd(transformed,one)
klein={(3,1,0):1,(0,3,1):1,(1,0,3):1}
assert transformed==klein, (transformed,klein)

def point_count(field,formula):
    q=field.q; m=field.mul;a=field.add;p=field.power
    def P(x,y,z):
        if formula=='klein':
            return a[a[m[p(x,3)][y]][m[p(y,3)][z]]][m[p(z,3)][x]]
        v=0
        for (i,j,k),co in explicit.items():
            term=m[m[p(x,i)][p(y,j)]][p(z,k)]
            v=a[v][m[co][term]]
        return v
    return (sum(P(1,y,z)==0 for y in range(q) for z in range(q))+
            sum(P(0,1,z)==0 for z in range(q))+(P(0,0,1)==0))

expected=(4,10,28)
for k,target in enumerate(expected,1):
    field=Field(k)
    count_trace=point_count(field,'trace')
    count_klein=point_count(field,'klein')
    assert count_trace==count_klein==target,(k,count_trace,count_klein,target)
    print(f'F_{{3^{k}}}: Klein={count_klein}, trace={count_trace}')

# Closed-form parameter count and orbit size for q=3, n=2, d=4.
N=(3**3-1)//(3-1)
assert N==13 and 4%N!=0
assert len({(4*j)%N for j in range(N)})==13

# The thirteen rational quartics give the 2-(13,4,1) incidence structure.
points=[(1,a,b) for a in range(3) for b in range(3)]+[(0,1,a) for a in range(3)]+[(0,0,1)]
def trace27(z):
    return K.add[K.add[z][K.power(z,3)]][K.power(z,9)]
def coordinate_Y(point):
    return K.add[K.add[K.mul[point[0]][basis[0]]][K.mul[point[1]][basis[1]]]][K.mul[point[2]][basis[2]]] 
blocks=[]
for j in range(13):
    lam=K.power(t,j)
    block=frozenset(i for i,point in enumerate(points)
        if trace27(K.mul[lam][K.power(coordinate_Y(point),4)])==0)
    assert len(block)==4
    blocks.append(block)
assert len(set(blocks))==13
assert all(sum(i in block for block in blocks)==4 for i in range(13))
assert all(len(blocks[i] & blocks[j])==1 for i in range(13) for j in range(i+1,13))
assert all(sum(i in block and j in block for block in blocks)==1
           for i in range(13) for j in range(i+1,13))
print('Incidence: 13 distinct four-point blocks, pairwise intersection 1; VERIFY_DESIGN_OK')

# Genus 3 Weil polynomial: if power sums s1,s2,s3 are zero,
# Newton identities + functional equation force 1 + 3^3*T^6.
s=[3**k+1-expected[k-1] for k in range(1,4)]
assert s==[0,0,0]
coefL=[1]
for k in range(1,4):
    raw=-sum(s[j-1]*coefL[k-j] for j in range(1,k+1))
    assert raw%k==0
    coefL.append(raw//k)
coefL.extend([3*coefL[2],9*coefL[1],27*coefL[0]])
assert coefL==[1,0,0,0,0,0,27]
print('L-polynomial coefficients:',coefL)
print('VERIFY_OK')
