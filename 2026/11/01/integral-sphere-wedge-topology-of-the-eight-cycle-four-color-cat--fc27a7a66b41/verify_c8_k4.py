#!/usr/bin/env python3
"""Exact combinatorial verification for Ind(C_8 x K_4).

All graph vertices are indexed 4*r+c, r in Z/8, c in {0,1,2,3}.
No external packages or downloaded data are needed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from itertools import combinations

M, N = 8, 4
V = M * N

def construct_graph():
    adjacency = []
    for r in range(M):
        for c in range(N):
            nbrs = {N*((r+dr) % M)+d for dr in (-1,1)
                    for d in range(N) if d != c}
            assert len(nbrs) == 6
            adjacency.append(sum(1 << u for u in nbrs))
    assert sum(a.bit_count() for a in adjacency) == 192
    assert all(bool(adjacency[u] >> v & 1) == bool(adjacency[v] >> u & 1)
               for u in range(V) for v in range(V))
    return adjacency

def enumerate_faces(adjacency):
    faces = [0]
    for v in range(V):
        bit = 1 << v
        earlier = list(faces)
        faces.extend(s | bit for s in earlier if not (adjacency[v] & s))
    assert len(set(faces)) == len(faces)
    return set(faces) - {0}

def facets(s):
    k = 0
    t = s
    while t:
        b = t & -t
        yield (s ^ b, 1 if k % 2 == 0 else -1)
        t ^= b
        k += 1

def pairing(all_faces):
    unmatched = set(all_faces)
    lower_to_upper = {}
    for v in range(V):
        bit = 1 << v
        for sigma in sorted(unmatched):
            tau = sigma | bit
            if sigma in unmatched and not (sigma & bit) and tau in unmatched:
                lower_to_upper[sigma] = tau
                unmatched.remove(sigma)
                unmatched.remove(tau)
    assert len(lower_to_upper) * 2 + len(unmatched) == len(all_faces)
    assert len(set(lower_to_upper.values())) == len(lower_to_upper)
    return lower_to_upper, unmatched

def check_hasse_acyclic(all_faces, matches):
    # Hasse arrows normally go from simplex to facet; matched pairs are reversed.
    outgoing = defaultdict(list)
    indegree = {s:0 for s in all_faces}
    count = 0
    for high in all_faces:
        for low, _ in facets(high):
            if not low:
                continue
            if matches.get(low) == high:
                source, target = low, high
            else:
                source, target = high, low
            outgoing[source].append(target)
            indegree[target] += 1
            count += 1
    queue = deque(s for s in all_faces if indegree[s] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert visited == len(all_faces), (visited,len(all_faces))
    return count

def integer_reduction(matches, critical):
    # Standard algebraic Morse cancellation: eliminate all matched unit pairs.
    # A matched upper face is zero in the projected chain group; lower faces are
    # recursively rewritten using the oriented boundary of their matched upper.
    @lru_cache(None)
    def reduce_face(s):
        if s in critical:
            return {s: 1}
        if s not in matches:
            return {}
        tau = matches[s]
        boundary = list(facets(tau))
        unit = next(a for t, a in boundary if t == s)
        assert unit in (-1, 1)
        result = Counter()
        for other, incidence in boundary:
            if other == s:
                continue
            for c, coefficient in reduce_face(other).items():
                result[c] -= unit * incidence * coefficient
        return {k: v for k,v in result.items() if v}

    lower = sorted(s for s in critical if s.bit_count() == 5)  # 4-cells
    upper = sorted(s for s in critical if s.bit_count() == 6)  # 5-cells
    assert len(lower) == 24 and len(upper) == 27
    matrix = [[0]*len(upper) for _ in lower]
    for j, simplex in enumerate(upper):
        image = Counter()
        for face, incidence in facets(simplex):
            for c, coefficient in reduce_face(face).items():
                image[c] += incidence * coefficient
        assert set(image).issubset(set(lower))
        for i,c in enumerate(lower):
            matrix[i][j] = image[c]
    return matrix, lower, upper, reduce_face.cache_info()

def exact_rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m,n=len(a),len(a[0]);rank=0
    for j in range(n):
        p=next((i for i in range(rank,m) if a[i][j]!=0),None)
        if p is None:continue
        a[rank],a[p]=a[p],a[rank]
        pivot=a[rank][j]
        for i in range(rank+1,m):
            if a[i][j]:
                multiple=a[i][j]/pivot
                for k in range(j,n):a[i][k]-=multiple*a[rank][k]
        rank+=1
        if rank==m:break
    return rank

def bareiss_determinant(mat):
    a = [[int(x) for x in row] for row in mat]
    n=len(a)
    sign = 1
    prev = 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot=next((j for j in range(k+1,n) if a[j][k]),None)
            if pivot is None: return 0
            a[k],a[pivot] = a[pivot],a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value = a[i][j]*p-a[i][k]*a[k][j]
                assert value % prev == 0
                a[i][j] = value // prev
            a[i][k] = 0
        prev = p
    return sign*a[-1][-1]

def main():
    adj=construct_graph()
    f=enumerate_faces(adj)
    matches,crit=pairing(f)
    arrows=check_hasse_acyclic(f,matches)
    counts=dict(sorted(Counter(s.bit_count()-1 for s in crit).items()))
    assert len(f)==196226 and len(matches)==98087
    assert counts=={0:1,4:24,5:27}
    matrix,lo,hi,info=integer_reduction(matches,crit)
    assert exact_rank(matrix)==21
    rows=tuple(list(range(20))+[21])
    cols=(1,2,3,4,5,6,7,8,9,10,11,14,15,16,17,18,19,20,21,22,23)
    minor=[[matrix[i][j] for j in cols] for i in rows]
    assert bareiss_determinant(minor)==-1
    by_dim=Counter(s.bit_count()-1 for s in f)
    fvector=[by_dim[i] for i in range(max(by_dim)+1)]
    assert fvector==[32,400,2560,9400,21440,33040,37728,34488,26336,16896,8864,3648,1120,240,32,2]
    euler=sum((-1)**d*z for d,z in by_dim.items())
    assert euler==1+3-6==-2
    print('GRAPH: 32 vertices, 96 edges, degree 6')
    print('INDEPENDENT NONEMPTY FACES:',len(f))
    print('FACE VECTOR:',fvector)
    print('MATCHED PAIRS:',len(matches),'ORIENTED HASSE EDGES:',arrows,'ACYCLIC: YES')
    print('CRITICAL CELLS:',counts)
    print('CRITICAL DIM-4 MASKS:',lo)
    print('CRITICAL DIM-5 MASKS:',hi)
    print('MORSE BOUNDARY: 24 x 27 integer matrix, rows critical dimension 4')
    for row in matrix: print(' '.join(map(str,row)))
    print('MORSE BOUNDARY RATIONAL RANK:',exact_rank(matrix))
    print('UNIT MINOR (0-based rows and columns):',rows,cols)
    print('UNIT MINOR DETERMINANT:',bareiss_determinant(minor))
    print('INTEGRAL SMITH FACTORS: twenty-one 1s and three zero diagonal entries')
    print('REDUCED INTEGRAL HOMOLOGY: H4=Z^3, H5=Z^6, others zero')
    print('HOMOTOPY TYPE: wedge of three S4 and six S5')
    print('RECURSIVE REDUCTION:',info)
    print('CYCLE8_K4_INTEGRAL_MORSE_VERIFIED')

if __name__=='__main__':main()
