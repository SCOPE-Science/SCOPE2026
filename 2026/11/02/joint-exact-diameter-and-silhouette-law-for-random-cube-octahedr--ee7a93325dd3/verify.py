"""Independent geometric and numerical checks for a random cube-shadow diameter law.
Run with: python3 verify.py. Uses only the standard library.
The finite tests corroborate, but do not replace, the analytic proof.
"""
import math
import random
from itertools import product

PI = math.pi
ROOT3 = math.sqrt(3.0)
T0 = 1.0 / ROOT3


def signed_slack(u):
    a,b,c = sorted(map(abs,u),reverse=True)
    return a-b-c


def density_l(l):
    if l < -T0 or l > 1.0: return 0.0
    if l >= 0:
        cosarc = (3*math.sqrt(2-l*l)+l)/(2*math.sqrt(2*(3-l*l)))
    else:
        cosarc = (3*math.sqrt(1-l*l)-math.sqrt(2)*l)/(2*math.sqrt(3-l*l))
    return 12/(PI*ROOT3)*math.acos(max(-1.,min(1.,cosarc)))


def simpson(f,a,b,n=4000):
    assert n%2==0
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+h*j) for j in range(1,n,2))+2*sum(f(a+h*j) for j in range(2,n,2)))*h/3


def cdf_l(l):
    if l<=-T0:return 0.0
    if l>=1:return 1.0
    if l<0:return simpson(density_l,-T0,l)
    return simpson(density_l,-T0,0)+simpson(density_l,0,l)


def cube_shadow_diameter_direct(u):
    # Unit side cube, differences between its vertices are in {-1,0,1}^3.
    return max(math.sqrt(max(0.0,sum(v*v for v in z)-sum(v*ui for v,ui in zip(z,u))**2))
               for z in product((-1,0,1),repeat=3) if any(z))


def projected_octahedron_vertices(u):
    # Project the six octahedron vertices into an explicitly built orthonormal plane frame.
    pivot=(1.,0.,0.) if abs(u[0])<.9 else (0.,1.,0.)
    t=sum(x*y for x,y in zip(pivot,u))
    e=[x-t*y for x,y in zip(pivot,u)]
    q=math.sqrt(sum(x*x for x in e));e=[x/q for x in e]
    f=(u[1]*e[2]-u[2]*e[1],u[2]*e[0]-u[0]*e[2],u[0]*e[1]-u[1]*e[0])
    pts=sorted(set((sgn*e[i],sgn*f[i]) for i in range(3) for sgn in (1.,-1.)))
    def turn(p,q,r):return (q[0]-p[0])*(r[1]-q[1])-(q[1]-p[1])*(r[0]-q[0])
    lower=[];upper=[]
    for p in pts:
        while len(lower)>1 and turn(lower[-2],lower[-1],p)<=1e-11:lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper)>1 and turn(upper[-2],upper[-1],p)<=1e-11:upper.pop()
        upper.append(p)
    return len(lower[:-1])+len(upper[:-1])


def random_normal(rng):
    v=[rng.gauss(0,1) for _ in range(3)]
    r=math.sqrt(sum(x*x for x in v))
    return [x/r for x in v]


def main():
    p6=(6/PI)*math.acos(1/3)-2
    assert abs(p6-4/PI*math.atan(math.sqrt(2)/5))<1e-14
    assert abs(simpson(density_l,-T0,0,10000)-p6)<2e-8
    assert abs(simpson(density_l,0,1,10000)-(1-p6))<2e-8
    assert abs(density_l(0)-2/ROOT3)<1e-13
    print('EXACT_SECTOR_NORMALIZATION_AND_SHADOW_PROBABILITY_PASSED')

    rng=random.Random(2026102901)
    for _ in range(1600):
        u=random_normal(rng)
        L=signed_slack(u)
        D=math.sqrt(3-L*L)
        assert abs(D-cube_shadow_diameter_direct(u))<1e-10
        assert projected_octahedron_vertices(u)==(6 if L<0 else 4)
    print('INDEPENDENT_ALL_VERTEX_PAIRS_AND_OCTAHEDRON_HULLS_PASSED 1600')

    N=160000
    samples=[]; count6=0
    for _ in range(N):
        u=random_normal(rng);L=signed_slack(u)
        samples.append(L)
        count6 += L<0
    assert abs(count6/N-p6)<.006
    for q in (-.5,-.25,0,.15,.4,.7,.92):
        observed=sum(v<=q for v in samples)/N
        assert abs(observed-cdf_l(q))<.008,(q,observed,cdf_l(q))
    print('INDEPENDENT_HAAR_SIGNED_SLACK_CDF_CHECKS_PASSED 7')

    # Exact analytical endpoint slopes corroborated with shrinking finite differences.
    for t in (.003,.004,.005):
        low=simpson(density_l,1-t,1,3000)
        assert abs(low/t**2-3/PI)<.03
        hex_on=simpson(density_l,-T0,-T0+t,3000)
        assert abs(hex_on/t**2-9*ROOT3/(4*PI))<.05
    print('SHARP_LOWER_AND_SIX_VERTEX_ONSET_EXPANSIONS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__': main()
