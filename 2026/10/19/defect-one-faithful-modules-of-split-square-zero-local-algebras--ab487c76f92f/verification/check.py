#!/usr/bin/env python3
"""Reproduce finite-field checks for extremal faithful modules of a square-zero algebra.
Pure Python, with no external modules. All module structures are over the specified prime field.
"""
from collections import Counter
from itertools import product
from math import prod


def mul(A, B, p):
    a, b, c, d = A
    e, f, g, h = B
    return ((a*e+b*g)%p, (a*f+b*h)%p,
            (c*e+d*g)%p, (c*f+d*h)%p)


def det(A, p):
    return (A[0]*A[3]-A[1]*A[2]) % p


def inverse(A, p):
    a,b,c,d=A
    z=pow(det(A,p), -1, p)
    return (d*z%p, -b*z%p, -c*z%p, a*z%p)


def gl2(p):
    return [tuple(x) for x in product(range(p),repeat=4) if det(x,p)]


def matrank(A,p):
    return 2 if det(A,p) else (1 if any(A) else 0)


def vector_rank(vectors,p):
    if not vectors:
        return 0
    a = [list(v) for v in vectors]
    ncol = len(a[0]); row=0
    for col in range(ncol):
        pivot=next((j for j in range(row,len(a)) if a[j][col]%p),None)
        if pivot is None: continue
        a[row],a[pivot] = a[pivot],a[row]
        inv=pow(a[row][col]%p,-1,p)
        a[row]=[(inv*x)%p for x in a[row]]
        for j in range(len(a)):
            if j!=row:
                fac=a[j][col]
                a[j]=[(x-fac*y)%p for x,y in zip(a[j],a[row])]
        row+=1
        if row==len(a): break
    return row


def trace_pair(B,A,p):
    # Trace(B*A) for row-major 2x2 vectors
    return (B[0]*A[0]+B[1]*A[2]+B[2]*A[1]+B[3]*A[3])%p


def vec_basis_kernel(B,p):
    vectors=[tuple(1 if i==j else 0 for i in range(4)) for j in range(4)]
    candidates=[v for v in product(range(p),repeat=4) if trace_pair(B,v,p)==0]
    basis=[]
    for v in candidates:
        if vector_rank(basis+[v],p)>len(basis): basis.append(v)
        if len(basis)==3: break
    assert len(basis)==3 and all(trace_pair(B,v,p)==0 for v in basis)
    return tuple(basis)


def normalized(A,p):
    a=next(x for x in A if x)
    inv=pow(a,-1,p)
    return tuple((inv*x)%p for x in A)


def gl(n,q):
    return prod(q**n-q**i for i in range(n))


def rank_count(n,t,q):
    return prod(q**n-q**i for i in range(t))**2//gl(t,q)


def formula(s,q):
    r=s*s-1
    G=gl(r,q); gs=gl(s,q)
    square={t:G*rank_count(s,t,q)//(gs*gs) for t in range(1,s+1)}
    for t,number in square.items():
        assert G*rank_count(s,t,q)%(gs*gs)==0
    rect=(q-1)*G//(gl(s-1,q)*gl(s+1,q))
    assert (q-1)*G%(gl(s-1,q)*gl(s+1,q))==0
    return square,rect, sum(square.values())+2*rect


def exhaustive_binary():
    p=2; gg=gl2(p); acts=[(P,inverse(Q,p)) for P in gg for Q in gg]
    allmat=[tuple(x) for x in product(range(p),repeat=4)]
    frames=[]
    for B in allmat[1:]:
        W=[A for A in allmat if trace_pair(B,A,p)==0]
        assert len(W)==8
        for A in W:
            if A==(0,0,0,0): continue
            for C in W:
                if vector_rank([A,C],p)!=2: continue
                for D in W:
                    if vector_rank([A,C,D],p)==3:
                        frames.append(((A,C,D),matrank(B,p)))
    assert len(frames)==2520
    unseen={frame for frame,_ in frames}
    orbits=Counter()
    while unseen:
        triple=next(iter(unseen))
        orbit={tuple(mul(mul(P,A,p),Qi,p) for A in triple) for P,Qi in acts}
        assert len(orbit)==36, (triple,len(orbit))
        assert orbit<=unseen
        unseen.difference_update(orbit)
        image=[triple[0],triple[1],triple[2]]
        normal=next(B for B in allmat[1:] if all(trace_pair(B,A,p)==0 for A in image))
        orbits[matrank(normal,p)]+=1
    assert orbits==Counter({1:42,2:28}),orbits
    print('F_2: full 2x2 hyperplane frame census = 2520, orbit sizes = 36, classes by normal rank =',dict(orbits))
    square,rect,total=formula(2,2)
    assert square=={1:42,2:28} and rect==1 and total==72
    print('F_2: add the two rectangular full-Hom types, total classes =',total)


def ternary_stabilizers():
    p=3; gg=gl2(p)
    allmat=list(product(range(p),repeat=4))
    normals=sorted({normalized(B,p) for B in allmat if any(B)})
    assert len(normals)==40
    counts=Counter()
    for B in normals:
        basis=vec_basis_kernel(B,p)
        stab=0
        for P in gg:
            for Q in gg:
                Qinv=inverse(Q,p)
                if all(mul(mul(P,A,p),Qinv,p)==A for A in basis): stab+=1
        assert stab==p-1,(B,stab)
        counts[matrank(B,p)]+=1
    assert counts==Counter({1:16,2:24}),counts
    square,rect,total=formula(2,p)
    assert square=={1:156,2:234} and rect==1 and total==392
    print('F_3: 40 projective normal matrices, common pointwise stabilizer size 2;',
          'normal-rank hyperplanes',dict(counts),'; classes',square,'+2 =',total)


if __name__=='__main__':
    for s in (2,3,4):
        for q in (2,3,4,5):
            square,rect,total=formula(s,q)
            print(f'formula s={s}, q={q}: square-rank strata={square}, each rectangular={rect}, total={total}')
    exhaustive_binary()
    ternary_stabilizers()
