from itertools import combinations


def partitions(n):
    out = []
    def rec(i, blocks):
        if i == n:
            labels = [None] * n
            for j, block in enumerate(blocks):
                for x in block:
                    labels[x] = j
            out.append(tuple(labels))
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            rec(i + 1, blocks)
            blocks[j].pop()
        blocks.append([i])
        rec(i + 1, blocks)
        blocks.pop()
    rec(0, [])
    return out


def canon(p):
    rename = {}
    nxt = 0
    ans = []
    for v in p:
        if v not in rename:
            rename[v] = nxt
            nxt += 1
        ans.append(rename[v])
    return tuple(ans)


def is_coarsening(p, q):
    n = len(p)
    return all(p[i] != p[j] or q[i] == q[j]
               for i in range(n) for j in range(n))


def collapse_on_tuple_values(p, q):
    m = {}
    for i, value in enumerate(p):
        if value in m:
            assert m[value] == q[i]
        else:
            m[value] = q[i]
    return m


def induced_partition(p, m):
    return canon(tuple(m[x] for x in p))


for n in range(8):
    ps = partitions(n)
    coarsening_pairs = 0
    for p in ps:
        for q in ps:
            if is_coarsening(p, q):
                coarsening_pairs += 1
                m = collapse_on_tuple_values(p, q)
                assert induced_partition(p, m) == canon(q)
    print(f"n={n} partitions={len(ps)} coarsening_pairs={coarsening_pairs}")
print("VERIFY_OK")
