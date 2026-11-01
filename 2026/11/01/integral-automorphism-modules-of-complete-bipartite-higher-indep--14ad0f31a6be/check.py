"""Finite signed-Lefschetz and Smith-form checks for bipartite higher-independence complexes.
Run: python check.py (requires sympy for integral Smith forms).
"""
from itertools import permutations, product
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def cycle_lengths(perm):
    seen = set(); out=[]
    for i in range(len(perm)):
        if i in seen: continue
        j=i; n=0
        while j not in seen:
            seen.add(j); j=perm[j]; n+=1
        out.append(n)
    return out


def poly_cycles(cycles, d):
    p=[1]+[0]*d
    for ell in cycles:
        s=(-1)**(ell+1) # factor 1-(-t)^ell
        for i in range(d,ell-1,-1):
            p[i]+=s*p[i-ell]
    return p


def divide_by_one_plus_t(poly):
    q=[]; prev=0
    for v in poly:
        w=v-prev; q.append(w); prev=w
    return q


def expected_character(a,b,r,pa,pb,exchange=False):
    if exchange:
        assert a==b
        full=[b+pb[i] for i in range(a)]+[pa[i] for i in range(a)]
        return divide_by_one_plus_t(poly_cycles(cycle_lengths(full),r))[r]
    full=list(pa)+[a+pb[j] for j in range(b)]
    pv=divide_by_one_plus_t(poly_cycles(cycle_lengths(full),r))
    pav=divide_by_one_plus_t(poly_cycles(cycle_lengths(pa),r))
    pbv=divide_by_one_plus_t(poly_cycles(cycle_lengths(pb),r))
    return pv[r]-pav[r]-pbv[r]


def face_is_valid(face,a,b,r):
    left=sum(i<a for i in face)
    right=len(face)-left
    return left==0 or right==0 or len(face)<=r


def inv_sign(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))


def reduced_lefschetz(a,b,r,p):
    n=a+b
    total=-1  # empty face contribution for reduced Lefschetz
    for mask in range(1,1<<n):
        face=[i for i in range(n) if mask>>i&1]
        if not face_is_valid(face,a,b,r): continue
        image=[p[i] for i in face]
        if sorted(image)==face:
            total+=(-1)**(len(face)-1)*inv_sign(image)
    return total


def coinvariants(a,b,exchange=False):
    pairs=list(product(range(a),range(b))); base=pairs[0]
    index={v:i for i,v in enumerate(pairs[1:])}
    n=len(index); gens=[]
    for z in range(a-1):
        gens.append((lambda p,z=z:(z+1 if p[0]==z else z if p[0]==z+1 else p[0],p[1]),1))
    for z in range(b-1):
        gens.append((lambda p,z=z:(p[0],z+1 if p[1]==z else z if p[1]==z+1 else p[1]),1))
    if exchange:
        assert a==b
        gens.append((lambda p:(p[1],p[0]),-1))
    cols=[]
    for transform,eps in gens:
        qbase=transform(base)
        for p in pairs[1:]:
            q=transform(p)
            col=[0]*n
            col[index[p]]+=1
            if q!=base: col[index[q]]-=eps
            if qbase!=base: col[index[qbase]]+=eps
            cols.append(col)
    m=Matrix(n,len(cols),lambda i,j:cols[j][i]); D=smith_normal_form(m,domain=ZZ)
    diagonal=[abs(int(D[i,i])) for i in range(min(D.shape))]
    return n-sum(v!=0 for v in diagonal), sorted(v for v in diagonal if v>1)


def run():
    cases=0; lefschetz_checks=0; ranks=0
    for a in range(2,6):
        for b in range(2,6):
            n=a+b
            pa_candidates=list(permutations(range(a))) if a<=3 else [tuple(range(a)),tuple(reversed(range(a))), tuple(list(range(1,a))+[0])]
            pb_candidates=list(permutations(range(b))) if b<=3 else [tuple(range(b)),tuple(reversed(range(b))), tuple(list(range(1,b))+[0])]
            for r in range(1,n):
                cases+=1
                expected_rank=comb(n-1,r)-(comb(a-1,r) if r<=a-1 else 0)-(comb(b-1,r) if r<=b-1 else 0)
                identity=tuple(range(n))
                observed=(-1)**(r-1)*reduced_lefschetz(a,b,r,identity)
                assert observed==expected_rank,(a,b,r,expected_rank,observed)
                ranks+=1
                for pa,pb in product(pa_candidates,pb_candidates):
                    p=list(pa)+[a+pb[j] for j in range(b)]
                    predicted=expected_character(a,b,r,pa,pb)
                    value=(-1)**(r-1)*reduced_lefschetz(a,b,r,p)
                    assert predicted==value,('nonexchange',a,b,r,pa,pb,predicted,value)
                    lefschetz_checks+=1
                if a==b:
                    for pa,pb in product(pa_candidates,pb_candidates):
                        p=[a+pb[i] for i in range(a)]+[pa[i] for i in range(a)]
                        predicted=expected_character(a,b,r,pa,pb,True)
                        value=(-1)**(r-1)*reduced_lefschetz(a,b,r,p)
                        assert predicted==value,('exchange',a,b,r,pa,pb,predicted,value)
                        lefschetz_checks+=1
    smith_tests=0
    for a in range(2,7):
        for b in range(2,7):
            got=coinvariants(a,b)
            exp=(0,[2]*((a==2)+(b==2)))
            assert got==exp,(a,b,got,exp)
            smith_tests+=1
        got=coinvariants(a,a,True)
        exp=(0,[2]) if a==2 else (0,[])
        assert got==exp,(a,got,exp)
        smith_tests+=1
    print('PASS',{'parameter_cases':cases,'signed_lefschetz':lefschetz_checks,'rank_checks':ranks,'integral_smith_tests':smith_tests})
if __name__=='__main__':run()
