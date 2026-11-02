"""Exact rational geometry and stochastic sanity tests for two-agent EF chore allocation."""
from fractions import Fraction as F
from itertools import product
from random import Random


def determinant(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

def tetra_volume(a,b,c,d):
    edges=[tuple(z-y for z,y in zip(q,a)) for q in (b,c,d)]
    return abs(F(determinant(*edges),6))

def exact_check():
    T=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    zero=(0,0,0)
    e1,e2,e3=(1,0,0),(0,1,0),(0,0,1)
    vol_t=tetra_volume(*T)
    vol_plus=tetra_volume(zero,e1,e2,e3)+tetra_volume((1,1,1),e1,e2,e3)
    p_even=vol_plus/vol_t
    p_odd=(F(1)-4*p_even)/4
    p_dominant=F(1,8)
    p_nondom_even=p_even-p_dominant
    p_nondom_odd=p_odd
    assert (vol_t,vol_plus,p_even,p_odd)==(F(8,3),F(1,2),F(3,16),F(1,16))
    assert p_nondom_even==p_nondom_odd==F(1,16)
    chamber_probs=[p_dominant]*4 +[F(1,16)]*8
    assert sum(chamber_probs)==1
    failure=sum(q*q for q in chamber_probs)
    assert failure==F(3,32) and 1-failure==F(29,32)
    p2=1-2*F(1,2)**2
    p3=1-4*F(1,4)**2
    assert (p2,p3)==(F(1,2),F(3,4))
    print('EXACT_GEOMETRY_OK', 'tetra',vol_t,'positive_octant',vol_plus,'even_sign',p_even,'odd_sign',p_odd)
    print('EXACT_CHAMBERS_OK','dominant 4 x',p_dominant,'non_dominant 8 x',F(1,16))
    print('EXACT_SUCCESS_PROBABILITIES_OK','m=1:',0,'m=2:',p2,'m=3:',p3,'m=4:',1-failure)


def signature(x):
    S=sum(x)
    m=len(x)
    if m==4:
        return (tuple(2*a>S for a in x),
                tuple(2*(x[0]+x[j])>S for j in (1,2,3)))
    if m==3:
        return tuple(2*a>S for a in x)
    if m==2:
        return x[0]>x[1]
    raise ValueError(m)


def ef_exists(x,y):
    m=len(x)
    A=sum(x);B=sum(y)
    for bits in product((0,1),repeat=m):
        sx=sum(v for v,z in zip(x,bits) if z)
        sy=sum(v for v,z in zip(y,bits) if z)
        if 2*sx<A and 2*sy>B: return True
    return False


def random_check():
    rng=Random(426135)
    for m,target,N in ((2,F(1,2),30000),(3,F(3,4),40000),(4,F(29,32),60000)):
        positive=0
        for i in range(N):
            x=[rng.expovariate(1) for _ in range(m)]
            y=[rng.expovariate(1) for _ in range(m)]
            from_signs=signature(x)!=signature(y)
            from_alloc=ef_exists(x,y)
            assert from_signs==from_alloc,(m,x,y,from_signs,from_alloc)
            positive+=from_alloc
        observed=positive/N
        assert abs(observed-float(target))<0.007,(m,observed,target)
        print('FINITE_SANITY_OK',m,N,'EF_rate',round(observed,6),'target',str(target))

if __name__=='__main__':
    exact_check()
    random_check()
