"""Exact commutator and numerical ordering checks for serial Holling-II predation.
Run: python3 verify.py. Python standard library only."""
from fractions import Fraction as F
from itertools import permutations
import random, math

def field(x, a, b, r):
    return x*(r-a/(1+b*x))

def deriv(x,a,b,r):
    return r-a/(1+b*x)**2

def bracket(x,ai,bi,aj,bj,r):
    return field(x,ai,bi,r)*deriv(x,aj,bj,r)-field(x,aj,bj,r)*deriv(x,ai,bi,r)

def polynomial_S(x,ai,bi,aj,bj):
    return aj*bj*(1+bi*x)**2-ai*bi*(1+bj*x)**2

def bracket_formula(x,ai,bi,aj,bj,r):
    return x*x*(-ai*aj*(bj-bi)+r*polynomial_S(x,ai,bi,aj,bj))/((1+bi*x)**2*(1+bj*x)**2)

def pair_threshold(ai,bi,aj,bj):
    assert bi<bj
    s0=aj*bj-ai*bi
    s1=2*bi*bj*(aj-ai)
    s2=bi*bj*(aj*bi-ai*bj)
    if s2>0 or (s2==0 and s1>0):
        return F(0),None,'unbounded'
    vertex=-s1/(2*s2) if s2<0 else None
    if vertex is not None and vertex>0:
        M=polynomial_S(vertex,ai,bi,aj,bj)
        witness=vertex
    else:
        M=s0
        witness=F(0)
    if M<=0:
        return math.inf,None,'nonpositive'
    return ai*aj*(bj-bi)/M,witness,'finite'

def rk4(x,a,b,r,t,steps=500):
    dt=t/steps
    for _ in range(steps):
        k1=float(field(x,a,b,r))
        k2=float(field(x+dt*k1/2,a,b,r))
        k3=float(field(x+dt*k2/2,a,b,r))
        k4=float(field(x+dt*k3,a,b,r))
        x+=dt*(k1+2*k2+2*k3+k4)/6
    return x

def run(order, x, stages, r, times):
    for i in order:
        a,b=stages[i]
        x=rk4(x,a,b,r,times[i])
    return x

def main():
    rng=random.Random(20261023)
    n_exact=0;n_threshold=0
    for _ in range(1500):
        ai=F(rng.randint(1,15),rng.randint(1,9))
        aj=F(rng.randint(1,15),rng.randint(1,9))
        bi=F(rng.randint(1,15),rng.randint(1,9))
        bj=F(rng.randint(1,15),rng.randint(1,9))
        r=F(rng.randint(1,12),rng.randint(1,11))
        x=F(rng.randint(1,12),rng.randint(1,11))
        assert bracket(x,ai,bi,aj,bj,r)==bracket_formula(x,ai,bi,aj,bj,r)
        n_exact+=1
        if bi==bj: continue
        if bi>bj: ai,aj,bi,bj=aj,ai,bj,bi
        t,w,k=pair_threshold(ai,bi,aj,bj)
        if t==math.inf:
            rr=F(1,1)
        elif t==0:
            rr=F(1,1)
        else:
            rr=t/F(2)
        if t!=0:
            for z in (F(1,200),F(1,2),F(1),F(3),F(10),F(100)):
                assert bracket(z,ai,bi,aj,bj,rr)<0
                n_threshold+=1
    # exact boundary for an analytically tractable two-phase example
    a1,b1,a2,b2=F(2),F(1,2),F(3),F(3,2)
    t,w,k=pair_threshold(a1,b1,a2,b2)
    assert (t,w,k)==(F(3,2),F(2,3),'finite')
    assert bracket(w,a1,b1,a2,b2,t)==0
    assert bracket(w,a1,b1,a2,b2,F(8,5))>0
    assert bracket(F(4),a1,b1,a2,b2,F(8,5))<0
    # growth can reverse phase ordering even while both phases cause population decline
    a1,b1,a2,b2=F(2),F(1),F(4),F(2)
    assert bracket(F(1,4),a1,b1,a2,b2,F(4,5))==F(-32,1125)
    assert bracket(F(3,4),a1,b1,a2,b2,F(4,5))==F(288,6125)
    for x,expected in ((.25,-1),(.75,1)):
        u=run((0,1),x,((2,1),(4,2)),.8,(.005,.005))
        v=run((1,0),x,((2,1),(4,2)),.8,(.005,.005))
        assert (u-v)*expected>0
    # all 3-phase permutations agree with low-b-to-high-b rule at r=0
    n_orders=0
    for _ in range(25):
        stages=sorted([(rng.uniform(.5,3),rng.uniform(.5,3)) for k in range(3)],key=lambda z:z[1])
        tvec=[rng.uniform(.05,.4) for k in range(3)]
        x0=rng.uniform(.05,5)
        vals=[(run(p,x0,stages,0.0,tvec),p) for p in permutations(range(3))]
        assert min(vals)[1]==(0,1,2)
        assert max(vals)[1]==(2,1,0)
        n_orders+=1
    print('PASS exact identities:',n_exact)
    print('PASS exact nonpositive-bracket threshold samples:',n_threshold)
    print('PASS illustrative exact boundary, sign reversals, and numeric 3-stage permutations:',n_orders)
if __name__=='__main__':main()
