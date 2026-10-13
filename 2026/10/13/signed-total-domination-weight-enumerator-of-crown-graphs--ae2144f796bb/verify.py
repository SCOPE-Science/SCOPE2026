from itertools import product
from math import comb, ceil


def valid_literal(n, lab):
    A=lab[:n]
    B=lab[n:]
    for i in range(n):
        if sum(B[j] for j in range(n) if j != i) < 1:
            return False
        if sum(A[j] for j in range(n) if j != i) < 1:
            return False
    return True


def eps(n):
    return 2 if n % 2 == 0 else 3

labelings=0
valid_functions=0
coefficient_checks=0
minimum_checks=0
classification_checks=0
for n in range(3,9):
    actual={}
    minw=None
    mincount=0
    for lab in product((-1,1), repeat=2*n):
        labelings += 1
        ok=valid_literal(n,lab)
        A=sum(lab[:n]); B=sum(lab[n:])
        pred=(A >= eps(n) and B >= eps(n))
        assert ok == pred
        classification_checks += 1
        if ok:
            valid_functions += 1
            pa=sum(x==1 for x in lab[:n])
            pb=sum(x==1 for x in lab[n:])
            actual[(pa,pb)] = actual.get((pa,pb),0)+1
            w=sum(lab)
            if minw is None or w < minw:
                minw=w; mincount=1
            elif w == minw:
                mincount += 1
    h=(n+eps(n))//2
    expected={(i,j):comb(n,i)*comb(n,j) for i in range(h,n+1) for j in range(h,n+1)}
    assert actual == expected
    coefficient_checks += len(expected)
    wantw=2*eps(n)
    wantcount=comb(n,h)**2
    assert (minw,mincount)==(wantw,wantcount)
    minimum_checks += 1
print(f"VERIFY_OK n_range=3..8 labelings={labelings} valid_functions={valid_functions} classification_checks={classification_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=16")
