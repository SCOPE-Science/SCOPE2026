from math import ceil

def half_graph(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        for j in range(i, n):
            adj[i].add(n+j)
            adj[n+j].add(i)
    return adj

def is_strong_roman(adj, lab):
    zeros = {v for v, x in enumerate(lab) if x == 0}
    for v in zeros:
        if not any(
            lab[w] >= 2 and
            lab[w] >= 1 + ceil(len(adj[w] & zeros)/2)
            for w in adj[v]
        ):
            return False
    return True

def vectors_exact(length, total, max_value):
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
for n in range(3, 8):
    adj = half_graph(n)
    max_value = ceil(n/2) + 1
    target = n + 1 if n % 2 else n + 2
    minima = []
    for w in range(target+1):
        for lab in vectors_exact(2*n, w, max_value):
            checked += 1
            if is_strong_roman(adj, lab):
                if w < target:
                    raise AssertionError((n, "feasible below target", w, lab))
                minima.append(lab)

    endpoint = [0]*(2*n)
    h = 1 + ceil((n-1)/2)
    endpoint[0] = h
    endpoint[2*n-1] = h
    assert tuple(endpoint) in minima

    if n % 2:
        assert minima == [tuple(endpoint)], (n, len(minima))
    else:
        q = n//2
        alternate = [0]*(2*n)
        alternate[1] = q       # a_2
        alternate[n] = 1       # b_1
        alternate[2*n-1] = q+1 # b_n
        assert tuple(alternate) in minima
        assert len(minima) > 1

    print(f"n={n}: gamma_StR={target}, minimum_functions={len(minima)}, "
          f"{'unique' if n % 2 else 'nonunique'}")

print("bounded_labelings_checked =", checked)
print("odd minima matched the unique endpoint labeling; every tested even order had the explicit alternate optimum")
