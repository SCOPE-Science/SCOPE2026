"""Exact integer checks for illumination of type-D root polytopes.

Run: python3 verify.py
Checks are finite corroboration of a separate dimension-free proof.
"""
from itertools import combinations, product


def roots(d):
    out = []
    for i,j in combinations(range(d),2):
        for a,b in product((-1,1),repeat=2):
            x = [0]*d
            x[i],x[j] = a,b
            out.append(tuple(x))
    return out


def facets(d):
    out = []
    for i in range(d):
        for sig in (-1,1):
            a = [0]*d
            a[i] = sig
            out.append((tuple(a),1))
    for s in product((-1,1),repeat=d):
        out.append((s,2))
    return out


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def vertex_illuminated(root, direction, facet_list):
    return all(dot(a,direction) < 0 for a,b in facet_list if dot(a,root)==b)


def pair_criterion(root,direction):
    ix = [i for i,z in enumerate(root) if z]
    i,j = ix
    return (root[i]*direction[i] < 0 and root[j]*direction[j] < 0
            and abs(direction[i])+abs(direction[j]) >
            sum(abs(direction[k]) for k in range(len(root)) if k not in ix))


def design(d):
    if d==3:
        return [tuple(1 if b==0 else -1 for b in row) for row in
                ((0,0,0),(0,1,1),(1,0,1),(1,1,0))]
    out = []
    for center in range(d):
        v = tuple((d if k==center else 1)*(1 if k>=center else -1)
                  for k in range(d))
        out.extend((v,tuple(-x for x in v)))
    return out


def main():
    tested = 0
    for d in range(3,9):
        R, F, U = roots(d), facets(d), design(d)
        assert len(R)==2*d*(d-1)
        assert len(U)==(4 if d==3 else 2*d)
        for v in R:
            assert all(dot(a,v)<=b for a,b in F)
            assert sum(dot(a,v)==b for a,b in F)==2+2**(d-2)
            hits = [u for u in U if vertex_illuminated(v,u,F)]
            assert len(hits)==1,(d,v,hits)
            tested+=len(U)
        for u in U:
            hits = [v for v in R if vertex_illuminated(v,u,F)]
            assert len(hits)==(3 if d==3 else d-1)
            assert all(pair_criterion(v,u) for v in hits)
            for v in R:
                assert vertex_illuminated(v,u,F)==pair_criterion(v,u)
        print('d=%s vertices=%s directions=%s per_direction=%s exact_cover=yes' %
              (d,len(R),len(U),(3 if d==3 else d-1)))
    checked=0
    for d in range(3,7):
        for w in product((1,2,3,4),repeat=d):
            heavy = [set(e) for e in combinations(range(d),2)
                     if 2*(w[e[0]]+w[e[1]])>sum(w)]
            assert len(heavy) <= (3 if d==3 else d-1)
            assert all(bool(e & f) for e,f in combinations(heavy,2))
            checked+=1
    print('EXACT_OK dimensions=3..8 incidence_checks=%s magnitude_profiles=%s' %
          (tested,checked))


if __name__=='__main__':
    main()
