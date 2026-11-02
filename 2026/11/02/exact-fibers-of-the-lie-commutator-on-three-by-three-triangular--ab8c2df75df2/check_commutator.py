#!/usr/bin/env python3
"""Independent finite-field checks of a triangular-matrix commutator fiber formula.

No third-party packages; checks literal matrix-coordinate brackets for q=2,3 and
compressed direct sums over all eight noncentral variables for q=4,5.
"""
from itertools import product
from collections import defaultdict, Counter

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def neg(a,q):
    return a if q==4 else (-a)%q

def sub(a,b,q):
    return add(a,neg(b,q),q)

def mul(a,b,q):
    if q!=4: return a*b%q
    p=0
    for i in range(2):
        if (b>>i)&1:p ^= a<<i
    if p&8:p ^= 0b1100 # x^3=x^2+x
    if p&4:p ^= 0b111  # x^2=x+1
    return p

def expected(q,u,v,w):
    z=q**3+q**2-q
    nz=q**3-q
    if u==v==0:
        return q**3*z*z-q**7+(q**8 if w==0 else 0)
    return q**3*(z if u==0 else nz)*(z if v==0 else nz)

def direct(q):
    fibers=defaultdict(int)
    # X=(d1,d2,d3,x12,x23,x13), and likewise Y.
    for d1,d2,d3,x,y,z in product(range(q), repeat=6):
        for e1,e2,e3,s,t,r in product(range(q), repeat=6):
            u=sub(mul(sub(d1,d2,q),s,q),mul(sub(e1,e2,q),x,q),q)
            v=sub(mul(sub(d2,d3,q),t,q),mul(sub(e2,e3,q),y,q),q)
            w=add(sub(mul(sub(d1,d3,q),r,q),mul(sub(e1,e3,q),z,q),q),sub(mul(x,t,q),mul(s,y,q),q),q)
            fibers[u,v,w]+=1
    assert len(fibers)==q**3
    assert sum(fibers.values())==q**12
    assert all(fibers[u,v,w]==expected(q,u,v,w) for u,v,w in product(range(q),repeat=3))
    return len(fibers),Counter(fibers.values())

def compressed(q):
    # Two scalar diagonal choices and two central entries are counted explicitly.
    # Sum directly over all 2-vectors a,b,S,T. This is independent of the closed
    # four-stratum multiplicity calculation.
    pairs=list(product(range(q),repeat=2))
    fibers=defaultdict(int)
    for a in pairs:
      for b in pairs:
        ab=(add(a[0],b[0],q),add(a[1],b[1],q))
        for S in pairs:
          u=add(mul(a[0],S[0],q),mul(a[1],S[1],q),q)
          for T in pairs:
            v=add(mul(b[0],T[0],q),mul(b[1],T[1],q),q)
            det=sub(mul(S[0],T[1],q),mul(S[1],T[0],q),q)
            if ab==(0,0):
              fibers[u,v,det]+=q**4
            else:
              for w in range(q):
                fibers[u,v,w]+=q**3
    assert len(fibers)==q**3
    assert sum(fibers.values())==q**12
    for u,v,w in product(range(q),repeat=3):
      assert fibers[u,v,w]==expected(q,u,v,w),(q,(u,v,w),fibers[u,v,w],expected(q,u,v,w))
    return len(fibers),Counter(fibers.values())

if __name__=='__main__':
    print('direct q=2:', direct(2))
    print('direct q=3:', direct(3))
    print('compressed q=4:', compressed(4))
    print('compressed q=5:', compressed(5))
    print('TRIANGULAR_BRACKET_FIBER_CENSUS_OK q=2,3,4,5')
