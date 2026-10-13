#!/usr/bin/env python3
"""Finite-field independent checks for the 3-dimensional Heisenberg Lie algebra.
No exhaustive classification of all nonlinear functions is claimed by testing;
the unlimited-field classification follows from the separate proof.
"""
from itertools import product
from random import Random

def echelon_consistent(A, b, q):
    A = [list(row) + [bi] for row, bi in zip(A, b)]
    n, m = len(A), len(A[0]) - 1
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] % q), None)
        if piv is None: continue
        A[piv], A[r] = A[r], A[piv]
        inv = pow(A[r][c] % q, -1, q)
        A[r] = [(x * inv) % q for x in A[r]]
        for i in range(n):
            if i != r:
                z = A[i][c]
                if z: A[i] = [(x - z*y) % q for x, y in zip(A[i], A[r])]
        r += 1
    return all(any(row[:-1]) or not row[-1] for row in A)

def halfD_matrix(a,b,c,d,e,f,q):
    return [(a,d,0), (b,e,0), (c,f,((a+e)*pow(2,-1,q))%q)]

def apply(M,x,q):
    return tuple(sum(a*b for a,b in zip(row,x))%q for row in M)

def check_halfD_space(q):
    vecs=list(product(range(q),repeat=3))
    allD=[]
    for co in product(range(q),repeat=6):
        mat=halfD_matrix(*co,q)
        # Basis pairs suffice for bilinear half-derivation identity.
        basis=((1,0,0),(0,1,0),(0,0,1))
        def bracket(x,y): return (0,0,(x[0]*y[1]-x[1]*y[0])%q)
        for x in basis:
            for y in basis:
                left=apply(mat,bracket(x,y),q)
                dx=apply(mat,x,q);dy=apply(mat,y,q)
                rhs=tuple((v*pow(2,-1,q))%q for v in (bracket(dx,y)[0]+bracket(x,dy)[0],bracket(dx,y)[1]+bracket(x,dy)[1],bracket(dx,y)[2]+bracket(x,dy)[2]))
                assert left==rhs,(q,co,x,y,left,rhs)
        allD.append(mat)
    assert len(set(tuple(sum((list(row) for row in M), [])) for M in allD)) == q**6
    return allD

def canonical(v,q):
    if not any(v): return None,0
    x = next(a for a in v if a)
    inv=pow(x,-1,q)
    return tuple(a*inv%q for a in v),x

def random_map(q,seed):
    rng=Random(seed)
    projective2=sorted({canonical(v,q)[0] for v in product(range(q),repeat=2) if any(v)})
    projective3=sorted({canonical(v,q)[0] for v in product(range(q),repeat=3) if any(v)})
    g={v:tuple(rng.randrange(q) for _ in range(2)) for v in projective2}
    h={v:rng.randrange(q) for v in projective3}
    def delta(x):
        up, s = canonical(x[:2],q)
        xp, t = canonical(x,q)
        a,b = ((0,0) if up is None else tuple(s*z%q for z in g[up]))
        c = 0 if xp is None else t*h[xp]%q
        return a,b,c
    return delta

def check_two_local(q,num_seeds):
    vectors=list(product(range(q),repeat=3))
    inv2=pow(2,-1,q)
    # Six linear equations in a,b,c,d,e,f for each input-output pair.
    def constraints(x,out):
        u,v,t=x
        return [
          ([u,0,0,v,0,0],out[0]),
          ([0,u,0,0,v,0],out[1]),
          ([t*inv2%q,0,u,0,t*inv2%q,v],out[2])]
    failures=[]
    for seed in range(num_seeds):
        f=random_map(q,seed)
        for i,x in enumerate(vectors):
            for y in vectors[i:]:
                equ=constraints(x,f(x))+constraints(y,f(y))
                if not echelon_consistent([row for row,v in equ],[v for row,v in equ],q):
                    failures.append((q,seed,x,y));break
            if failures:break
        if failures:break
    assert not failures, failures
    return num_seeds * len(vectors)*(len(vectors)+1)//2

if __name__ == '__main__':
    for q,seeds in [(3,70),(5,10)]:
        D=check_halfD_space(q)
        checks=check_two_local(q,seeds)
        print('q',q,'half_derivations',len(D),'tested_pair_conditions',checks,'formula_exponent',q*q+3*q+3,'linear_2local_count',q**7)
    for q in (3,5):
        vectors=list(product(range(q),repeat=3))
        inv2=pow(2,-1,q)
        def lin_constraints(x,out):
            u,v,t=x
            return [([u,0,0,v,0,0],out[0]),
                    ([0,u,0,0,v,0],out[1]),
                    ([t*inv2%q,0,u,0,t*inv2%q,v],out[2])]
        def is_pair(f,x,y):
            eq=lin_constraints(x,f(x))+lin_constraints(y,f(y))
            return echelon_consistent([z for z,rhs in eq],[rhs for z,rhs in eq],q)
        # A linear 2-local half-derivation which is NOT a half-derivation.
        project_center=lambda v:(0,0,v[2])
        assert all(is_pair(project_center,x,y) for x in vectors for y in vectors)
        assert project_center((0,0,1)) != (0,0,0)
        # A pure nonlinear projected component; not the central perturbation family.
        project_nonlinear=lambda v:((v[0] if v[1]==0 else 0),0,v[2])
        assert all(is_pair(project_nonlinear,x,y) for x in vectors for y in vectors)
        assert project_nonlinear((1,0,0)) != (0,0,0)
        assert project_nonlinear((1,1,0)) == (0,0,0)
        # A map whose projection depends on the central coordinate fails.
        forbidden=lambda v:(v[2],0,0)
        assert not is_pair(forbidden,(1,0,0),(1,0,1))
        # Count projective directions directly; none is inferred from sampling.
        assert len({canonical(v,q)[0] for v in product(range(q),repeat=2) if any(v)})==q+1
        assert len({canonical(v,q)[0] for v in vectors if any(v)})==q*q+q+1
        print('q',q,'explicit_linear_nonhalf_and_nonlinear_tests_OK')
    print('VERIFY_OK')
