#!/usr/bin/env python3
"""Reproduce the topological distinction between the Hoffman graph and Q4.

No external dependencies. All masks, incidences, and characteristic-polynomial
coefficients are computed afresh from two explicitly given 16-vertex graphs.
"""
from collections import Counter, defaultdict, deque
import json
from pathlib import Path
from math import comb

# A(H) = [0 D; D^T 0], with vertices 0..7 followed by 8..15.
HOFFMAN_BIPARTITE = (
    (1, 1, 1, 1, 0, 0, 0, 0),
    (1, 1, 1, 0, 1, 0, 0, 0),
    (1, 0, 0, 1, 0, 1, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (0, 0, 1, 1, 0, 0, 1, 1),
    (1, 0, 0, 0, 1, 1, 1, 0),
    (0, 1, 0, 0, 1, 1, 0, 1),
    (0, 0, 1, 0, 1, 0, 1, 1),
)

def graphs():
    h = [[0] * 16 for _ in range(16)]
    for i in range(8):
        for j in range(8):
            h[i][8+j] = h[8+j][i] = HOFFMAN_BIPARTITE[i][j]
    q = [[int((i ^ j).bit_count() == 1) for j in range(16)] for i in range(16)]
    return h, q

def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

def characteristic_polynomial(a):
    # Faddeev-LeVerrier: exact integer arithmetic, no symbolic library.
    n = len(a)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    ans = [1]
    for k in range(1, n+1):
        ab = matmul(a, b)
        trace = sum(ab[i][i] for i in range(n))
        assert trace % k == 0
        ck = -trace // k
        ans.append(ck)
        b = [[ab[i][j] + (ck if i == j else 0) for j in range(n)]
             for i in range(n)]
    return tuple(ans)

def polyprod(roots):
    p = [1]
    for root in roots:
        q = [0] * (len(p)+1)
        for j,x in enumerate(p):
            q[j] += x
            q[j+1] -= root*x
        p = q
    return tuple(p)

def independent_faces(a):
    n = len(a)
    assert n == 16
    adj = [sum(a[i][j] << j for j in range(n)) for i in range(n)]
    good = {0}
    for mask in range(1, 1<<n):
        low = mask & -mask
        v = low.bit_length()-1
        other = mask ^ low
        if other in good and not (other & adj[v]):
            good.add(mask)
    return good

def matching_certificate(faces, certificate_data):
    # Deterministic greedy vertex-pivot matching, excluding the empty face.
    rem = faces - {0}
    pairs = []
    counts = []
    for v in range(16):
        bit = 1 << v
        p = [(a, a | bit) for a in sorted(rem)
             if not (a & bit) and (a | bit) in rem]
        assert len(set(x for pair in p for x in pair)) == 2*len(p)
        for a,b in p:
            rem.remove(a)
            rem.remove(b)
        pairs.extend(p)
        counts.append(len(p))
    assert 2*len(pairs)+len(rem) == len(faces)-1
    assert certificate_data['pairs'] == [[x, y] for x,y in pairs]
    assert certificate_data['critical_masks'] == sorted(rem)
    pm = {(lo, hi) for lo,hi in pairs}
    # Forman's directed Hasse graph: unmatched incidences down, matched up.
    # The Kahn traversal certifies EVERY directed edge is globally acyclic.
    nodes = sorted(faces-{0})
    explicit_order = certificate_data['topological_order']
    assert len(explicit_order) == len(nodes)
    assert set(explicit_order) == set(nodes)
    positions = {x:i for i,x in enumerate(explicit_order)}
    indegree = {x:0 for x in nodes}
    arrows = defaultdict(list)
    total = 0
    for hi in nodes:
        t = hi
        while t:
            low = t & -t
            lo = hi ^ low
            t ^= low
            if lo == 0:continue
            src,dst = (lo,hi) if (lo,hi) in pm else (hi,lo)
            # Check the explicit finite topological-order certificate directly.
            assert positions[src] < positions[dst], ('invalid certificate arrow',src,dst)
            arrows[src].append(dst)
            indegree[dst]+=1
            total+=1
    work = deque(x for x in nodes if indegree[x]==0)
    sorted_count = 0
    while work:
        x=work.popleft()
        sorted_count+=1
        for y in arrows[x]:
            indegree[y]-=1
            if indegree[y]==0:work.append(y)
    assert sorted_count == len(nodes), ('directed Morse cycle',sorted_count,len(nodes))
    assert all(indegree[v]==0 for v in nodes)
    assert all(x in faces for x in rem)
    return counts, Counter(x.bit_count()-1 for x in rem),len(pairs),total

def mod2_boundary_ranks(faces):
    bysize=defaultdict(list)
    for s in sorted(faces):bysize[s.bit_count()].append(s)
    ranks={}
    for k in range(1,max(bysize)+1):
        index={x:j for j,x in enumerate(bysize[k-1])}
        basis={}
        for top in bysize[k]:
            col=0; left=top
            while left:
                bit=left & -left;left ^= bit
                col ^= 1 << index[top ^ bit]
            while col:
                j=col.bit_length()-1
                if j in basis:col ^= basis[j]
                else:
                    basis[j]=col
                    break
        ranks[k]=len(basis)
    betti={k-1:len(bysize[k])-ranks.get(k,0)-ranks.get(k+1,0)
           for k in range(max(bysize)+1)}
    return tuple(ranks.get(i,0) for i in range(1,max(bysize)+1)),betti

def analyze(name,a,expected_f,expected_pairs,expected_crit,expected_rank):
    assert all(a[i][i]==0 and sum(a[i])==4 and all(a[i][j]==a[j][i] for j in range(16)) for i in range(16))
    f=independent_faces(a)
    counts=tuple(sum(s.bit_count()==k for s in f) for k in range(9))
    assert counts==expected_f,(name,counts)
    cert = json.loads((Path(__file__).parent/'morse_certificate.json').read_text(encoding='utf8'))
    pcounts, crit, pairs, arrows = matching_certificate(f, cert[name])
    assert pairs==expected_pairs and dict(crit)==expected_crit,(name,pairs,crit)
    ranks,betti=mod2_boundary_ranks(f)
    assert ranks==expected_rank,(name,ranks)
    assert all(beta==(expected_crit.get(3,0) if k==3 else 0) for k,beta in betti.items() if k>=0),(name,betti)
    charpoly=characteristic_polynomial(a)
    print(name,'faces',len(f),'f_vector',counts)
    print(name,'matching_pivots',tuple(pcounts),'pairs',pairs,
          'critical',dict(sorted(crit.items())),'DAG_incidences',arrows)
    print(name,'mod2_reduced_boundary_ranks',ranks,
          'reduced_betti',tuple(betti.get(j,0) for j in range(8)))
    return counts,charpoly

def main():
    h,q=graphs()
    hf,hp=analyze('HOFFMAN',h,(1,16,88,208,228,132,56,16,2),371,{0:1,3:3},(1,15,73,135,90,42,14,2))
    qf,qp=analyze('Q4',q,(1,16,88,208,228,128,56,16,2),367,{0:1,3:7},(1,15,73,135,86,42,14,2))
    target=polyprod((4,2,2,2,2,0,0,0,0,0,0,-2,-2,-2,-2,-4))
    assert hp==qp==target
    print('IDENTICAL_ADJACENCY_CHARACTERISTIC_POLYNOMIAL',target)
    assert all(hf[k]==qf[k] for k in range(9) if k!=5)
    assert hf[5]-qf[5]==4
    print('INDEPENDENCE_POLYNOMIAL_H_MINUS_Q4_EQUALS_4z^5')
    print('EXACT_HOMOTOPY_TYPES_HOFFMAN_WEDGE_3_S3_Q4_WEDGE_7_S3')
    print('VERIFY_OK_HOFFMAN_Q4_SPECTRAL_INDEPENDENCE_HOMOTOPY')
if __name__=='__main__':main()
