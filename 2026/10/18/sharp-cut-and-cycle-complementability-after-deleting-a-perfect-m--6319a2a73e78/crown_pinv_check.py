#!/usr/bin/env python3
"""Independent floating-point Laplacian pseudoinverse cross-check.

Requires numpy. Exact arithmetic is covered by crown_verify.py.
"""
import numpy as np


def edges(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def predicted(n, source, target):
    a,b=source
    i,j=target
    def s(k):
        return (int(k==a)-int(k==b))/(2*n)
    def c(k):
        return ((int(k==a)+int(k==b))/2-1/n)/(n-2)
    return s(i)-s(j)+c(i)+c(j)+1/(n*(n-1))


def check(n):
    ee=edges(n)
    incidence=np.zeros((2*n,len(ee)))
    for idx,(i,j) in enumerate(ee):
        incidence[i,idx]=1
        incidence[n+j,idx]=-1
    projection=incidence.T@np.linalg.pinv(incidence@incidence.T)@incidence
    expected=np.array([[predicted(n,src,target) for src in ee] for target in ee])
    errors=(np.max(np.abs(projection-expected)),
            np.max(np.abs(projection@projection-projection)),
            np.max(np.abs(incidence@(np.eye(len(ee))-projection))))
    assert max(errors)<1e-11,(n,errors)
    return max(errors)


if __name__=='__main__':
    values=[(n,check(n)) for n in range(3,11)]
    print('PASS: independent incidence pseudoinverse checks n=3,...,10')
    print('Largest absolute discrepancy:',max(x for _,x in values))
