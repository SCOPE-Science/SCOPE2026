import itertools
from collections import Counter

G=list(itertools.permutations(range(3)))
idx={p:i for i,p in enumerate(G)}

def compose(p,q):
    return tuple(p[q[i]] for i in range(3))

def inverse_perm(p):
    out=[0]*3
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)

mul=[[idx[compose(p,q)] for q in G] for p in G]
inv=[idx[inverse_perm(p)] for p in G]
e=idx[(0,1,2)]

def power(x,n):
    if n<0:
        return power(inv[x],-n)
    z=e
    for _ in range(n):
        z=mul[z][x]
    return z

def is_rb(B):
    for g in range(6):
        for h in range(6):
            lhs=mul[B[g]][B[h]]
            arg=mul[mul[mul[g][B[g]]][h]][inv[B[g]]]
            if lhs!=B[arg]:
                return False
    return True

ops=[
    B for B in itertools.product(range(6),repeat=6)
    if is_rb(B)
]
assert len(ops)==8

dist=Counter()
for B in ops:
    ker=sum(1 for x in B if x==e)
    im=len(set(B))
    dist[(ker,im)]+=1
assert dist==Counter({(6,1):1,(3,2):3,(2,3):3,(1,6):1}),dist

def conj(a,x):
    return mul[mul[a][x]][inv[a]]

def aut_transform(B,a):
    # phi=Ad_a and B^(phi)=phi^{-1} B phi
    return tuple(conj(inv[a],B[conj(a,x)]) for x in range(6))

pool=set(ops)
orbits=[]
while pool:
    B=next(iter(pool))
    O={aut_transform(B,a) for a in range(6)}
    assert O<=set(ops)
    orbits.append(O)
    pool-=O
assert sorted(map(len,orbits))==[1,1,3,3]

def tilde(B):
    return tuple(mul[inv[g]][B[inv[g]]] for g in range(6))

orbit_index={}
for i,O in enumerate(orbits):
    for B in O:
        orbit_index[B]=i

pairs=set()
for i,O in enumerate(orbits):
    j=orbit_index[tilde(next(iter(O)))]
    pairs.add(tuple(sorted((i,j))))
assert len(pairs)==2
assert all(i!=j for i,j in pairs)

def desc_mul(B,x,y):
    return mul[mul[mul[x][B[x]]][y]][inv[B[x]]]

def desc_order(B,x):
    z=e
    for n in range(1,13):
        z=desc_mul(B,z,x)
        if z==e:
            return n
    raise AssertionError("order not found")

for B in ops:
    ker=sum(1 for x in B if x==e)
    im=len(set(B))
    orders=sorted(desc_order(B,x) for x in range(6))
    if (ker,im) in ((3,2),(2,3)):
        assert orders==[1,2,3,3,6,6],orders
    else:
        assert orders==[1,2,2,2,3,3],orders

# Choose r=(123), s=(12).
r=idx[(1,2,0)]
s=idx[(1,0,2)]
assert power(r,3)==e and power(s,2)==e
assert mul[mul[s][r]][s]==inv[r]

# B2 on S3=A3 <s>: B2(r^i s^j)=s^j.
B2=[None]*6
for i in range(3):
    for j in range(2):
        g=mul[power(r,i)][power(s,j)]
        assert B2[g] is None
        B2[g]=power(s,j)
B2=tuple(B2)

# B3 on S3=<s> A3: B3(s^j r^i)=r^{-i}.
B3=[None]*6
for j in range(2):
    for i in range(3):
        g=mul[power(s,j)][power(r,i)]
        assert B3[g] is None
        B3[g]=power(r,-i)
B3=tuple(B3)

assert B2 in ops and B3 in ops
assert tilde(B2)==B3
assert tilde(B3)==B2

B0=tuple(e for _ in range(6))
Bminus=tuple(inv[g] for g in range(6))
assert B0 in ops and Bminus in ops
assert tilde(B0)==Bminus
assert tilde(Bminus)==B0

print({
    "operators":len(ops),
    "kernel_image_distribution":dict(sorted(dist.items())),
    "automorphism_orbit_sizes":sorted(map(len,orbits)),
    "combined_aut_tilde_classes":len(pairs),
})
print("VERIFY_OK")
