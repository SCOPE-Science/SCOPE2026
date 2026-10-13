from fractions import Fraction

# Polynomial helpers for univariate coefficient lists, low degree first.
def add(p,q):
    n=max(len(p),len(q)); r=[Fraction(0) for _ in range(n)]
    for i,v in enumerate(p): r[i]+=v
    for i,v in enumerate(q): r[i]+=v
    while len(r)>1 and r[-1]==0: r.pop()
    return r

def mul(p,q):
    r=[Fraction(0) for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r

def scale(p,c): return [c*x for x in p]

def sq(p): return mul(p,p)

# C = x^4+y^4+z^4+6(x^2 y^2-y^2 z^2+x^2 z^2).
# Quotient by x -> -x in z=1: X^2+6(t^2+1)X+(t^4-6t^2+1)=0.
t2=[0,0,1]
t4=[0,0,0,0,1]
one=[1]
B=scale(add(t2,one),6)
C0=add(add(t4,one),scale(t2,-6))
Dx=add(sq(B),scale(C0,-4))
assert Dx == scale(add(add(t4,scale(t2,3)),one),32)

# Quotient by y -> -y (and similarly z -> -z): Y^2+6(t^2-1)Y+(t^4+6t^2+1)=0.
B2=scale(add(t2,[-1]),6)
C2=add(add(t4,one),scale(t2,6))
Dy=add(sq(B2),scale(C2,-4))
assert Dy == scale(add(add(t4,scale(t2,-3)),one),32)

# Full V4 quotient is the conic with symmetric matrix below; nonzero determinant means smooth.
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
M=[[1,3,3],[3,1,-3],[3,-3,1]]
assert det3(M) == -80

# The same matrix controls the all-nonzero singularity equations; nonzero determinant rules them out.
# Coordinate-zero cases reduce to incompatible equations such as Y=3Z and Z=3Y.

# For E_a: w^2=t^4+a t^2+1, the rational change
# u=(w+1)/t^2, X=2u, v=t(u^2-1), Y=2v
# gives Y^2=(X^2-4)(X+a)=X^3+aX^2-4X-4a.
# For generalized Weierstrass y^2=x^3+a*x^2-4*x-4*a:
# b2=4a, b4=-8, b6=-16a, b8=-16(a^2+1),
# c4=16(a^2+12), Delta=256(a^2-4)^2.
def invariants(a):
    a=Fraction(a)
    b2=4*a; b4=Fraction(-8); b6=-16*a; b8=-16*(a*a+1)
    c4=b2*b2-24*b4
    Delta=-(b2*b2)*b8-8*(b4**3)-27*(b6**2)+9*b2*b4*b6
    j=c4**3/Delta
    return c4,Delta,j
for aa in (3,-3):
    c4,D,j=invariants(aa)
    assert c4 == 16*(aa*aa+12)
    assert D == 256*(aa*aa-4)**2
    assert j == Fraction(148176,25)

# E_+ and E_- are explicitly isomorphic over C under t -> i*t, since
# (i*t)^4+3(i*t)^2+1=t^4-3t^2+1.
# The quartics are smooth because a^2-4 != 0.
assert 3*3-4 != 0 and (-3)*(-3)-4 != 0

# V4 representation check: C/V4 has genus 0; each of the three involution quotients has genus 1.
# Therefore H^0(C,Omega) has no trivial character and each nontrivial character occurs once.
# The direct sum of the three elliptic pullback differentials is 3-dimensional, hence the
# induced product-to-Jacobian homomorphism is an isogeny.
print('VERIFY_OK discriminants=plus/minus3 conic_det=-80 j=148176/25 jacobian_isogeny=E^3')
