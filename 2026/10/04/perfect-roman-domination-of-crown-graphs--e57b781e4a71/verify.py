from itertools import product

def crown(n):
    # A = 0..n-1, B = n..2n-1; all cross edges except a_i b_i.
    N = 2*n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def is_prdf(adj, lab):
    for v, x in enumerate(lab):
        if x == 0:
            if sum(1 for u in adj[v] if lab[u] == 2) != 1:
                return False
    return True

def predicted_minimum(n, lab):
    if sum(lab) != 4:
        return False
    A = lab[:n]
    B = lab[n:]
    if A.count(2) != 1 or B.count(2) != 1:
        return False
    if A.count(0) != n-1 or B.count(0) != n-1:
        return False
    ia = A.index(2)
    ib = B.index(2)
    return ia == ib

graphs = 0
labelings = 0
minimum_functions = 0

for n in range(3, 8):
    adj = crown(n)
    best = 10**9
    mins = []
    for lab in product((0,1,2), repeat=2*n):
        labelings += 1
        w = sum(lab)
        if w > best:
            continue
        if is_prdf(adj, lab):
            if w < best:
                best = w
                mins = []
            mins.append(lab)
    assert best == 4, (n, best)
    assert len(mins) == n, (n, len(mins))
    assert all(predicted_minimum(n, lab) for lab in mins), n
    minimum_functions += len(mins)
    graphs += 1

print("VERIFY_OK")
print("crown_graphs_checked =", graphs)
print("labelings_checked =", labelings)
print("minimum_functions_checked =", minimum_functions)
print("parameters n = 3..7")
print("all perfect Roman domination numbers equal 4")
print("all minimum functions are exactly matched pairs of label-2 vertices")
print("all minimum-function counts equal n")
