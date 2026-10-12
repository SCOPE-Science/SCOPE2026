"""Direct independent verification of the divisor-coset constructions.

This finite test is corroboration only; the theorem requires the accompanying proof.
"""
from math import factorial

def build(n, d, residue, first_row):
    assert n % d == 0 and 3*d <= n and 0 <= residue < d
    b = n-2*d
    cols=[]
    for p in first_row:
        flag = p % d == residue
        mid = p - (2*d if flag else d)
        last = p - d if flag else p + d
        col = ([(p-j)%n for j in range(d)] +
               [(mid-j)%n for j in range(b)] +
               [(last-j)%n for j in range(d)])
        cols.append(col)
    return tuple(tuple(col[i] for col in cols) for i in range(n))

def check(n, a):
    sym = set(range(n))
    assert len(a)==n and all(set(row)==sym for row in a)
    assert all({a[i][j] for i in range(n)}==sym for j in range(n))
    return sum(a[i][j] < a[i+1][j] for i in range(n-1) for j in range(n))

total=0
for n in range(3, 51):
    first = tuple(range(n))
    seen=set()
    ds=[d for d in range(1,n+1) if n%d==0 and 3*d<=n]
    for d in ds:
        for r in range(d):
            a=build(n,d,r,first)
            assert check(n,a)==n+1, (n,d,r)
            assert a not in seen, (n,d,r)
            seen.add(a)
    assert len(seen)==sum(ds), (n,len(seen),ds)
    total+=len(seen)
    if n in (3,4,5,6,8,9,10,12,15,18,24,30,36,48,50):
        print(f'n={n} normalized_classes={len(seen)} full_coefficient={factorial(n)*len(seen)}')
print(f'PASS all order-3-to-50 constructions and distinctness; normalized witnesses={total}')
