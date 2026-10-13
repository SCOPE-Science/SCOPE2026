from fractions import Fraction
import itertools
import math

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1] == 0:
        p.pop()
    return p

def add(p,q):
    n=max(len(p),len(q))
    r=[Fraction(0) for _ in range(n)]
    for i,v in enumerate(p): r[i]+=v
    for i,v in enumerate(q): r[i]+=v
    return trim(r)

def sub(p,q):
    return add(p,[-v for v in q])

def mul(p,q):
    r=[Fraction(0) for _ in range(len(p)+len(q)-1)]
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j]+=a*b
    return trim(r)

def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    q=[Fraction(0) for _ in range(max(1,len(a)-len(b)+1))]
    r=a[:]
    while len(r)>=len(b) and any(r):
        k=len(r)-len(b)
        c=r[-1]/b[-1]
        q[k]+=c
        t=[Fraction(0)]*k+[c*x for x in b]
        r=sub(r,t)
    return trim(q),trim(r)

def monic(p):
    p=trim(p)
    if p == [0]: return p
    lead=p[-1]
    return [x/lead for x in p]

def gcd_poly(a,b):
    a=trim(a); b=trim(b)
    while b != [0]:
        _,r=divmod_poly(a,b)
        a,b=b,r
    return monic(a)

def primitive_tuple(p):
    p=monic(p)
    # all polynomials generated here are integral after monic normalization
    den=1
    for x in p:
        den=math.lcm(den,x.denominator)
    ints=[int(x*den) for x in p]
    g=0
    for x in ints:
        g=math.gcd(g,abs(x))
    ints=[x//g for x in ints]
    if ints[-1] < 0:
        ints=[-x for x in ints]
    return tuple(ints)

def word_polys(signs):
    U=[Fraction(0)]
    C=[Fraction(0)]
    cumulatives=[[Fraction(0)]]
    us=[]
    for s in signs:
        U=add([Fraction(s)], [Fraction(0)]+U)
        C=add(C,U)
        us.append(U)
        cumulatives.append(C)
    return us,cumulatives

# Exact gcd classification for periods below six.
period_gcds={}
for p in range(1,7):
    classes={}
    for signs in itertools.product((1,-1),repeat=p):
        us,cs=word_polys(signs)
        g=primitive_tuple(gcd_poly(us[-1],cs[-1]))
        if len(g)>1:
            classes[g]=classes.get(g,0)+1
    period_gcds[p]=classes

assert period_gcds[1] == {}
assert period_gcds[2] == {}
assert period_gcds[3] == {}
assert period_gcds[5] == {}
assert set(period_gcds[4]) == {
    (1,2,1),      # (b+1)^2
    (1,0,1),      # b^2+1
    (-1,0,1),     # b^2-1
}
assert all(c == 2 for c in period_gcds[4].values())

q1=(-1,1,1)       # b^2+b-1
q2=(-1,0,1,0,1)   # b^4+b^2-1

candidate_words={q1:[],q2:[]}
for signs in itertools.product((1,-1),repeat=6):
    us,cs=word_polys(signs)
    g=gcd_poly(us[-1],cs[-1])
    for q in (q1,q2):
        _,r=divmod_poly(g,[Fraction(x) for x in q])
        if r == [0]:
            candidate_words[q].append(signs)

assert candidate_words[q1] == [
    (1,1,-1,-1,-1,1),
    (-1,-1,1,1,1,-1),
]
assert candidate_words[q2] == [
    (1,-1,1,-1,-1,1),
    (-1,1,-1,1,1,-1),
]

phi=(1+math.sqrt(5))/2
b1=1/phi
b2=1/math.sqrt(phi)
assert abs(b1*b1+b1-1) < 2e-15
assert abs(b2**4+b2*b2-1) < 2e-15

def replay(beta,r,steps=6):
    x=r
    u=0.0
    signs=[]
    xs=[x]
    us=[u]
    for _ in range(steps):
        assert abs(x) > 1e-13
        s=1.0 if x>0 else -1.0
        signs.append(1 if s>0 else -1)
        u=beta*u+s
        x=x-u   # eta normalized to one
        xs.append(x); us.append(u)
    return signs,xs,us

# First resonance.
for r in (1.05,1.2,1.4,phi-0.05):
    signs,xs,us=replay(b1,r)
    assert tuple(signs)==(1,1,-1,-1,-1,1)
    assert abs(xs[-1]-r) < 2e-13
    assert abs(us[-1]) < 2e-13
    avg=sum(abs(x) for x in xs[:-1])/6
    assert abs(avg-(1+3*phi)/6) < 2e-13

# Second resonance.
for r in (b2+0.02,0.85,0.92,0.98):
    signs,xs,us=replay(b2,r)
    assert tuple(signs)==(1,-1,1,-1,-1,1)
    assert abs(xs[-1]-r) < 3e-13
    assert abs(us[-1]) < 3e-13
    avg=sum(abs(x) for x in xs[:-1])/6
    target=(1-b2+phi+1/b2)/6
    assert abs(avg-target) < 3e-13

# Curvature and step only rescale gradient norms.
for a in (0.2,1.0,7.0):
    for eta in (0.01,0.3,2.0):
        r=1.3
        signs,xs,us=replay(b1,r)
        mean_grad=sum(abs(a*eta*x) for x in xs[:-1])/6
        target=a*eta*(1+3*phi)/6
        assert abs(mean_grad-target) < 5e-13*max(1.0,target)

print("verification passed")
