import sympy as sp
from itertools import product

# Basis e1=(1,0), e2=(0,1), column vectors.
e1=sp.Matrix([1,0]); e2=sp.Matrix([0,1]); basis=[e1,e2]

def bop(table,x,y):
    out=sp.zeros(2,1)
    for i in range(2):
        for j in range(2):
            out += x[i]*y[j]*table.get((i,j), sp.zeros(2,1))
    return sp.simplify(out)

# Mainellis Trias_2^33, the class cited by the 2023 source:
# e1⊢e1=e1, e1⊢e2=e2,
# e1⊣e1=e1, e2⊣e1=e2,
# e1⊥e1=e1, e1⊥e2=e2.
vd={(0,0):e1,(0,1):e2}
da={(0,0):e1,(1,0):e2}
pe={(0,0):e1,(0,1):e2}
V=lambda x,y:bop(vd,x,y)
D=lambda x,y:bop(da,x,y)
P=lambda x,y:bop(pe,x,y)

# Standard 11 triassociative identities.
tri_identities=[
 lambda x,y,z:(V(V(x,y),z),V(x,V(y,z))),
 lambda x,y,z:(D(D(x,y),z),D(x,D(y,z))),
 lambda x,y,z:(V(D(x,y),z),V(x,V(y,z))),
 lambda x,y,z:(D(D(x,y),z),D(x,V(y,z))),
 lambda x,y,z:(D(V(x,y),z),V(x,D(y,z))),
 lambda x,y,z:(V(P(x,y),z),V(x,V(y,z))),
 lambda x,y,z:(D(D(x,y),z),D(x,P(y,z))),
 lambda x,y,z:(P(V(x,y),z),V(x,P(y,z))),
 lambda x,y,z:(D(P(x,y),z),P(x,D(y,z))),
 lambda x,y,z:(P(D(x,y),z),P(x,V(y,z))),
 lambda x,y,z:(P(P(x,y),z),P(x,P(y,z))),
]
for f in tri_identities:
    for x,y,z in product(basis, repeat=3):
        l,r=f(x,y,z)
        assert sp.simplify(l-r)==sp.zeros(2,1)

# If Example 4.9's first display is read literally (the left product e1⊣e1 is absent),
# it is not a trialgebra: D1 at (e1,e1,e1) gives 0=e1.
da_literal={(1,0):e2}
Dl=lambda x,y:bop(da_literal,x,y)
literal_left=V(Dl(e1,e1),e1)
literal_right=V(e1,V(e1,e1))
assert literal_left==sp.zeros(2,1) and literal_right==e1

# Diagonal twist alpha(e1)=a e1, alpha(e2)=b e2.
a,b=sp.symbols("a b")
A=sp.diag(a,b)
ops=[V,D,P]
endo_diffs=[]
for op in ops:
    for x,y in product(basis, repeat=2):
        diff=sp.simplify(A*op(x,y)-op(A*x,A*y))
        endo_diffs.extend([sp.factor(w) for w in diff if w!=0])
# Nonzero equations reduce exactly to a(1-a)=0 and b(1-a)=0.
factors={sp.factor(w) for w in endo_diffs}
assert -a*(a-1) in factors and -b*(a-1) in factors and len(factors)==2
G=sp.groebner([a*(a-1), b*(a-1)], a,b)
for w in endo_diffs:
    assert G.reduce(sp.expand(w))[1]==0

# Conversely the two branches are exact over every field:
# (a,b)=(0,0), or a=1 with b arbitrary.
def twisted(op,A):
    return lambda x,y: sp.simplify(A*op(x,y))

def check_hom(A):
    VV,DD,PP=[twisted(op,A) for op in (V,D,P)]
    al=lambda x: A*x
    # Hom-dialgebra 5 identities + middle Hom-associativity + five mixed identities.
    ids=[
      lambda x,y,z:(VV(VV(x,y),al(z)),VV(al(x),VV(y,z))),
      lambda x,y,z:(DD(DD(x,y),al(z)),DD(al(x),DD(y,z))),
      lambda x,y,z:(VV(DD(x,y),al(z)),VV(al(x),VV(y,z))),
      lambda x,y,z:(DD(DD(x,y),al(z)),DD(al(x),VV(y,z))),
      lambda x,y,z:(DD(VV(x,y),al(z)),VV(al(x),DD(y,z))),
      lambda x,y,z:(PP(PP(x,y),al(z)),PP(al(x),PP(y,z))),
      lambda x,y,z:(DD(DD(x,y),al(z)),DD(al(x),PP(y,z))),
      lambda x,y,z:(DD(PP(x,y),al(z)),PP(al(x),DD(y,z))),
      lambda x,y,z:(PP(DD(x,y),al(z)),PP(al(x),VV(y,z))),
      lambda x,y,z:(PP(VV(x,y),al(z)),VV(al(x),PP(y,z))),
      lambda x,y,z:(VV(PP(x,y),al(z)),VV(al(x),VV(y,z))),
    ]
    for f in ids:
        for x,y,z in product(basis,repeat=3):
            l,r=f(x,y,z)
            if sp.simplify(l-r)!=sp.zeros(2,1):
                return False
    # multiplicativity for all three products
    for op in (VV,DD,PP):
        for x,y in product(basis,repeat=2):
            if sp.simplify(al(op(x,y))-op(al(x),al(y)))!=sp.zeros(2,1):
                return False
    return True

t=sp.symbols("t")
assert check_hom(sp.diag(1,t))
assert check_hom(sp.zeros(2))
# Invalid advertised arbitrary parameter: (a,b)=(2,1).
A_bad=sp.diag(2,1)
assert A_bad*V(e1,e1) != V(A_bad*e1,A_bad*e1)

# Theorem 4.21 descendants for the corrected trialgebra.
A_good=sp.diag(1,t)
VV,DD,PP=[twisted(op,A_good) for op in (V,D,P)]
curly=lambda x,y: sp.simplify(VV(x,y)-DD(y,x))
square=lambda x,y: sp.simplify(PP(x,y)-PP(y,x))
assert all(curly(x,y)==sp.zeros(2,1) for x,y in product(basis,repeat=2))
assert square(e1,e2)==sp.Matrix([0,t])
assert square(e2,e1)==sp.Matrix([0,-t])
assert square(e1,e1)==sp.zeros(2,1) and square(e2,e2)==sp.zeros(2,1)

# Zero branch has zero descendants.
A0=sp.zeros(2)
VV0,DD0,PP0=[twisted(op,A0) for op in (V,D,P)]
assert all(VV0(x,y)-DD0(y,x)==sp.zeros(2,1) for x,y in product(basis,repeat=2))
assert all(PP0(x,y)-PP0(y,x)==sp.zeros(2,1) for x,y in product(basis,repeat=2))

# Finite-field replay: q+1 diagonal endomorphism twists.
for q in (3,5,7,11):
    good=[]
    for aa in range(q):
        for bb in range(q):
            if (aa*(aa-1))%q==0 and (bb*(aa-1))%q==0:
                good.append((aa,bb))
    assert len(good)==q+1
    assert set(good)=={(0,0)}|{(1,bb) for bb in range(q)}
    print({"q":q,"valid_diagonal_twists":len(good),"nonzero_yau_line":q})

print("VERIFY_OK")
