from itertools import combinations, product

def vertices(word):
    ca = cb = 0
    out = []
    for symbol in word:
        if symbol == "A":
            out.append(("A", ca)); ca += 1
        else:
            out.append(("B", cb)); cb += 1
    return out

def all_edges(word):
    vs = vertices(word)
    pos = {v:i for i,v in enumerate(vs)}
    A = [v for v in vs if v[0] == "A"]
    B = [v for v in vs if v[0] == "B"]
    E = [(a,b) for a in A for b in B]
    return vs, E, pos

def connected(vs, edges):
    adj = {v:set() for v in vs}
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen = {vs[0]}; stack = [vs[0]]
    while stack:
        u = stack.pop()
        for v in adj[u] - seen:
            seen.add(v); stack.append(v)
    return len(seen) == len(vs)

def blocks(word):
    out = []
    for symbol in word:
        if not out or out[-1][0] != symbol:
            out.append([symbol,1])
        else:
            out[-1][1] += 1
    return [(x,k) for x,k in out]

def theorem_predicts(word):
    n = word.count("B")
    bl = blocks(word)
    if bl[0][1] != 1:
        return False
    if word[0] == "A":
        if bl == [("A",1),("B",n),("A",2)]: return False
        if bl == [("A",1),("B",1),("A",2),("B",n-1)]: return False
    else:
        if bl == [("B",1),("A",3),("B",n-1)]: return False
        if bl == [("B",1),("A",1),("B",n-1),("A",2)]: return False
    return True

def construct(word):
    if not theorem_predicts(word): return None
    vs,E,pos = all_edges(word)
    root = vs[0]
    A = [v for v in vs if v[0] == "A"]
    B = [v for v in vs if v[0] == "B"]
    parent = {}
    if root[0] == "A":
        s = root
        i = 1; first = []
        while i < len(vs) and vs[i][0] == "B":
            first.append(vs[i]); i += 1
        a1,a2 = sorted([a for a in A if a != s], key=pos.get)
        if len(first) >= 2:
            b1,b2 = first[:2]
            c = min([b for b in B if b not in first], key=pos.get)
            parent[a1]=b1; parent[a2]=b2; parent[c]=a1
            for b in B:
                if b != c: parent[b]=s
        else:
            b0 = first[0]
            c = min([b for b in B if pos[a1] < pos[b] < pos[a2]], key=pos.get)
            d = min([b for b in B if b not in {b0,c}], key=pos.get)
            parent[b0]=s; parent[a1]=b0; parent[c]=s; parent[a2]=c; parent[d]=a1
            for b in B:
                if b not in {b0,c,d}: parent[b]=s
    else:
        s = root
        i = 1; first = []
        while i < len(vs) and vs[i][0] == "A":
            first.append(vs[i]); i += 1
        if len(first) == 2:
            a0,a1 = first
            b1 = min([b for b in B if b != s], key=pos.get)
            a2 = [a for a in A if a not in first][0]
            d = min([b for b in B if b not in {s,b1}], key=pos.get)
            parent[a0]=s; parent[a1]=s; parent[b1]=a0; parent[a2]=b1; parent[d]=a1
            for b in B:
                if b not in {s,b1,d}: parent[b]=a0
        elif len(first) == 1:
            a0 = first[0]
            j = 2; second = []
            while j < len(vs) and vs[j][0] == "B":
                second.append(vs[j]); j += 1
            b1 = second[0]
            a1 = vs[j]
            a2 = [a for a in A if a not in {a0,a1}][0]
            c = min([b for b in B if pos[b] > pos[a1]], key=pos.get)
            parent[a0]=s; parent[a1]=b1; parent[a2]=s; parent[c]=a1
            for b in B:
                if b not in {s,c}: parent[b]=a0
        else:
            raise AssertionError((word, blocks(word)))
    assert set(parent) == set(vs)-{root}
    tree = []
    for v,p in parent.items():
        assert p[0] != v[0] and pos[p] < pos[v]
        tree.append(tuple(sorted((p,v))))
    T = set(tree)
    complement = [e for e in E if tuple(sorted(e)) not in T]
    assert len(tree) == len(vs)-1 and connected(vs,tree) and connected(vs,complement)
    return tree

def brute(word):
    vs,E,pos = all_edges(word)
    sources=[]; non=[]; choices=[]
    for v in vs:
        pred=[u for u in vs if u[0] != v[0] and pos[u] < pos[v]]
        if not pred: sources.append(v)
        else: non.append(v); choices.append(pred)
    if len(sources) != 1: return False
    for selected in product(*choices):
        T={tuple(sorted((v,p))) for v,p in zip(non,selected)}
        complement=[e for e in E if tuple(sorted(e)) not in T]
        if connected(vs,complement): return True
    return False

def words(n):
    N=n+3
    for apos in combinations(range(N),3):
        S=set(apos)
        yield ''.join('A' if i in S else 'B' for i in range(N))

constructed = exhaustive = 0
for n in range(4,31):
    for word in words(n):
        if theorem_predicts(word):
            construct(word); constructed += 1
for n in range(4,8):
    for word in words(n):
        got=brute(word); expected=theorem_predicts(word); exhaustive += 1
        if got != expected:
            raise AssertionError((n,word,blocks(word),got,expected))
print(f"ALL CHECKS PASSED; constructed_cases={constructed}; exhaustive_cases={exhaustive}; exhaustive_n=4..7; construction_n=4..30")
