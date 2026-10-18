"""Independent finite checks for signed Roman domination of Kneser two-subset graphs.

This checks explicit constructions and low-order local balance enumerators.
It is not a substitute for the unbounded lower-bound proof.
"""
from itertools import combinations, product
from math import comb


def labeling(n):
    if n < 9:
        raise ValueError("n must be at least 9")
    a = (n-3)//2 if n % 2 else n//2-1
    A = tuple(range(a))
    B = tuple(range(a,n))
    f = {}
    for i,j in combinations(range(n),2):
        f[i,j] = -1 if (i in A)!=(j in A) else 1
    for u in range(a):
        x,y = sorted((u,(u+1)%a))
        f[x,y] = 2
    if not n % 2:
        for j in range(3):
            f[B[2*j],B[2*j+1]] = 2
    return f


def check(n,f):
    assert len(f)==comb(n,2) and set(f.values())<={-1,1,2}
    W=sum(f.values())
    s=[sum(f[min(i,j),max(i,j)] for j in range(n) if j!=i) for i in range(n)]
    assert sum(s)==2*W
    min_closed=10**10
    twos={e for e,w in f.items() if w==2}
    for (i,j),w in f.items():
        direct=sum(t for (u,v),t in f.items() if (u,v)==(i,j) or len({i,j,u,v})==4)
        identity=W-s[i]-s[j]+2*w
        assert direct==identity,(n,(i,j),direct,identity)
        assert identity>=1,(n,(i,j),identity)
        if w==-1:
            assert any(i not in e and j not in e for e in twos),(n,(i,j))
        min_closed=min(min_closed,identity)
    for i in range(n):
        star=sum(W-s[i]-s[j]+2*f[min(i,j),max(i,j)] for j in range(n) if j!=i)
        assert star==(n-3)*W-(n-4)*s[i]
    return W,min_closed,s


def local_balance_count(a):
    E=list(combinations(range(a),2)); cnt=0
    for values in product((-1,1,2),repeat=len(E)):
        s=[0]*a
        for (i,j),x in zip(E,values):
            s[i]+=x;s[j]+=x
        if all(v==a+1 for v in s):
            cnt+=1
    return cnt


if __name__=='__main__':
    tests=0
    for n in range(9,81):
        W,low,s=check(n,labeling(n))
        assert W==(3 if n%2 else 4)
        assert low>=1
        tests+=1
    print('CONSTRUCTIONS_OK',tests,'orders 9..80; all closed-neighborhood and defender conditions checked')
    for a,count in [(3,1),(4,3),(5,12)]:
        actual=local_balance_count(a)
        assert actual==count,(a,actual,count)
        print('ODD_OPTIMAL_INTERNAL_LABELINGS',a,actual,'total',comb(2*a+3,a)*actual)
    print('VERIFY_OK')
