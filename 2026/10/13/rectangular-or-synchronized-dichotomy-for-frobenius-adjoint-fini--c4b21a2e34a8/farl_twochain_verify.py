"""Exact finite checks for Frobenius-adjoint Gödel two-chain products.
Run: python3 farl_twochain_verify.py
Only Python standard library is required.
"""
from itertools import product
from math import comb


def instance(m, n):
    elements = tuple(product(range(m), range(n)))
    zero, one = (0, 0), (m-1, n-1)
    def le(a,b): return a[0] <= b[0] and a[1] <= b[1]
    def meet(a,b): return min(a[0], b[0]), min(a[1], b[1])
    def join(a,b): return max(a[0], b[0]), max(a[1], b[1])
    def arrow(a,b): return (m-1 if a[0] <= b[0] else b[0],
                            n-1 if a[1] <= b[1] else b[1])
    def adjoints(core):
        core = tuple(core)
        upper = {x: [c for c in core if le(x,c)] for x in elements}
        lower = {x: [c for c in core if le(c,x)] for x in elements}
        if any(not v for v in upper.values()) or any(not v for v in lower.values()):
            return None
        if any(not any(all(le(c,d) for d in upper[x]) for c in upper[x]) for x in elements):
            return None
        if any(not any(all(le(d,c) for d in lower[x]) for c in lower[x]) for x in elements):
            return None
        g = {x: next(c for c in upper[x] if all(le(c,d) for d in upper[x])) for x in elements}
        f = {x: next(c for c in lower[x] if all(le(d,c) for d in lower[x])) for x in elements}
        return f,g
    def axioms(f,g):
        return (all(le(f[x],x) for x in elements)
                and all((le(g[x],y) == le(x,f[y])) for x in elements for y in elements)
                and all(f[arrow(g[x],y)] == arrow(g[x],f[y])
                        and f[join(g[x],y)] == join(g[x],f[y])
                        and g[meet(x,g[y])] == meet(g[x],g[y])
                        for x in elements for y in elements))
    def typ(core):
        C=set(core)
        xs={x for x,y in C}; ys={y for x,y in C}
        if C == set(product(xs,ys)):
            return 'rectangular'
        chain=sorted(C)
        if all(chain[i][0] < chain[i+1][0] and chain[i][1] < chain[i+1][1]
               for i in range(len(chain)-1)):
            return 'diagonal'
        return 'other'
    return elements,zero,one,le,meet,join,arrow,adjoints,axioms,typ


def core_check(m,n):
    e,zero,one,le,meet,join,arrow,adjoints,axioms,typ=instance(m,n)
    mids=[x for x in e if x not in (zero,one)]
    hits={'rectangular':0,'diagonal':0,'other':0}
    tested=0
    for bits in range(1<<len(mids)):
        C=(zero,one)+tuple(x for i,x in enumerate(mids) if bits>>i&1)
        Cset=set(C)
        if any(meet(a,b) not in Cset or join(a,b) not in Cset or arrow(a,b) not in Cset
               for a in C for b in C):continue
        tested+=1
        pair=adjoints(C)
        if pair and axioms(*pair):
            hits[typ(C)]+=1
    expected_rect=2**(m+n-4)
    expected_diag=comb(m+n-4,m-2)
    assert hits == {'rectangular':expected_rect, 'diagonal':expected_diag, 'other':0}, (m,n,hits)
    print('CORE',m,n,'subalgebras',tested,'rect',hits['rectangular'],'diag',hits['diagonal'])
    return hits


def raw_adjunction_check(m,n):
    e,zero,one,le,meet,join,arrow,adjoints,axioms,typ=instance(m,n)
    def monotone_sequences(length):
        for seq in product(e, repeat=length):
            if all(le(seq[i],seq[i+1]) for i in range(length-1)):
                yield seq
    xs=list(monotone_sequences(m-1));ys=list(monotone_sequences(n-1))
    hits={'rectangular':0,'diagonal':0,'other':0}
    checked=0
    for row in xs:
        for col in ys:
            checked+=1
            g={(i,j):join(zero if i==0 else row[i-1],zero if j==0 else col[j-1])
               for i,j in e}
            f={y:(max((x[0] for x in e if le(g[x],y)),default=0),
                  max((x[1] for x in e if le(g[x],y)),default=0)) for y in e}
            if axioms(f,g):
                C={g[x] for x in e}
                hits[typ(C)]+=1
                gf=adjoints(C)
                assert gf is not None and gf==(f,g)
    exp={'rectangular':2**(m+n-4),'diagonal':comb(m+n-4,m-2),'other':0}
    assert hits==exp, (m,n,hits,exp)
    print('RAW_ADJOINT',m,n,'g_candidates',checked,'rect',hits['rectangular'],'diag',hits['diagonal'])


def main():
    for m,n in ((2,2),(2,3),(3,3),(3,4),(4,4),(3,5)):
        core_check(m,n)
    for m,n in ((2,2),(2,3),(3,3),(3,4)):
        raw_adjunction_check(m,n)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
