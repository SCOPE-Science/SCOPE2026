"""Independent exhaustive finite certificate for cyclic 2-star-forming rigidity.

Run with Python 3.10+: python3 verify.py
"""
from collections import Counter

POTENTIAL = (
    '0000000211122234000000011111223100000002111222310000000011102000'
    '0000000211122234000000011111200000000002111222000000000011102000'
    '0000000211122234000000011111223100000002111222310000000011102000'
    '0000000211122234000000011111200000000002111222000000000011102000'
)

def is_star_forming(mask, n):
    selected = {v for v in range(n) if mask & (1 << v)}
    for v in range(n):
        if v in selected:
            continue
        # Enumerate three distinct vertices of each 2-edge path including v,
        # rather than relying on a local Boolean simplification.
        works = False
        for c in range(n):
            nb = {(c - 1) % n, (c + 1) % n}
            for a in nb:
                for b in nb:
                    if a != b and v in {c, a, b} and {c, a, b} - {v} <= selected:
                        works = True
                        break
                if works:
                    break
            if works:
                break
        if not works:
            return False
    return True


def is_minimal(mask, n):
    return is_star_forming(mask, n) and all(
        not is_star_forming(mask ^ (1 << i), n)
        for i in range(n) if mask & (1 << i)
    )


def local_star(x, j):
    # x covers indices -4,...,4; valid for -2<=j<=2.
    if x[j + 4]:
        return True
    return bool(x[j+2]*x[j+3] or x[j+3]*x[j+5] or x[j+5]*x[j+6])


def permitted(bits):
    x = [(bits >> k) & 1 for k in range(9)]
    if x[4] == 0:
        return local_star(x, 0)
    x[4] = 0
    return any(not local_star(x, j) for j in range(-2, 3))


def scc(nodes, arcs):
    adjacency = {u: [] for u in nodes}
    for u, v in arcs:
        adjacency[u].append(v)
    index = {}; low = {}; stack = []; instack = set(); components = []
    def visit(u):
        index[u] = low[u] = len(index)
        stack.append(u); instack.add(u)
        for v in adjacency[u]:
            if v not in index:
                visit(v)
                low[u] = min(low[u], low[v])
            elif v in instack:
                low[u] = min(low[u], index[v])
        if low[u] == index[u]:
            comp = []
            while True:
                v = stack.pop(); instack.remove(v); comp.append(v)
                if v == u: break
            components.append(comp)
    for u in nodes:
        if u not in index:
            visit(u)
    return components


def verify():
    assert len(POTENTIAL) == 256, len(POTENTIAL)
    h = [int(v) for v in POTENTIAL]
    assert min(h) == 0 and max(h) == 4
    E = []
    for bits in range(512):
        if permitted(bits):
            u, v = bits & 255, (bits >> 1) & 255
            w = 3*((bits >> 4)&1)-2
            assert w <= h[v]-h[u], ('violating potential', bits, u, v, w, h[u], h[v])
            E.append((u,v,w,bits))
    assert len(E)==332, len(E)
    tight=[(u,v) for u,v,w,b in E if h[v]-h[u]==w]
    assert len(tight)==242, len(tight)
    comps=scc(range(256),tight)
    recurrent=[]
    for c in comps:
        if len(c)>1 or (c[0],c[0]) in tight:
            recurrent.append(set(c))
    assert {frozenset(c) for c in recurrent} == {frozenset([109,182,219]), frozenset([60,121,158,207,231,243])}, recurrent
    # Exact cyclic order and simplicity of the two recurrent components.
    for c in recurrent:
        internal=[(u,v) for u,v in tight if u in c and v in c]
        assert len(internal)==len(c)
        for u in c:
            assert sum(a==u for a,b in internal)==1
            assert sum(b==u for a,b in internal)==1
        word=''.join(str((u>>4)&1) for u,v in internal)
        assert len(word) in {3,6}
    # Compare independent definition against the rolling 9-bit predicate.
    max_sets={}
    for n in range(3,15):
        values=[]
        for mask in range(1<<n):
            a=is_minimal(mask,n)
            if n>=9:
                b=all(permitted(sum(((mask>>((i+j)%n))&1)<<j for j in range(9))) for i in range(n))
                assert a==b, ('local window mismatch', n,mask)
            if a: values.append(mask)
        max_size=max(m.bit_count() for m in values)
        best={m for m in values if m.bit_count()==max_size}
        assert max_size==(2*n)//3, (n,max_size)
        max_sets[n]=len(best)
        if n%3==0:
            protos=['110'*(n//3)]
            if n%6==0:
                protos.append('111100'*(n//6))
            expected=set()
            for p in protos:
                for offset in range(n):
                    shifted=p[offset:]+p[:offset]
                    expected.add(sum((int(v)<<i) for i,v in enumerate(shifted)))
            assert best==expected, (n,best,expected)
            assert len(best)==(9 if n%6==0 else 3)
    print('VERIFY_OK windows=512 allowed_arcs=332 potential_heights=0..4 tight_arcs=242 cyclic_SCCs=(3,6) brute_n=3..14 counts='+repr(max_sets))

if __name__=='__main__':
    verify()
