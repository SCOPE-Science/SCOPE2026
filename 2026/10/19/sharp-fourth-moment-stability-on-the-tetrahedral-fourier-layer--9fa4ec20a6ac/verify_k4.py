"""Independent finite checks of a sharp fourth-moment identity on the quadratic four-torus layer."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import cmath
import random

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
PAIRS = [(0,5),(1,4),(2,3)]

def moments_by_convolution(a,modulus=None):
    sums=defaultdict(complex)
    for i,e in enumerate(EDGES):
        for j,f in enumerate(EDGES):
            freq=tuple((int(k in e)+int(k in f)) if modulus is None else
                       (int(k in e)+int(k in f))%modulus for k in range(4))
            sums[freq]+=a[i]*a[j]
    return sum(abs(s)**2 for s in sums.values())

def predicted(a):
    S=sum(abs(v)**2 for v in a)
    p=[a[i]*a[j] for i,j in PAIRS]
    return 2*S*S-sum(abs(v)**4 for v in a)+8*sum((p[i]*p[j].conjugate()).real for i in range(3) for j in range(i+1,3))

def deficit(a):
    S=sum(abs(v)**2 for v in a)
    t=[abs(a[i])**2+abs(a[j])**2 for i,j in PAIRS]
    delta=[abs(a[i])**2-abs(a[j])**2 for i,j in PAIRS]
    p=[a[i]*a[j] for i,j in PAIRS]
    rhs=0.5*sum((t[i]-t[j])**2 for i in range(3) for j in range(i+1,3))
    rhs+=0.5*sum(d*d for d in delta)
    rhs+=8*sum(t[i]*t[j]/4-(p[i]*p[j].conjugate()).real for i in range(3) for j in range(i+1,3))
    return 2.5*S*S-predicted(a),rhs

def close(x,y):
    assert abs(x-y)<1e-8*max(1.0,abs(x),abs(y)), (x,y)

def main():
    rng=random.Random(20261015)
    checks=0
    for k in range(2000):
        a=[complex(rng.randrange(-7,8),rng.randrange(-7,8)) for _ in range(6)]
        m=moments_by_convolution(a)
        close(m,predicted(a)); checks+=1
        d,ss=deficit(a); close(d,ss); assert d>=-1e-8; checks+=1
        if k<100:
            close(m,moments_by_convolution(a,3)); checks+=1
            close(m,moments_by_convolution(a,4)); checks+=1
    one=[1+0j]*6
    close(moments_by_convolution(one),90)
    assert moments_by_convolution(one,2)!=90
    for k in range(100):
        phase=[cmath.exp(1j*2*cmath.pi*rng.random()) for _ in range(4)]
        scalar=complex(rng.randrange(-5,6),rng.randrange(-5,6))
        a=[scalar*phase[i]*phase[j] for i,j in EDGES]
        close(moments_by_convolution(a),2.5*sum(abs(v)**2 for v in a)**2); checks+=1
    # Symbolic rational verification of energy for every signed ternary real coefficient pattern.
    for a in product((-1,0,1),repeat=6):
        a=tuple(complex(v) for v in a)
        close(moments_by_convolution(a),predicted(a));checks+=1
    print(f'PASS {checks} direct algebraic and finite-group comparisons, including 729 signed patterns')

if __name__=='__main__':
    main()
