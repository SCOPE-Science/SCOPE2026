from itertools import combinations, permutations

N=12
DIVS=(1,2,3,4,6,12)
UNITS=(1,5,7,11)
B5=(0,1,2,3,5)
B6=(0,1,2,3,5,10)

# Uniform distribution over every divisor of 12.
def uniform(S):
    m=len(S)
    for d in DIVS:
        counts=[0]*d
        for x in S: counts[x%d]+=1
        lo=m//d; hi=(m+d-1)//d
        if any(c not in (lo,hi) for c in counts): return False
    return True

def affine_image(S,a,b):
    return tuple(sorted((a*x+b)%N for x in S))

def orbit(S):
    return {affine_image(S,a,b) for a in UNITS for b in range(N)}

def canon(S):
    return min(orbit(S))

def comp(S):
    return tuple(sorted(set(range(N))-set(S)))

expected={
    1:{(0,)},
    2:{(0,1)},
    3:{(0,1,2)},
    4:{(0,1,2,3)},
    5:{(0,1,2,3,4),B5},
    6:{(0,1,2,3,4,5),B6},
}
for m in range(1,7):
    U=[S for S in combinations(range(N),m) if uniform(S)]
    assert {canon(S) for S in U}==expected[m]

assert len(orbit(B5))==48
assert len(orbit(B6))==12
assert affine_image(B6,1,6)==comp(B6)

# Exact arithmetic in Z[z]/(Phi_12), Phi_12=z^4-z^2+1.
ZERO=(0,0,0,0); ONE=(1,0,0,0); Z=(0,1,0,0)
def add(a,b): return tuple(a[i]+b[i] for i in range(4))
def neg(a): return tuple(-x for x in a)
def mul(a,b):
    t=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b): t[i+j]+=x*y
    for d in range(6,3,-1):
        c=t[d]
        if c:
            t[d]=0; t[d-2]+=c; t[d-4]-=c
    return tuple(t[:4])
POW=[ONE]
for _ in range(1,N): POW.append(mul(POW[-1],Z))
assert POW[6]==(-1,0,0,0)

def sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1
PERMS={m:[(p,sign(p)) for p in permutations(range(m))] for m in (5,6)}
def det_exact(R,C):
    acc=ZERO
    for p,sgn in PERMS[len(R)]:
        term=ONE
        for i,r in enumerate(R): term=mul(term,POW[(r*C[p[i]])%N])
        acc=add(acc,term if sgn==1 else neg(term))
    return acc

W5=(0,1,4,7,8)
W6=(0,1,2,4,7,8)
assert det_exact(B5,W5)==ZERO
assert det_exact(B6,W6)==ZERO

# Direct exact zero-minor counts for the two bad representatives.
assert sum(det_exact(B5,C)==ZERO for C in combinations(range(N),5))==12
assert sum(det_exact(B6,C)==ZERO for C in combinations(range(N),6))==120

# Consecutive representatives are Vandermonde full spark. As an independent
# finite check, reduce at a primitive 12th root modulo 1009; nonzero images
# certify nonzero cyclotomic determinants over characteristic zero.
p=1009; z=160
assert pow(z,12,p)==1 and all(pow(z,d,p)!=1 for d in (1,2,3,4,6))
def detmod(R,C):
    A=[[pow(z,(r*c)%N,p) for c in C] for r in R]
    d=1; n=len(R)
    for j in range(n):
        rr=next((i for i in range(j,n) if A[i][j]%p),None)
        if rr is None: return 0
        if rr!=j: A[j],A[rr]=A[rr],A[j]; d=-d
        piv=A[j][j]%p; d=d*piv%p; inv=pow(piv,p-2,p)
        for i in range(j+1,n):
            f=A[i][j]*inv%p
            for k in range(j+1,n): A[i][k]=(A[i][k]-f*A[j][k])%p
    return d%p
for m in range(1,7):
    R=tuple(range(m))
    assert all(detmod(R,C)!=0 for C in combinations(range(N),m))

# Full classification counts among uniformly distributed sets; complement
# symmetry supplies sizes >6.
rows=[]
for m in range(1,12):
    U=[S for S in combinations(range(N),m) if uniform(S)]
    bad=[]
    for S in U:
        exceptional=(canon(S) in {B5,B6} or canon(comp(S)) in {B5,B6})
        if exceptional: bad.append(S)
    rows.append((m,len(U),len(U)-len(bad),len(bad),len({canon(S) for S in U})))
expected_rows=[
(1,12,12,0,1),(2,24,24,0,1),(3,24,24,0,1),(4,24,24,0,1),
(5,72,24,48,2),(6,36,24,12,2),(7,72,24,48,2),(8,24,24,0,1),
(9,24,24,0,1),(10,24,24,0,1),(11,12,12,0,1)]
assert rows==expected_rows
print('m uniform full nonfull affine_orbits')
for r in rows: print(*r)
print('B5_zero_minors',12,'witness',W5)
print('B6_zero_minors',120,'witness',W6)
print('VERIFY_OK')
