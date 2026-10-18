#!/usr/bin/env python3
"""Independent orbit-stabilizer and rational-osculation checks; stdlib only."""
import itertools
MON=[(i,j) for i in range(4) for j in range(i,4)]
REPS=[(20,555,5040),(40,205,5040),(20,613,5040),(20,552,10080),
      (40,206,5040),(20,609,2520),(20,842,2520),(20,554,5040)]
def canonical(a,b):
    return tuple(sorted((a,b,a^b))[:2])
def full_rank(rows):
    p={}
    for q in rows:
        x=q
        while x:
            k=x.bit_length()-1
            if k in p:x^=p[k]
            else:p[k]=x;break
    return len(p)==4
def polyimage(q,rows):
    vals=[]
    for i,j in MON:
        z=0
        for s in range(4):
            for t in range(4):
                if ((rows[i]>>s)&1) and ((rows[j]>>t)&1):
                    z ^= 1<<MON.index(tuple(sorted((s,t))))
        vals.append(z)
    out=0
    for j in range(10):
        if q>>j&1:out^=vals[j]
    return out
G=[r for r in itertools.product(range(1,16),repeat=4) if full_rank(r)]
assert len(G)==20160
for a,b,expected in REPS:
    images={canonical(polyimage(a,g),polyimage(b,g)) for g in G}
    assert len(images)==expected,(a,b,len(images),expected)
print("GROUP_ORDER=20160")
print("PROJECTIVE_ORBIT_SIZES",[(a,b,n) for a,b,n in REPS])
# Separate direct algebraic rational-point and plane tests, no use of first checker.
P=[p for p in itertools.product((0,1),repeat=4) if any(p)]
def f(q,p):
    return sum(((q>>i)&1)*p[u]*p[v] for i,(u,v) in enumerate(MON))%2
def points(a,b):return [p for p in P if not f(a,p) and not f(b,p)]
def planes_through_every_point(pts):
    return [h for h in range(1,16) if all(
        sum(((h>>i)&1)*p[i] for i in range(4))%2==0 for p in pts)]
for a,b,n in REPS:
    if (a,b) in ((20,609),(20,842),(40,206)):
        pts=points(a,b)
        assert len(pts)==4
        print("FOUR_POINT_PLANE",a,b,planes_through_every_point(pts))
assert planes_through_every_point(points(20,609))==[]
assert planes_through_every_point(points(20,842))==[2]
assert planes_through_every_point(points(40,206))==[]
# A local-algebra certificate for the order-four plane on C_{20,609}:
# under x0=0, x2=1, the two equations are x1^2 and x1+x1*x3+x3^2.
# Eliminating x1 yields (x3^2/(1+x3))^2, hence a unique
# geometric intersection at x1=x3=0 with length four.
# More concretely the Groebner ideal equals (x1+x3^3+x3^2, x3^4).
# In P^3, x0=x2=0 would force x1=x3=0, so no point outside the chart.
print("CONTACT_CERTIFICATE: (x1+x3^3+x3^2,x3^4) at (0:0:1:0)")
print("VERIFY_INDEPENDENT_OK")
