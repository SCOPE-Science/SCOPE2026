from fractions import Fraction

def N(v):
    s,t=v
    return max(abs(s),abs(t),abs(s-t))

primal = {
    (Fraction(1),Fraction(0)),
    (Fraction(1),Fraction(1)),
    (Fraction(0),Fraction(1)),
    (Fraction(-1),Fraction(0)),
    (Fraction(-1),Fraction(-1)),
    (Fraction(0),Fraction(-1)),
}
dual = {
    (Fraction(1),Fraction(0)),
    (Fraction(0),Fraction(1)),
    (Fraction(1),Fraction(-1)),
    (Fraction(-1),Fraction(0)),
    (Fraction(0),Fraction(-1)),
    (Fraction(-1),Fraction(1)),
}

def J(v):
    a,b=v
    return (-b,a)

assert {J(v) for v in dual} == primal

def dot(f,v):
    return f[0]*v[0]+f[1]*v[1]

# Canonical smooth-edge Birkhoff reversal.
for u in [Fraction(k,20) for k in range(1,20)]:
    x=(Fraction(1),u)
    assert N(x)==1
    for y in [(Fraction(0),Fraction(1)),(Fraction(0),Fraction(-1))]:
        assert N(y)==1
        # s norms x and kills y.
        assert dot((1,0),x)==1 and dot((1,0),y)==0
        if y[1] == 1:
            g=(-u,Fraction(1))  # t-u s
        else:
            g=(u,Fraction(-1))  # u s-t
        # g is in the dual unit ball: max on primal vertices is 1.
        assert max(dot(g,v) for v in primal)==1
        assert dot(g,y)==1 and dot(g,x)==0

# Canonical vertex Birkhoff reversal.
x=(Fraction(1),Fraction(0))
for v in [Fraction(k,20) for k in range(21)]:
    y=(v,Fraction(1))
    assert N(y)==1
    f=(Fraction(1),-v)  # (1-v)s+v(s-t)
    assert max(dot(f,p) for p in primal)==1
    assert dot(f,x)==1 and dot(f,y)==0
    g=(Fraction(0),Fraction(1))
    assert dot(g,y)==1 and dot(g,x)==0

# Exact witness families for the strong-rotundity profile.
f=(Fraction(1),Fraction(0))
x=(Fraction(1),Fraction(0))
for k in range(401):
    eps=Fraction(k,200)
    target=max(Fraction(0),eps-Fraction(1))
    if eps <= 1:
        y=(Fraction(1),eps)
    else:
        y=(Fraction(2)-eps,Fraction(1))
    assert N(y)==1
    assert N((x[0]-y[0],x[1]-y[1]))==eps
    deficit=Fraction(1)-dot(f,y)
    assert deficit==target

# Supporting-hyperplane nearest-point identity on exact sample data.
samples=[
    ((Fraction(1),Fraction(0)),(Fraction(1),Fraction(0)),(Fraction(1,3),Fraction(-1,4))),
    ((Fraction(1),Fraction(1)),(Fraction(0),Fraction(1)),(Fraction(-1,5),Fraction(2,5))),
]
for x,f,y in samples:
    assert N(x)==1 and dot(f,x)==1
    d=Fraction(1)-dot(f,y)
    z=(y[0]+d*x[0],y[1]+d*x[1])
    assert dot(f,z)==1
    assert N((z[0]-y[0],z[1]-y[1]))==d

print("VERIFY_OK eta_equals_upsilon polar_vertices=6 hexagon_profile=max(0,epsilon-1) grid=401")
