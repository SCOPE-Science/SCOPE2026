"""Reproduce two-sided zero-bracket graph and all-arity identities for a central Leibniz family.
Uses only the Python standard library. Run: python verify.py
"""
from collections import Counter
from itertools import product
from math import comb


def predicted_structure(q, c):
    m = q * (q - 1)
    if c % q == (-1) % q:
        return [('clique', m)] * (q + 1)
    if c % q == 1:
        return [('clique', m)] * 2 + [('biclique', m)] * ((q - 1) // 2)
    return [('clique', m)] * 2 + [('isolated', 1)] * (q * (q - 1) ** 2)


def expected_tuples(q, c, k):
    if k == 0:
        return 1
    m = q * (q - 1)
    if c % q == (-1) % q:
        return (q + 1) * q ** (2 * k) - q ** (k + 1)
    if c % q == 1:
        return (2 * q ** (2 * k) - q ** k +
                (q - 1) // 2 * (2 * k * m * q ** (k - 1) +
                (k * (k - 1) * m * m * q ** (k - 2) if k >= 2 else 0)))
    N = q * (q - 1) ** 2
    return 2 * q ** (2 * k) - q ** k + N * k * q ** (k - 1)


def test_one(q, c):
    assert q in (3, 5, 7, 11) and c % q
    E = list(product(range(q), repeat=3))
    n = len(E)
    leftzero = [[False] * n for _ in range(n)]
    mask = [0] * n
    sym_degree = [0] * n
    adjacent = [set() for _ in E]
    for i, (x, y, z) in enumerate(E):
        for j, (u, v, w) in enumerate(E):
            b1 = (x * v + c * y * u) % q
            b2 = (u * y + c * v * x) % q
            leftzero[i][j] = (b1 == 0)
            if b1 == b2 == 0:
                mask[i] |= 1 << j
                sym_degree[i] += 1
                if i != j:
                    adjacent[i].add(j)
    assert all(leftzero[i][j] == leftzero[j][i] for i in range(n) for j in range(n)) is False if c not in (1, q-1) else True
    assert [sym_degree[i] for i in range(n) if E[i][:2] == (0, 0)] == [q**3]*q
    for i, (x, y, _) in enumerate(E):
        pred = q**3 if x == y == 0 else (q**2 if c % q in (1, q-1) or x*y == 0 else q)
        assert sym_degree[i] == pred, ('sym-degree',q,c,i,sym_degree[i],pred)
    assert n == q**3
    for k in (1,2,3):
        if k == 1:
            actual = n
        elif k == 2:
            actual = sum(int.bit_count(t) for t in mask)
        else:
            actual = sum(int.bit_count(mask[i] & mask[j]) for i in range(n)
                         for j in range(n) if mask[i] & (1 << j))
        target = expected_tuples(q, c, k)
        assert actual == target, ('tuple',q,c,k,actual,target)
    center = {i for i,e in enumerate(E) if e[:2] == (0,0)}
    assert all(adjacent[i] == set(range(n)) - {i} for i in center)
    noncentral = set(range(n)) - center
    comps = []
    while noncentral:
        root = noncentral.pop()
        frontier = {root}
        group = {root}
        while frontier:
            v = frontier.pop()
            new = (adjacent[v] & noncentral)
            noncentral -= new
            frontier |= new
            group |= new
        comps.append(group)
    expected = sorted(predicted_structure(q,c))
    found = []
    for comp in comps:
        size = len(comp)
        edges = sum(len(adjacent[i] & comp) for i in comp)//2
        if size == 1:
            typ, m0 = 'isolated', 1
        elif edges == size*(size-1)//2:
            typ, m0 = 'clique', size
        else:
            assert size % 2 == 0 and edges == (size//2)**2
            a = next(iter(comp))
            part = adjacent[a] & comp
            other = comp - part
            assert len(part) == len(other) == size//2
            assert all((adjacent[i]&comp)==other for i in part)
            assert all((adjacent[i]&comp)==part for i in other)
            typ, m0 = 'biclique', size//2
        found.append((typ,m0))
    assert sorted(found) == expected, ('components',q,c,Counter(found),Counter(expected))
    # Independently count cliques of sizes 1,2,3 in the full graph.
    cnt2=sum(len(t) for t in adjacent)//2
    cnt3=0
    for i in range(n):
        for j in adjacent[i]:
            if j>i:
                cnt3 += sum(1 for k in adjacent[i]&adjacent[j] if k>j)
    def poly_coeff(k):
        s=0
        for typ,m0 in predicted_structure(q,c):
            if typ=='clique': s+=comb(m0,k) if k<=m0 else 0
            elif typ=='isolated': s+=int(k==1)
            elif typ=='biclique': s += (2*m0 if k==1 else m0*m0 if k==2 else 0)
        if k==0: return 1
        # Product of (1+z)^q and component-union polynomial.
        return sum(comb(q,j)*(1 if k-j==0 else (
            sum((comb(m0,k-j) if k-j<=m0 else 0) if typ=='clique'
                else int(k-j==1) if typ=='isolated'
                else (2*m0 if k-j==1 else m0*m0 if k-j==2 else 0)
                for typ,m0 in predicted_structure(q,c))))
            for j in range(min(q,k)+1))
    assert cnt2==poly_coeff(2),(q,c,'cliques2',cnt2,poly_coeff(2))
    assert cnt3==poly_coeff(3),(q,c,'cliques3',cnt3,poly_coeff(3))
    print('CENSUS_OK',q,c,'vertices',n,'components',dict(Counter(found)),
          'ordered_2',expected_tuples(q,c,2),'ordered_3',expected_tuples(q,c,3),
          'cliques_2',cnt2,'cliques_3',cnt3)
    return mask, adjacent



def check_gf9(c):
    """Independent field implementation: GF(9)=GF(3)[t]/(t*t+1), a+3*b*t."""
    q=9
    def mul(a,b):
        a0,a1=a%3,a//3; b0,b1=b%3,b//3
        return ((a0*b0+2*a1*b1)%3)+3*((a0*b1+a1*b0)%3)
    def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def neg(a): return ((-a)%3)+3*((-(a//3))%3)
    def zero_c(x,y,u,v):
        return (add(mul(x,v),mul(c,mul(y,u)))==0 and
                add(mul(u,y),mul(c,mul(v,x)))==0)
    assert all(mul(a,1)==a for a in range(9))
    assert all(any(mul(a,b)==1 for b in range(9)) for a in range(1,9))
    E=list(product(range(q),repeat=3))
    masks=[]; edges=[set() for _ in E]
    for i,(x,y,z) in enumerate(E):
        mask=0
        for j,(u,v,w) in enumerate(E):
            if zero_c(x,y,u,v):
                mask |= 1<<j
                if i!=j: edges[i].add(j)
        masks.append(mask)
    expected={k:expected_tuples(q,1 if c==1 else q-1 if c==2 else 3,k) for k in (1,2,3)}
    # This arithmetic branch uses c=3 and c=4 as generic representatives.
    assert sum(int.bit_count(row) for row in masks)==expected[2]
    triple=sum(int.bit_count(masks[i]&masks[j]) for i in range(len(E))
               for j in range(len(E)) if masks[i]&(1<<j))
    assert triple==expected[3]
    center={i for i,e in enumerate(E) if e[:2]==(0,0)}
    remaining=set(range(len(E)))-center
    sizes=[]; shapes=[]
    while remaining:
        root=remaining.pop(); C={root}; stack=[root]
        while stack:
            i=stack.pop()
            new=edges[i]&remaining
            remaining-=new;C|=new;stack+=list(new)
        sizes.append(len(C))
        count=sum(len(edges[i]&C) for i in C)//2
        if len(C)==1:shapes.append(('isolated',1))
        elif count==len(C)*(len(C)-1)//2:shapes.append(('clique',len(C)))
        elif count==(len(C)//2)**2:shapes.append(('biclique',len(C)//2))
        else:raise AssertionError(('unexpected component',len(C),count))
    assert sorted(shapes)==sorted(predicted_structure(q,1 if c==1 else q-1 if c==2 else 3))
    print('GF9_OK',c,expected[2],expected[3],dict(Counter(shapes)))
    return masks

def main():
    cases = {3:[1,2],5:[1,2,3,4],7:[1,2,3,6]}
    for q,cc in cases.items():
        masks={}
        for c in cc:
            masks[c]=test_one(q,c)[0]
        if q==7:
            assert masks[2]==masks[3], 'generic graph differs between 2 and 3'
            assert 3 not in (2,pow(2,-1,q))
            assert expected_tuples(q,q-1,2)==expected_tuples(q,1,2)
            assert expected_tuples(q,q-1,3)-expected_tuples(q,1,3)==q**3*(q-1)**4
    m3=check_gf9(3)
    m4=check_gf9(4)
    check_gf9(1)
    check_gf9(2)
    assert m3==m4
    print('VERIFY_OK: 10 complete prime-field adjacency and clique censuses, four GF(9) component and tuple censuses; exact graph collisions')

if __name__=='__main__':
    main()
