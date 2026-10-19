"""Reproduce finite checks for a Brownian exit limit of random-input pair coalescence."""
from math import cosh, sqrt, exp
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def transition(n, state, letter):
    x,y=state
    if letter=='a':
        return ((x+1)%n,(y+1)%n)
    return (0 if x==n-1 else x, 0 if y==n-1 else y)


def macro_trial(n,d,u,v):
    x,y=0,d
    steps=0
    for phase in range(n-1):
        assert x==phase
        if phase==n-1-d and u:
            x,y=transition(n,(x,y),'b');steps+=1
            if x==y:return 0,'upper',steps
        x,y=transition(n,(x,y),'a');steps+=1
        if x==y:return 0,'unexpected',steps
    assert x==n-1
    x,y=transition(n,(x,y),'b' if v else 'a');steps+=1
    if x==y:return 0,'lower',steps
    assert x==0
    return (y-x)%n,'survive',steps


def exhaustive_macro():
    checks=0
    for n in range(3,31):
        for d in range(1,n):
            for u in (0,1):
                for v in (0,1):
                    observed, tag, steps=macro_trial(n,d,u,v)
                    if d==n-1 and u: expval,exptag=0,'upper'
                    elif d+u-v==0: expval,exptag=0,'lower'
                    else: expval,exptag=d+u-v,'survive'
                    assert (observed,tag)==(expval,exptag),(n,d,u,v,observed,tag,expval,exptag)
                    checks+=1
    return checks


def finite_laplace(n,p,s,x):
    # Independently solve all noncoalesced ordered-pair equations, with
    # exact (finite-state) transitions rather than the cycle reduction.
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    ids={v:i for i,v in enumerate(pairs)}
    k=len(pairs)
    z=exp(-s/n**3)
    mat=lil_matrix((k,k))
    rhs=np.zeros(k)
    for (i,j),row in ids.items():
        mat[row,row]=1
        for symbol,pr in [('a',p),('b',1-p)]:
            x1,y1=transition(n,(i,j),symbol)
            if x1==y1:rhs[row]+=z*pr
            else:mat[row,ids[tuple(sorted((x1,y1)))]]-=z*pr
    F=spsolve(mat.tocsc(),rhs)
    i=0;j=round(x*n)
    return F[ids[i,j]]


def limit_laplace(p,s,x):
    D=p*p*(1-p)
    k=sqrt(s/D)
    return cosh((x-.5)*k)/cosh(.5*k)


def main():
    checks=exhaustive_macro()
    values=[]
    for p in (0.5,2/3):
        for x in (0.25,0.5):
            s=.75
            target=limit_laplace(p,s,x)
            seq=[finite_laplace(n,p,s,x) for n in (20,40,80)]
            # Convergence check with expanding n; finite n differs due
            # phase convention and order-n^2 boundary effects.
            assert abs(seq[-1]-target)<abs(seq[0]-target)
            assert abs(seq[-1]-target)<0.045, (p,x,seq,target)
            values.append((p,x,round(target,7),*[round(t,7) for t in seq]))
    print('VERIFY_OK macro_branch_cases=%d direct_full_pair_Laplace_n=20,40,80 p=1/2,2/3 x=1/4,1/2 s=3/4'%checks)
    for row in values:print('Laplace',row)

if __name__=='__main__':main()
