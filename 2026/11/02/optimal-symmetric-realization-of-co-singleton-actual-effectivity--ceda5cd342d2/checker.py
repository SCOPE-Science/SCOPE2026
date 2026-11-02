"""Independent finite validation of symmetric veto game matrices."""
from itertools import product

def form(n):
    if n < 3:
        raise ValueError('no realization')
    if n % 2:
        inv2 = pow(2,-1,n)
        return [[(((i+j)*inv2)%n) if i!=j else ((i+1)%n) for j in range(n)] for i in range(n)]
    p=n-1
    inv2=pow(2,-1,p)
    def F(i,j):
        if i==p and j==p: return 0
        if i==p: return (j+1)%p
        if j==p: return (i+1)%p
        if i==j: return p
        return ((i+j)*inv2)%p
    return [[F(i,j) for j in range(n)] for i in range(n)]

def check_form(n):
    m=form(n)
    for i in range(n):
        assert set(m[i]) == set(range(n))-{i},(n,i,m[i])
        assert {m[j][i] for j in range(n)} == set(range(n))-{i}
        for j in range(n):
            assert m[i][j]==m[j][i] and m[i][j] not in {i,j},(n,i,j,m[i][j])

for n in range(3,201): check_form(n)

def count_symmetric(n):
    cells=[(i,j) for i in range(n) for j in range(i,n)]
    allowed=[tuple(k for k in range(n) if k not in (i,j)) for i,j in cells]
    total=good=0
    for values in product(*allowed):
        total+=1
        rows=[set() for _ in range(n)]
        for (i,j),v in zip(cells,values):
            rows[i].add(v); rows[j].add(v)
        if all(rows[i] == set(range(n))-{i} for i in range(n)): good+=1
    return total,good
assert count_symmetric(3)==(8,8),count_symmetric(3)
assert count_symmetric(4)==(5184,288),count_symmetric(4)
print('ALL_CHECKS_OK: 198 constructed orders (3..200); exhaustive symmetric n=3: 8/8 and n=4: 288/5184')
