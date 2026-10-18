"""Finite binary (3,3) forms and the automorphisms of a split quadric."""
from collections import Counter, defaultdict

GL2 = [(a,b,c,d) for a in (0,1) for b in (0,1)
       for c in (0,1) for d in (0,1) if a*d ^ b*c]
assert len(GL2)==6

def poly_product(u,v):
    z=0
    for i in range(4):
        for j in range(4-i):
            if (u>>i & 1) and (v>>j & 1): z ^= 1 << (i+j)
    return z

def power(u,n):
    out=1
    for _ in range(n):out=poly_product(out,u)
    return out

def cubic_action(matrix):
    a,b,c,d=matrix
    U=a|(b<<1); V=c|(d<<1)
    return [poly_product(power(U,3-i),power(V,i)) for i in range(4)]

def make_actions():
    out=[]
    for g in GL2:
        for h in GL2:
            X=cubic_action(g);Y=cubic_action(h)
            for swap in (False,True):
                vec=[]
                for j in range(4):
                    for i in range(4):
                        I,J=(j,i) if swap else (i,j)
                        v=0
                        for a in range(4):
                            for b in range(4):
                                if (X[I]>>a & 1) and (Y[J]>>b & 1):
                                    v^=1<<(4*b+a)
                        vec.append(v)
                out.append(vec)
    assert len(out)==72
    return out
ACTIONS=make_actions()

def transform(mask,vec):
    v=0
    while mask:
        b=mask & -mask
        v^=vec[b.bit_length()-1]
        mask^=b
    return v

def fibre(mask,proj,coordinate):
    """proj=0 restrict first coordinate; 1 restrict second.
    P1(F2) points: coordinate 0,1,2 correspond [1:0],[1:1],[0:1].
    """
    c=0
    for k in range(4):
        bit=0
        for a in range(4):
            i,j=(a,k) if proj==0 else (k,a)
            if (coordinate==0 and a==0) or coordinate==1 or (coordinate==2 and a==3):
                bit^=(mask>>(4*j+i))&1
        c|=bit<<k
    return c

def total(mask,proj):
    return sum(fibre(mask,proj,t) in (1,8,15) for t in range(3))

def profile(mask):
    return tuple(sorted((total(mask,0),total(mask,1))))

def smooth_orbits(smooth):
    seen=set();orbits=[]
    for m in range(1,65536):
        if smooth[m] or m in seen:continue
        orbit={transform(m,vec) for vec in ACTIONS}
        assert not (orbit & seen) and all(not smooth[u] for u in orbit)
        assert len(orbit) in (6,12,18,24,36,72)
        assert all(profile(u)==profile(m) for u in orbit)
        seen.update(orbit)
        orbits.append((m,len(orbit),profile(m)))
    assert len(seen)==16020 and len(orbits)==252
    return orbits
