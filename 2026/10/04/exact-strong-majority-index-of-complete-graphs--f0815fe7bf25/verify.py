from itertools import combinations, product


def edges(n):
    return list(combinations(range(n), 2))


def strong_ok(n, coloring):
    threshold = n - 2
    colors = set(coloring.values())
    deg = {v:{c:0 for c in colors} for v in range(n)}
    for (u,v), c in coloring.items():
        deg[u][c] += 1
        deg[v][c] += 1
    for (u,v), edge_color in coloring.items():
        for c in colors:
            count = deg[u][c] + deg[v][c] - (2 if c == edge_color else 0)
            if count > threshold:
                return False
    return True


def explicit3():
    return {(0,1):0,(0,2):1,(1,2):2}


def explicit4():
    col = {}
    for e in edges(4):
        col[e] = 0 if 0 in e else 1
    return col


def explicit5():
    classes = {
        0:[(0,3),(0,4),(2,3)],
        1:[(0,1),(0,2),(1,2),(1,4)],
        2:[(1,3),(2,4),(3,4)],
    }
    col={}
    for c, es in classes.items():
        for e in es: col[tuple(sorted(e))]=c
    return col


def cycle_edges(seq):
    return {tuple(sorted((seq[i], seq[(i+1)%len(seq)]))) for i in range(len(seq))}


def explicit7():
    cycles=[
        [0,1,2,3,4,5,6],
        [0,2,4,6,1,3,5],
        [0,3,6,2,5,1,4],
    ]
    col={}
    for c, cyc in enumerate(cycles):
        for e in cycle_edges(cyc):
            assert e not in col
            col[e]=c
    assert set(col)==set(edges(7))
    return col


def equitable(n):
    parts=[[],[],[]]
    for v in range(n):
        parts[v%3].append(v)
    part_of={v:i for i,P in enumerate(parts) for v in P}
    col={}
    for e in edges(n):
        a,b=part_of[e[0]],part_of[e[1]]
        if a==b:
            c=a
        else:
            s={a,b}
            c=2 if s=={0,1} else (0 if s=={1,2} else 1)
        col[e]=c
    return col


def any_two_coloring(n):
    E=edges(n)
    for bits in product((0,1), repeat=len(E)):
        col=dict(zip(E,bits))
        if strong_ok(n,col):
            return col
    return None


assert strong_ok(3, explicit3())
assert strong_ok(4, explicit4())
assert strong_ok(5, explicit5())
assert strong_ok(7, explicit7())
assert strong_ok(6, equitable(6))
for n in range(8, 201):
    assert strong_ok(n, equitable(n)), n

small={n:(any_two_coloring(n) is not None) for n in range(3,7)}
assert small == {3:False,4:True,5:False,6:False}, small

for n in range(6,201):
    if n==7:
        continue
    if n==6 or n>=8:
        assert 2*((n+2)//3) <= n-2

print('ALL CHECKS PASSED')
print('explicit orders: 3,4,5,7')
print('equitable construction checked: n=6 and 8..200')
print('exhaustive two-colour check: n=3..6; only n=4 succeeds')
