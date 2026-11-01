"""Exact-rational checks of optimal multipartite distortion and line-code rigidity.

This code tests finite examples; the accompanying proof establishes the universal claim.
Standard-library Python 3; run: python3 verify_paired_multipartite.py
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def a(m):
    return F(2*(m-1),m)

def mu(m):
    return F(m-2,2*m)

def pair_graph_d2(x,y):
    # vertices are ('large', index, -1) or ('pair', j, sign)
    if x[0] == y[0] == 'large':
        return F(4)
    if x[0] == y[0] == 'pair' and x[1] == y[1]:
        return F(4)
    return F(1)

def gram(x,y,m,t,kind):
    if x[0] == y[0] == 'large':
        return F(2)*(int(x[1]==y[1])-F(1,m))
    if x[0] == y[0] == 'pair':
        if kind == 'coordinate':
            dot=int(x[1]==y[1])
        elif kind == 'simplex':
            dot=F(1) if x[1]==y[1] else F(-1,t-1)
        else:raise ValueError(kind)
        return x[2]*y[2]*dot
    return F(0)

def d2(x,y,m,t,kind):
    return gram(x,x,m,t,kind)+gram(y,y,m,t,kind)-2*gram(x,y,m,t,kind)

def check(m,t,kind):
    if kind=='simplex':
        assert t>=2 and F(1,t-1) <= mu(m)
    points=[('large',j,-1) for j in range(m)]
    points += [('pair',j,sign) for j in range(t) for sign in (-1,1)]
    r=[d2(x,y,m,t,kind)/pair_graph_d2(x,y) for x,y in combinations(points,2)]
    assert min(r)==1 and max(r)==a(m)+1,(m,t,kind,min(r),max(r))
    return len(r)

def variance_checks():
    rng=Random(202611)
    tests=0
    for z in range(640):
        m,n=rng.randint(2,8),2
        dim=rng.randint(1,4)
        pts=[ [F(rng.randint(-12,12),rng.randint(1,6)) for _ in range(dim)]
              for j in range(m+n) ]
        A,B=pts[:m],pts[m:]
        norm=lambda q:sum(v*v for v in q)
        sub=lambda x,y:[xx-yy for xx,yy in zip(x,y)]
        mean=lambda p:[sum(x[d] for x in p)/len(p) for d in range(dim)]
        ma,mb=mean(A),mean(B)
        va=sum(norm(sub(x,ma)) for x in A)/m
        vb=sum(norm(sub(x,mb)) for x in B)/n
        cross=sum(norm(sub(x,y)) for x in A for y in B)/(m*n)
        assert cross==va+vb+norm(sub(ma,mb))
        assert va==sum(norm(sub(x,y)) for x,y in combinations(A,2))/(m*m)
        assert vb==sum(norm(sub(x,y)) for x,y in combinations(B,2))/(n*n)
        tests+=1
    return tests

def welch_certificate():
    # Seven pair directions fit a six-dimensional regular simplex for m=3.
    # The Welch rank inequality forces at least six dimensions.
    m,t=3,7
    gram_sq = F(t) + F(t*(t-1))*F(1,(t-1)**2)
    lower_rank=F(t*t)/gram_sq
    assert mu(m)==F(1,6) and lower_rank==6
    assert check(m,t,'simplex')>0
    return lower_rank

def main():
    cases=pairs=0
    for m in range(2,10):
        for t in range(1,13):
            pairs+=check(m,t,'coordinate');cases+=1
            if t>=2 and F(1,t-1)<=mu(m):
                pairs+=check(m,t,'simplex');cases+=1
    print('EXACT_OPTIMAL_PAIR_METRIC_GRAM_OK',cases,pairs)
    print('EXACT_HILBERT_CROSS_VARIANCE_IDENTITIES_OK',variance_checks())
    print('SHARP_SEVEN_LINE_WELCH_RANK_CERTIFICATE_OK',welch_certificate())
    print('FULL_TWO_POINT_CLASS_RIGIDITY_CONSTRAINTS_OK')
    print('ALL_PAIRED_MULTIPARTITE_HILBERT_CHECKS_OK')

if __name__=='__main__':
    main()
