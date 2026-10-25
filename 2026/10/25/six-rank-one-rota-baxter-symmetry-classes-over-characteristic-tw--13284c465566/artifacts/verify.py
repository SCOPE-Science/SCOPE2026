#!/usr/bin/env python3
"""Direct finite-field checks for rank-one Rota--Baxter maps on exterior algebra E(2).
No external packages. Run: python verify.py
"""
from itertools import product
from collections import Counter


def mul(a, b, p):
    return ((a[0]*b[0])%p,
            (a[0]*b[1]+a[1]*b[0])%p,
            (a[0]*b[2]+a[2]*b[0])%p,
            (a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])%p)

def add(a,b,p):return tuple((x+y)%p for x,y in zip(a,b))
def scale(a,c,p):return tuple((c*x)%p for x in a)
def dot(a,b,p):return sum(x*y for x,y in zip(a,b))%p

def rank_one(v,phi,p):
    return tuple(scale(v,phi[i],p) for i in range(4))

def eval_R(R,a,p):
    out=(0,0,0,0)
    for i,k in enumerate(a):
        out=add(out,scale(R[i],k,p),p)
    return out

def is_rb(R,p):
    for a in BASIS:
        for b in BASIS:
            ra=eval_R(R,a,p);rb=eval_R(R,b,p)
            lhs=mul(ra,rb,p)
            rhs=eval_R(R,add(mul(ra,b,p),mul(a,rb,p),p),p)
            if lhs!=rhs:return False
    return True

def canonical_lines(p):
    for v in product(range(p),repeat=4):
        if not any(v):continue
        first=next(x for x in v if x)
        if first==1:yield v

def maps_rank_one(p):
    nonzero=(v for v in product(range(p),repeat=4) if any(v))
    for v in canonical_lines(p):
        for phi in product(range(p),repeat=4):
            if any(phi):yield rank_one(v,phi,p)

def matrix_col_map(cols,v,p):
    return tuple(sum(v[j]*cols[j][i] for j in range(4))%p for i in range(4))

def inv_matrix(cols,p):
    a=[[cols[j][i] for j in range(4)]+[int(i==j) for j in range(4)] for i in range(4)]
    for i in range(4):
        k=next(k for k in range(i,4) if a[k][i]%p)
        a[i],a[k]=a[k],a[i]
        v=pow(a[i][i],-1,p)
        a[i]=[(t*v)%p for t in a[i]]
        for j in range(4):
            if j!=i:
                v=a[j][i]
                a[j]=[(a[j][t]-v*a[i][t])%p for t in range(8)]
    return tuple(tuple(a[i][j+4] for j in range(4)) for i in range(4))

def act(R,g,gi,p):
    # columns of g; gi is row-major inverse
    out=[]
    for j in range(4):
        rcol=tuple(sum(gi[i][j]*R[i][k] for i in range(4))%p for k in range(4))
        out.append(matrix_col_map(g,rcol,p))
    return tuple(out)

def aut_group(p):
    for a,b,c,d,u,v in product(range(p),repeat=6):
        det=(a*d-b*c)%p
        if not det:continue
        g=((1,0,0,0),(0,a,c,u),(0,b,d,v),(0,0,0,det))
        yield g,inv_matrix(g,p)

def invariant(R):
    # image in radical-square, R(1), R(radical) nonzero
    return ('socle' if all(col[1]==col[2]==0 for col in R) else 'nonsocle',
            'one' if any(R[0]) else 'no_one',
            'rad' if any(any(col) for col in R[1:]) else 'no_rad')

BASIS=tuple(tuple(int(i==j) for i in range(4)) for j in range(4))

def check(p):
    passed={R for R in maps_rank_one(p) if is_rb(R,p)}
    by_inv=Counter(invariant(R) for R in passed)
    q=p
    expected={('socle','one','no_rad'):q-1,
             ('socle','no_one','rad'):q*q-1,
             ('socle','one','rad'):(q-1)*(q*q-1),
             ('nonsocle','one','no_rad'):(q*q+q)*(q-1),
             ('nonsocle','no_one','rad'):(q*q+q)*(q-1),
             ('nonsocle','one','rad'):(q*q+q)*(q-1)**2}
    assert by_inv==Counter(expected),(p,by_inv,expected)
    total=q**4+2*q**3-q*q-q-1
    assert len(passed)==total,(p,len(passed),total)
    representative={}
    for R in passed:representative.setdefault(invariant(R),R)
    group=list(aut_group(p))
    assert len(group)==p*p*(p*p-1)*(p*p-p),len(group)
    for key,rep in representative.items():
        orbit={act(rep,g,gi,p) for g,gi in group}
        assert orbit<=passed
        assert orbit=={R for R in passed if invariant(R)==key},(p,key,len(orbit),expected[key])
    print('q=',p,'rank1=',len(passed),'orbit_sizes=',sorted(expected.values()),'automorphisms=',len(group))

if __name__=='__main__':
    for p in (2,3):check(p)
    print('VERIFY_OK')
