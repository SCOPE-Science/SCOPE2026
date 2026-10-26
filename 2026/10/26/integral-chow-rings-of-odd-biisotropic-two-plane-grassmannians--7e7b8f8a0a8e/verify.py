"""Exact Schubert-Pieri checks for biisotropic two-plane sections.

Uses only integer arithmetic and the integral Pieri rule on Gr(2,2n+1).
"""
from collections import defaultdict
from math import comb


def partitions(p, width):
    return [(p-j, j) for j in range(p//2+1)
            if p-j <= width and p-j >= j]


def times_h(v, width):
    out = defaultdict(int)
    for (a,b), c in v.items():
        if a < width:
            out[a+1,b] += c
        if b < a:
            out[a,b+1] += c
    return dict(out)


def times_h2(lam,width):
    return times_h(times_h({lam:1},width),width)


def det_bareiss(a):
    a = [list(map(int,row)) for row in a]
    n = len(a)
    s = 1
    old = 1
    for k in range(n-1):
        if a[k][k] == 0:
            swap = next((j for j in range(k+1,n) if a[j][k]),None)
            if swap is None:return 0
            a[k],a[swap] = a[swap],a[k]
            s *= -1
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q = a[i][j]*pivot - a[i][k]*a[k][j]
                assert q % old == 0
                a[i][j] = q//old
            a[i][k] = 0
        old = pivot
    return s*(a[-1][-1] if n else 1)


def catalan(k):
    return comb(2*k,k)//(k+1)


def check(n):
    assert n>=2
    width = 2*n-1
    middle = 2*n-2
    b = partitions(middle,width)
    assert len(b) == n
    gram = [[times_h2(b[j],width).get((width-b[i][1],width-b[i][0]),0)
              for j in range(n)] for i in range(n)]
    predicted = [[(1 if abs(i-j)==1 or (i==j==n-1) else 2 if i==j else 0)
                  for j in range(n)] for i in range(n)]
    assert gram==predicted,(n,gram,predicted)
    assert det_bareiss(gram)==1,(n,gram)
    for p in range(middle):
        source=partitions(p,width)
        target=partitions(p+2,width)
        assert len(target)>=len(source)
        # For p < middle, the first len(source) target rows form a unitriangular minor.
        minor=[[times_h2(lam,width).get(tgt,0) for lam in source]
               for tgt in target[:len(source)]]
        assert det_bareiss(minor)==1,(n,p,minor)
    # The Grassmannian top power of hyperplane, equivalent to the Plucker degree.
    power={(0,0):1}
    for _ in range(4*n-2):
        power=times_h(power,width)
    assert power=={(width,width):catalan(2*n-1)},(n,power)
    assert catalan(2*n-1)>catalan(2*n-2)
    return catalan(2*n-1)


if __name__=='__main__':
    out=[(n,check(n)) for n in range(2,16)]
    print('VERIFY_OK n=2..15 middle_integral_forms_det=1; low_degree_h2_primitive=true; Plucker_Catalan_degrees=true')
    print('degree_samples='+str(out[:7]))
