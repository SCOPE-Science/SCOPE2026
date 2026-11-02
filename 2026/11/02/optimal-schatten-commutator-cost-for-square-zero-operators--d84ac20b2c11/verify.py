"""Finite consistency checks for the square-zero Schatten commutator-cost formula.

Requires Python >=3.9, standard library only. These finite checks are
supplementary; the universal inequality is proved analytically in RESULT.md.
"""
from math import sqrt, isclose
from random import Random


def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def norm2(a):
    return sqrt(sum(abs(v)**2 for row in a for v in row))


def close(a,b):
    return isclose(a,b, rel_tol=3e-12, abs_tol=3e-12)


def example(s,p):
    """Check matrix representation, Schatten norms, and dual pairing."""
    r=len(s)
    n=2*r
    mat=lambda:[[0.0 for _ in range(n)] for _ in range(n)]
    a=mat();b=mat();target=mat();w=mat()
    for j,v in enumerate(s):
        a[j][j]=sqrt(v)/2
        a[j+r][j+r]=-sqrt(v)/2
        b[j][j+r]=sqrt(v)
        target[j][j+r]=v
        w[j+r][j]=v**(p-1)
    ab=matmul(a,b);ba=matmul(b,a)
    c=[[ab[i][j]-ba[i][j] for j in range(n)] for i in range(n)]
    assert norm2([[c[i][j]-target[i][j] for j in range(n)] for i in range(n)])<1e-11
    m=sum(v**p for v in s)
    ap=(2*sum((sqrt(v)/2)**(2*p) for v in s))**(1/(2*p))
    bp=sum(v**p for v in s)**(1/(2*p))
    predicted=2**(1/(2*p)-1)*m**(1/p)
    assert close(ap*bp,predicted)
    tr=sum(matmul(w,target)[i][i] for i in range(n))
    assert close(tr,m)
    wc=matmul(w,a);cw=matmul(a,w)
    h=[[wc[i][j]-cw[i][j] for j in range(n)] for i in range(n)]
    tr2=sum(matmul(h,b)[i][i] for i in range(n))
    assert close(tr2,m)
    q=(2*p)/(2*p-1)
    dual_norm=(max(v**(p-1) for v in s) if p==1 else sum(v**p for v in s)**((p-1)/p))
    hn=sum(v**((p-.5)*q) for v in s)**(1/q)
    assert close(hn,2**(1-1/(2*p))*dual_norm*ap)
    return 5


def endpoint():
    # W has only P-from-Q entries and hence W^2 = 0.
    r=3;n=3*r;s=[.5,1.25,2.5]
    w=[[0j]*n for _ in range(n)]
    for i,v in enumerate(s): w[i][i+r]=v
    rg=Random(20261027)
    checks=0
    for _ in range(250):
        x=[[complex(rg.uniform(-2,2),rg.uniform(-2,2)) for _ in range(n)] for _ in range(n)]
        wx=matmul(w,x);xw=matmul(x,w)
        comm=[[wx[i][j]-xw[i][j] for j in range(n)] for i in range(n)]
        assert norm2(comm) <= sqrt(2)*max(s)*norm2(x)+1e-10
        checks+=1
    return checks


def main():
    samples=[(1.,),(1.,2.,3.5),(.13,1.1,3.1,8.9,2.0),(1.,)*8]
    exponents=(1,1.1,1.5,2,3,6,12)
    count=sum(example(list(s),p) for s in samples for p in exponents)
    count+=endpoint()
    print(f"PASS {count} finite assertions (factorizations, cost, dual identities, endpoints)")

if __name__=='__main__': main()
