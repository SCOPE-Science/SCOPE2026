"""Independent finite checks for co-rank-one isotone inverse involutions."""
from itertools import combinations

def mate(i,t):
    if t >= i+2:
        return t-1,i
    if t <= i-1:
        return t,i+1
    return i,t

def transformation(n,i,t):
    image=[u for u in range(1,n+1) if u != t]
    return tuple(image[x-1 if x<=i else x-2] for x in range(1,n+1)) if False else tuple(
        image[(x-1 if x<=i else x-2)] for x in range(1,n+1))

def compose(f,g):
    return tuple(g[x-1] for x in f)

for n in range(2,10):
    cells={(i,t) for i in range(1,n) for t in range(1,n+1)}
    assert {mate(i,t) for i,t in cells}==cells
    assert all(mate(*mate(i,t))==(i,t) for i,t in cells)
    assert all((mate(i,t)==(i,t)) == (t in (i,i+1)) for i,t in cells)
    assert all((lambda j,u: u in (i,i+1) and t in (j,j+1))(*mate(i,t)) for i,t in cells)
    for i,t in cells:
        f=transformation(n,i,t)
        j,u=mate(i,t)
        g=transformation(n,j,u)
        assert compose(compose(f,g),f)==f,(n,i,t,j,u)
        assert compose(compose(g,f),g)==g,(n,i,t,j,u)
    print(f'n={n}: {len(cells)} maps, {(n-1)*(n-2)//2} two-cycles, {2*(n-1)} fixed idempotents: OK')
print('VERIFY_OK')
