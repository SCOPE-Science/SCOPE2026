"""Exhaustive finite-field incidence-profile check for affine-plane flat posets.

Only elementary finite-field arithmetic is used. Reproducibility check, not a
substitute for the incidence-axiom argument for arbitrary affine planes.
"""
import itertools
from collections import defaultdict


def field(q):
    if q in (2, 3, 5, 7):
        return (lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q)
    if q not in (4, 9):
        raise ValueError(q)
    p=2 if q==4 else 3
    def digits(x):return (x%p,x//p)
    def add(a,b):
        x,y=digits(a);z,w=digits(b)
        return (x+z)%p + p*((y+w)%p)
    def mul(a,b):
        x,y=digits(a);z,w=digits(b)
        # t^2 = t + 1 over F_2; t^2 = -1 over F_3
        const=(x*z + (y*w if p==2 else -y*w))%p
        coef=(x*w+y*z+(y*w if p==2 else 0))%p
        return const+p*coef
    return add,mul


def flats(q):
    add,mul=field(q)
    pts=list(itertools.product(range(q),repeat=2))
    lines=[]
    for a,b in [(0,1)]+[(1,m) for m in range(q)]:
        for c in range(q):
            lines.append(frozenset(i for i,(x,y) in enumerate(pts)
                if add(mul(a,x),mul(b,y))==c))
    assert len(lines)==q*(q+1) and len(set(lines))==len(lines)
    assert all(len(L)==q for L in lines)
    return [frozenset()]+[frozenset({i}) for i in range(q*q)]+lines+[frozenset(range(q*q))]


def rank(flat,q):
    n=len(flat)
    return {0:0,1:1,q:2,q*q:3}[n]


def pt(A,B,q):
    ra,rb=rank(A,q),rank(B,q)
    if A==B: state='equal'
    elif A<B:state='subset'
    elif A>B:state='superset'
    elif ra==rb==2:state='parallel' if not (A&B) else 'intersect'
    else:state='incomparable'
    return (ra,rb,state)


def profile(q):
    F=flats(q);n=len(F)
    type_ids={}
    types=[[] for _ in range(n)]
    for i in range(n):
        types[i]=[pt(F[i],F[j],q) for j in range(n)]
    for i in range(n):
        for j in range(n):
            anchor=types[i][j]
            support=frozenset((types[i][k],types[j][k]) for k in range(n))
            if anchor in type_ids:
                assert type_ids[anchor]==support, ('anchor not uniform',q,anchor)
            else:
                type_ids[anchor]=support
    return type_ids,n


def main():
    ref=None
    for q in [2,3,4,5,7,9]:
        d,n=profile(q)
        total=sum(len(s) for s in d.values())
        assert len(d)==21
        assert total==(144 if q==2 else 148), (q,total)
        if q==2:small=d
        else:
            if ref is None:ref=d
            assert d==ref, ('different extension table',q)
        print('q=%d flats=%d pair_types=%d extension_patterns=%d' % (q,n,len(d),total))
    mismatch={a:(ref[a]-small[a]) for a in ref if ref[a]!=small[a]}
    assert sum(map(len,mismatch.values()))==4
    assert set(mismatch)=={(1,2,'incomparable'),(2,1,'incomparable'),(2,2,'parallel')}
    print('exceptional pair types:',sorted(map(str,mismatch)))
    print('PROFILE_CHECK_OK')

if __name__=='__main__':main()
