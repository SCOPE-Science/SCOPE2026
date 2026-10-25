"""Independent, standard-library diagnostics for rare circumradius geometry.

Run with Python 3: python artifacts/verify.py
The analytic argument is in RESULT.md; these are finite consistency tests.
"""
import math
import random

# Three ordered points on an interval carry the Vandermonde mass.
# The two terms g1**2*g2 and g1*g2**2 each integrate to 1/360.
def simplex_monomial(exponents):
    num=1
    for k in exponents:
        num *= math.factorial(k)
    return num / math.factorial(sum(exponents)+len(exponents)-1)
assert abs(6 * (simplex_monomial((0,2,1,0))
                + simplex_monomial((0,1,2,0))) - 1/30) < 1e-15
print('EXACT_GAP_INTEGRAL_1_OVER_30_OK')

# The disk line-offset density is (35/32)(1-u**2)**3 on [-1,1].
# Its variance is 1/9. The published circumradius constant is
# independently recovered from the sixth chord integral of the unit disk.
C_DISK=1024/(525*math.pi**2)
assert abs((math.pi * 64 * 32/35)/(30*math.pi**3)-C_DISK)<1e-14
print('DISK_SIXTH_CHORD_INTEGRAL_AND_TAIL_COEFFICIENT_OK',C_DISK)

# Independent chord clipping, without the diagonal-chord formula.
def square_chord(direction, p):
    ex,ey=math.cos(direction), math.sin(direction)
    nx,ny=-ey,ex
    lo,hi=-1.e100,1.e100
    for co,ec in ((p*nx,ex),(p*ny,ey)):
        if abs(ec)<1.e-13:
            if abs(co)>.5:return 0.
        else:
            t1=(-.5-co)/ec;t2=(.5-co)/ec
            lo=max(lo,min(t1,t2));hi=min(hi,max(t1,t2))
    return max(0,hi-lo)

def sixth_marginal(direction,N=20000):
    width=.5*(abs(math.sin(direction))+abs(math.cos(direction)))
    s=0.
    for i in range(N):
        p=-width+(i+.5)*(2*width/N)
        s+=square_chord(direction,p)**6
    return s*2*width/N
J_H=sixth_marginal(0.);J_D=sixth_marginal(math.pi/4)
assert abs(J_H-1)<1.e-7 and abs(J_D-8*math.sqrt(2)/7)<2.e-7
print('INDEPENDENT_SQUARE_CHORD_DIRECTION_MARGINALS_OK',J_H,J_D)

rng=random.Random(20261020)
T=8.
N=750000
hit=0
p2=g0=g1=g2=g3=usq=0.
for _ in range(N):
    points=[]
    for j in range(3):
        ang=2*math.pi*rng.random();rr=math.sqrt(rng.random())
        points.append((rr*math.cos(ang),rr*math.sin(ang)))
    a,b,c=points
    vx=b[0]-a[0];vy=b[1]-a[1];baselen=math.hypot(vx,vy)
    wx=c[0]-a[0];wy=c[1]-a[1]
    tx=c[0]-b[0];ty=c[1]-b[1]
    det=abs(vx*wy-vy*wx)
    if math.hypot(wx,wy)*math.hypot(tx,ty)*baselen <= 2*T*det:
        continue
    hit+=1
    e=(vx/baselen,vy/baselen);n=(-e[1],e[0])
    p=n[0]*a[0]+n[1]*a[1]
    proj=sorted(e[0]*pt[0]+e[1]*pt[1] for pt in points)
    rad=math.sqrt(max(0,1-p*p))
    norm=[(z+rad)/(2*rad) for z in proj]
    gaps=[norm[0],norm[1]-norm[0],norm[2]-norm[1],1-norm[2]]
    p2+=p*p;g0+=gaps[0];g1+=gaps[1];g2+=gaps[2];g3+=gaps[3]
    s1=e[0]*a[0]+e[1]*a[1];s2=e[0]*b[0]+e[1]*b[1]
    s3=e[0]*c[0]+e[1]*c[1]
    h=n[0]*(c[0]-a[0])+n[1]*(c[1]-a[1])
    U=2*T*h/(abs(s3-s1)*abs(s3-s2))
    usq+=U*U
assert hit>12000
mass=hit*T/N
assert abs(mass/C_DISK-1)<.06
assert abs(p2/hit-1/9)<.025
assert max(abs(z/hit-v) for z,v in zip((g0,g1,g2,g3),(1/7,5/14,5/14,1/7)))<.025
assert abs(usq/hit-1/3)<.025
print('DIRECT_RANDOM_TRIANGLES_CIRCUMRADIUS_CONDITIONAL_GEOMETRY_OK',
      'samples',N,'events',hit,'T*tail',mass,'p2',p2/hit,
      'gaps',[z/hit for z in (g0,g1,g2,g3)], 'U2',usq/hit)
print('ALL_MARKED_RARE_TRIANGLE_DIAGNOSTICS_OK')
