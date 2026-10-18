"""Exact rational chain and symmetry-character checks for folded-five-cube neighborhood topology.
Run: python3 verify.py (requires sympy)."""
from itertools import combinations,permutations
from collections import Counter
from sympy import SparseMatrix

NCOORD=5
ALL=(1<<NCOORD)-1

def norm(x):
    return x ^ (ALL if x&16 else 0)

def move(x,p):
    y=0
    for i in range(5):
        if x&(1<<i):y ^= 1<<p[i]
    return norm(y)

def sgn(p):
    return -1 if sum(x>y for i,x in enumerate(p) for y in p[i+1:])%2 else 1

def cycle_type(p):
    seen=set(); parts=[]
    for i in range(len(p)):
        if i not in seen:
            j=i;length=0
            while j not in seen:
                seen.add(j);length+=1;j=p[j]
            parts.append(length)
    return tuple(sorted(parts,reverse=True))

V=list(range(16)); ix={x:i for i,x in enumerate(V)}
N=[sorted({ix[norm(x^(1<<i))] for i in range(5)}) for x in V]
assert all(len(row)==5 for row in N) and len(set(map(tuple,N)))==16
faces=[set() for _ in range(5)]
for row in N:
    for k in range(1,6):
        faces[k-1].update(combinations(row,k))
faces=[sorted(s) for s in faces]
assert tuple(map(len,faces))==(16,80,160,80,16)

D=[]
for k in range(1,5):
    look={s:i for i,s in enumerate(faces[k-1])}
    data={}
    for j,s in enumerate(faces[k]):
        for i in range(k+1):
            data[look[s[:i]+s[i+1:]],j]=(-1)**i
    D.append(SparseMatrix(len(faces[k-1]),len(faces[k]),data))
for i in range(3):
    assert D[i]*D[i+1]==SparseMatrix(D[i].rows,D[i+1].cols,{})
ranks=[x.rank() for x in D]  # exact rational ranks, not modular inference
assert ranks==[15,65,64,16],ranks
assert tuple([16-ranks[0], 80-ranks[0]-ranks[1],160-ranks[1]-ranks[2],80-ranks[2]-ranks[3],16-ranks[3]])==(1,0,31,0,0)

def oriented_trace(f,action):
    result=0
    for simplex in f:
        im=[action[j] for j in simplex]
        if tuple(sorted(im))==simplex:
            result+=(-1)**(sum(x>y for i,x in enumerate(im) for y in im[i+1:])%2)
    return result

def equivariant_homology_trace(t,p):
    action=[ix[norm(t^move(x,p))] for x in V]
    assert len(set(action))==16
    # H2 only reduced homology. Subtract augmented H0 trace = 1.
    return sum((-1)**k*oriented_trace(f,action) for k,f in enumerate(faces))-1

perms=list(permutations(range(5)))
identity=tuple(range(5))
trace={p:[equivariant_homology_trace(t,p) for t in V] for p in perms}
assert len(trace)==120 and sum(len(row) for row in trace.values())==1920
assert Counter(v for row in trace.values() for v in row)==Counter({1:944,-1:825,-5:80,3:60,7:10,31:1})

def even_lift(y):
    return y if y.bit_count()%2==0 else y^ALL

def fourier(p,y):
    w=even_lift(y)
    num=sum(a*(-1)**((t&w).bit_count()%2) for t,a in enumerate(trace[p]))
    assert num%16==0,(p,y,num)
    return num//16

mult={y:fourier(identity,y) for y in V}
assert mult[0]==6
assert all(mult[y]==(1 if even_lift(y).bit_count()==2 else 3) for y in V if y)
assert sum(mult.values())==31

# Translation-trivial piece has S5 character of exterior square of the standard module.
for p in perms:
    fixed=sum(p[i]==i for i in range(5))
    p2=tuple(p[p[i]] for i in range(5))
    fixed2=sum(p2[i]==i for i in range(5))
    standard=fixed-1
    expected=(standard*standard-(fixed2-1))//2
    assert fourier(p,0)==expected,('S5',p)

# Weight-two little-group character on the stabilizer S_{2} x S_{3}.
y2=3
stab2=[p for p in perms if move(y2,p)==y2]
assert len(stab2)==12
for p in stab2:
    other=tuple(p[i]-2 for i in (2,3,4))
    assert fourier(p,y2)==sgn(other),('weight2',p)

# Weight-four little-group character on S4: sgn times the 3-d standard rep.
y4=15
stab4=[p for p in perms if move(y4,p)==y4]
assert len(stab4)==24
for p in stab4:
    restrict=p[:4]
    expected=sgn(restrict)*(sum(p[i]==i for i in range(4))-1)
    assert fourier(p,y4)==expected,('weight4',p)

# Every remaining nonzero character block is conjugate to a checked representative;
# verify their stabilizer characters using an explicit transporter.
for y in V:
    if y in (0,y2,y4):continue
    target=y2 if even_lift(y).bit_count()==2 else y4
    transporter=next(p for p in perms if move(target,p)==y)
    inverse=tuple(transporter.index(i) for i in range(5))
    for p in perms:
        if move(y,p)!=y:continue
        # h = transporter^-1 * p * transporter
        conj=tuple(inverse[p[transporter[i]]] for i in range(5))
        assert fourier(p,y)==fourier(conj,target),('transport',y,p)
print('VERIFY_OK 16_VERTICES 352_FACES BOUNDARY_RANKS_15_65_64_16')
print('AFFINE_AUTOMORPHISMS_1920 HOMOLOGY_31 IRREDUCIBLES_6_10_15')
