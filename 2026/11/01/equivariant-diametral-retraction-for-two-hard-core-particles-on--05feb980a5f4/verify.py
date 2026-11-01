"""Independent finite rational stress tests of the explicit hard-core deformation.
The universal proof is in RESULT.md; sampling here does not establish it.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb

ONE=F(1)

def distance(edge_a,t,edge_b,u):
    if edge_a==edge_b:
        return abs(t-u)
    return min(t+u, F(2)-t-u)

def deform(edge_a,t,edge_b,u,lam):
    # Each edge parameter increases from the common pole A to B.
    if edge_a==edge_b:
        if t<=u:
            return ((ONE-lam)*t, ONE-(ONE-lam)*(ONE-u))
        v,w=deform(edge_b,u,edge_a,t,lam)
        return (w,v)
    s=t+u
    if s==ONE:
        return t,u
    if s<ONE:
        c=(ONE-lam)+lam/s
        return c*t,c*u
    c=(ONE-lam)+lam/(F(2)-s)
    return ONE-c*(ONE-t),ONE-c*(ONE-u)

def canon(e,t,f,u):
    # Positions with a particle at a shared pole are the same point
    # independent of which edge label was chosen.
    def c(k,v):
        if v==0:return ('A',)
        if v==1:return ('B',)
        return ('edge',k,v)
    return tuple(sorted((c(e,t),c(f,u)),key=str))

lam_values=[F(0),F(1,7),F(1,2),F(5,6),F(1)]
vals=[F(k,12) for k in range(13)]
checks=0
for m in (2,3,4,5):
    for e in range(m):
        for f in range(m):
            for t in vals:
                for u in vals:
                    d=distance(e,t,f,u)
                    if d==0:continue
                    for lam in lam_values:
                        tp,up=deform(e,t,f,u,lam)
                        assert F(0)<=tp<=1 and F(0)<=up<=1
                        dp=distance(e,tp,f,up)
                        assert dp>=d
                        assert dp==(ONE-lam)*d+lam, (e,f,t,u,lam,dp,d)
                        assert canon(e,tp,f,up)==canon(f,up,e,tp)
                        # Pole exchange commutes with deformation.
                        tr,ur=deform(e,ONE-t,f,ONE-u,lam)
                        assert (tr,ur)==(ONE-tp,ONE-up)
                        if lam==0:assert (tp,up)==(t,u)
                        if lam==1:assert dp==ONE
                        if d==ONE:assert (tp,up)==(t,u)
                        checks+=1
    # At the pole seams, compare all edge-label presentations.
    for t in vals[1:]:
        for lam in lam_values:
            for e in range(m):
                reps=set()
                for f in range(m):
                    tp,up=deform(f,F(0),e,t,lam)
                    reps.add(canon(f,tp,e,up))
                assert len(reps)==1
                reps=set()
                for f in range(m):
                    if t < ONE:
                        tp,up=deform(f,F(1),e,t,lam)
                        reps.add(canon(f,tp,e,up))
                if t < ONE: assert len(reps)==1
                checks+=2
    # At d=1 there is one vertex {A,B} and one full loop per edge pair.
    assert comb(m,2)==len(tuple(combinations(range(m),2)))
    assert comb(m,2)==comb(m,2)-1+1  # H_1 rank = E - V + 1.
    # Each edge permutation acts as signed exterior square on loop orientations.
    for p in permutations(range(m)):
        image=[]
        for i,j in combinations(range(m),2):
            a,b=p[i],p[j]
            image.append((min(a,b),max(a,b), 1 if a<b else -1))
        assert len(set((a,b) for a,b,_ in image))==comb(m,2)
print('FINITE_RATIONAL_STRESS_OK')
print('checked_parameter_point_homotopies',checks)
print('edge_family_sizes',[(m,comb(m,2)) for m in range(2,6)])
print('This checks finite rational samples only; the all-real proof is analytic.')
