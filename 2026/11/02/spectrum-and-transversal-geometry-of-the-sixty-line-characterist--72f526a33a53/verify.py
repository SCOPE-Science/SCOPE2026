"""Exact reconstruction of the 60-line incidence graph on a quartic K3.

Requires Python 3.10+ and SymPy. Run: python verify.py
All finite-field elements are represented by integer polynomial bit masks.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from sympy import Matrix, Symbol, factor

MOD=0x13  # F_16=F_2[t]/(t^4+t+1)
def mul(x,y):
    z=0
    while y:
        if y&1: z ^= x
        y >>= 1
        x <<= 1
        if x&16: x ^= MOD
    return z

def power(x,n):
    z=1
    while n:
        if n&1: z=mul(z,x)
        x=mul(x,x); n//=2
    return z

def inverse(x):
    assert x
    return power(x,14)

root=next(x for x in range(2,16) if power(x,5)==1 and x!=1)
mu=1 ^ power(root,2) ^ power(root,3)
assert mu not in (0,1) and (mul(mu,mu)^mu^1)==0
U=(power(root,3),1,0,power(root,3)^root^1,root)
V=(power(root,4),0,1,1,power(root,4))
PAIRS=list(combinations(range(5),2))

def plucker(u,v):
    p=tuple(mul(u[i],v[j])^mul(u[j],v[i]) for i,j in PAIRS)
    s=inverse(next(x for x in p if x))
    return tuple(mul(x,s) for x in p)

def permute_line(u,v,perm):
    a=[0]*5; b=[0]*5
    for i in range(5): a[perm[i]]=u[i]; b[perm[i]]=v[i]
    return tuple(a),tuple(b)

line_by_key={}
for g in permutations(range(5)):
    a,b=permute_line(U,V,g)
    line_by_key[plucker(a,b)]=(a,b)
keys=sorted(line_by_key)
assert len(keys)==60
idx={p:i for i,p in enumerate(keys)}

def frob_key(p):
    q=tuple(power(x,4) for x in p)
    a=inverse(next(x for x in q if x))
    return tuple(mul(x,a) for x in q)

frob=[idx[frob_key(p)] for p in keys]
assert all(frob[frob[i]]==i and frob[i]!=i for i in range(60))

def determinant4(m):
    z=0  # in characteristic two all determinant permutation signs are +
    for sigma in permutations(range(4)):
        t=1
        for i,j in enumerate(sigma):t=mul(t,m[i][j])
        z ^= t
    return z

def meet(a,b,c,d):
    for omit in range(5):
        rows=[i for i in range(5) if i!=omit]
        if determinant4([[v[i] for v in (a,b,c,d)] for i in rows]):
            return False
    return True

adj=[]
for i,p in enumerate(keys):
    row=[]
    for j,q in enumerate(keys):
        row.append(int(i!=j and meet(*line_by_key[p],*line_by_key[q])))
    adj.append(row)
assert all(sum(row)==17 for row in adj)
assert all(adj[i][j]==adj[j][i] for i in range(60) for j in range(60))

x=Symbol('x')
charpoly=factor(Matrix(adj).charpoly(x).as_expr())
expected=(x-17)*(x-2)**40*(x+3)**5*(x+4)**4*(x+5)**5*(x+8)**4*(x+9)
assert (charpoly-expected).expand()==0

profile=defaultdict(Counter)
maximal=[]
for i in range(60):
    for j in range(i+1,60):
        k=sum(adj[i][v]*adj[j][v] for v in range(60))
        profile[adj[i][j]][k]+=1
        if adj[i][j]==0 and k==8: maximal.append((i,j))
assert dict(profile[1])=={0:150,2:360}
assert dict(profile[0])=={4:150,5:360,6:360,7:240,8:150}
assert len(maximal)==150
assert all(adj[i][frob[i]]==0 and
           sum(adj[i][k]*adj[frob[i]][k] for k in range(60))==8
           for i in range(60))

# Independently compute all S_5-orbits on the 150 maximally transversal skew pairs.
actions=[]
for g in permutations(range(5)):
    actions.append([idx[plucker(*permute_line(*line_by_key[p],g))] for p in keys])
maximal_set=set(maximal)
seen=set(); orb_sizes=[]; conj_count=0
for edge in maximal:
    if edge in seen:continue
    i,j=edge
    orbit={tuple(sorted((h[i],h[j]))) for h in actions}
    assert orbit<=maximal_set
    seen.update(orbit); orb_sizes.append(len(orbit))
    if frob[i]==j:
        conj_count+=1
        assert len(orbit)==30
assert seen==maximal_set and sorted(orb_sizes)==[30,60,60]
assert conj_count==1

# An independent RREF census confirms no further F_16-rational lines.
def polynomial(t):
    s2=0; s4=0
    for i,j in PAIRS: s2 ^= mul(t[i],t[j])
    for omit in range(5):
        p=1
        for j in range(5):
            if j!=omit:p=mul(p,t[j])
        s4 ^= p
    return s4 ^ mul(mu,mul(s2,s2))

def projective_line_on_surface(u,v):
    for s,t in [(1,0),(0,1),(1,1),(1,root),(1,power(root,2))]:
        z=[mul(s,u[i])^mul(t,v[i]) for i in range(4)]
        z5=(z[0]^z[1]^z[2]^z[3],*z)
        if polynomial(z5): return False
    return True

def enumerate_rref(q):
    hit=0;total=0
    for a,b in combinations(range(4),2):
        coords=[(0,c) for c in range(a+1,4) if c!=b]+[(1,c) for c in range(b+1,4)]
        for t in product(q,repeat=len(coords)):
            u=[0]*4;v=[0]*4
            u[a]=1;v[b]=1
            for (row,col),value in zip(coords,t):
                (u if row==0 else v)[col]=value
            total+=1
            hit+=projective_line_on_surface(u,v)
    assert total==(len(q)**2+1)*(len(q)**2+len(q)+1)
    return total,hit

assert enumerate_rref([0,1,6,7])==(357,0)
assert enumerate_rref(list(range(16)))==(70161,60)

print('F16 polynomial:',hex(MOD),'primitive fifth root:',root,'mu:',mu)
print('Geometric lines:',len(keys),'S5 orbit; graph degree:',17,'edges:',510)
print('Adjacency characteristic polynomial:',charpoly)
print('Intersecting-pair common neighbors:',dict(sorted(profile[1].items())))
print('Skew-pair common transversals:',dict(sorted(profile[0].items())))
print('Maximal transversal pairs: orbit sizes',sorted(orb_sizes))
print('Frobenius-paired lines: 30 skew pairs, each with 8 common transversals')
print('RREF checks: F4 0/357 lines; F16 60/70161 lines')
print('VERIFY_OK')
