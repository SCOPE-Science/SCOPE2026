#!/usr/bin/env python3
import itertools

def rt_block(x,y,q):
    if y % q:
        return 2
    if x % q:
        return 1
    return 0

def dist(x,y,q):
    return rt_block((x[0]-y[0])%q,(x[1]-y[1])%q,q)+rt_block((x[2]-y[2])%q,(x[3]-y[3])%q,q)

def good(C,q):
    return all(dist(x,y,q)>=3 for x,y in itertools.combinations(C,2))

def binary_census():
    V=list(itertools.product(range(2), repeat=4))
    maxima=[]
    best=0
    for r in range(1,5):
        found=[]
        for C in itertools.combinations(V,r):
            if good(C,2): found.append(C)
        if found:
            best=r; maxima=found
    assert best==4 and len(maxima)==16
    def affine(C):
        C=set(C); a=next(iter(C))
        T={tuple(xi^ai for xi,ai in zip(x,a)) for x in C}
        return (0,0,0,0) in T and all(tuple(xi^yi for xi,yi in zip(x,y)) in T for x in T for y in T)
    assert all(affine(C) for C in maxima)
    # Natural affine ordered isometries: translations, independent shears
    # (a,b)->(a+t b,b), (c,d)->(c+s d,d), and block swap.
    def act(x,tr,t,s,swap):
        a,b,c,d=x
        y=((a+t*b)%2,b,(c+s*d)%2,d)
        if swap: y=(y[2],y[3],y[0],y[1])
        return tuple((yi+ti)%2 for yi,ti in zip(y,tr))
    base=maxima[0]
    orbit=set()
    for tr in V:
        for t,s,sw in itertools.product(range(2),range(2),range(2)):
            orbit.add(tuple(sorted(act(x,tr,t,s,sw) for x in base)))
    assert len(orbit)==16
    assert orbit=={tuple(sorted(C)) for C in maxima}
    return best,len(maxima),len(orbit)

def ternary_family():
    q=3
    perms=list(itertools.permutations(range(q)))
    seen=set(); count=0
    # Frows[u] is permutation v -> F(u,v); Gcols[v] is permutation u -> G(u,v)
    for Frows in itertools.product(perms, repeat=q):
        for Gcols in itertools.product(perms, repeat=q):
            C=tuple(sorted((Frows[u][v],u,Gcols[v][u],v) for u in range(q) for v in range(q)))
            assert good(C,q)
            seen.add(C); count+=1
    assert count==(6**6)==46656
    assert len(seen)==count
    return count

if __name__=='__main__':
    b,nb,no=binary_census()
    n3=ternary_family()
    print(f'VERIFY_OK q2_max={b} q2_labeled_maxima={nb} q2_orbits={1 if no==16 else 0} q3_constructed={n3} formula_q3={6**6}')
