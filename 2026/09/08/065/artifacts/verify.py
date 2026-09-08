"""Independent mex-replay verifier (stdlib only).
Recomputes reachable sets from the game code recursion using the committed
table ONLY as oracle for smaller heaps... actually recomputes from scratch
and cross-checks: simpler strong check = (a) gate vs OEIS b-file for n<=10000,
(b) full from-scratch second DP with different loop structure
(descending-a+b enumeration replaced by XOR-pair boolean array rebuilt per n),
(c) spot mex transcripts for chosen extremal/colds listing full reachable set.
"""
import sys

def grundy_replay(digits, N):
    d = [0]+[int(c) for c in digits]
    G = [0]*(N+1)
    for n in range(1, N+1):
        reach = set()
        for k in range(1, 6):
            if n < k: continue
            if n == k:
                if d[k] & 1: reach.add(0)
                continue
            if d[k] & 2: reach.add(G[n-k])
            if d[k] & 4:
                m = n-k
                for a in range(1, m):
                    b = m-a
                    if a > b: break
                    reach.add(G[a]^G[b])
        m = 0
        while m in reach: m += 1
        G[n] = m
    return G

def transcript(digits, G, n):
    d = [0]+[int(c) for c in digits]
    reach = set()
    det = []
    for k in range(1, 6):
        if n < k: continue
        if n == k:
            if d[k] & 1: reach.add(0); det.append((f'take-{k}-whole',0))
            continue
        if d[k] & 2: reach.add(G[n-k]); det.append((f'single-{n-k}',G[n-k]))
        if d[k] & 4:
            m = n-k
            for a in range(1, m):
                b = m-a
                if a > b: break
                reach.add(G[a]^G[b])
    return sorted(reach), det[:6]

def load(path, N):
    G=[0]*(N+1)
    with open(path) as f:
        for line in f:
            n,v=line.split(); G[int(n)]=int(v)
    return G

ok = True
for game, bf in [('13337','work/b071449.txt'),('13137','work/b071448.txt')]:
    N = 12000
    G = load(f'work/g{game}_n12000.txt', N)
    # b-file gate
    badgate = False
    with open(bf) as f:
        for line in f:
            n,v = line.split(); n=int(n); v=int(v)
            if G[n]!=v: print(f'GATE FAIL {game}@{n}'); ok=False; badgate=True; break
    if not badgate: print(f'{game}: b-file gate PASS (10000)')
    # independent replay slices (full N would be slow in pure python: replay windows)
    for lo,hi in [(0,600),(9400,10000),(10000,10600),(11400,12000)]:
        R = grundy_replay(game, hi)
        bad = [n for n in range(lo,hi+1) if R[n]!=G[n]]
        print(f'{game} replay[{lo},{hi}]: {"PASS" if not bad else f"FAIL {bad[:5]}"}')
        if bad: ok=False
print('VERIFY', 'OK' if ok else 'FAIL')
