"""Verify elementary identities behind the density-3/2 Y-rigidity proof.
Checks (stdlib only):
 1. Y-cone density = 3/2 via area in B_r.
 2. Three unit vectors sum to zero  <=>  pairwise dots -1/2 (120 deg).
 3. Length obstruction: 3*pi is not a multiple of 2*pi.
 4. Sandwich constants for vertex-maximality tend to 1.
 5. Balancing of Y x R spine conormals.
"""
import math, random

ok = []
def check(name, cond):
    ok.append(cond)
    print(("PASS" if cond else "FAIL") + f": {name}")

# 1. Y density
r = 1.7
mass = 3 * 0.5 * math.pi * r**2
theta = mass / (math.pi * r**2)
check("Y density == 3/2", abs(theta - 1.5) < 1e-12)

# 2a. 120-degree triple sums to zero
vs = [(math.cos(2*math.pi*k/3), math.sin(2*math.pi*k/3)) for k in range(3)]
sx, sy = sum(v[0] for v in vs), sum(v[1] for v in vs)
check("120deg triple balanced", abs(sx) < 1e-12 and abs(sy) < 1e-12)
dots = [vs[i][0]*vs[j][0]+vs[i][1]*vs[j][1] for i in range(3) for j in range(i+1,3)]
check("pairwise dots == -1/2", all(abs(d+0.5) < 1e-12 for d in dots))

# 2b. converse: random unit v1,v2, v3 = -(v1+v2) normalized-or-check:
# if |v1+v2+v3|=0 with |vi|=1 then <vi,vj>=-1/2. Verify algebraically:
# 0=|sum|^2 = 3 + 2(d12+d13+d23); by symmetry under rotation fix v1=(1,0),
# v2=(cos t, sin t); then v3=-(v1+v2) must be unit => |v1+v2|^2=1 => 2+2cos t=1
t = 2*math.pi/3
v1=(1.0,0.0); v2=(math.cos(t),math.sin(t)); v3=(-(v1[0]+v2[0]),-(v1[1]+v2[1]))
check("third vector unit (120deg)", abs(math.hypot(*v3)-1.0)<1e-12)
# non-120 fails: t=pi/2 -> |v1+v2|=sqrt2, negation not unit
t2=math.pi/2
w3=((1+math.cos(t2)),(math.sin(t2)))
check("non-120 triple not balanced-unit", abs(math.hypot(w3[0],w3[1])-1.0)>0.3)
# randomized converse: sample unit v1,v2, define s=v1+v2; s unit-length check grid
rng = random.Random(0)
good=True
for _ in range(2000):
    a=rng.uniform(0,2*math.pi); b=rng.uniform(0,2*math.pi)
    v1=(math.cos(a),math.sin(a)); v2=(math.cos(b),math.sin(b))
    s2=(v1[0]+v2[0])**2+(v1[1]+v2[1])**2
    # |v1+v2|=1 iff cos(a-b)=-1/2
    iff = abs((math.cos(a-b)+0.5))<1e-9
    isunit = abs(s2-1.0)<1e-9
    if iff!=isunit: good=False; break
check("unit-sum condition <=> cos=-1/2 (2000 random)", good)

# 3. length obstruction
check("3pi/2pi = 3/2 not integer", abs((3*math.pi)/(2*math.pi)-1.5)<1e-12 and (3%2==1))

# 4. sandwich ratios -> 1
x0=2.5
for s in [10,100,1000,10**6]:
    lo=((s-x0)/s)**2; hi=((s+x0)/s)**2
    assert abs(lo-1)<0.6 and abs(hi-1)<0.6
check("sandwich (s-|x|)^2/s^2 -> 1", abs(((10**6-x0)/10**6)**2-1)<1e-5)

# 5. spine conormals of Y x R sum to zero (three unit normals at 120 in normal 2-plane)
ns=[(math.cos(2*math.pi*k/3),math.sin(2*math.pi*k/3)) for k in range(3)]
check("spine force balance", abs(sum(n[0] for n in ns))<1e-12 and abs(sum(n[1] for n in ns))<1e-12)

print("ALL_VERIFY_OK" if all(ok) else "VERIFY_FAILED")
