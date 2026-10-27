"""Exact finite-field and integer-matrix checks for the zeta polynomial of an F4 quartic K3.
Standard-library only; prints VERIFY_OK if every test succeeds.
"""
from itertools import permutations, combinations, product

POLY = 0b11111  # F_16 = F_2[a]/(a^4+a^3+a^2+a+1)

def mul(x,y):
    z=0
    while y:
        if y&1: z^=x
        y>>=1
        x<<=1
        if x&16: x^=POLY
    return z

def power(x,n):
    y=1
    for _ in range(n): y=mul(y,x)
    return y

INV=[0]+[next(y for y in range(1,16) if mul(x,y)==1) for x in range(1,16)]

def rref(rows):
    a=[list(row) for row in rows]
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=INV[a[rank][j]]
        a[rank]=[mul(inv,x) for x in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][j]:
                d=a[i][j]
                a[i]=[x^mul(d,y) for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a): break
    return tuple(tuple(row) for row in a if any(row))

def rank_mod(matrix,prime=1000003):
    a=[list(row) for row in matrix]
    nr=len(a)
    nc=len(a[0])
    r=0
    for j in range(nc):
        i=next((t for t in range(r,nr) if a[t][j]%prime),None)
        if i is None: continue
        a[r],a[i]=a[i],a[r]
        x=pow(a[r][j]%prime,-1,prime)
        a[r][j:]=[y*x%prime for y in a[r][j:]]
        for i in range(r+1,nr):
            x=a[i][j]%prime
            if x:
                a[i][j:]=[(y-x*z)%prime for y,z in zip(a[i][j:],a[r][j:])]
        r+=1
        if r==nr: break
    return r

def elementary(xs,k):
    out=0
    for indices in combinations(range(5),k):
        z=1
        for i in indices: z=mul(z,xs[i])
        out^=z
    return out

a=2
mu=1^power(a,2)^power(a,3)
assert power(a,5)==1 and a!=1
assert power(mu,3)==1 and mu!=1 and mul(mu,mu)^mu^1==0
c=1^a^power(a,3)
d=1^a^power(a,2)^power(a,3)
# The published line uses coordinates x1,...,x5, and x5 = x1+x2+x3+x4.
row1=(1,0,c,a,1^c^a)
row2=(0,1,1,d,1^1^d)
lines=sorted({rref([[row[j] for j in perm] for row in (row1,row2)])
              for perm in permutations(range(5))})
assert len(lines)==60
# Check, coefficient by coefficient, that the source line lies on e4+mu*e2^2=0.
def polymul(p,q):
    out={}
    for i,x in p.items():
        for j,y in q.items():out[i+j]=out.get(i+j,0)^mul(x,y)
    return {i:v for i,v in out.items() if v}
def restricted_elementary(k):
    out={}
    for inds in combinations(range(5),k):
        p={0:1}
        for j in inds:p=polymul(p,{0:row1[j],1:row2[j]})
        for i,x in p.items():out[i]=out.get(i,0)^x
    return {i:v for i,v in out.items() if v}
e2=restricted_elementary(2)
e4=restricted_elementary(4)
for i,x in polymul(e2,e2).items():e4[i]=e4.get(i,0)^mul(mu,x)
assert not any(e4.values())

# Distinct lines on a smooth quartic have intersection product 0 or 1.
G=[[-2 if i==j else int(len(rref((*u,*v)))==3)
    for j,v in enumerate(lines)] for i,u in enumerate(lines)]
assert all(sum(1 for v in row if v==1)==17 for row in G)
assert sum(v==1 for row in G for v in row)==1020
fmap={line:i for i,line in enumerate(lines)}
pi=[fmap[rref([[power(x,4) for x in row] for row in u])] for u in lines]
assert all(pi[pi[i]]==i and pi[i]!=i for i in range(60))
assert all(G[pi[i]][pi[j]]==G[i][j] for i in range(60) for j in range(60))
# For cycle permutation P, the image of G(I+/-P) is the +/- eigenspace
# in the Neron-Severi span. Modular ranks give certified lower bounds
# over Q. The published NS rank 20 caps their sum at 20.
plus=[[G[i][j]+G[i][pi[j]] for j in range(60)] for i in range(60)]
minus=[[G[i][j]-G[i][pi[j]] for j in range(60)] for i in range(60)]
rplus=rank_mod(plus)
rminus=rank_mod(minus)
assert (rplus,rminus)==(10,10)
# Exhaustive geometric point enumeration in P^3(Fq): e1=0 uniquely
# sets the fifth coordinate, and each projective point has q-1 lifts.
counts=[]
for field in ([0,1,mu,mu^1],list(range(16))):
    q=len(field)
    Naffine=0
    for u,v,w,z in product(field,repeat=4):
        xs=(u,v,w,z,u^v^w^z)
        if not any(xs):continue
        e2x=elementary(xs,2)
        if elementary(xs,4)^mul(mu,mul(e2x,e2x))==0:
            Naffine+=1
    assert Naffine%(q-1)==0
    counts.append(Naffine//(q-1))
assert counts==[20,554], counts
# By trace formula and the 10+10 algebraic Frobenius eigenspaces:
t1=counts[0]-(1+4**2)-4*(rplus-rminus)
t2=counts[1]-(1+4**4)-4**2*(rplus+rminus)
det=(t1*t1-t2)//2
assert (t1,t2,det)==(3,-23,16)
print('VERIFY_OK: 60 F16 lines, Frobenius NS eigenmultiplicities (10,10),')
print('  F4 and F16 point counts (20,554), transcendental x^2-3x+16')
