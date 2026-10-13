from math import comb

def half_graph(n):
    # a_i = i-1, b_j = n+j-1; edge a_i b_j iff i <= j.
    adj = [set() for _ in range(2*n)]
    for i in range(1, n+1):
        for j in range(i, n+1):
            a = i-1
            b = n+j-1
            adj[a].add(b)
            adj[b].add(a)
    return adj

def is_k_rdf(adj, lab, k):
    for v, x in enumerate(lab):
        if x < k:
            active = [u for u in adj[v] if lab[u] > 0]
            total = x + sum(lab[u] for u in active)
            if total < k + len(active):
                return False
    return True

def bounded_vectors(length, total, max_value):
    vec = [0]*length
    def rec(i, rem):
        if i == length:
            if rem == 0:
                yield tuple(vec)
            return
        for x in range(min(max_value, rem)+1):
            vec[i] = x
            yield from rec(i+1, rem-x)
    yield from rec(0, total)

print("VERIFY_OK")
checked = 0
for k in range(2, 6):
    for n in range(3, 6):
        adj = half_graph(n)
        target = 2*(k+1)
        feasible_below = 0
        minima = []
        for w in range(target+1):
            for lab in bounded_vectors(2*n, w, k+1):
                checked += 1
                if is_k_rdf(adj, lab, k):
                    if w < target:
                        feasible_below += 1
                    elif w == target:
                        minima.append(lab)
        expected = [0]*(2*n)
        expected[0] = k+1       # a_1
        expected[2*n-1] = k+1   # b_n
        assert feasible_below == 0, (k, n, feasible_below)
        assert minima == [tuple(expected)], (k, n, len(minima), minima[:3])
        print(f"k={k}, n={n}: gamma_[kR]={target}, minimum_functions=1")

print("bounded_labelings_checked =", checked)
print("all minima matched the unique endpoint labeling")
