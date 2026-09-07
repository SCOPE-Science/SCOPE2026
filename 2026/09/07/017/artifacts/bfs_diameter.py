"""BFS diameter census for Cay(G,S), G=PSL(2,13), S={a,A,b,B}. Stdlib only."""
from collections import deque

P = 13

def mm(A, B):
    return ((A[0]*B[0]+A[1]*B[2]) % P,
            (A[0]*B[1]+A[1]*B[3]) % P,
            (A[2]*B[0]+A[3]*B[2]) % P,
            (A[2]*B[1]+A[3]*B[3]) % P)

def neg(A):
    return ((-A[0]) % P, (-A[1]) % P, (-A[2]) % P, (-A[3]) % P)

def canon(A):
    B = neg(A)
    return A if A < B else B

A_MAT = (1, 1, 0, 1)
B_MAT = (1, 0, 1, 1)
AINV = (1, 12, 0, 1)
BINV = (1, 0, 12, 1)
GENS = [('a', A_MAT), ('A', AINV), ('b', B_MAT), ('B', BINV)]
GDICT = dict(GENS)
IDENT = (1, 0, 0, 1)

def bfs(source):
    dist = {source: 0}
    parent = {source: None}
    q = deque([source])
    while q:
        u = q.popleft()
        for L, G in GENS:
            v = canon(mm(u, G))
            if v not in dist:
                dist[v] = dist[u] + 1
                parent[v] = (u, L)
                q.append(v)
    return dist, parent

def word_of(parent, source, v):
    w = []
    while v != source:
        u, L = parent[v]
        w.append(L)
        v = u
    w.reverse()
    return ''.join(w)

def eval_word(w):
    M = IDENT
    for ch in w:
        M = mm(M, GDICT[ch])
    return M

def main():
    # order checks
    sl = [(x0, x1, x2, x3)
          for x0 in range(P) for x1 in range(P)
          for x2 in range(P) for x3 in range(P)
          if (x0*x3 - x1*x2) % P == 1]
    assert len(sl) == 2184, len(sl)
    assert len(set(canon(M) for M in sl)) == 1092
    start = canon(IDENT)
    dist, parent = bfs(start)
    assert len(dist) == 1092, len(dist)
    D = max(dist.values())
    spheres = [sum(1 for v in dist if dist[v] == i) for i in range(D+1)]
    print("PSL order:", len(dist))
    print("diameter:", D)
    print("spheres:", spheres)
    assert sum(spheres) == 1092
    diam_nodes = sorted(v for v in dist if dist[v] == D)
    print("num diametral:", len(diam_nodes))
    for v in diam_nodes:
        w = word_of(parent, start, v)
        assert len(w) == D
        assert canon(eval_word(w)) == v, (w, v)
        print(v, w)
    # degree check
    nbs = set(canon(mm(start, G)) for _, G in GENS)
    assert len(nbs) == 4, nbs
    print("degree at identity: 4 OK")
    # generation
    print("generation <a,b>=G: BFS reached all 1092 OK")

if __name__ == "__main__":
    main()
