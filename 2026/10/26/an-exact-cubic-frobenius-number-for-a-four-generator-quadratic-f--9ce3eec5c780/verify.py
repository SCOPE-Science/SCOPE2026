"""Independent finite residue-class shortest-path checks of the stated theorem."""
from heapq import heappop, heappush

def frobenius(n):
    a=n*n
    gens=(a+1,a+n+1,a+n+2)
    dist=[None]*a
    dist[0]=0
    heap=[(0,0)]
    while heap:
        d,r=heappop(heap)
        if dist[r]!=d:
            continue
        for g in gens:
            nr=(r+g)%a
            nd=d+g
            if dist[nr] is None or nd<dist[nr]:
                dist[nr]=nd
                heappush(heap,(nd,nr))
    return max(dist)-a

def main():
    for n in range(2,101):
        got=frobenius(n)
        expected=n**3-2
        assert got==expected,(n,got,expected)
    print('VERIFY_OK parameters=2..100 all_exact_frobenius_checks')

if __name__=='__main__':
    main()
