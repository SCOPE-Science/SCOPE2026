"""Finite integral discrete-Morse certificate for distance-neighborhood complexes of the icosahedral graph.
Run: python3 verify_icosa_morse.py (standard library only).
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 12
EDGES = set()
def edge(a, b):
    assert a != b
    EDGES.add(tuple(sorted((a,b))))

for i in range(5):
    edge(0, 1+i)
    edge(11, 6+i)
    edge(1+i, 1+(i+1)%5)
    edge(6+i, 6+(i+1)%5)
    edge(1+i, 6+i)
    edge(1+i, 6+(i-1)%5)
assert len(EDGES) == 30
ADJ = {v: set() for v in range(N)}
for a,b in EDGES:
    ADJ[a].add(b)
    ADJ[b].add(a)
assert all(len(ADJ[v]) == 5 for v in range(N))

DIST = {}
for start in range(N):
    distances = {start:0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in sorted(ADJ[v]):
            if w not in distances:
                distances[w] = distances[v]+1
                queue.append(w)
    assert Counter(distances.values()) == {0:1,1:5,2:5,3:1}
    DIST[start] = distances
ANTI = {v:next(w for w in range(N) if DIST[v][w] == 3) for v in range(N)}
assert all(DIST[ANTI[v]][w] == 3-DIST[v][w] for v in range(N) for w in range(N))

def faces(D):
    facets = [sum(1<<w for w in range(N) if DIST[v][w] in D) for v in range(N)]
    return {mask for facet in facets for mask in range(1,1<<N) if (mask & ~facet)==0}

def boundary(t):
    verts = [v for v in range(N) if t>>v & 1]
    return {t ^ (1<<v): (1 if i%2==0 else -1)
            for i,v in enumerate(verts) if t^(1<<v)}

def verify(D):
    F = faces(D)
    remaining = set(F)
    pairs = []
    # Process vertices in ascending order. At each stage pair currently
    # unpaired simplices with their one-vertex extensions when both occur.
    for v in range(N):
        bit = 1<<v
        for s in sorted(remaining):
            t = s|bit
            if s in remaining and (s&bit)==0 and t in remaining:
                remaining.remove(s)
                remaining.remove(t)
                pairs.append((s,t))
    assert len(F)==2*len(pairs)+len(remaining)
    low_to_high = dict(pairs)
    high_to_low = {t:s for s,t in pairs}
    assert len(low_to_high)==len(high_to_low)==len(pairs)
    critical = Counter(s.bit_count()-1 for s in remaining)

    # Full verification of acyclicity: reverse matched Hasse edges;
    # every other codimension-one incidence points from coface to face.
    indegree = dict.fromkeys(F,0)
    oriented = {s:[] for s in F}
    incidences = 0
    for t in F:
        for s in boundary(t):
            if low_to_high.get(s)==t:
                a,b=s,t
            else:
                a,b=t,s
            oriented[a].append(b)
            indegree[b] += 1
            incidences += 1
    queue = deque(s for s,v in indegree.items() if v == 0)
    visited = 0
    while queue:
        s = queue.popleft()
        visited += 1
        for t in oriented[s]:
            indegree[t] -= 1
            if indegree[t]==0:
                queue.append(t)
    assert visited == len(F), f'cyclic gradient for distance set {D}'

    # In the only two cases with adjacent critical dimensions,
    # compute the signed integral degree of every 3-cell attaching map.
    if D in ((0,1,3),(0,2,3)):
        critical2 = sorted(s for s in remaining if s.bit_count()==3)
        critical3 = sorted(s for s in remaining if s.bit_count()==4)
        assert len(critical2)==6 and len(critical3)==21
        @lru_cache(None)
        def reduce_face(a):
            if a in remaining:
                return {a:1}
            if a in high_to_low:
                return {}  # matched as a higher simplex
            b = low_to_high[a]
            pivot = boundary(b)[a]
            assert pivot in (-1,1)
            result = defaultdict(int)
            for s,coef in boundary(b).items():
                if s != a:
                    for r,amount in reduce_face(s).items():
                        result[r] -= pivot*coef*amount
            return {r:amount for r,amount in result.items() if amount}
        for top in critical3:
            coeffs = defaultdict(int)
            for s,coef in boundary(top).items():
                for r,amount in reduce_face(s).items():
                    coeffs[r] += coef*amount
            assert all(coeffs.get(r,0)==0 for r in critical2)
            assert all(coeffs.get(r,0)==0 for r in coeffs)
    return len(F),len(pairs),critical,incidences

EXPECTED = {
 1:{0:12}, 2:{0:1,2:23}, 3:{0:1,2:1}, 4:{0:1,2:23},
 5:{0:1,2:1}, 6:{0:1,4:1}, 7:{0:1,10:1}, 8:{0:12},
 9:{0:6}, 10:{0:1,2:1}, 11:{0:1,2:6,3:21},
 12:{0:1,2:1}, 13:{0:1,2:6,3:21}, 14:{0:1,10:1}, 15:{0:1}
}
EXPECTED_TOTAL = {1:12,2:264,3:446,4:264,5:446,6:3366,7:4094,8:12,
                  9:18,10:446,11:1006,12:446,13:1006,14:4094,15:4095}

def main():
    for mask in range(1,16):
        D=tuple(i for i in range(4) if mask&(1<<i))
        n,p,critical,inc=verify(D)
        assert n==EXPECTED_TOTAL[mask] and critical==EXPECTED[mask]
        print(f'D={D} faces={n} pairs={p} critical={dict(sorted(critical.items()))} incidences={inc}')
    for mask in range(1,16):
        complement_mask=sum(1<<(3-i) for i in range(4) if mask&(1<<i))
        assert faces(tuple(i for i in range(4) if mask&(1<<i))) == faces(tuple(i for i in range(4) if complement_mask&(1<<i)))
    print('ICOSAHEDRAL_DISTANCE_MORSE_PASS')
if __name__=='__main__':main()
