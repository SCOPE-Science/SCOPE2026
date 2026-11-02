"""Independent finite-field verification of canonical Heisenberg affine RB operators.
Public reproducibility: python check_affine_heisenberg.py (Python 3.10+, no dependencies).
"""
from itertools import product


def vecs(p):
    return tuple(product(range(p), repeat=3))


def add(u,v,p):
    return tuple((a+b)%p for a,b in zip(u,v))


def neg(u,p):
    return tuple(-a%p for a in u)


def sub(u,v,p):
    return add(u,neg(v,p),p)


def br(u,v,p):
    return (0,0,(u[0]*v[1]-u[1]*v[0])%p)


def linear(m,u,p):
    return tuple(sum(m[3*i+j]*u[j] for j in range(3))%p for i in range(3))


def apply(m,c,u,p):
    return add(linear(m,u,p),c,p)


def bracket_aff(u,v,p):
    return add(br(u,v,p),v,p)


def idempotent(m,p):
    E=((1,0,0),(0,1,0),(0,0,1))
    return all(linear(m,linear(m,e,p),p)==linear(m,e,p) for e in E)


def lin_rb(m,p):
    E=((1,0,0),(0,1,0),(0,0,1))
    for x in E:
        for y in E:
            rx,ry=linear(m,x,p),linear(m,y,p)
            inside=sub(add(br(rx,y,p),br(x,ry,p),p),br(x,y,p),p)
            if linear(m,inside,p)!=br(rx,ry,p):
                return False
    return True


def trans_good(m,c,p):
    if linear(m,c,p)!=(0,0,0): return False
    E=((1,0,0),(0,1,0),(0,0,1))
    return all(linear(m,br(c,e,p),p)==br(c,linear(m,e,p),p) for e in E)


def canonical_rb_direct(m,c,p):
    V=vecs(p)
    for x in V:
        px=apply(m,c,x,p)
        for y in V:
            py=apply(m,c,y,p)
            descendant=add(sub(bracket_aff(px,y,p),bracket_aff(x,y,p),p),bracket_aff(x,py,p),p)
            if apply(m,c,descendant,p)!=bracket_aff(px,py,p):
                return False
    return True


def all_operators(p):
    zero=(0,0,0)
    candidates=[]
    for m in product(range(p),repeat=9):
        if not idempotent(m,p) or not lin_rb(m,p): continue
        for c in vecs(p):
            if trans_good(m,c,p): candidates.append((m,c))
    return candidates


def rank(m,p):
    vectors=[linear(m,u,p) for u in vecs(p)]
    return {1:0,p:1,p*p:2,p**3:3}[len(set(vectors))]


def automorphisms(p):
    # All Lie automorphisms (2 x 2 invertible quotient, arbitrary central shears)
    for a,b,c,d in product(range(p),repeat=4):
        det=(a*d-b*c)%p
        if det==0: continue
        for s,t in product(range(p),repeat=2):
            mat=(a,b,0,c,d,0,s,t,det)
            for w in range(p):
                yield mat,(0,0,w)


def action(op,f,p):
    # Conjugate P by affine Lie automorphism f, by evaluating on 0 and e_i.
    m,c=op
    a,w=f
    # Calculate f P = P' f, solve via inverse by bijective enumeration on small field.
    V=vecs(p)
    perm={apply(a,w,x,p):x for x in V}
    output={y:apply(a,w,apply(m,c,perm[y],p),p) for y in V}
    z=(0,0,0)
    c2=output[z]
    cols=[sub(output[e],c2,p) for e in ((1,0,0),(0,1,0),(0,0,1))]
    mat=tuple(cols[j][i] for i in range(3) for j in range(3))
    return mat,c2


def run():
    for p in (2,3):
        ops=all_operators(p)
        assert len(ops)==2*p**4+3*p**3+1,(p,len(ops))
        distribution=[sum(rank(m,p)==r for m,c in ops) for r in range(4)]
        assert distribution==[p**3,p**3*(p+1),p**3*(p+1),1],(p,distribution)
        for op in ops:
            assert canonical_rb_direct(*op,p),('failed full identity',p,op)
        if p==2:
            # Independent exhaustive scan of every affine map, not just algebraically filtered candidates.
            brute={(m,c) for m in product(range(p),repeat=9) for c in vecs(p) if canonical_rb_direct(m,c,p)}
            assert brute==set(ops),('independent exhaustive mismatch',p)
        orbit_sizes=[]
        remaining=set(ops)
        group=list(automorphisms(p))
        assert len(group)==p**3*(p*p-1)*(p*p-p)
        while remaining:
            seed=next(iter(remaining))
            orb={action(seed,f,p) for f in group}
            assert orb<=set(ops)
            remaining-=orb
            orbit_sizes.append(len(orb))
        expected=sorted([p,p**3-p,p**3*(p+1),p*p*(p+1),p*p*(p*p-1),1])
        assert sorted(orbit_sizes)==expected, (p,orbit_sizes,expected)
        print('p=%d: operators=%d rank-counts=%s affine-orbits=%s automorphisms=%d'%(p,len(ops),distribution,sorted(orbit_sizes),len(group)))
    print('VERIFY_OK')


if __name__=='__main__':run()
