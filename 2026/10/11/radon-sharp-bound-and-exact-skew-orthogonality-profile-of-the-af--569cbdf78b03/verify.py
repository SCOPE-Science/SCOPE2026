from fractions import Fraction

# N(s,t)=max(|s|,|t|,|s-t|).
def N(v):
    s,t=v
    return max(abs(s),abs(t),abs(s-t))

# Signed facet coefficient vectors.
facets=[
    (1,0), (0,1), (1,-1),
    (-1,0), (0,-1), (-1,1),
]
verts=[
    (1,0),(1,1),(0,1),
    (-1,0),(-1,-1),(0,-1),
]

def dot(f,v):
    return f[0]*v[0]+f[1]*v[1]

# Every listed vertex is unit and each facet has support value 1.
for v in verts:
    assert N(v)==1
for f in facets:
    assert max(dot(f,v) for v in verts)==1

# R(s,t)=(t,t-s), S(s,t)=(t,s) preserve the norm and permute vertices/facets.
def R(v):
    s,t=v
    return (t,t-s)
def S(v):
    s,t=v
    return (t,s)
assert {R(v) for v in verts}==set(verts)
assert {S(v) for v in verts}==set(verts)
for s in range(-3,4):
    for t in range(-3,4):
        assert N(R((s,t)))==N((s,t))
        assert N(S((s,t)))==N((s,t))

# Canonical interior-edge certificate.
for u in [Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(5,6)]:
    x=(Fraction(1),u)
    yp=(Fraction(0),Fraction(1))
    ym=(Fraction(0),Fraction(-1))
    assert N(x)==N(yp)==N(ym)==1

    # g=t-u s norms yp and annihilates x.
    g=(-u,Fraction(1))
    assert dot(g,yp)==1
    assert dot(g,x)==0
    # h=u s-t norms ym and annihilates x.
    h=(u,Fraction(-1))
    assert dot(h,ym)==1
    assert dot(h,x)==0

# Canonical vertex family.
x=(Fraction(1),Fraction(0))
for v in [Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(1)]:
    y=(v,Fraction(1))
    assert N(y)==1
    # f=s-vt is a convex combination (1-v)s + v(s-t), norms x, kills y.
    f=(Fraction(1),-v)
    assert dot(f,x)==1
    assert dot(f,y)==0
    # t norms y and kills x.
    assert dot((0,1),y)==1
    assert dot((0,1),x)==0

# Equality pair for both parameter orderings.
x=(Fraction(1),Fraction(0))
y=(Fraction(0),Fraction(-1))
for a,b in [
    (Fraction(1),Fraction(3)),
    (Fraction(2),Fraction(5)),
    (Fraction(1),Fraction(1)),
    (Fraction(5),Fraction(2)),
    (Fraction(7),Fraction(1)),
]:
    A=N((a*x[0]+b*y[0],a*x[1]+b*y[1]))
    B=N((b*x[0]-a*y[0],b*x[1]-a*y[1]))
    assert A==a+b
    assert B==max(a,b)
    q=(A-B)/a
    assert q==min(Fraction(1),b/a)

print("VERIFY_OK facets=6 radon_support_cases=edge+vertex profile=min(1,beta/alpha)")
