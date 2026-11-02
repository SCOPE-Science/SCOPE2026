"""Exact finite certificate for the Shrikhande independence-complex symmetry action.

Python 3 standard library only. Every oriented face, graph automorphism and
Hasse incidence is generated afresh from the explicit graph definition.
"""
from collections import Counter, defaultdict, deque
from itertools import product

V = list(product(range(4), repeat=2))
I = {x: k for k, x in enumerate(V)}
D = {(1,0), (3,0), (0,1), (0,3), (1,1), (3,3)}
N = [sum(1 << j for j, y in enumerate(V)
         if ((y[0]-x[0])%4,(y[1]-x[1])%4) in D)
     for x in V]
assert all(mask.bit_count() == 6 for mask in N)
assert all(bool(N[i] & (1<<j)) == bool(N[j] & (1<<i)) for i in range(16) for j in range(16))
assert all((N[i]&N[j]).bit_count() == 2 for i in range(16) for j in range(i+1,16))

# Exhaustive face census, including the empty face.
S = {0}
for mask in range(1,1<<16):
    bit=mask & -mask
    v=bit.bit_length()-1
    lower=mask ^ bit
    if lower in S and not (lower & N[v]):
        S.add(mask)
F = S - {0}
fvec = Counter(mask.bit_count()-1 for mask in F)
assert fvec == {0:16,1:72,2:96,3:16} and len(F)==200

# Forman matching: sequentially toggle vertices, using only still-unmatched faces.
U=set(F); matched=[]
for v in range(16):
    bit=1<<v
    for mask in sorted(U):
        if mask & bit:
            continue
        target=mask | bit
        if target in U:
            U.remove(mask);U.remove(target)
            matched.append((mask,target))
crit=Counter(mask.bit_count()-1 for mask in U)
assert len(matched)==88 and crit=={0:1,2:23}, (len(matched),crit)

# Verify all directed cover relations form a DAG after reversing matched covers.
matched_set=set(matched)
indeg={s:0 for s in F}; arrows=defaultdict(list); count=0
for upper in F:
    for v in range(16):
        bit=1<<v
        if not upper & bit: continue
        lower=upper ^ bit
        if lower not in F: continue
        src,dst = (lower,upper) if (lower,upper) in matched_set else (upper,lower)
        arrows[src].append(dst); indeg[dst]+=1; count+=1
assert count==496, count
queue=deque(s for s in F if not indeg[s]);seen=0
while queue:
    a=queue.popleft();seen+=1
    for b in arrows[a]:
        indeg[b]-=1
        if indeg[b]==0:queue.append(b)
assert seen==len(F), ('directed matching cycle',seen)

# All affine graph automorphisms: sixteen translations and the twelve
# invertible linear maps fixing the six-element neighbor set.
GL=[]
for a,b,c,d in product(range(4), repeat=4):
    if (a*d-b*c)%2 == 0: continue
    if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in D} == D:
        GL.append((a,b,c,d))
assert len(GL)==12
# A graph automorphism fixing zero is determined by its action on its six
# neighbors: they form a C6. Each other vertex has a distinct two-neighbor
# signature inside that C6, proving an upper bound of 16*12.
orig=I[(0,0)]
nb=[i for i in range(16) if N[orig]>>i & 1]
assert len(nb)==6
assert all(sum(bool(N[i]>>j & 1) for j in nb)==2 for i in nb)
# The six-neighbor induced 2-regular graph is connected, hence exactly C6.
queue_nb=deque([nb[0]]); reached={nb[0]}
while queue_nb:
    w=queue_nb.popleft()
    for z in nb:
        if z not in reached and (N[w]>>z&1):
            reached.add(z);queue_nb.append(z)
assert len(reached)==6
d2=[i for i in range(16) if i!=orig and i not in nb]
sigs=[tuple(j for j in nb if N[i]>>j&1) for i in d2]
assert len(d2)==9 and len(set(sigs))==9


def sign_perm_indices(indices):
    return -1 if sum(indices[i]>indices[j]
                     for i in range(len(indices)) for j in range(i+1,len(indices)))%2 else 1


def lefschetz(p):
    value=-1 # reduced Lefschetz number: ordinary Euler chain trace minus H_0.
    for mask in F:
        verts=[v for v in range(16) if mask>>v&1]
        image=[p[v] for v in verts]
        if set(verts)==set(image):
            positions={v:j for j,v in enumerate(verts)}
            parity=sign_perm_indices([positions[v] for v in image])
            value+=(-1)**(len(verts)-1)*parity
    return value

allchars=Counter();transchars=Counter();transgrid=[[0]*4 for _ in range(4)]
for a,b,c,d in GL:
    for u,v in product(range(4),repeat=2):
        p=[I[((a*x+b*y+u)%4,(c*x+d*y+v)%4)] for x,y in V]
        assert len(set(p))==16
        assert all((N[i]>>j & 1)==(N[p[i]]>>p[j] &1) for i in range(16) for j in range(16))
        value=lefschetz(p)
        allchars[value]+=1
        if (a,b,c,d)==(1,0,0,1):
            transchars[value]+=1
            transgrid[u][v]=value

assert allchars==Counter({-7:12,-3:4,-1:69,0:32,1:24,2:32,3:18,23:1}),allchars
assert transchars==Counter({23:1,3:6,-1:9}),transchars
assert sum(k*v for k,v in allchars.items())==0
assert sum(k*v for k,v in transchars.items())==32
assert transgrid==[[23,-1,-1,-1],[-1,-1,3,3],[-1,3,-1,3],[-1,3,3,-1]]

# Fourier inversion over the 16 one-dimensional complex characters of T.
# Integer result: sixteen multiplicities, all nonnegative, sum 23.
mult=[]
for a in range(4):
    row=[]
    for b in range(4):
        z=sum(transgrid[u][v] * (1j)**(-a*u-b*v)
              for u,v in product(range(4),repeat=2))/16
        assert abs(z.imag)<1e-8 and abs(z.real-round(z.real))<1e-8
        row.append(round(z.real))
    mult.append(row)
assert mult==[[2,1,1,1],[1,2,2,1],[1,2,1,2],[1,1,2,2]], mult
assert sum(map(sum,mult))==23

print('SHRIKHANDE_INDEPENDENCE_FULL_192_EQUIVARIANT_CHARACTER_OK')
print('faces',len(F),'matching',len(matched),'critical',dict(crit),'incidences',count)
print('automorphisms',sum(allchars.values()),'character frequencies',dict(sorted(allchars.items())))
print('translation multiplicities',mult,'translation-invariants',sum(k*v for k,v in transchars.items())//16)
print('full invariants',sum(k*v for k,v in allchars.items())//192)
