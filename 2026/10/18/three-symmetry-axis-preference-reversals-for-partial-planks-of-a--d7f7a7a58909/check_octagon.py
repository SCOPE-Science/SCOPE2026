"""Independent formula checks for symmetry-axis strips of a regular octagon.

Requires Python 3 and SymPy. Run: python check_octagon.py
Finite floating-point checks support, but do not replace, the analytic proof.
"""
import math
from sympy import S, symbols, sqrt, simplify, N

r = sqrt(2)
a = r / 2
c = sqrt(2 + r) / 2
d = sqrt(2 - r) / 2
z = symbols('z', real=True)
CV1 = r - 2*z + (r - 1)*z**2
CV2 = (1 + r)*(1-z)**2
CE1 = r - 2*c*z
CE2 = (c-z)*(c+2*d-z)
assert simplify(CV1.subs(z,a) - CV2.subs(z,a)) == 0
assert simplify(CE1.subs(z,d) - CE2.subs(z,d)) == 0
assert simplify(CE1.subs(z,0)-r) == 0
assert simplify(CE2.subs(z,c)) == 0
assert simplify(CV2.subs(z,1)) == 0
assert simplify((CE2-CV2).subs(z,S.Half+d)) == 0

s1 = 2*(1-c)/(r-1)
m = 2-r
h = c+d
s2 = (h-1+sqrt((h-1)**2-m**2/4))/m
s3 = S.Half+d
P2 = simplify(CE2-CV1)
assert all(abs(float(N((P2 - (m*z**2-2*(h-1)*z+m/4)).subs(z,val),35)))<1e-27 for val in (0,1,2))
assert abs(float(N(P2.subs(z,s2),35))) < 1e-28
assert 0 < float(N(s1,35)) < float(N(d,35))
assert float(N(d,35)) < float(N(s2,35)) < float(N(a,35))
assert float(N(a,35)) < float(N(s3,35)) < float(N(c,35))
assert -0.00241 < float(N((CE1-CV1).subs(z,d),35)) < -0.00239
assert 0.00579 < float(N((CE2-CV1).subs(z,a),35)) < 0.00580
assert float(N((CE2-CV2).subs(z,c),35)) < 0

# Independent direct polygon clipping (not derived from the cap formulas).
vertices = [(math.cos(j*math.pi/4), math.sin(j*math.pi/4)) for j in range(8)]

def clipped_area(normal_angle, offset):
    nx, ny = math.cos(normal_angle), math.sin(normal_angle)
    old = vertices[:]
    new = []
    for u,v in zip(old,old[1:]+old[:1]):
        f = u[0]*nx+u[1]*ny-offset
        g = v[0]*nx+v[1]*ny-offset
        if f >= 0: new.append(u)
        if (f < 0 <= g) or (g < 0 <= f):
            t = f/(f-g)
            new.append((u[0]+t*(v[0]-u[0]),u[1]+t*(v[1]-u[1])))
    return abs(sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(new,new[1:]+new[:1])))/2 if len(new)>=3 else 0.0

A=math.sqrt(2)
af,cf,df=map(float,(a,c,d))
def cap_v(s):
    if s >= 1:return 0
    return math.sqrt(2)-2*s+(math.sqrt(2)-1)*s*s if s<=af else (1+math.sqrt(2))*(1-s)**2
def cap_e(s):
    if s >= cf:return 0
    return math.sqrt(2)-2*cf*s if s<=df else (cf-s)*(cf+2*df-s)

checks=0
for i in range(2001):
    s=1.05*i/2000
    for theta,cap in ((0.0,cap_v),(math.pi/8,cap_e)):
        error=abs(clipped_area(theta,s)-cap(s))
        assert error<6e-13,(s,theta,error)
        checks+=1
thresholds=list(map(float,(s1,s2,s3)))
for i in range(1,1600):
    s=cf*i/1600
    dv=cap_e(s)-cap_v(s)
    predicted=1 if (s<thresholds[0] or thresholds[1]<s<thresholds[2]) else -1
    if min(abs(s-t) for t in thresholds)>0.0001:
        assert dv*predicted>0,(s,dv,predicted)
    checks+=1
print('OCTAGON_SYMMETRY_PLANK_CHECK_OK',checks,'root_halfwidths',*[float(N(t,17)) for t in (s1,s2,s3)])
