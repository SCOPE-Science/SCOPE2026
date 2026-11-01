"""Exact-rational finite examples for polyhedral translation-depth stabilization.

Run: python verify_polyhedral_depth.py
All universality statements are proved analytically; these tests check explicit witnesses.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def inside_polytope(x, a_rows, bounds):
    return all(dot(a,x) <= b for a,b in zip(a_rows,bounds))

def check_case(name, a_rows, bounds, facets, dim, seed):
    rng = Random(seed)
    D = len(a_rows)
    assert all(dot(a,p) == bounds[j] for j,p in enumerate(facets) for a in [a_rows[j]])
    assert all(dot(a_rows[i],facets[j]) < bounds[i] for j in range(D) for i in range(D) if i!=j)
    count=0
    for run in range(10):
        points=[tuple(Q(rng.randint(-8,8),8) for _ in range(dim)) for k in range(12)]
        weights=[rng.randint(1,9) for k in points]
        for _ in range(70):
            y=tuple(Q(rng.randint(-20,20),8) for _ in range(dim))
            candidates=[]
            for j,u in enumerate(a_rows):
                q=dot(u,y)
                vals=[dot(u,x) for x in points]
                small=[v for v in vals if v<q]
                if not small:
                    candidates.append(0)
                    continue
                top=max(small)
                a=max(vals) if q>max(vals) else (top+q)/2
                assert a < q
                u2=dot(u,u)
                z=tuple(a*v/u2 for v in u)
                p=facets[j]
                t=Q(200)
                flag=[]
                for x in points:
                    memberships=[dot(ai, tuple(xk-zk+t*pk for xk,zk,pk in zip(x,z,p))) <=t*bi for ai,bi in zip(a_rows,bounds)]
                    flag.append(all(memberships))
                    assert flag[-1] == (dot(u,x)<=a), (name,j,x,a,y)
                assert not inside_polytope(tuple(yk-zk+t*pk for yk,zk,pk in zip(y,z,p)), a_rows, [t*b for b in bounds])
                amount=sum(w for w,v in zip(weights,vals) if v<q)
                assert amount==sum(w for w,valid in zip(weights,flag) if valid)
                candidates.append(amount)
                count+=1
            assert max(candidates)==max(sum(w for w,x in zip(weights,points) if dot(u,x)<dot(u,y)) for u in a_rows)
    return count


def main():
    sq_a=[(Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))]
    sq_b=[Q(1)]*4
    sq_p=[(Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))]
    tr_a=[(Q(-1),Q(0)),(Q(0),Q(-1)),(Q(1),Q(1))]
    tr_b=[Q(0),Q(0),Q(2)]
    tr_p=[(Q(0),Q(1)),(Q(1),Q(0)),(Q(1),Q(1))]
    dia_a=[(Q(1),Q(1)),(Q(-1),Q(-1)),(Q(1),Q(-1)),(Q(-1),Q(1))]
    dia_b=[Q(2)]*4
    dia_p=[(Q(1),Q(1)),(Q(-1),Q(-1)),(Q(1),Q(-1)),(Q(-1),Q(1))]
    o_a=[tuple(Q(v) for v in signs) for signs in product((-1,1), repeat=3)]
    o_b=[Q(1)]*8
    o_p=[tuple(v/Q(3) for v in u) for u in o_a]
    cases=[('square',sq_a,sq_b,sq_p,2),('triangle',tr_a,tr_b,tr_p,2),('diamond',dia_a,dia_b,dia_p,2),('octahedron',o_a,o_b,o_p,3)]
    total=0
    for i,(name,A,b,p,d) in enumerate(cases):
        c=check_case(name,A,b,p,d,101+i)
        print(name,':',c,'exact facet-witness comparisons')
        total+=c
    # Sharpness witness: a uniform 1D segment of width w=1 and a test interval shorter than w.
    # At y in (t*l,1), avoiding y captures at most t*l fraction, while
    # the directional halfspace left of y captures y fraction.
    for length in (Q(1,8),Q(1,3),Q(2,3),Q(7,8)):
        y=(length+1)/2
        assert length<y<1
        assert max(min(length,y),min(length,1-y)) < y
        total+=1
    print('PASS:',total,'exact checks and four sharpness witnesses')

if __name__=='__main__':main()
