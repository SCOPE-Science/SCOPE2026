"""Finite symbolic sanity checks for squarefree quartic gradient geometry.
Does not replace the all-parameter algebraic proof.
"""
from itertools import combinations
from sympy import symbols, expand, diff, Matrix, binomial
for n in (6,7):
    x=symbols('x0:'+str(n))
    F=expand(sum(__import__('functools').reduce(lambda a,b:a*b,(x[i] for i in S),1) for S in combinations(range(n),4)))
    grads=[diff(F,z) for z in x]
    # coordinate-line points are singular identically
    for i,j in combinations(range(n),2):
        for g in grads:
            assert expand(g.subs({x[k]:0 for k in range(n) if k not in (i,j)}))==0
    # generic two-support transverse Hessian rank n-2
    H=Matrix([[diff(diff(F,x[p]),x[q]).subs({x[0]:2,x[1]:3,**{x[k]:0 for k in range(2,n)}}) for q in range(2,n)] for p in range(2,n)])
    assert H.det()!=0 and H.det()==(-1)**(n-3)*(n-3)*6**(n-2)
    # No spurious singularity on selected supports >=3 over Q
    for v in ((1,2,3)+(0,)*(n-3), (1,1,1)+(0,)*(n-3), (1,2,3,4)+(0,)*(n-4), (1,)*n):
        assert any(g.subs(dict(zip(x,v))) !=0 for g in grads)
print('VERIFY_OK: symbolic 6- and 7-variable derivative tests; coordinate-line and transverse Hessian identities')
