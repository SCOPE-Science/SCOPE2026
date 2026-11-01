#!/usr/bin/env python3
"""Standalone exact checks of majority dynamics on untwisted and Möbius ladders.

All arithmetic is over integers. Graphs carry fixed vertex labels; no quotient
by rotation, reflection, or rung swap is used.
"""
from collections import defaultdict


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def run_count(n):
    return lucas(n) + (2, 1, -1, -2, -1, 1)[n % 6]


def analytic(n, kind):
    r = run_count(n)
    if kind == 'prism':
        fixed = r + 2
        two = (r + 2) ** 2 if n % 2 == 0 else run_count(2*n) + 2
    else:
        fixed = r
        two = r*r if n % 2 else run_count(2*n) + 2
    return fixed, two, (two-fixed)//2


def update_prism(x,n):
    m = (1 << n) - 1
    a = x & m
    b = (x >> n) & m
    la = ((a << 1) | (a >> (n-1))) & m
    ra = ((a >> 1) | (a << (n-1))) & m
    lb = ((b << 1) | (b >> (n-1))) & m
    rb = ((b >> 1) | (b << (n-1))) & m
    ua = (la & ra) | (la & b) | (ra & b)
    ub = (lb & rb) | (lb & a) | (rb & a)
    return ua | (ub << n)


def update_mobius(x,n):
    N = 2*n
    mask = (1 << N) - 1
    left = ((x << 1) | (x >> (N-1))) & mask
    right = ((x >> 1) | (x << (N-1))) & mask
    rung = ((x << n) | (x >> n)) & mask
    return (left & right) | (left & rung) | (right & rung)



def graph_edges(n,kind):
    """Return zero-indexed undirected graph edges, with two  n-vertex rails."""
    out=set()
    def edge(a,b): out.add(tuple(sorted((a,b))))
    if kind=='prism':
        for j in range(2):
            for i in range(n):
                edge(j*n+i, j*n+(i+1)%n)
                edge(i,n+i)
    else:
        for k in range(2*n):
            edge(k,(k+1)%(2*n))
            edge(k,(k+n)%(2*n))
    return out


def check_double_cover(n,kind):
    """Explicit, label-preserving edge-bijection test for the cover lemma."""
    raw=graph_edges(n,kind)
    canon=set()
    def edge(a,b): canon.add(tuple(sorted((a,b))))
    for u,v in raw:
        edge(u,2*n+v)
        edge(2*n+u,v)
    if kind=='prism' and n%2:
        dest=graph_edges(2*n,'prism')
        def mapv(v,t):
            i=v%n;j=v//n
            k=i if (i%2)==t else i+n
            return j*(2*n)+(k+n*j)%(2*n)
    elif kind=='mobius' and n%2==0:
        dest=graph_edges(2*n,'prism')
        def mapv(v,t):
            s=t^(v&1)
            return s*(2*n)+(v+n*s)%(2*n)
    else:
        dest=graph_edges(n,kind)|{
            tuple(sorted((u+2*n,v+2*n))) for u,v in graph_edges(n,kind)}
        if kind=='prism':
            def mapv(v,t):
                i=v%n;j=v//n
                return v+2*n*(t^((i+j)%2))
        else:
            def mapv(v,t):
                return v+2*n*(t^(v%2))
    images=[mapv(v,t) for t in range(2) for v in range(2*n)]
    assert set(images)==set(range(4*n)),(n,kind,'not a vertex bijection')
    mapped={tuple(sorted((images[u],images[v]))) for u,v in canon}
    assert mapped==dest,(n,kind,'cover edge mismatch',len(mapped),len(dest))


def check_word_count(n):
    return sum(all(not ((x >> i)&1) != ((x >> ((i-1)%n))&1) == ((x >> ((i+1)%n))&1)
                   for i in range(n)) for x in range(1 << n))


def direct(n,kind):
    N=1<<(2*n)
    upd=update_prism if kind=='prism' else update_mobius
    f=[upd(x,n) for x in range(N)]
    fixed=sum(1 for x,y in enumerate(f) if x==y)
    two=sum(1 for x,y in enumerate(f) if f[y]==x)
    assert (two-fixed)%2==0
    return fixed,two,(two-fixed)//2


def main():
    for n in range(3,31):
        for kind in ("prism","mobius"):
            check_double_cover(n,kind)
    for n in range(3,16):
        # Direct verification of no singleton bit runs; no floating-point Lucas calculation.
        assert check_word_count(n)==run_count(n),(n,check_word_count(n),run_count(n))
    for n in range(3,11):
        prism=analytic(n,'prism')
        mobius=analytic(n,'mobius')
        delta=prism[2]-mobius[2]
        L=lucas(n)
        expected= {0:4*L+6,1:-L,2:L,3:2*L,4:L,5:-L}[n%6]
        assert delta==expected,(n,delta,expected)
        for kind, result in [('prism',prism),('mobius',mobius)]:
            actual=direct(n,kind)
            assert result==actual,(n,kind,result,actual)
            print(f'n={n:2d} {kind:6s} fixed={actual[0]:6d} returning={actual[1]:8d} orbits={actual[2]:7d}')
    for n in range(3,1001):
        d=analytic(n,'prism')[2]-analytic(n,'mobius')[2]
        L=lucas(n)
        assert d=={0:4*L+6,1:-L,2:L,3:2*L,4:L,5:-L}[n%6]
    print('TWISTED_LADDER_MAJORITY_VERIFY_OK')

if __name__=='__main__':
    main()
