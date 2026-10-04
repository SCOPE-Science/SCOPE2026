from itertools import combinations, permutations, product
from math import comb, factorial


def closed_injective(n):
    return sum(comb(n,p) * factorial(p)**(n-p) for p in range(n+1))


def explicit_cp(n):
    labels=tuple(range(n))
    enc=set()
    for p in range(n+1):
        for P in combinations(labels,p):
            P=tuple(P)
            Pset=set(P)
            C=tuple(x for x in labels if x not in Pset)
            orders=list(permutations(P))
            for prefs in product(orders, repeat=len(C)):
                enc.add((P, tuple(zip(C,prefs))))
    return len(enc)


def stirling2(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

expected=[1,2,4,11,54,567,13928]
for n,e in enumerate(expected):
    got=explicit_cp(n)
    assert got==e==(closed_injective(n)), (n,got,e,closed_injective(n))

assert [closed_injective(n) for n in range(1,9)] == [2,4,11,54,567,13928,837321,134985098]

# Empty-signature base class: f_p=1, hence only the P/C sort pattern matters.
for n in range(9):
    assert sum(comb(n,p) for p in range(n+1)) == 2**n

b=[]
for n in range(1,8):
    b.append(sum(stirling2(n,k)*closed_injective(k) for k in range(1,n+1)))
assert b == [2,6,25,150,1444,27059,1231654]
print('VERIFY_OK')
