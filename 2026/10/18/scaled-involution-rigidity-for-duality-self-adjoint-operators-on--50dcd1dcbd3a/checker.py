"""Finite diagnostics for a normalized-duality self-adjointness theorem.

Uses only the Python standard library. The theorem's infinite-dimensional
assertion is proved analytically; these checks are not an exhaustive proof.
"""
import cmath
import math
import random


def jmap(x, p):
    norm = sum(abs(z)**p for z in x)**(1.0/p)
    if norm == 0:
        return [0j for z in x]
    return [norm**(2-p) * abs(z)**(p-2)*z.conjugate() if z else 0j for z in x]


def apply(A,x):
    return [sum(a*y for a,y in zip(row,x)) for row in A]


def transpose_apply(A,v):
    return [sum(A[i][j]*v[i] for i in range(len(A))) for j in range(len(A))]


def example(rng,n):
    ids=list(range(n));rng.shuffle(ids)
    pi=list(range(n))
    while len(ids)>=2:
        i=ids.pop()
        if rng.random() < 0.35:
            continue
        j=ids.pop();pi[i],pi[j]=j,i
    omega=[1.0+0j]*n
    for j in range(n):
        if pi[j]==j:
            omega[j]=complex(rng.choice((-1,1)))
        elif j < pi[j]:
            z=cmath.exp(2j*math.pi*rng.random())
            omega[j]=z;omega[pi[j]]=z.conjugate()
    c=0.2+3*rng.random()
    T=[[0j]*n for _ in range(n)]
    for j in range(n):T[pi[j]][j]=c*omega[j]
    return T,c


def max_err(u,v):
    return max(abs(a-b) for a,b in zip(u,v))


def run():
    rng=random.Random(786231)
    accepted=excluded=0
    for p in (1.2,1.5,1.8,3.,4.,6.):
        for n in (2,3,5,8):
            for _ in range(20):
                T,c=example(rng,n)
                x=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
                assert max_err(jmap(apply(T,x),p),transpose_apply(T,jmap(x,p)))<3e-11
                for j in range(n):
                    basis=[0j]*n;basis[j]=1
                    twice=apply(T,apply(T,basis))
                    assert max_err(twice,[c*c*y for y in basis])<2e-11
                accepted+=1
                y=[1+0j,1+0j]+[0j]*(n-2)
                # Neither a nontrivial band projection nor unequal diagonal
                # scaling satisfies the normalized duality adjoint identity.
                for diag in ([1]+[0]*(n-1),[1,2]+[1]*(n-2)):
                    D=[[complex(diag[i] if i==j else 0) for j in range(n)] for i in range(n)]
                    diff=max_err(jmap(apply(D,y),p),transpose_apply(D,jmap(y,p)))
                    assert diff>1e-4, (n,p,diag,diff)
                    excluded+=1
    print(f'passed {accepted} constructive-family tests; {excluded} exclusion tests')

if __name__=='__main__':
    run()
