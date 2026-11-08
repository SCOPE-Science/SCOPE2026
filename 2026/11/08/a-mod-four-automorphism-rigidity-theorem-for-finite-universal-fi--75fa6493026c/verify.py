"""Self-contained checks of the de Bruijn / finite-groupoid symmetry theorem.
Run with Python 3.9 or later: python verify.py
"""
from itertools import permutations


def euler_edges(m):
    # Directed quotient of the looped complete digraph by simultaneous phase flip.
    # Its arc set consists of (source-orbit, target-orbit, phase difference).
    adj = [[(b,delta) for b in range(m) for delta in (0,1)] for _ in range(m)]
    stack = [(0, None)]
    circuit = []
    while stack:
        v, incoming = stack[-1]
        if adj[v]:
            w, delta = adj[v].pop()
            stack.append((w, (v,w,delta)))
        else:
            stack.pop()
            if incoming is not None:
                circuit.append(incoming)
    edges = list(reversed(circuit))
    assert len(edges)==2*m*m
    assert edges[0][0] == 0 and edges[-1][1]==0
    assert len(set(edges)) == len(edges)
    return edges


def lifted_word(m):
    # n=2m, m odd.  Letter 2*a+phase, phase in {0,1}.
    assert m>=1 and m%2==1
    edges=euler_edges(m)
    vertices=[]
    phase=0
    for shift in (0,1):
        assert phase==shift
        for a,b,delta in edges:
            vertices.append(2*a+phase)
            phase ^= delta
        assert phase==1-shift
    assert phase==0
    n=2*m
    assert len(vertices)==n*n
    assert len({(vertices[i],vertices[(i+1)%(n*n)]) for i in range(n*n)})==n*n
    for i in range(n*n//2):
        assert vertices[i+n*n//2] == (vertices[i]^1)
    return vertices


def operation(word):
    n=len(set(word))
    op = [[None]*n for _ in range(n)]
    for i in range(n*n):
        a,b,c=word[i],word[(i+1)%(n*n)],word[(i+2)%(n*n)]
        assert op[a][b] is None
        op[a][b]=c
    return op


def aut_group(word):
    n=len(set(word)); op=operation(word)
    found=[]
    for p in permutations(range(n)):
        if all(p[op[a][b]]==op[p[a]][p[b]] for a in range(n) for b in range(n)):
            found.append(p)
    return found


def all_debruijn_cycles(n):
    # independent exhaustive tour enumeration for n=2,3,4.
    seen=set()
    def recur(word, edges):
        if len(word)==n*n:
            if (word[-1],word[0]) not in edges and len(edges)==n*n-1:
                cycle=tuple(word)
                # canonical rotation by unique occurrence of pair (0,0)
                for i in range(n*n):
                    if cycle[i]==0 and cycle[(i+1)%(n*n)]==0:
                        cycle=cycle[i:]+cycle[:i]
                        break
                seen.add(cycle)
            return
        for c in range(n):
            edge=(word[-1],c)
            if edge not in edges:
                recur(word+[c],edges|{edge})
    recur([0,0],{(0,0)})
    return seen


def main():
    cases=[]
    for n in (2,3,4):
        cycles=all_debruijn_cycles(n)
        expected={2:1,3:24,4:20736}[n]  # (n!)^n / n^2, source count.
        assert len(cycles)==expected,(n,len(cycles))
        sizes={len(aut_group(list(c))) for c in cycles}
        assert sizes==({2} if n==2 else {1}), (n,sizes)
        cases.append((n,len(cycles),sorted(sizes)))
    # Every one-cell operation change of a periodic UFS-groupoid in n=2,3
    # produces a strictly preperiodic UFS-groupoid (Klimov Theorem 4.3).
    # Test its automorphism group directly, not by sequence uniqueness.
    mutation_total=0
    for n in (2,3):
        for cyc in all_debruijn_cycles(n):
            op=operation(cyc)
            for a in range(n):
                for b in range(n):
                    for c in range(n):
                        if c==op[a][b]:
                            continue
                        modified=[row.copy() for row in op]
                        modified[a][b]=c
                        for p in permutations(range(n)):
                            if all(p[modified[x][y]]==modified[p[x]][p[y]] for x in range(n) for y in range(n)):
                                assert p==tuple(range(n))
                        mutation_total+=1
    assert mutation_total==4+24*9*2
    cases.append(('modified_periodic_n2_n3',mutation_total,'C1'))
    for m in (1,3,5):
        word=lifted_word(m)
        n=2*m
        if n<=6:
            auts=aut_group(word)
            assert len(auts)==2,(n,len(auts))
        cases.append((n,'constructed','C2'))
    # n=4 explicit example via base-n Euler tour, check all 4!=24 permutations.
    def ordinary_word(n):
        adj=[list(range(n)) for _ in range(n)]
        stack=[0]; path=[]
        while stack:
            if adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            else:path.append(stack.pop())
        w=list(reversed(path))[:-1]
        assert len(w)==n*n
        return w
    for n in (3,4):
        w=ordinary_word(n)
        assert len({(w[i],w[(i+1)%(n*n)]) for i in range(n*n)})==n*n
        assert len(aut_group(w))==1
        cases.append((n,'ordinary','C1'))
    print('VERIFY_OK',repr(cases))

if __name__=='__main__':
    main()
