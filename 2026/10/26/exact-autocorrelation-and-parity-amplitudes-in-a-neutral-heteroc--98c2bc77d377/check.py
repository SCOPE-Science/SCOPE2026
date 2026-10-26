"""Independent exact-rational checks for a central-coordinate correlation law.
Run: python3 check.py. Finite tests are not a proof of the infinite theorem.
"""
from fractions import Fraction as Q
from math import comb
from collections import defaultdict

N = 12

# Exact weighted random-walk recursion. States are (height, historical minimum).
p = {(0, 0): Q(1)}
walk_cov = []
for n in range(N+1):
    walk_cov.append(sum((w * Q(1, 2)**(s-2*m) for (s,m), w in p.items()), Q(0)) / 12)
    nxt = defaultdict(Q)
    for (s,m), w in p.items():
        for t in (-1,1):
            nxt[(s+t,min(m,s+t))] += w/2
    p = dict(nxt)

# Coefficients of r=(1-sqrt(1-z^2))/z; r=z(1+r^2)/2.
r = [Q(0)]*(N+2)
for k in range(N//2+1):
    j=2*k+1
    if j<len(r):
        r[j] = Q(comb(2*k,k),k+1) / 2**(2*k+1)

# Formal convolution: C(z)=(r/z)/(6*(1-r/2)^2).
def times(a,b):
    out=[Q(0)]*(N+2)
    for i,u in enumerate(a):
        if not u: continue
        for j,v in enumerate(b[:len(out)-i]):
            if v: out[i+j]+=u*v
    return out
one=[Q(1)]+[Q(0)]*(N+1)
B=[Q(0)]*(N+2)
powr=one
for j in range(N+2):
    factor=Q(j+1,2**j)
    for k in range(N+2):B[k]+=factor*powr[k]
    powr=times(powr,r)
G=times(r[1:]+[Q(0)],B)
series_cov=[v/6 for v in G[:N+1]]
assert walk_cov==series_cov, (walk_cov,series_cov)
assert walk_cov[:7]==[Q(1,12), Q(1,24), Q(7,192), Q(5,192), Q(73,3072), Q(115,6144), Q(859,49152)]

# Independent exact area integration of actual four branches on dyadic rectangles.
# Each rectangle stores original x,y intervals and current diagonal affine coordinates.
rectangles=[(Q(0),Q(1),Q(0),Q(1),Q(1),Q(0),Q(1),Q(0))]
branches=[(Q(0),Q(1,4),Q(0),Q(1),Q(4),Q(0),Q(1,2),Q(0)),
          (Q(1,4),Q(1,2),Q(0),Q(1),Q(4),Q(-1),Q(1,2),Q(1,2)),
          (Q(1,2),Q(1),Q(0),Q(1,2),Q(2),Q(-1),Q(2),Q(0)),
          (Q(1,2),Q(1),Q(1,2),Q(1),Q(2),Q(-1),Q(2),Q(-1))]

def integral(rect):
    xl,xh,yl,yh,ax,bx,ay,by=rect
    # integrate (y0-.5)*(ay*y0+by-.5) over initial rectangle
    A=ay
    B=by-Q(1,2)-ay/2
    C=-(by-Q(1,2))/2
    return (xh-xl)*(A*(yh**3-yl**3)/3 + B*(yh**2-yl**2)/2 + C*(yh-yl))

def nextrect(rect, branch):
    xl,xh,yl,yh,ax,bx,ay,by=rect
    lx,hx,ly,hy,sx,tx,sy,ty=branch
    xl2=max(xl,(lx-bx)/ax)
    xh2=min(xh,(hx-bx)/ax)
    yl2=max(yl,(ly-by)/ay)
    yh2=min(yh,(hy-by)/ay)
    if xh2<=xl2 or yh2<=yl2: return None
    return (xl2,xh2,yl2,yh2,sx*ax,sx*bx+tx,sy*ay,sy*by+ty)

for n in range(7):
    actual=sum(map(integral,rectangles),Q(0))
    assert actual==series_cov[n], (n, actual, series_cov[n])
    if n<6:
        new=[]
        for rect in rectangles:
            for branch in branches:
                candidate=nextrect(rect,branch)
                if candidate is not None:new.append(candidate)
        rectangles=new
print(f'PASS: {N+1} exact random-walk versus generating-function coefficients;')
print('PASS: 7 exact direct planar-map covariance integrals (iterates 0..6);')
print('PASS: first seven exact coefficients; total checks = 21.')
