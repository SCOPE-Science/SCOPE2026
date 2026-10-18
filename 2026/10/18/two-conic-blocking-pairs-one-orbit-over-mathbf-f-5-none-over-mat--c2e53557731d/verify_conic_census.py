"""Exact normalized-coefficient census of smooth conic-pair blocking incidence.

The field orders are 5 and 7. No randomized search or geometric
smoothness sampling is involved. Run: python verify_conic_census.py.
"""
from itertools import product


def normalized_vectors(q, dimension):
    for leading in range(dimension):
        for tail in product(range(q), repeat=dimension-leading-1):
            yield (0,)*leading+(1,)+tail


def quadratic(v, p, q):
    x,y,z=p
    a,b,c,d,e,f=v
    return (a*x*x+b*x*y+c*x*z+d*y*y+e*y*z+f*z*z)%q


def smooth(v, q):
    a,b,c,d,e,f=v
    A,B,C=2*a,b,c
    D,E,F=b,2*d,e
    G,H,I=c,e,2*f
    return (A*(E*I-F*H)-B*(D*I-F*G)+C*(D*H-E*G))%q != 0


def census(q):
    ps=list(normalized_vectors(q,3))
    lines=[sum(1<<i for i,(x,y,z) in enumerate(ps) if (a*x+b*y+c*z)%q==0) for a,b,c in ps]
    def points(v):
        return sum(1<<i for i,p in enumerate(ps) if quadratic(v,p,q)==0)
    original=(0,0,1,(-1)%q,0,0)
    F0=points(original)
    assert smooth(original,q) and F0.bit_count()==q+1
    uncovered=[m for m in lines if not m&F0]
    accepted=[]
    n_smooth=0
    for v in normalized_vectors(q,6):
        if not smooth(v,q):
            continue
        n_smooth+=1
        candidate=points(v)
        if all(candidate & line for line in uncovered):
            accepted.append((v,(candidate&F0).bit_count(),(candidate|F0).bit_count()))
    assert n_smooth==q**5-q**2
    return n_smooth,accepted

if __name__=='__main__':
    n5,a5=census(5)
    n7,a7=census(7)
    assert len(a5)==12 and all(inter==1 and size==11 for _,inter,size in a5),a5
    assert len(a7)==0,a7
    print('q=5: smooth conics',n5,'blocking mates for fixed conic',len(a5), 'pairs total',n5*len(a5)//2)
    print('q=5: intersection profile',sorted(set((k,s) for _,k,s in a5)))
    print('q=7: smooth conics',n7,'blocking mates for fixed conic',len(a7))
    print('PASS')
