"""Independent exact-cover enumeration of dominating induced matchings of GP(n,3).
Python 3 standard library only. Every edge must be dominated exactly once.
"""

def graph(n):
    edges = set()
    for i in range(n):
        edges.add(tuple(sorted((i, (i+1) % n))))
        edges.add((i, n+i))
        edges.add(tuple(sorted((n+i, n+(i+3) % n))))
    assert len(edges) == 3*n
    return tuple(sorted(edges))


def solutions(n):
    edges = graph(n)
    m = len(edges)
    cover = []
    for a,b in edges:
        mask = 0
        for j,(c,d) in enumerate(edges):
            if a==c or a==d or b==c or b==d:
                mask |= 1<<j
        assert mask.bit_count()==5
        cover.append(mask)
    candidates = [tuple(j for j in range(m) if cover[j]>>i&1) for i in range(m)]
    full = (1<<m)-1
    seen = []
    count = 0
    def rec(remaining, chosen):
        nonlocal count
        if remaining==0:
            assert len(chosen)*5==m
            count+=1
            if count<=5:seen.append(tuple(chosen))
            return
        best = None
        bits=remaining
        while bits:
            bit=bits&-bits; bits-=bit
            i=bit.bit_length()-1
            possible=[j for j in candidates[i] if cover[j]&remaining==cover[j]]
            if not possible:return
            if best is None or len(possible)<len(best): best=possible
            if len(best)==1:break
        for j in best:
            rec(remaining ^ cover[j],chosen+(j,))
    rec(full,())
    assert len(set(seen))==len(seen)
    return count

if __name__=='__main__':
    for n in range(7,51):
        actual=solutions(n)
        expected=5 if n%5==0 else 0
        assert actual==expected,(n,actual,expected)
        print(f'n={n} dominating_induced_matchings={actual}')
    print('PASS: exact-cover enumeration for all 7<=n<=50')
