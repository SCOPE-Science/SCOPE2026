"""Independent exact finite-sample checks for the root-degree/profile covariance theorem."""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def transform(v):
    """Multiply polynomial by z-1."""
    out = [Q(0)] * (len(v) + 1)
    for i, x in enumerate(v):
        out[i] -= x
        out[i + 1] += x
    return out


def moments(nmax):
    a,b,h=[Q(1)],[Q(1)],[Q(0)]
    yield 1,a,b,h
    for n in range(1,nmax):
        ca,cb,ch=transform(a),transform(b),transform(h)
        aa=[(a[i] if i<len(a) else Q(0))+ca[i]/n for i in range(len(ca))]
        aa[0]+=1
        bb=[(b[i] if i<len(b) else Q(0))+cb[i]/n for i in range(len(cb))]
        hh=[(h[i] if i<len(h) else Q(0))+ch[i]/n+cb[i]/n-ca[i]/Q(n*n) for i in range(len(ch))]
        a,b,h=aa,bb,hh
        yield n+1,a,b,h


def independent_enumeration(n):
    count=factorial(n-1)
    sum_root=0
    sum_profile=[0]*n
    sum_prod=[0]*n
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        degrees=[0]*n
        for p in parents:
            degrees[p-1]+=1
        root=degrees[0]
        sum_root+=root
        for d in degrees:
            sum_profile[d]+=1
            sum_prod[d]+=root
    return [Q(sum_prod[d],count)-Q(sum_root*sum_profile[d],count*count) for d in range(n)]


def main():
    cases=0
    for n,a,b,h in moments(60):
        assert sum(h)==0, ('conservation',n)
        if n>=2:
            assert h[0]==Q(n-2,2*(n-1)),('leaf-check',n,h[0])
        assert b[0]==0 if n>=2 else b[0]==1
        cases+=3
        if n<=9:
            independent=independent_enumeration(n)
            for j in range(n):
                assert h[j]==independent[j], ('enumeration',n,j,h[j],independent[j])
                cases+=1
    print(f'PASS: {cases} exact rational checks; independent enumeration of all recursive trees through 9 vertices.')

if __name__=='__main__':
    main()
