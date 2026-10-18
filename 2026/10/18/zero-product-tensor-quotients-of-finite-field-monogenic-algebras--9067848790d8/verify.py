#!/usr/bin/env python3
"""Exhaustive zero-product tensor-span checks for small monogenic algebras.

Runs over prime fields only. The theorem concerns every finite field; finite
checks independently test the tensor-kernel formula in small cases.
"""
from itertools import product


def mul(x, y, f, p):
    n = len(f)-1
    c = [0]*(2*n-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            c[i+j] = (c[i+j] + a*b)%p
    for k in range(2*n-2, n-1, -1):
        v=c[k]
        if v:
            for j in range(n):
                c[k-n+j] = (c[k-n+j]-v*f[j])%p
    return tuple(c[:n])


def rank_incremental(rows, p, width):
    piv={}
    for row in rows:
        v=list(row)
        while True:
            i=next((j for j,x in enumerate(v) if x), None)
            if i is None:
                break
            if i not in piv:
                scale=pow(v[i],-1,p)
                piv[i]=[(scale*x)%p for x in v]
                break
            s=v[i]; w=piv[i]
            for j in range(i,width):
                v[j]=(v[j]-s*w[j])%p
    return len(piv)


def testcase(p, f, factors):
    n=len(f)-1
    assert f[-1]==1
    assert sum(d*e for d,e in factors)==n
    es=list(product(range(p),repeat=n))
    zero=(0,)*n
    def zero_tensors():
        for a in es:
            for b in es:
                if mul(a,b,f,p)==zero:
                    yield tuple((x*y)%p for x in a for y in b)
    actual=rank_incremental(zero_tensors(),p,n*n)
    dimension=sum(d*d*e*(e+1)//2 for d,e in factors)
    expected=n*n-dimension
    assert actual==expected, (p,f,factors,actual,expected)
    return {'p':p,'polynomial':f,'factor_degrees_powers':factors,
            'ring_dimension':n,'zero_tensor_span_dim':actual,
            'universal_quotient_dim':n*n-actual,'predicted_quotient_dim':dimension,
            'bilinear_defect_dim':dimension-n}


def main():
    cases=[
        (3,(0,1),[(1,1)]),                   # t
        (3,(0,0,1),[(1,2)]),                 # t^2
        (3,(0,0,0,1),[(1,3)]),               # t^3
        (3,(0,0,0,0,1),[(1,4)]),             # t^4
        (3,(0,1,1),[(1,1),(1,1)]),           # t(t+1)
        (3,(0,0,2,1),[(1,2),(1,1)]),         # t^2(t+2)
        (3,(0,1,0,1),[(1,1),(2,1)]),         # t(t^2+1)
        (3,(1,0,1),[(2,1)]),                 # t^2+1 irreducible
        (3,(1,0,2,0,1),[(2,2)]),             # (t^2+1)^2
        (5,(0,0,1),[(1,2)]),
        (5,(1,0,1),[(1,1),(1,1)]),           # t^2+1 splits mod 5
        (2,(1,1,1),[(2,1)]),                 # irreducible over F2
        (2,(1,0,1),[(1,2)]),                 # (t+1)^2 mod 2
        (2,(0,1,1,1),[(1,1),(2,1)]),         # t(t^2+t+1)
    ]
    for p,f,factors in cases:
        print(testcase(p,f,factors))
    print('VERIFY_OK',len(cases),'exhaustive configurations')

if __name__=='__main__':
    main()
