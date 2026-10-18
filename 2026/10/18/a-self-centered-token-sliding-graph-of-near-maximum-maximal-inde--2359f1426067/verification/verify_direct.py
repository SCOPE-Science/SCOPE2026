"""Exhaustively verify the cyclic-interval model inside odd Möbius ladders."""
from collections import deque, Counter
import json


def graph(n):
    size = 2 * n
    nbr = tuple(sum(1 << j for j in {(v-1)%size, (v+1)%size, (v+n)%size}) for v in range(size))
    return nbr


def interval_state(n, a, b):
    h = (n-1)//2
    odd = sum(1 << (2*((h*t)%n)+1) for t in range(a, a+b))
    excluded = {(a-1+t)%n for t in range(b+2)}
    even = sum(1 << (2*((h*(s-1))%n)) for s in range(n) if s not in excluded)
    return odd | even


def all_maximal_independent(n, k, nbr):
    total = 2*n
    full = (1 << total) - 1
    closed = tuple(nbr[v] | (1<<v) for v in range(total))
    out = set()
    def visit(available, selected, dominated):
        if selected.bit_count() > k:
            return
        if not available:
            if selected.bit_count()==k and dominated==full:
                out.add(selected)
            return
        bit = available & -available
        v = bit.bit_length()-1
        visit(available ^ bit, selected, dominated)
        visit(available & ~closed[v], selected | bit, dominated | closed[v])
    visit(full,0,0)
    return out


def neighbors_by_slide(s,nbr,states):
    out=set()
    selected=s
    while selected:
        bit=selected & -selected
        selected ^= bit
        v=bit.bit_length()-1
        unocc=nbr[v] & ~s
        while unocc:
            nextbit=unocc & -unocc
            unocc ^= nextbit
            target=s ^ bit ^ nextbit
            if target in states:
                out.add(target)
    return out


def interval_neighbors(n,a,b):
    res=[]
    if b < n-3:
        res.extend([((a-1)%n,b+1),(a,b+1)])
    if b>1:
        res.extend([(a,b-1),((a+1)%n,b-1)])
    return set(res)


def check(n):
    nbr=graph(n);k=n-2
    labeled={(a,b):interval_state(n,a,b) for b in range(1,n-2) for a in range(n)}
    assert len(labeled)==n*(n-3)
    assert len(set(labeled.values()))==len(labeled)
    exhaustive=all_maximal_independent(n,k,nbr)
    assert exhaustive==set(labeled.values()),(n,'sets',len(exhaustive),len(labeled))
    reverse={s:ab for ab,s in labeled.items()}
    links=0;degrees=Counter()
    adj={}
    for ab,s in labeled.items():
        actual={reverse[t] for t in neighbors_by_slide(s,nbr,exhaustive)}
        expected=interval_neighbors(n,*ab)
        assert actual==expected, (n,ab,actual,expected)
        adj[ab]=actual;links+=len(actual);degrees[len(actual)]+=1
    assert links//2==2*n*(n-4)
    assert degrees[2]==2*n
    assert degrees[4]==n*(n-5)
    for src in labeled:
        distances={src:0};q=deque([src])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in distances:
                    distances[v]=distances[u]+1;q.append(v)
        assert len(distances)==len(labeled)
        assert max(distances.values())==n
    return {'n':n,'states':len(labeled),'edges':links//2,'degrees':dict(sorted(degrees.items())), 'radius':n,'diameter':n}


def main():
    rows=[check(n) for n in (5,7,9,11,13,15)]
    for row in rows: print(json.dumps(row,sort_keys=True))
    print('VERIFY_OK')

if __name__=='__main__':main()
