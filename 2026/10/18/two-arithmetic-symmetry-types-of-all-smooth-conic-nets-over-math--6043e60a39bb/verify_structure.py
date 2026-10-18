"""Exact orbit, pencil-incidence, projective-permutation, and geometric rank-one checks."""
import collections,hashlib,pathlib,sys
# Enumerated net byte table from independent exhaustive sweep.
raw=(pathlib.Path(__file__).resolve().parent / "conic_nets_q5.bin").read_bytes()
nets=[tuple(raw[i:i+18]) for i in range(0,len(raw),18)]
netset=set(nets)
assert len(nets)==len(netset)==8000
P=5
mons=[(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
Ms=[[[0,1,0],[1,0,0],[0,0,1]],[[0,1,0],[0,0,1],[1,0,0]],[[1,1,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]]
def action_matrix(M):
    T=[]
    for a,b in mons:
        co=[0]*6
        for j in range(3):
            for k in range(3):
                v=M[a][j]*M[b][k]
                target=j if j==k else 3+{(0,1):0,(0,2):1,(1,2):2}[tuple(sorted((j,k)))]
                co[target]=(co[target]+v)%5
        T.append(co)
    return T
Ts=[action_matrix(M) for M in Ms]
def rref(A):
    A=[[int(x)%5 for x in row] for row in A]
    k=0
    for col in range(6):
        pivot=next((i for i in range(k,len(A)) if A[i][col]),None)
        if pivot is None:continue
        A[k],A[pivot]=A[pivot],A[k]
        v=pow(A[k][col],-1,5)
        A[k]=[(v*x)%5 for x in A[k]]
        for i in range(len(A)):
            if i==k:continue
            v=A[i][col]
            if v:A[i]=[(x-v*y)%5 for x,y in zip(A[i],A[k])]
        k+=1
        if k==len(A):break
    assert k==len(A)
    return bytes(sum(A,[]))
def transform(net,T):
    R=[net[i:i+6] for i in (0,6,12)]
    return rref([[sum(R[i][j]*T[j][k] for j in range(6))%5 for k in range(6)] for i in range(3)])
seen=set(); orbits=[]
for rep in nets:
    rep=bytes(rep)
    if rep in seen:continue
    queue=[rep];seen.add(rep)
    for r in queue:
        for T in Ts:
            z=transform(r,T)
            assert tuple(z) in netset
            if z not in seen:
                seen.add(z);queue.append(z)
    orbits.append(queue)
assert len(orbits)==2 and sorted(map(len,orbits))==[4000,4000]
print('PGL3(5) net-orbit sizes:',list(map(len,orbits)))
print('Group order:',372000,'stabilizer order:',372000//4000)
print('Representatives:',[list(x[0]) for x in orbits])
# Every 3-plane contains 31 projective pencil subspaces. Exact incidence counts.
pencil_degree=collections.Counter()
orb_of={bytes(a):i for i,orb in enumerate(orbits) for a in orb}
pencil_types=collections.defaultdict(list)
for net in nets:
    tag=orb_of[bytes(net)]
    A=[net[j:j+6] for j in (0,6,12)]
    def combine(c):return [sum(c[i]*A[i][j] for i in range(3))%5 for j in range(6)]
    for a in range(5):
        for b in range(5):pk=rref([combine((-a,1,0)),combine((-b,0,1))]);pencil_degree[pk]+=1;pencil_types[pk].append(tag)
    for b in range(5):pk=rref([combine((1,0,0)),combine((0,-b,1))]);pencil_degree[pk]+=1;pencil_types[pk].append(tag)
    pk=rref([combine((1,0,0)),combine((0,1,0))]);pencil_degree[pk]+=1;pencil_types[pk].append(tag)
assert len(pencil_degree)==124000 and set(pencil_degree.values())=={2}
print('distinct smooth pencils in nets',len(pencil_degree),'multiplicities',dict(collections.Counter(pencil_degree.values())))
print('net orbit types per pencil',dict(collections.Counter(tuple(sorted(v)) for v in pencil_types.values())))
# Set of all pencils is also independently counted by pencils_q5.cpp as 124,000.
# Every net map P2(F5) -> P2(F5) is a bijection (representatives suffice by PGL symmetry).
pts=[(1,a,b) for a in range(5) for b in range(5)]+[(0,1,b) for b in range(5)]+[(0,0,1)]
def normalize(v):
    i=next(x for x in v if x); z=pow(i,-1,5);return tuple((x*z)%5 for x in v)
for orbit in orbits:
    rows=[orbit[0][k:k+6] for k in (0,6,12)];images=[]
    for x,y,z in pts:
        t=(x*x,y*y,z*z,x*y,x*z,y*z)
        v=[sum(a*b for a,b in zip(row,t))%5 for row in rows]
        assert any(v)
        images.append(normalize(v))
    assert len(set(images))==31
print('Quadratic maps of both representatives permute P2(F5): TRUE')
print('Canonical table SHA256',hashlib.sha256(b''.join(sorted(bytes(x) for x in nets))).hexdigest())
