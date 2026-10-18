"""Independent integer-arithmetic checks for the carry-pair transition theorem."""
from collections import deque

START = object()

def graph(g, k):
    """Enumerate every accessible state, not just the proposed eight."""
    edges = {}
    todo = deque([START])
    seen = {START}
    while todo:
        u = todo.popleft()
        R, L = (0, 0) if u is START else u
        out = []
        for low in range(g):
            t = k * low + L
            high, lowcarry = t % g, t // g
            highcarry = low + g * R - k * high
            if not (0 <= highcarry < k and 0 <= lowcarry < k):
                continue
            if u is START and (high == 0 or low == 0):
                continue
            v = (highcarry, lowcarry)
            out.append((high, low, v))
            if v not in seen:
                seen.add(v)
                todo.append(v)
        edges[u] = sorted(out)
    return edges

def expected(m):
    g=m*m-1; k=g-m; a=m-2; b=m*a; c=k-1
    A=(0,0); B=(0,b); C=(a,a); D=(a,c)
    E=(b,0); F=(b,b); G=(c,a); H=(c,c)
    table={
      A:[(0,0,A),(1,k,B)],
      B:[(0,a,C),(1,g-2,D)],
      C:[(a,0,E),(a+1,k,F)],
      D:[(a,a,G),(a+1,g-2,H)],
      E:[(k,1,A),(k+1,k+1,B)],
      F:[(k,m-1,C),(k+1,g-1,D)],
      G:[(g-2,1,E),(g-1,k+1,F)],
      H:[(g-2,m-1,G),(g-1,g-1,H)],
      START:[(1,k,B)]}
    return {x:sorted(v) for x,v in table.items()}, (A,C,F,H), (A,D,E,H)

def main():
    for m in range(3,101):
        g=m*m-1; k=g-m
        actual=graph(g,k)
        reference,even,odd=expected(m)
        assert actual==reference,(m,actual,reference)
        nodes=set(actual)-{START}
        actual_even={v for v in nodes if v[0]==v[1]}
        actual_odd={v for v in nodes if any(w==(v[1],v[0]) for _,_,w in actual[v])}
        assert actual_even==set(even),(m,actual_even,even)
        assert actual_odd==set(odd),(m,actual_odd,odd)
        # Strong connectivity to an even pivot: all reachable nodes survive Y-pruning.
        target=even[0]
        for v in nodes:
            reach={v}; Q=deque([v])
            while Q:
                for _,_,w in actual[Q.popleft()]:
                    if w not in reach:
                        reach.add(w); Q.append(w)
            assert target in reach,(m,v)
    print('PASS: complete carry-pair graphs and pivot classes for m=3..100')

if __name__=='__main__':
    main()
