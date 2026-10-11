from itertools import combinations
from math import comb

def disconnected_survivors(n,F):
    F=set(F); S=[v for v in range(n) if v not in F]
    if not S: return False
    adj={v:[] for v in S}
    ss=set(S)
    for v in S:
        for d in (1,2,-1,-2):
            w=(v+d)%n
            if w in ss: adj[v].append(w)
    seen={S[0]}; stack=[S[0]]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen)<len(S)

def formulas(k):
    n=k+6
    f=[comb(n,j) for j in range(1,5)]
    f4=k*(k+6)*(k*k+3*k+8)//6
    f5=(k-1)*(k+6)*(3*k*k-k+8)//12
    e=-(k**4+2*k**3-21*k*k+18*k+8)//8
    return f+[f4,f5],e

def check(k):
    n=k+6
    facets=[frozenset(F) for F in combinations(range(n),6) if disconnected_survivors(n,F)]
    faces=[set() for _ in range(6)]
    for F in facets:
        L=tuple(F)
        for r in range(1,7):
            for T in combinations(L,r): faces[r-1].add(T)
    f=[len(x) for x in faces]
    ff,e=formulas(k)
    assert f==ff,(k,f,ff)
    red=-1+sum((1 if i%2==0 else -1)*f[i] for i in range(6))
    assert red==e,(k,red,e)
    return k,n,f,red

if __name__=='__main__':
    for k in range(3,15):
        k,n,f,e=check(k)
        print(k,n,f,e)
    print('VERIFY_OK')
