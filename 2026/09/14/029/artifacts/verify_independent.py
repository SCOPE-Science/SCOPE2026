"""Independent verifier: different graph encoding, different BFS, different
enumeration order (reverse Gray-free stride using step coprime to 2^24),
recomputes the full ledger and the exact verdict inequality."""
import sys

# vertices (x,y); horizontal edges: y in 0..3, x in 0..2; vertical: x in 0..4? no, 0..3, y in 0..2
H = [(((x, y), (x + 1, y))) for y in range(4) for x in range(3)]
V = [(((x, y), (x, y + 1))) for x in range(4) for y in range(3)]
E = H + V
assert len(E) == 24
V2I = {(x, y): y * 4 + x for y in range(4) for x in range(4)}
AE = [(V2I[a], V2I[b]) for a, b in E]
ADJ = [[] for _ in range(16)]
for e, (u, v) in enumerate(AE):
    ADJ[u].append((v, e))
    ADJ[v].append((u, e))
SRC = [V2I[(0, y)] for y in range(4)]
TGT = {V2I[(3, y)] for y in range(4)}


def S_of(mask):
    from collections import deque
    d = [-1] * 16
    q = deque()
    for s in SRC:
        d[s] = 0
        q.append(s)
    while q:
        u = q.popleft()
        for w, e in ADJ[u]:
            if (mask >> e) & 1 and d[w] < 0:
                d[w] = d[u] + 1
                q.append(w)
    b = min((d[t] for t in TGT if d[t] >= 0), default=-1)
    return b


def main():
    N = 1 << 24
    STEP = 2 * N // 3 + 1  # odd => coprime to N, visits every mask exactly once
    assert STEP % 2 == 1
    hist = {}
    nc = 0
    ss = 0
    m = 0
    for _ in range(N):
        s = S_of(m)
        if s >= 0:
            nc += 1
            ss += s
            hist[s] = hist.get(s, 0) + 1
        m = (m + STEP) % N
    print("n_cross =", nc)
    print("sum_S =", ss)
    for k in sorted(hist):
        print(f"N[S={k}] =", hist[k])
    print("5*sum_S =", 5 * ss, " vs 18*n_cross =", 18 * nc)
    print("VERDICT =", "HOLDS" if 5 * ss >= 18 * nc else "DISPROVED")
    print("mean =", ss / nc)


main()
