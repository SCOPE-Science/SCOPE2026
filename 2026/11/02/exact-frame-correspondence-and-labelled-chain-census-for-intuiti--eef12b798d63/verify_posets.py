"""Direct axiom-vs-order criterion checks; standard Python 3, no packages."""
import random
from itertools import product


def transitive_closure(edges, n):
    E=[edges[i] | (1<<i) for i in range(n)]
    for k in range(n):
        for i in range(n):
            if E[i] & (1<<k): E[i] |= E[k]
    return E


def upsets(order):
    n=len(order)
    return [u for u in range(1<<n) if all(not u&(1<<i) or order[i]&~u == 0 for i in range(n))]


def semantically_valid(order,N):
    n=len(order)
    full=(1<<n)-1
    T=[all(N[v]!=0 for v in range(n) if order[w]&(1<<v)) for w in range(n)]
    for U in upsets(order):
        bad_sets=sum((1<<a) for a in range(1<<n) if (a&U)==0)
        D=[all(not (N[v]&bad_sets) for v in range(n) if order[w]&(1<<v)) for w in range(n)]
        for w in range(n):
            Q=all(not T[t] or D[t] for t in range(n) if order[w]&(1<<t))
            if Q and not D[w]: return False
    return True


def criterion(order,N):
    n=len(order)
    T=[all(N[v]!=0 for v in range(n) if order[w]&(1<<v)) for w in range(n)]
    down=[]
    for a in range(1<<n):
        d=0
        for i in range(n):
            if any(a&(1<<j) and order[i]&(1<<j) for j in range(n)):
                d|=1<<i
        down.append(d)
    for w in range(n):
        for v in range(n):
            if not order[w]&(1<<v):continue
            for a in range(1<<n):
                if not N[v]&(1<<a):continue
                if not any(T[s] and order[w]&(1<<s) and any(N[s]&(1<<b) and b&~down[a]==0 for b in range(1<<n)) for s in range(n)):
                    return False
    return True


def all_posets_3():
    # Every labelled 3-element poset as a reflexive, antisymmetric, transitive relation.
    n=3
    for code in range(1<<(n*(n-1))):
        E=[1<<i for i in range(n)]
        idx=0
        for i in range(n):
            for j in range(n):
                if i==j:continue
                if code&(1<<idx): E[i]|=1<<j
                idx+=1
        if any(i!=j and (E[i]&(1<<j)) and (E[j]&(1<<i)) for i in range(n) for j in range(n)):
            continue
        if transitive_closure(E,n)!=E:continue
        yield E


def test():
    rng=random.Random(77631)
    posets=list(all_posets_3())
    assert len(posets)==19
    cases=0
    for E in posets:
        for _ in range(300):
            N=[rng.randrange(1<<(1<<len(E))) for _ in E]
            assert semantically_valid(E,N)==criterion(E,N),(E,N)
            cases+=1
    for n in (4,5):
        for _ in range(250):
            P=[1<<i for i in range(n)]
            for i in range(n):
                for j in range(i+1,n):
                    if rng.random()<0.35:P[i]|=1<<j
            E=transitive_closure(P,n)
            for _ in range(6):
                N=[rng.getrandbits(1<<n) for _ in E]
                assert semantically_valid(E,N)==criterion(E,N),(E,N)
                cases+=1
    # Noncontinual but axiom-valid three-world chain: 0<1<2.
    E=[0b111,0b110,0b100]
    N=[1<<(0b100),0,1<<(0b001)]
    assert semantically_valid(E,N) and criterion(E,N)
    assert N[0] and not N[1]
    # All two-world posets and all neighbourhood assignments: no noncontinual valid frame.
    for E in [[1,2],[3,2],[1,3]]:
        for code in range(256):
            N=[code&0b1111,(code>>4)&0b1111]
            assert semantically_valid(E,N)==criterion(E,N)
            continual=all(not N[w] or all(N[v] for v in range(2) if E[w]&(1<<v)) for w in range(2))
            if not continual: assert not semantically_valid(E,N)
    print('ALL_POSET_CHECKS_OK: 19 labelled three-world posets,',cases,'random cases on n=3..5, three-world strictness witness, all 2-world frames')
if __name__=='__main__':test()
