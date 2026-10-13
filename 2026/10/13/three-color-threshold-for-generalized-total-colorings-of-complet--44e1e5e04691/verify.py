from itertools import product


def forest(nv, edges):
    parent=list(range(nv))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for u,v in edges:
        ru,rv=find(u),find(v)
        if ru==rv:
            return False
        parent[ru]=rv
    return True


def three_exists(m,n):
    # Enumerate all vertex 3-colorings. In K_{m,n}, properness forces
    # disjoint color sets on the two shores. Every edge then has exactly
    # one possible third color, so no edge-color branching remains.
    V=m+n
    tested=0
    for cols in product(range(3), repeat=V):
        ok=True
        for i in range(m):
            for j in range(n):
                if cols[i]==cols[m+j]:
                    ok=False; break
            if not ok: break
        if not ok:
            continue
        tested += 1
        classes=[[] for _ in range(3)]
        for i in range(m):
            for j in range(n):
                forbidden={cols[i],cols[m+j]}
                if len(forbidden)!=2:
                    raise AssertionError('proper edge endpoints must differ')
                c=next(c for c in range(3) if c not in forbidden)
                classes[c].append((i,m+j))
        if all(forest(V,E) for E in classes):
            return True,tested
    return False,tested


def explicit_four_K3n(n):
    m=3; V=m+n
    vc=[0,1,2]+[3]*n
    classes=[[] for _ in range(4)]
    # edges from a_0,a_1,a_2 receive colors 1,2,0 respectively
    ec=[1,2,0]
    for i in range(3):
        for j in range(n):
            u,v=i,3+j
            c=ec[i]
            assert vc[u]!=vc[v]
            assert c!=vc[u] and c!=vc[v]
            classes[c].append((u,v))
    return all(forest(V,E) for E in classes)

parameter_cases=0
vertex_assignments=0
for m in range(1,7):
    for n in range(m,7):
        got,tested=three_exists(m,n)
        vertex_assignments += tested
        parameter_cases += 1
        want=(m<=2)
        assert got==want,(m,n,got,want)

for n in range(3,101):
    assert explicit_four_K3n(n)

print('ALL CHECKS PASSED; '
      f'three_color_parameter_cases={parameter_cases}; '
      f'three_color_vertex_assignments={vertex_assignments}; '
      'three_color_range=1<=m<=n<=6; '
      'four_color_K3n_cases=98; four_color_range=3<=n<=100')
