"""Reconstruct prescribed period-three ideals and compare with true rowmotion.
Checks the all-parameter bipartite formula at finite test sizes. Stdlib only.
"""
from itertools import combinations,product

def rotate(n,E,S,T):
    avail={j for j,(u,v) in enumerate(E) if u in S and v in S}
    Tnew=avail-T
    Snew=set(range(n))-S
    for j in Tnew:Snew.update(E[j])
    return Snew,Tnew

def colored_states(n,E):
    result={}
    for labels in product(range(4),repeat=n):
        X={i for i,c in enumerate(labels) if c==3}
        Ys=[{i for i,c in enumerate(labels) if c==j} for j in range(3)]
        if any(u in X and v in X for u,v in E):continue
        if any(labels[u]!=labels[v] and u not in X and v not in X for u,v in E):continue
        if any(any(not any(y in Ys[j] for a,b in E
                  for y in ([b] if a==x else ([a] if b==x else [])))
                    for j in range(3)) for x in X):continue
        orbit=[]
        for i in range(3):
            S=set(range(n))-Ys[i]
            T={k for k,(u,v) in enumerate(E) if u in X|Ys[(i+1)%3]
               and v in X|Ys[(i+1)%3]}
            orbit.append((S,T))
        for i in range(3):
            assert rotate(n,E,*orbit[i])==orbit[(i+1)%3],(E,labels,i)
        enc=tuple(sorted((tuple(sorted(a)),tuple(sorted(b))) for a,b in orbit))
        result.setdefault(enc,0)
        result[enc]+=1
    assert all(mult==3 for mult in result.values())
    return len(result)

def surj3(n):
    return 3**n-3*2**n+3

def run():
    for a in range(1,5):
        for b in range(1,5):
            n=a+b
            E=[(i,a+j) for i in range(a) for j in range(b)]
            actual=colored_states(n,E)
            expected=1+(surj3(a)+surj3(b))//3
            assert actual==expected,(a,b,actual,expected)
            print('K',a,b,actual)
    for n in range(3,9):
        E=[(i,(i+1)%n) for i in range(n)]
        assert colored_states(n,E)==1
    print('CONSTRUCTIVE_THREE_CYCLE_AND_BICLIQUE_PASS')

if __name__=='__main__':run()
