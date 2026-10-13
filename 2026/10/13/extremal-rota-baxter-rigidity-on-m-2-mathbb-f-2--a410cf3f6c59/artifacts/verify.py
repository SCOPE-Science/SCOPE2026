from collections import Counter

# M_2(F_2) is encoded by four bits in the ordered basis
# (E11,E12,E21,E22).  A linear endomorphism is a tuple of four
# such bit-vectors, namely its four basis images.
BASIS=(1,2,4,8)
ID=tuple(BASIS)
ZERO=(0,0,0,0)
ONE=1|8

def mul(a,b):
    A=[(a>>i)&1 for i in range(4)]
    B=[(b>>i)&1 for i in range(4)]
    C=[A[0]*B[0]^A[1]*B[2],
       A[0]*B[1]^A[1]*B[3],
       A[2]*B[0]^A[3]*B[2],
       A[2]*B[1]^A[3]*B[3]]
    return sum(c<<i for i,c in enumerate(C))

def apply(R,x):
    y=0
    for i in range(4):
        if (x>>i)&1:
            y ^= R[i]
    return y

def compose(A,B):
    return tuple(apply(A,B[j]) for j in range(4))

def add(A,B):
    return tuple(a^b for a,b in zip(A,B))

def rb_ok_basis(R,weight):
    for x in BASIS:
        rx=apply(R,x)
        for y in BASIS:
            ry=apply(R,y)
            lhs=mul(rx,ry)
            z=mul(rx,y)^mul(x,ry)^(mul(x,y) if weight else 0)
            if lhs != apply(R,z):
                return False
    return True

def rb_ok_all(R,weight):
    for x in range(16):
        rx=apply(R,x)
        for y in range(16):
            ry=apply(R,y)
            lhs=mul(rx,ry)
            z=mul(rx,y)^mul(x,ry)^(mul(x,y) if weight else 0)
            if lhs != apply(R,z):
                return False
    return True

def minimal_polynomial(R):
    powers=[ID]
    for d in range(1,5):
        powers.append(compose(R,powers[-1]))
        for mask in range(1<<d):
            s=powers[d]
            for i in range(d):
                if (mask>>i)&1:
                    s=add(s,powers[i])
            if s==ZERO:
                return d, mask|(1<<d)
    raise AssertionError('minimal polynomial not found')

def poly_name(bits):
    names={1:'1',2:'x',3:'x+1',4:'x^2',5:'x^2+1',6:'x^2+x',7:'x^2+x+1',
           8:'x^3',9:'x^3+1',10:'x^3+x',11:'x^3+x+1',12:'x^3+x^2',
           13:'x^3+x^2+1',14:'x^3+x^2+x',15:'x^3+x^2+x+1'}
    return names[bits]

def det(a):
    A=[(a>>i)&1 for i in range(4)]
    return A[0]*A[3]^A[1]*A[2]

def inv_element(a):
    for b in range(16):
        if mul(a,b)==ONE and mul(b,a)==ONE:
            return b
    raise AssertionError('not invertible')

def conjugation(P):
    Q=inv_element(P)
    return tuple(mul(mul(P,e),Q) for e in BASIS)

def inverse_linear(A):
    # enough for the six algebra automorphisms used below
    for B in AUT:
        if compose(A,B)==ID and compose(B,A)==ID:
            return B
    raise AssertionError('inverse not found')

def conjugate_operator(R,psi):
    return compose(inverse_linear(psi),compose(R,psi))

def transpose_element(x):
    a=[(x>>i)&1 for i in range(4)]
    return a[0]|(a[2]<<1)|(a[1]<<2)|(a[3]<<3)

TRANSPOSE=tuple(transpose_element(e) for e in BASIS)
def transpose_action(R):
    return compose(TRANSPOSE,compose(R,TRANSPOSE))

def phi(R):
    # in characteristic two at weight one, -R-id = R+id
    return add(R,ID)

def linear_rank(R):
    rows=[]
    for i in range(4):
        rows.append(sum((((R[j]>>i)&1)<<j) for j in range(4)))
    rank=0
    for col in range(4):
        pivot=next((k for k in range(rank,4) if (rows[k]>>col)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for k in range(4):
            if k!=rank and ((rows[k]>>col)&1): rows[k]^=rows[rank]
        rank+=1
    return rank

def all_algebra_automorphisms():
    out=[]
    for code in range(1<<16):
        T=tuple((code>>(4*j))&15 for j in range(4))
        if linear_rank(T)!=4 or apply(T,ONE)!=ONE:
            continue
        ok=True
        for x in BASIS:
            for y in BASIS:
                if apply(T,mul(x,y)) != mul(apply(T,x),apply(T,y)):
                    ok=False; break
            if not ok: break
        if ok: out.append(T)
    return out

# Build automorphisms in two independent ways.
GL2=[a for a in range(16) if det(a)]
AUT=[]
for P in GL2:
    c=conjugation(P)
    if c not in AUT: AUT.append(c)
AUT2=all_algebra_automorphisms()
assert set(AUT)==set(AUT2) and len(AUT)==6
assert compose(TRANSPOSE,TRANSPOSE)==ID

def aut_orbits(S):
    S=set(S); seen=set(); out=[]
    for r in sorted(S):
        if r in seen: continue
        o={conjugate_operator(r,a) for a in AUT}
        assert o<=S
        seen|=o; out.append(o)
    assert seen==S
    return out

def generated_orbits(S,weight,use_transpose,use_phi):
    S=set(S); seen=set(); out=[]
    for seed in sorted(S):
        if seed in seen: continue
        o={seed}; stack=[seed]
        while stack:
            r=stack.pop()
            nxt=[conjugate_operator(r,a) for a in AUT]
            if use_transpose: nxt.append(transpose_action(r))
            if use_phi and weight==1: nxt.append(phi(r))
            for q in nxt:
                assert q in S
                if q not in o:
                    o.add(q); stack.append(q)
        seen|=o; out.append(o)
    assert seen==S
    return out

solutions={}
for w in (0,1):
    ss=[]
    for code in range(1<<16):
        R=tuple((code>>(4*j))&15 for j in range(4))
        if rb_ok_basis(R,w):
            assert rb_ok_all(R,w)  # independent all-element recheck
            ss.append(R)
    solutions[w]=ss

assert len(solutions[0])==28
assert len(solutions[1])==110
assert Counter(minimal_polynomial(R)[0] for R in solutions[0])==Counter({1:1,2:21,3:6})
assert Counter(minimal_polynomial(R)[0] for R in solutions[1])==Counter({1:2,2:84,3:24})

ext={w:[R for R in solutions[w] if minimal_polynomial(R)[0]==3] for w in (0,1)}
assert Counter(poly_name(minimal_polynomial(R)[1]) for R in ext[0])==Counter({'x^3':6})
assert Counter(poly_name(minimal_polynomial(R)[1]) for R in ext[1])==Counter({'x^3+x^2':12,'x^3+x':12})

au0=aut_orbits(ext[0]); au1=aut_orbits(ext[1])
assert sorted(map(len,au0))==[3,3]
assert sorted(map(len,au1))==[6,6,6,6]
at0=generated_orbits(ext[0],0,True,False)
at1=generated_orbits(ext[1],1,True,False)
assert list(map(len,at0))==[6]
assert sorted(map(len,at1))==[12,12]
full0=generated_orbits(ext[0],0,True,True)
full1=generated_orbits(ext[1],1,True,True)
assert list(map(len,full0))==[6]
assert list(map(len,full1))==[24]

# Integral canonical operators from Gubarev, reduced to F_2 for n=2.
B0=(2,0,1,0)  # E11->E12, E12->0, E21->E11, E22->0
B1=(8,2,0,0)  # E11->E22, E12->E12, E21->0, E22->0
assert B0 in ext[0] and B1 in ext[1]

# Transpose exchanges the two weight-zero Aut-orbits.  For weight one,
# transpose merges the four Aut-orbits in pairs, then phi merges those pairs.
def orbit_index(r,orbits):
    return next(i for i,o in enumerate(orbits) if r in o)
assert orbit_index(transpose_action(min(au0[0])),au0) != 0
pairs_tau={tuple(sorted((i,orbit_index(transpose_action(min(o)),au1)))) for i,o in enumerate(au1)}
assert len(pairs_tau)==2
# At the Aut+transpose level, phi exchanges the two 12-element blocks.
assert len(at1)==2
assert phi(min(at1[0])) in at1[1]

print('VERIFY_OK')
print('automorphisms',len(AUT))
print('weight0_total',len(solutions[0]),'degree_distribution',dict(sorted(Counter(minimal_polynomial(R)[0] for R in solutions[0]).items())))
print('weight1_total',len(solutions[1]),'degree_distribution',dict(sorted(Counter(minimal_polynomial(R)[0] for R in solutions[1]).items())))
print('weight0_extremal',len(ext[0]),'aut_orbits',sorted(map(len,au0)),'aut_plus_transpose',list(map(len,at0)),'full',list(map(len,full0)))
print('weight1_extremal',len(ext[1]),'aut_orbits',sorted(map(len,au1)),'aut_plus_transpose',sorted(map(len,at1)),'full',list(map(len,full1)))
print('weight0_extremal_minpoly',dict(Counter(poly_name(minimal_polynomial(R)[1]) for R in ext[0])))
print('weight1_extremal_minpoly',dict(Counter(poly_name(minimal_polynomial(R)[1]) for R in ext[1])))
print('B0',B0,'B1',B1)
