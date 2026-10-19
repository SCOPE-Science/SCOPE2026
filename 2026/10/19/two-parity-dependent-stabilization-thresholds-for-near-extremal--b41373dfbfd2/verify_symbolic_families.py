"""Direct certification of explicit near-maximum sum-free families and swap edges.
Independent of exhaustive search: generates only the closed-form families and
checks their Schur-free property, exact cardinalities, and all edges by pairs.
"""
from itertools import combinations


def is_sumfree(A):
    a=set(A)
    return not any(x+y in a for x in a for y in a)


def family(n):
    if n%2:
        m=(n-1)//2
        O=[frozenset(range(1,2*m+2,2))-{x} for x in range(1,2*m+2,2)]
        U=[frozenset(range(m+1,2*m+2))-{t} for t in range(m+1,2*m+2)]
        A=frozenset(range(m,2*m))
        B=frozenset([m,*range(m+2,2*m),2*m+1])
        return O,U,[A,B]
    m=n//2
    O=[frozenset(range(1,2*m,2))-{x} for x in range(1,2*m,2)]
    U=[frozenset(range(m+1,2*m+1))-{t} for t in range(m+1,2*m+1)]
    V=[frozenset(range(m,2*m))-{s} for s in range(m+1,2*m)]
    W0=frozenset(range(m-1,2*m-2))
    W1=frozenset([m-1,*range(m+1,2*m-2),2*m-1])
    W2=frozenset([m-1,*range(m+2,2*m-2),2*m-1,2*m])
    return O,U,V,[W0,W1,W2]


def profile(n):
    groups=family(n)
    states=[x for g in groups for x in g]
    k=(n+1)//2-1
    assert len(states)==len(set(states))
    assert all(len(A)==k and is_sumfree(A) and max(A)<=n and min(A)>=1 for A in states)
    edges=[]
    for i,j in combinations(range(len(states)),2):
        if len(states[i]&states[j])==k-1:edges.append((i,j))
    adjacency=[set() for _ in states]
    for i,j in edges:adjacency[i].add(j);adjacency[j].add(i)
    seen=set(); components=[]
    for i in range(len(states)):
        if i in seen:continue
        frontier=[i];seen.add(i)
        for j in frontier:
            for t in adjacency[j]:
                if t not in seen:seen.add(t);frontier.append(t)
        components.append(len(frontier))
    components.sort(reverse=True)
    m=n//2
    if n%2:
        expected=(2*m+4,m*(m+1)+5,[m+3,m+1])
    else:
        expected=(3*m+2,m*(m-1)+(m-1)*(m-2)//2+2*(m-1)+9,[2*m+2,m])
    assert (len(states),len(edges),components)==expected,(n,len(states),len(edges),components,expected)
    return (len(states),len(edges),components)


if __name__=='__main__':
    for n in list(range(15,100,2))+list(range(20,101,2)):
        profile(n)
    for n in (15,17,19,20,22,24,29,30,61,100):
        print(n,profile(n))
    print('VERIFY_OK')
