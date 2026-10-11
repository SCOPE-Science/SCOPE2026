"""Exact rational verification of a finite-equilateral Lipschitz-free-space witness."""
from fractions import Fraction as F
from itertools import product

half = F(1,2)
p = (F(1,2),F(1,4),F(1,4))
q = (F(3,4),F(1,8),F(1,8))

def orbit_average(r,s):
    choices=[]
    for a,b in product((False, True),repeat=2):
        rr=tuple([r[0],r[2],r[1]]) if a else tuple(r)
        ss=tuple([s[0],s[2],s[1]]) if b else tuple(s)
        choices.append((rr,ss))
    return choices

def tv(x,y):
    return sum((abs(a-b) for a,b in zip(x,y)), F(0))/2

prototypes=(
    ((F(0),F(0),F(1)), (F(7,8),F(1,8),F(0))),
    ((F(1,8),F(0),F(7,8)), (F(1),F(0),F(0))),
    ((F(1),F(0),F(0)), (F(1,2),F(1,2),F(0))),
)
weights=(F(2,11),F(4,11),F(5,11))
assert sum(weights)==1
bary_r=[F(0)]*3
bary_s=[F(0)]*3
for weight,(r,s) in zip(weights,prototypes):
    assert sum(r)==sum(s)==1
    for rr,ss in orbit_average(r,s):
        assert tv(rr,p)+tv(ss,q)==F(7,8), (rr,ss)
        for i in range(3):
            bary_r[i]+=weight*rr[i]/4
            bary_s[i]+=weight*ss[i]/4
assert tuple(bary_r)==p and tuple(bary_s)==q,(bary_r,bary_s)

# Signed zero-mass coordinates and all oriented molecules.
x=p+tuple(-t for t in q)
assert sum(x)==0 and sum(abs(t) for t in x)/2==1
D={}
for i in range(6):
    for j in range(6):
        if i==j:continue
        mol=[F(0)]*6
        mol[i]=1;mol[j]=-1
        D[(i,j)]=sum(abs(mol[k]-x[k]) for k in range(6))/2
assert min(D.values())==F(3,4)
assert D[(0,3)]==F(3,4)
assert min(v for key,v in D.items() if key!=(0,3))>F(3,4)
# In every coupling of the three positive and three negative masses,
# lambda(0,0) >= p(0)+q(0)-1 = 1/4. This is exact by marginal totals.
assert p[0]+q[0]-1==F(1,4)
print('PASS: 12 orbit witnesses, exact barycenter, radius 7/8; nearest molecule radius 3/4; forced edge mass 1/4.')
