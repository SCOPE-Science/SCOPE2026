from itertools import combinations
from math import comb

def words(n):
    m=(n+2)//3
    cap=n-m+1
    for a in range(2,m+1):
        for b in range(a+1,cap+1):
            x=['0']*n
            for j in (1,a,b):x[j-1]='1'
            yield ''.join(x)

def orbit_key(x):
    return min(x[i:]+x[:i] for i in range(len(x)))

def verify(n):
    C=list(words(n))
    assert len(C)==(n-1)*(n-2)//6,(n,len(C))
    for u in C:
        for v in C:
            for k in range(1,n):
                assert u[-k:]!=v[:k],(n,u,v,k)
    all_orbits={orbit_key(''.join('1' if i in ss else '0' for i in range(n))) for ss in combinations(range(n),3)}
    primitive={s for s in all_orbits if all(s[i:]+s[:i]!=s for i in range(1,n))}
    assert {orbit_key(c) for c in C}==primitive,(n,len(primitive),len(C))
    return n,len(C),len(primitive)

if __name__=='__main__':
    for n in range(3,31):
        print(*verify(n))
    print('Verified construction, overlap, and full primitive necklace cover for n=3..30.')
