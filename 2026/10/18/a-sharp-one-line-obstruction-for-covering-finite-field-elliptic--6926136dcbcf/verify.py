#!/usr/bin/env python3
"""Finite exact checks for the elliptic line-covering theorem.

Only checks explicit finite witnesses; the infinite argument is in RESULT.md.
No third-party dependencies required.
"""

def cyclic_triples(m):
    if m % 2:
        pair = [(a, a, (-2*a-1)%m) for a in range(m)]
    else:
        k=m//2
        pair = [(a, a if a < k else a+1,
                 (-a-(a if a < k else a+1)-1)%m)
                for a in range(m-1)]
    return [tuple((3*a, 3*b+1, 3*c+2)) for a,b,c in pair]

def check_cyclic(m):
    n=3*m
    ts=cyclic_triples(m)
    assert len(ts)==(m if m%2 else m-1)
    assert all(len(set(t))==3 and sum(t)%n==0 for t in ts)
    flat=[x for t in ts for x in t]
    assert len(set(flat))==len(flat)
    remaining=set(range(n))-set(flat)
    if m%2:
        assert remaining==set()
    else:
        assert remaining=={3*(m-1),3*(m//2)+1,2}
        assert sum(remaining)%n==n//2
    return len(ts),len(remaining)

def points(p,a,b):
    return [None]+[(x,y) for x in range(p) for y in range(p)
                   if (y*y-x*x*x-a*x-b)%p==0]

def add(P,Q,p,a):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u and (y+v)%p==0:return None
    if P==Q:
        assert (2*y)%p!=0
        slope=((3*x*x+a)*pow(2*y,-1,p))%p
    else:
        slope=((v-y)*pow((u-x)%p,-1,p))%p
    xx=(slope*slope-x-u)%p
    return (xx,(slope*(x-xx)-y)%p)

def multiply(P,k,p,a):
    R=None
    while k:
        if k&1:R=add(R,P,p,a)
        P=add(P,P,p,a);k//=2
    return R

def check_curve(p,a,b,expected_n,expected_torsion):
    assert (4*a*a*a+27*b*b)%p
    ps=points(p,a,b)
    n=len(ps)
    assert n==expected_n and n%3==0
    torsion=[P for P in ps if add(P,P,p,a)is None]
    assert len(torsion)==expected_torsion
    # For unique-involution examples, check a point of order n exists
    # so each cyclic symbolic triple corresponds to a genuine geometric trisecant.
    if expected_torsion==2:
        factors=[r for r in range(2,n+1) if n%r==0 and
                 all(r%d for d in range(2,int(r**.5)+1))]
        G=next((P for P in ps[1:] if all(multiply(P,n//r,p,a) is not None
                                       for r in factors)),None)
        assert G is not None
        index=[multiply(G,i,p,a) for i in range(n)]
        assert set(index)==set(ps)
        for t in cyclic_triples(n//3):
            A,B,C=(index[i] for i in t)
            assert add(add(A,B,p,a),C,p,a)is None
            assert len({A,B,C})==3
            # Verify the three projective points lie on one actual F_p-line.
            vec=lambda P: (0,1,0) if P is None else (P[0],P[1],1)
            (x,y,z),(u,v,w),(r,s,t)=(vec(A),vec(B),vec(C))
            assert (x*(v*t-w*s)-y*(u*t-w*r)+z*(u*s-v*r))%p==0
    return n,len(torsion)

def main():
    for m in range(1,201): check_cyclic(m)
    # Smooth cyclic examples: y^2=x^3+a*x+b over prime fields.
    samples=[(5,0,1,6,2), (7,3,1,12,2),
             (11,1,3,18,2), (17,1,2,24,2)]
    observed=[(p,check_curve(p,a,b,n,t)) for p,a,b,n,t in samples]
    # Also verify a complete zero-sum triple partition in a noncyclic
    # full rational 2-torsion example of order 12.
    p,a,b=7,0,1
    pp=points(p,a,b)
    assert len(pp)==12
    assert sum(add(P,P,p,a)is None for P in pp)==4
    def partition(mask):
        if mask==0:return []
        i=(mask & -mask).bit_length()-1
        for j in range(i+1,len(pp)):
            if not mask&(1<<j):continue
            for k in range(j+1,len(pp)):
                if not mask&(1<<k):continue
                if add(add(pp[i],pp[j],p,a),pp[k],p,a) is not None:continue
                tail=partition(mask ^ (1<<i) ^ (1<<j) ^ (1<<k))
                if tail is not None:return [(i,j,k)]+tail
        return None
    partition4=partition((1<<len(pp))-1)
    assert partition4 is not None and len(partition4)==4
    print('PASS: cyclic covers for 1<=m<=200; unique-involution examples:',observed)
    print('PASS: full 2-torsion noncyclic example: p=7, y^2=x^3+1, 12 points, 4 zero-sum triples')

if __name__=='__main__': main()
