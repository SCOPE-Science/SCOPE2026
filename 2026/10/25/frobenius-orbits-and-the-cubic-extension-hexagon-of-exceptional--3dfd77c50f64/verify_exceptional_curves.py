"""Exact finite checks for nine-cycle E8 roots and the base-locus polynomial.
Uses only Python's standard library; no downloaded data are required.
"""
from itertools import combinations
from collections import Counter

P=5
f=(4,1,0,0,0,0,1,0,0,1)   # z^9+z^6+z-1 over F_5

def trim(a):
    a=list(a)
    while a and a[-1]==0: a.pop()
    return tuple(a)

def rem(a,b):
    a=list(trim(a)); b=trim(b)
    while len(a)>=len(b) and a:
        c=a[-1]*pow(b[-1],-1,P)%P
        j=len(a)-len(b)
        for i,v in enumerate(b):a[j+i]=(a[j+i]-c*v)%P
        a=list(trim(a))
    return tuple(a)

def mulmod(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):z[i+j]=(z[i+j]+u*v)%P
    return rem(z,f)

def powmod(a,k):
    o=(1,)
    while k:
        if k&1:o=mulmod(o,a)
        a=mulmod(a,a); k>>=1
    return o

def gcd(a,b):
    a,b=trim(a),trim(b)
    while b:a,b=b,rem(a,b)
    return tuple((v*pow(a[-1],-1,P))%P for v in a) if a else ()

def sub(a,b):
    return trim(tuple(((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%P for i in range(max(len(a),len(b)))))

x=(0,1)
for d in (1,3):
    xd=powmod(x,5**d)
    assert gcd(f,sub(xd,x))==(1,), (d,xd)
assert powmod(x,5**9)==x
print('irreducible: z^9+z^6+z-1 mod 5 (Rabin criterion)')

# Root representatives r=d H-sum_{i=0}^8 m_i E_i in (3H-sum E_i)^perp / Z(3H-sum E_i)
roots=[]
for i in range(9):
    for j in range(9):
        if i==j:continue
        m=[0]*9;m[i]=1;m[j]=-1
        roots.append((0,tuple(m)))
for d,s in ((1,3),(2,6)):
    for ii in combinations(range(9),s):
        m=tuple(int(i in ii) for i in range(9))
        roots.append((d,m))
assert len(roots)==len(set(roots))==240
for d,m in roots:
    assert sum(m)==3*d and sum(v*v for v in m)==d*d+2
root_set=set(roots)
def frob(r):
    d,m=r
    return d,tuple(m[(i-1)%9] for i in range(9))

visited=set();orbits=[]
for r in roots:
    if r in visited:continue
    orbit=[];cur=r
    while cur not in visited:
        visited.add(cur);orbit.append(cur);cur=frob(cur)
    assert cur==r
    orbits.append(orbit)
assert len(visited)==240
hist=dict(sorted(Counter(map(len,orbits)).items()))
print('orbit histogram:',hist)
assert hist=={3:2,9:26}
fixed=[]
for r in roots:
    t=r
    for _ in range(3):t=frob(t)
    if t==r:fixed.append(r)
assert len(fixed)==6
print('F_{5^3}-defined curves:',len(fixed))

def intersect(a,b):
    d,m=a;e,n=b
    # exceptional class is root - K; intersection is r.s+1
    return d*e-sum(x*y for x,y in zip(m,n))+1

assert all(intersect(r,r)==-1 for r in roots)
disjoint=[];pairhist=Counter()
for i,j in combinations(range(6),2):
    z=intersect(fixed[i],fixed[j]);pairhist[z]+=1
    if z==0:disjoint.append((i,j))
assert pairhist=={0:6,2:6,3:3}, pairhist
assert len(disjoint)==6
assert all(sum(i in edge for edge in disjoint)==2 for i in range(6))
print('six-curve pairwise intersection histogram:',dict(sorted(pairhist.items())))
print('disjointness graph is connected cycle:',end=' ')
start=0;seen={start};todo=[start]
while todo:
    u=todo.pop()
    for a,b in disjoint:
        if u in (a,b):
            v=b if u==a else a
            if v not in seen:seen.add(v);todo.append(v)
assert len(seen)==6
print('C6')
print('all tests PASS')
