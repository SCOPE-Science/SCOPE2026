"""Exact F_5 extraction of the genus-four complete-intersection Hasse--Witt matrix.
Run: python3 verify_canonical.py. No external packages.
"""
from itertools import permutations

P=5

def add(a,b):
    c=dict(a)
    for m,v in b.items():
        c[m]=(c.get(m,0)+v)%P
        if not c[m]: del c[m]
    return c

def mul(a,b):
    c={}
    for m,x in a.items():
        for n,y in b.items():
            k=tuple(i+j for i,j in zip(m,n))
            c[k]=(c.get(k,0)+x*y)%P
    return {m:v for m,v in c.items() if v}

def mon(exps,c=1):return {tuple(exps):c%P}

def pol(a):return {i:v for i,v in enumerate(a) if v%P}

def padd(a,b):
    out=dict(a)
    for i,v in b.items():out[i]=(out.get(i,0)+v)%P
    return {i:v for i,v in out.items() if v}

def pmul(a,b):
    c={}
    for i,v in a.items():
        for j,w in b.items():c[i+j]=(c.get(i+j,0)+v*w)%P
    return {i:v for i,v in c.items() if v}

# Monomial order: X,Y,Z,W,lambda. Q=XW-YZ and G=sum cubes+lambda XZW.
Q=add(mon((1,0,0,1,0)),mon((0,1,1,0,0),4))
G={}
for i in range(4):
    m=[0]*5;m[i]=3;G=add(G,mon(m))
G=add(G,mon((1,0,1,1,1)))
R=mul(Q,G)
F=mon((0,0,0,0,0))
for _ in range(4):F=mul(F,R)

def entry(i,j):
    # Kudo--Harashita Hasse--Witt coefficient extraction (i,j) for K=O_C(1).
    vi=[1]*4; vj=[1]*4;vi[i]=2;vj[j]=2
    ex=tuple(5*vj[k]-vi[k] for k in range(4))
    return {m[4]:c for m,c in F.items() if m[:4]==ex}

H=[[entry(i,j) for j in range(4)] for i in range(4)]
z={};one=pol([1]); l2=pol([0,0,1]); l4_plus_l=pol([0,1,0,0,1]);one_minus_l3=pol([1,0,0,4])
expected=[[z,z,z,one],[z,l2,one_minus_l3,z],[z,one,l4_plus_l,z],[one,z,z,z]]
assert H==expected,(H,expected)

def determinant(mat):
    value={}
    for perm in permutations(range(4)):
        coeff=1
        for i in range(4):
            for j in range(i+1,4):
                if perm[i]>perm[j]:coeff=-coeff
        term=pol([coeff%5])
        for i in range(4):term=pmul(term,mat[i][perm[i]])
        value=padd(value,term)
    return value
D=pol([4,0,0,2,0,0,1])
assert determinant(H)=={i:(-v)%5 for i,v in D.items()}
print('CANONICAL_HW_OK; terms=',len(F),'H=',H,'det=-(',D,')')
