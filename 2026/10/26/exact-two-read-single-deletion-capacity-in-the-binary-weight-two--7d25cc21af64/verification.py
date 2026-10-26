"""Finite consistency check; the theorem is proved by the parity argument."""
from itertools import combinations
for n in range(2,19):
    pairs=list(combinations(range(n),2))
    descendants={}
    for i,j in pairs:
        w=['0']*n
        w[i]=w[j]='1'
        descendants[(i,j)]={''.join(w[:k]+w[k+1:]) for k in range(n)}
    code=[(i,j) for i,j in pairs if (j-i)%2]
    assert len(code)==n*n//4
    for x,y in combinations(code,2):
        assert len(descendants[x] & descendants[y])<=1,(n,x,y)
    for i in range(n-1):
        for j in range(i+1,n-1):
            assert len(descendants[(i,j)]&descendants[(i,j+1)])>=2,(n,i,j)
print('PASS two-read odd-gap constructions and row obstructions, n=2..18')
