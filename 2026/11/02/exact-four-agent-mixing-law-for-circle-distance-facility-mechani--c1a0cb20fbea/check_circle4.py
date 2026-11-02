"""Exact-rational independent checks for a four-report circle facility rule.

Requires Python 3.10+ standard library only. Run: python check_circle4.py
All coordinates are fractions of the circle circumference.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from random import Random

ONE = Q(1)

def d(a, b):
    z = abs(a-b)
    return min(z, ONE-z)

def costs(points):
    return [sum(d(a,b) for b in points) for a in points]

def rd_cost(points):
    return sum(costs(points), Q(0)) / len(points)

def pcd3_full_cost(survivors, full):
    ordered = sorted((x%ONE for x in survivors))
    assert len(ordered) == 3
    if ordered[0] == ordered[2]:
        return sum(d(ordered[0],y) for y in full)
    gaps = [(ordered[(i+1)%3]-ordered[i])%ONE for i in range(3)]
    return sum(gaps[(i+1)%3]*sum(d(x,y) for y in full)
               for i,x in enumerate(ordered))

def epcd_delete_cost(points):
    assert len(points)==4
    return sum((pcd3_full_cost([p for j,p in enumerate(points) if j!=i],points)
                for i in range(4)), Q(0)) / 4

def epcd_gap_cost(points):
    points=sorted((x%ONE for x in points))
    if points[0] == points[-1]:
        return sum(d(points[0],y) for y in points)
    gaps=[(points[(i+1)%4]-points[i])%ONE for i in range(4)]
    weights=[(gaps[(i+1)%4]+gaps[(i+2)%4])/2 for i in range(4)]
    assert sum(weights,Q(0))==ONE
    return sum((a*b for a,b in zip(weights,costs(points))),Q(0))

def shifted_param_check(a,b,c):
    """Reconstruct the separate three-case algebra independently of enumeration."""
    assert Q(0)<=a<=Q(1,2) and Q(0)<=b<=c<=Q(1,2)
    pts=[-a,Q(0),b,c]
    # -a may be negative but circle distances are still well-defined.
    actual=5*(a+b+c)-4*epcd_delete_cost(pts)
    if a+c<=Q(1,2):
        u=a+c
        rhs=u*(1-2*u)+2*(c-a-b)**2+2*b*b+b
        assert rhs>=0
        regime=0
    elif a+b<=Q(1,2):
        s=a+b;t=s+c
        rhs=t*(2*t-1)+2*(s-c)**2
        assert rhs>=0
        regime=1
    else:
        s=a+b
        rhs=4*s*s+3*s+4*c*c-c-2
        assert rhs>=Q(7,16)
        regime=2
    assert actual==rhs,(pts,actual,rhs)
    return regime

def verify(points):
    p=sorted(points)
    ep=epcd_delete_cost(p)
    assert ep==epcd_gap_cost(p), (p,ep,epcd_gap_cost(p))
    ds=costs(p)
    opt=min(ds)
    rd=rd_cost(p)
    assert 4*ep<=5*opt,(p,'epcd',ep,opt)
    assert 2*rd<=3*opt,(p,'rd',rd,opt)
    mix=(rd+ep)/2
    assert 8*mix<=11*opt,(p,'mrp',mix,opt)
    return opt,rd,ep

def main():
    total=0; maxratio=Q(0); equality=[]
    for denominator in (24,36,48):
        count=0
        for aa,bb,cc in combinations_with_replacement(range(denominator),3):
            p=[Q(0),Q(aa,denominator),Q(bb,denominator),Q(cc,denominator)]
            opt,rd,ep=verify(p)
            if opt:
                ratio=(rd+ep)/(2*opt)
                if ratio>maxratio: maxratio=ratio
                if 8*(rd+ep)==22*opt: equality.append((denominator,aa,bb,cc))
            count+=1
        total+=count
        print('grid',denominator,'profiles',count)
    rng=Random(20261030)
    for j in range(6500):
        den=rng.randrange(2,420)
        p=[Q(rng.randrange(den),den) for _ in range(4)]
        opt,rd,ep=verify(p)
        lam=Q(rng.randrange(101),100)
        assert 4*(lam*rd+(1-lam)*ep)<=(5+lam)*opt
        total+=1
    # Reproduce each of the polynomial case identities at independent rational inputs.
    cases=[0,0,0]
    for a_num in range(21):
        for b_num in range(21):
            for c_num in range(b_num,21):
                k=shifted_param_check(Q(a_num,40),Q(b_num,40),Q(c_num,40))
                cases[k]+=1
    special=[Q(0),Q(0),Q(1,4),Q(3,4)]
    opt,rd,ep=verify(special)
    assert (opt,rd,ep)==(Q(1,2),Q(3,4),Q(5,8))
    assert (rd+ep)/(2*opt)==Q(11,8)
    for lam in (Q(0),Q(1,7),Q(1,2),Q(3,4),Q(1)):
        assert (lam*rd+(1-lam)*ep)/opt==(5+lam)/4
    print('independent profiles tested',total)
    print('symbolic case identity parameter checks',cases,'total',sum(cases))
    print('largest grid half-mixture ratio',maxratio)
    print('grid sharp witnesses',equality[:12],'number',len(equality))
    print('sharp profile opt, RD, EPCD',opt,rd,ep)
    print('PASS exact rational checks')

if __name__=='__main__':
    main()
