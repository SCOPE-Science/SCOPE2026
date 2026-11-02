"""Exact rational checks for a two-branch symplectic torus map's 3-cycle islands.

Run: python3 verify_period3.py
Requires Python 3 standard library only.
"""
from fractions import Fraction as Q
from itertools import product

TWO = Q(2)


def torus_step(x, y, c, d):
    x, y, d = x % TWO, y % TWO, d % TWO
    force = d if y < c else d + c - y
    return y, (-x + force) % TWO


def island(x, y, c, d):
    x, y, d = x % TWO, y % TWO, d % TWO
    return c < x < 2 and c < y < 2 and c < ((d + c - x - y) % TWO) < 2


def clip(poly, lower, s):
    """Keep x+y >= s if lower, otherwise x+y <= s."""
    if not poly: return []
    def v(p): return p[0]+p[1]-s
    def allowed(p): return v(p)>=0 if lower else v(p)<=0
    ans=[]; a=poly[-1]
    for b in poly:
        fa,fb=allowed(a),allowed(b)
        if fa!=fb:
            va,vb=v(a),v(b); t=va/(va-vb)
            ans.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
        if fb: ans.append(b)
        a=b
    return ans


def polygon_area(poly):
    if not poly: return Q(0)
    z=sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1]))
    return abs(z)/2


def geometric_area(c,d):
    d=d % 2
    sq=[(c,c),(TWO,c),(TWO,TWO),(c,TWO)]
    return sum((polygon_area(clip(clip(sq, True, d+c-2-2*n),False,d-2*n))
                for n in range(-4,5)), Q(0))


def bspline(h,t):
    pos=lambda z: max(Q(0),z)
    return (pos(t)**2-3*pos(t-h)**2+3*pos(t-2*h)**2-pos(t-3*h)**2)/2


def convolution_area(c,d):
    h=TWO-c
    d=d % 2
    return sum((bspline(h,d-2*c+2*k) for k in range(-5,6)),Q(0))


def one_parameter_area(d):
    d=d % 2
    if d<=1: return (d*d+(1-d)*(1-d))/2
    return 1-((d-1)*(d-1)+(2-d)*(2-d))/2


def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def check():
    A0=((0,1),(-1,0)); A1=((0,1),(-1,-1)); I=((1,0),(0,1))
    words=[]
    for word in product((0,1),repeat=3):
        M=I
        for branch in word: M=mm((A0,A1)[branch],M)
        if M==I: words.append(word)
    assert words==[(1,1,1)], words
    area_tests=0
    for numerator in range(1,24):
        c=Q(numerator,12)
        for k in range(24):
            d=Q(k,12)
            A=geometric_area(c,d); B=convolution_area(c,d)
            assert A==B, (c,d,A,B)
            residue=(d-2*c)%2
            h=TWO-c
            expected_present=(h>Q(2,3) or (0<residue<3*h))
            assert (A>0)==expected_present,(c,d,A,expected_present)
            if c==1:
                assert A==one_parameter_area(d),(c,d,A)
            area_tests+=1
    orbit_tests=0
    for c,d in product((Q(1,2),Q(1),Q(3,2),Q(7,4)),
                       (Q(0),Q(1,4),Q(1,2),Q(1),Q(3,2),Q(7,4))):
        for i,j in product(range(31),repeat=2):
            x,y=Q(2*i+1,31),Q(2*j+1,31)
            if island(x,y,c,d):
                z=(x,y)
                for _ in range(3):
                    z=torus_step(*z,c,d)
                    assert island(*z,c,d), (c,d,x,y,z)
                assert z==(x,y),(c,d,x,y,z)
                orbit_tests+=1
    assert one_parameter_area(Q(0))==Q(1,2)
    assert one_parameter_area(Q(1,2))==Q(1,4)
    assert one_parameter_area(Q(1))==Q(1,2)
    assert one_parameter_area(Q(3,2))==Q(3,4)
    assert area_tests==552 and orbit_tests>1000
    print(f'PASS: 8 derivative words; {area_tests} exact area/positivity comparisons; '
          f'{orbit_tests} exact three-step orbit tests; exact shift extrema')


if __name__=='__main__': check()
