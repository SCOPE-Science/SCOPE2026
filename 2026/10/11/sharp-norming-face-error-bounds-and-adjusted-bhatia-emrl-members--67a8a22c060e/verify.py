"""Exact rational stress tests for real L1 norming-face stability.
Finite experiments test algebraic identities, not the infinite-dimensional proof.
"""
from fractions import Fraction as Q
from itertools import product

VALUES = (Q(-1), Q(-3,4), Q(-1,2), Q(0), Q(1,2), Q(3,4), Q(1))

def parts(total, length):
    if length == 0:
        if total == 0: yield ()
        return
    for j in range(total+1):
        for tail in parts(total-j, length-1): yield (j,)+tail

def signed_mass(n, denom=4):
    for a in product(range(-denom,denom+1), repeat=n):
        if sum(map(abs,a)) == denom:
            yield tuple(Q(x,denom) for x in a)

def exact_face_distance(v,g):
    good = [i for i,t in enumerate(g) if abs(t)==1 and v[i]*t>0]
    mass = sum((abs(v[i]) for i in good),Q(0))
    return 2*(1-mass)

def brute_face_distance(v,g,denom=4):
    a = [i for i,t in enumerate(g) if abs(t)==1]
    best = None
    for z in parts(denom,len(a)):
        y = [Q(0)]*len(g)
        for i,k in zip(a,z): y[i] = Q(k,denom)*(1 if g[i]>0 else -1)
        dist=sum(map(abs,(v[i]-y[i] for i in range(len(g)))),Q(0))
        if best is None or dist < best: best=dist
    return best

def run():
    comparisons=0; sharpness=0; cases=0
    for n in (2,3):
        for g in product(VALUES, repeat=n):
            if max(map(abs,g)) != 1: continue
            cases+=1
            A=[i for i,t in enumerate(g) if abs(t)==1]
            B=[i for i,t in enumerate(g) if abs(t)!=1]
            for v in signed_mass(n):
                d=exact_face_distance(v,g)
                assert brute_face_distance(v,g)==d,(g,v,d)
                e=1-sum((g[i]*v[i] for i in range(n)),Q(0))
                assert e>=0
                if B:
                    r=max(abs(g[i]) for i in B)
                    assert d*(1-r) <=2*e,(g,v)
                else:
                    assert d == e,(g,v)
                comparisons+=1
            if B:
                r=max(abs(g[i]) for i in B)
                for j in B:
                    if abs(g[j])==r:
                        v=[Q(0)]*n
                        v[j]=Q(1) if g[j]>=0 else Q(-1)
                        d=exact_face_distance(v,g)
                        e=1-sum(g[i]*v[i] for i in range(n))
                        assert d==2 and d/e==Q(2)/(1-r)
                        sharpness+=1
                        break
    print(f'VERIFY_OK finite_functionals={cases} exact_face_distances={comparisons} sharp_ratio_witnesses={sharpness} infinite_case_requires_proof=True')

if __name__ == '__main__': run()
