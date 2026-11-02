#!/usr/bin/env python3
"""Direct finite checks of restricted four-word universal-cycle enumeration.
Only Python standard library is required.
"""
from itertools import product
from math import factorial, comb
from fractions import Fraction


def family(q):
    assert q >= 2
    return [w for w in product(range(q), repeat=4) if len(set(w)) == 2]


def graph(q):
    edges = family(q)
    vs = sorted({e[:3] for e in edges} | {e[1:] for e in edges})
    indeg = {v: 0 for v in vs}
    outdeg = {v: 0 for v in vs}
    adj = {v: [] for v in vs}
    for e in edges:
        u, v = e[:3], e[1:]
        adj[u].append(e)
        indeg[v] += 1
        outdeg[u] += 1
    return vs, edges, adj, indeg, outdeg


def determinant_bareiss(mat):
    a = [row[:] for row in mat]
    n = len(a)
    if not n:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((r for r in range(k + 1, n) if a[r][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            x = a[i][k]
            for j in range(k+1, n):
                value = a[i][j] * pivot - x * a[k][j]
                assert value % prev == 0
                a[i][j] = value // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def rooted_tree_cofactor(q):
    vs, edges, adj, indeg, outdeg = graph(q)
    assert len(edges) == 7*q*(q-1)
    assert len(vs) == q + 3*q*(q-1)
    assert all(outdeg[v] == indeg[v] == ((q-1) if len(set(v)) == 1 else 2) for v in vs)
    idx = {v:i for i,v in enumerate(vs)}
    matrix = [[0]*len(vs) for _ in vs]
    for v in vs:
        matrix[idx[v]][idx[v]] = outdeg[v]
    for e in edges:
        matrix[idx[e[:3]]][idx[e[1:]]] -= 1
    root_index = idx[(0,0,0)]
    minor = [[matrix[i][j] for j in range(len(vs)) if j != root_index]
             for i in range(len(vs)) if i != root_index]
    return determinant_bareiss(minor)


def tree_formula(q):
    return (2**((q-1)*(q+2)) * (q**(q-2)) * 7**comb(q-1,2))


def cycle_formula(q):
    return tree_formula(q) * factorial(q-2)**q


def brute_binary():
    _, edges, adj, _, _ = graph(2)
    assigned = {e:i for i,e in enumerate(edges)}
    first = (0,0,0,1)
    assert first in assigned
    total = len(edges)
    memo = {}
    def count(node, mask):
        if mask == (1<<total)-1:
            return int(node == (0,0,0))
        key = (node,mask)
        if key not in memo:
            memo[key] = sum(count(e[1:], mask | (1<<assigned[e]))
                            for e in adj[node] if not (mask & (1<<assigned[e])))
        return memo[key]
    return count(first[1:], 1<<assigned[first])


def construct_cycle(q):
    _, edges, adj, _, _ = graph(q)
    first=(0,0,0,1)
    assert first in edges
    used=set([first])
    # Hierholzer on residual edges after first, start at first head, end at tail.
    available={v:sorted([e for e in es if e != first],reverse=True) for v,es in adj.items()}
    stack=[(first[1:],None)]
    circuit=[]
    while stack:
        node, incoming=stack[-1]
        if available[node]:
            e=available[node].pop()
            assert e not in used
            used.add(e)
            stack.append((e[1:],e))
        else:
            stack.pop()
            if incoming is not None:
                circuit.append(incoming)
    circuit.reverse()
    assert len(circuit)==len(edges)-1 and len(used)==len(edges)
    assert circuit[-1][1:]==first[:3]
    edge_list=[first]+circuit
    s=''.join(str(e[0]) for e in edge_list)
    circular_windows={tuple(map(int,(s+s[:3])[i:i+4])) for i in range(len(s))}
    assert len(s)==len(edges)
    assert circular_windows==set(edges)
    assert len(circular_windows)==len(s)
    return s



def verify_six_state_gadget():
    X = [[2,-1,-1,0,0,0],
         [0,2,0,0,-1,-1],
         [0,0,2,-1,0,0],
         [0,0,0,2,-1,-1],
         [0,-1,-1,0,2,0],
         [-1,0,0,0,0,2]]
    assert determinant_bareiss(X)==28
    # Signed couplings: row A_a points to B_ab; D_ba points to A_a.
    # The second ordered direction interchanges a and b.
    U = [[-1,0,0,0,0,0],[0,0,0,-1,0,0]]
    T = [[0,0],[0,0],[0,-1],[0,0],[0,0],[-1,0]]
    # Solve X Y=T exactly over rationals.
    aug=[[Fraction(x) for x in X[i]+T[i]] for i in range(6)]
    for j in range(6):
        r=next(r for r in range(j,6) if aug[r][j])
        aug[r],aug[j]=aug[j],aug[r]
        pivot=aug[j][j]
        aug[j]=[e/pivot for e in aug[j]]
        for i in range(6):
            if i!=j:
                factor=aug[i][j]
                aug[i]=[x-factor*y for x,y in zip(aug[i],aug[j])]
    Y=[row[6:] for row in aug]
    transfer=[[sum(U[i][k]*Y[k][j] for k in range(6)) for j in range(2)]
              for i in range(2)]
    assert transfer==[[Fraction(3,7),Fraction(4,7)],
                      [Fraction(4,7),Fraction(3,7)]]
    return 'det X=28; transfer=1/7 [[3,4],[4,3]]'

def main():
    print(verify_six_state_gadget())
    assert brute_binary() == 16
    for q in range(2,7):
        t=rooted_tree_cofactor(q)
        assert t==tree_formula(q), (q,t,tree_formula(q))
        print('q',q,'vertices',q+3*q*(q-1),'edges',7*q*(q-1),
              'arborescences',t,'cycles',cycle_formula(q))
    for q in (2,3,4):
        s=construct_cycle(q)
        print('cyclic witness q',q,':',s)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
