import sympy as s

pi=s.pi
alpha=pi/10
c=s.cos(pi/5)
sn=s.sin(pi/5)
a=s.tan(alpha)
R=s.sec(alpha)
t=s.symbols("t", real=True)

# Exact sector endpoint identities.
assert s.simplify(R-a-s.tan(2*alpha))==0
assert s.simplify(R+a-s.tan(3*alpha))==0

# Ten regular-decagon normals; each edge midpoint normal has perpendicular
# direction equal to a vertex direction because N=10=4*2+2.
for j in range(10):
    normal_angle=s.Rational(j,5)*pi
    perp=s.simplify(normal_angle+pi/2)
    # Vertex directions are odd multiples of alpha modulo pi/5.
    q=s.simplify(perp/alpha)
    assert int(q)%2==1

# Canonical family.  n_1 and n_9 are active throughout because their
# dominance differences are affine in t and nonnegative at both endpoints.
xp=s.Matrix([1,t])
yp=s.Matrix([0,R])
normals=[
    s.Matrix([s.cos(s.Rational(j,5)*pi),s.sin(s.Rational(j,5)*pi)])
    for j in range(10)
]
plus=xp+yp
minus=xp-yp
A=s.simplify(normals[1].dot(plus))
B=s.simplify(normals[9].dot(minus))

for j,nj in enumerate(normals):
    dplus=s.expand_trig(s.simplify(A-nj.dot(plus)))
    dminus=s.expand_trig(s.simplify(B-nj.dot(minus)))
    for tt in (-a,a):
        vp=s.N(dplus.subs(t,tt),50)
        vm=s.N(dminus.subs(t,tt),50)
        assert vp >= -s.Float("1e-45"), (j,"plus",vp)
        assert vm >= -s.Float("1e-45"), (j,"minus",vm)

F=s.simplify((A**2-B**2)/4)
expected=s.simplify((c+sn*R)*sn*t)
assert s.simplify(s.trigsimp(s.expand_trig(F-expected)))==0
slope=s.N(s.diff(F,t),50)
assert slope>0

Aend=s.trigsimp(A.subs(t,a))
Bend=s.trigsimp(B.subs(t,a))
phi=(1+s.sqrt(5))/2
assert s.simplify(s.expand_trig(Aend)-phi)==0
assert s.simplify(s.expand_trig(Bend)-(s.sqrt(5)-1))==0

C=s.simplify((phi**2-(s.sqrt(5)-1)**2)/4)
target=(5*s.sqrt(5)-9)/8
assert s.simplify(C-target)==0
assert s.simplify(F.subs(t,a)-target)==0

print("VERIFY_OK facets=10 canonical_birkhoff_family=1 CB=(5sqrt5-9)/8")
