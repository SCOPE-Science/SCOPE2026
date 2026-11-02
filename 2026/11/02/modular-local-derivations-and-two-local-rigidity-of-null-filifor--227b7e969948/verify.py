#!/usr/bin/env python3
"""Finite-field checks of local derivations of a cyclic right Leibniz algebra.
Only standard library, prime fields. General theorem uses symbolic arguments.
"""
import itertools

def product(v,w,p,n):
    return tuple((w[0]*v[i-1])%p if i>=1 else 0 for i in range(n))

def deriv_columns(a,p,n):
    columns=[]
    for i in range(1,n+1):
        col=[0]*n
        col[i-1]=(i*a[0])%p
        for j in range(2,n-i+2):
            col[i+j-2]=a[j-1]
        columns.append(tuple(col))
    return columns

def matrix_action(cols,v,p,n):
    return tuple(sum(v[i]*cols[i][j] for i in range(n))%p for j in range(n))

def predicted(cols,p,n):
    for i in range(n):
        if any(cols[i][j] for j in range(i)):
            return False
        if (i+1)%p==0 and cols[i][i]!=0:
            return False
    return True

def verify(p,n,exhaustive=True):
    vset=list(itertools.product(range(p),repeat=n))
    dcols=[deriv_columns(a,p,n) for a in vset]
    sample_d=dcols if exhaustive else dcols[:min(4,len(dcols))]
    sample_vectors=vset if exhaustive else vset[:min(8,len(vset))]
    for cols in sample_d:
        for u in sample_vectors:
            for v in sample_vectors:
                lhs=matrix_action(cols,product(u,v,p,n),p,n)
                du=matrix_action(cols,u,p,n);dv=matrix_action(cols,v,p,n)
                rhs=tuple((x+y)%p for x,y in zip(product(du,v,p,n),product(u,dv,p,n)))
                assert lhs==rhs
    if not exhaustive:
        print('DERIVATIONS_OK',p,n,p**n)
        return
    targets={v:{matrix_action(d,v,p,n) for d in dcols} for v in vset}
    seen_pred=seen_real=seen_twopred=0
    for flat in itertools.product(range(p),repeat=n*n):
        cols=[flat[i*n:(i+1)*n] for i in range(n)]
        a=predicted(cols,p,n)
        b=all(matrix_action(cols,v,p,n) in targets[v] for v in vset)
        assert a==b,(p,n,flat,a,b)
        seen_pred+=a;seen_real+=b
        if b:
            # Any two-local map must equal the one derivation determined by its e1 value.
            if cols==dcols[vset.index(tuple(cols[0]))]:seen_twopred+=1
    expected=p**(n*(n+1)//2-n//p)
    assert seen_real==expected,(p,n,seen_real,expected)
    assert seen_twopred==p**n,(p,n,seen_twopred)
    print('LOCAL_AND_TWO_LOCAL_OK',p,n,'linear_maps',p**(n*n),'local',seen_real,'two_local',seen_twopred)

if __name__=='__main__':
    for p,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:
        verify(p,n)
    for p,n in [(2,5),(3,4),(5,4)]:
        verify(p,n,False)
    print('MODULAR_LEIBNIZ_LOCAL_DERIVATIONS_OK')
