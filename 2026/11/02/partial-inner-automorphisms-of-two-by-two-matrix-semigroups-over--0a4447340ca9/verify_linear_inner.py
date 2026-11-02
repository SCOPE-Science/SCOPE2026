"""Independent finite-field checks of partial inner automorphism monoids of M_2(F_p).
Reproducible with Python 3 and no external dependencies.
"""
from itertools import product

def check(p):
    mats=list(product(range(p),repeat=4))
    idx={x:i for i,x in enumerate(mats)}
    n=len(mats)
    mult=[]
    for a,b,c,d in mats:
        mult.append([idx[((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)] for e,f,g,h in mats])
    z=idx[(0,0,0,0)]
    ident=idx[(1,0,0,1)]
    dom=[]
    for P in range(n):
        dom.append(tuple(A for A in range(n) if mult[P][A]==A==mult[A][P]))
    generators={}
    for g in range(n):
        for h in range(n):
            d=dom[mult[g][h]]
            signature=tuple((a,mult[h][mult[a][g]]) for a in d)
            generators[signature]=True
    maps=list(generators)
    expected_group=p*(p*p-1)
    ni=p*(p+1)
    nn=p+1
    expected=1+expected_group+ni*ni+(p-1)*nn*nn
    by_size={k:sum(len(v)==k for v in maps) for k in [1,p,n]}
    assert len(maps)==expected,(p,len(maps),expected)
    assert by_size == {1:1,p:ni*ni+(p-1)*nn*nn,n:expected_group},(p,by_size)
    # Composition verification, with a map represented as ordered (domain,image) pairs.
    sigset=set(maps)
    for left in maps:
        ld=dict(left)
        for right in maps:
            rd=dict(right)
            composed=tuple((a,rd[b]) for a,b in left if b in rd)
            assert composed in sigset,(p,left,right,composed)
    print('VERIFY_OK',{'p':p,'matrix_count':n,'generators_considered':n*n,
                       'different_partial_inner_maps':len(maps),
                       'domain_size_distribution':by_size,
                       'complete_composition_pairs_tested':len(maps)**2})
if __name__=='__main__':
    check(2)
    check(3)
