from itertools import combinations_with_replacement, product

def partitions(n, r, lo=1):
    if r == 0:
        if n == 0:
            yield ()
        return
    for x in range(lo, n + 1):
        if n - x < x * (r - 1):
            break
        for rest in partitions(n - x, r - 1, x):
            yield (x,) + rest

def spider(lengths):
    adj=[set()]
    arms=[]
    for ell in lengths:
        arm=[]
        prev=0
        for _ in range(ell):
            v=len(adj)
            adj.append(set())
            adj[prev].add(v)
            adj[v].add(prev)
            arm.append(v)
            prev=v
        arms.append(arm)
    return adj, arms

def is_zero_forcing(adj, mask):
    n=len(adj)
    blue=mask
    while True:
        changed=False
        for u in range(n):
            if not ((blue>>u)&1):
                continue
            whites=[v for v in adj[u] if not ((blue>>v)&1)]
            if len(whites)==1:
                blue |= 1<<whites[0]
                changed=True
                break
        if not changed:
            break
    return blue == (1<<n)-1

def minimal_zero_forcing_masks(adj):
    n=len(adj)
    out=[]
    tested=0
    for mask in range(1<<n):
        tested += 1
        if not is_zero_forcing(adj, mask):
            continue
        ok=True
        for v in range(n):
            if ((mask>>v)&1) and is_zero_forcing(adj, mask & ~(1<<v)):
                ok=False
                break
        if ok:
            out.append(mask)
    return out, tested

def predicted_masks(lengths, arms):
    k=len(lengths)
    out=set()

    # Type C: centered. Omit one arm; every represented arm contributes
    # its center-neighbor and must have length at least two.
    for omit in range(k):
        occ=[i for i in range(k) if i != omit]
        if all(lengths[i] >= 2 for i in occ):
            mask=1  # center
            for i in occ:
                mask |= 1 << arms[i][0]
            out.add(mask)

    # Type N: noncentered. Omit exactly one arm. On every represented arm:
    # R = center-neighbor singleton (passive, only if nonleaf);
    # L = leaf singleton (trigger);
    # D_t = adjacent pair at positions t,t+1, 1 <= t <= ell-2 (trigger).
    # At least one trigger is needed. A shallow D_1 may occur only when
    # it is the unique trigger.
    for omit in range(k):
        local=[]
        for i in range(k):
            if i == omit:
                continue
            arm=arms[i]
            ell=lengths[i]
            opts=[]
            if ell >= 2:
                opts.append((1 << arm[0], False, False))
            opts.append((1 << arm[-1], True, False))
            for s in range(0, ell-2):
                opts.append(((1 << arm[s]) | (1 << arm[s+1]), True, s == 0))
            local.append(opts)

        for choices in product(*local):
            triggers=sum(int(x[1]) for x in choices)
            shallow=sum(int(x[2]) for x in choices)
            if triggers == 0:
                continue
            if shallow and triggers != 1:
                continue
            mask=0
            for m,_,_ in choices:
                mask |= m
            out.add(mask)
    return out

def upper_formula(lengths):
    k=len(lengths)
    q=sum(ell == 1 for ell in lengths)
    L=sum(ell >= 4 for ell in lengths)
    extra=max(1 if q <= 1 else 0, min(k-1, L))
    return (k-1) + extra

types=subsets=minsets=0
for n in range(4, 14):
    for k in range(3, n):
        for lengths in partitions(n-1, k):
            adj, arms=spider(lengths)
            actual, tested=minimal_zero_forcing_masks(adj)
            pred=predicted_masks(lengths, arms)
            actual_set=set(actual)
            assert actual_set == pred, (
                lengths,
                sorted(actual_set - pred),
                sorted(pred - actual_set),
            )
            upper=max(mask.bit_count() for mask in actual)
            assert upper == upper_formula(lengths), (lengths, upper, upper_formula(lengths))
            assert min(mask.bit_count() for mask in actual) == k-1
            types += 1
            subsets += tested
            minsets += len(actual)

print("VERIFY_OK")
print("spider_isomorphism_types_checked =", types)
print("vertex_subsets_checked =", subsets)
print("minimal_zero_forcing_sets_checked =", minsets)
print("orders = 4..13")
print("all minimal-set classifications matched exactly")
print("all upper-zero-forcing formulas matched")
print("minimum zero forcing number k-1 matched")
