"""Exhaustive exact generation-profile certificate for sl_3(F_2).

Run: python3 verify.py. Uses only Python's standard library.
Each nine-bit integer encodes a 3 by 3 binary matrix, in row-major order.
"""
from collections import Counter


def mm(a,b):
    """Ordinary 3 by 3 matrix product over F_2."""
    out=0
    for i in range(3):
        for j in range(3):
            x=0
            for k in range(3):
                x ^= ((a>>(3*i+k)) & 1) & ((b>>(3*k+j)) & 1)
            out |= x << (3*i+j)
    return out

L=tuple(a for a in range(512) if
        (((a>>0)&1)^((a>>4)&1)^((a>>8)&1)) == 0)
assert len(L)==256 and 0 in L
S=set(L)
comm={(a,b):mm(a,b)^mm(b,a) for a in L for b in L}
assert all(c in S for c in comm.values())
assert all(comm[a,b]==comm[b,a] for a in L for b in L)
assert all(comm[a,a]==0 for a in L)


def push(basis,v):
    """Insert a vector into a GF(2) echelon basis; return if rank grows."""
    w=v
    while w:
        k=w.bit_length()-1
        if k in basis:
            w ^= basis[k]
        else:
            basis[k]=w
            return True
    return False


def bracket_closure(a,b):
    """Algorithm I: close a generating basis under all pairwise brackets."""
    basis={}; gener=[]
    for z in (a,b):
        if push(basis,z): gener.append(z)
    i=0
    while i<len(gener):
        for j in range(i):
            z=comm[gener[i],gener[j]]
            if push(basis,z):
                gener.append(z)
        i+=1
    return len(gener)


def adjoint_closure(a,b):
    """Algorithm II: smallest subspace stable under ad(a) and ad(b).
    Jacobi makes this a Lie subalgebra, and it contains the generators.
    Independent of Algorithm I's basis-pair closure and update order.
    """
    vectors=[]; pivot={}
    for z in (a,b):
        if push(pivot,z): vectors.append(z)
    todo=0
    while todo<len(vectors):
        v=vectors[todo]
        for z in (a,b):
            w=comm[z,v]
            if push(pivot,w):vectors.append(w)
        todo+=1
    return len(vectors)

hist1=Counter(); hist2=Counter()
for a in L:
    for b in L:
        hist1[bracket_closure(a,b)] += 1
        hist2[adjoint_closure(a,b)] += 1
assert hist1==hist2
expected={0:1,1:765,2:3618,3:7392,4:20160,5:20160,8:13440}
assert dict(hist1)==expected, (hist1,expected)
assert sum(hist1.values())==256**2

# A genuine six-dimensional Lie subalgebra exists: the stabilizer of
# the first coordinate line, i.e. matrices with entries (1,0)=(2,0)=0.
parabolic=[a for a in L if not ((a>>3)&1) and not ((a>>6)&1)]
assert len(parabolic)==64
parabolic_set=set(parabolic)
assert all(comm[a,b] in parabolic_set for a in parabolic for b in parabolic)
assert all(bracket_closure(a,b)<=5 for a in parabolic for b in parabolic)

# Direct pair witness generates all eight dimensions.
assert bracket_closure(10,70)==8 and adjoint_closure(10,70)==8

# All 3 by 3 invertible matrices, tested by their action on F_2^3.
def act(g,v):
    w=0
    for i in range(3):
        bit=0
        for j in range(3):bit^=((g>>(3*i+j))&1)&((v>>j)&1)
        w |= bit<<i
    return w
GL=[g for g in range(512) if all(act(g,v) for v in range(1,8))]
assert len(GL)==168
# The centralizer of all E_ij (i != j) in GL_3(F2) is identity.
E=[1<<(3*i+j) for i in range(3) for j in range(3) if i!=j]
assert sum(all(mm(g,e)==mm(e,g) for e in E) for g in GL)==1
assert expected[8] % len(GL)==0
assert expected[8]//len(GL)==80

print('VERIFY_OK: 65536 ordered pairs; closure algorithms agree')
print('dimension profile:', dict(sorted(hist1.items())))
print('generating pairs:',hist1[8],'generating probability:',f'{hist1[8]}/65536')
print('GL3(F2) order:',len(GL),'free-conjugacy orbits of generating pairs:',80)
print('six-dimensional parabolic verified; generator masks 10,70')
