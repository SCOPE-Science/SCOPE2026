"""Exact E(n): for each AHU a-type (valid fiber), exhaust all b completions with BFS.
Saves checkpoints; prints maxima + witnesses."""
import itertools, math, sys, time, json
from itertools import product
sys.path.insert(0, 'output/artifacts')
from ahu import ahu_code
from bfs2 import rt_forward

def fiber_need(a):
    n = len(a)
    ia = [0]*n
    for q in range(n):
        ia[a[q]] += 1
    return [2-ia[q] for q in range(n)]

def multiset_perms(slots):
    # distinct permutations via backtracking on Counter
    from collections import Counter
    c = Counter(slots)
    keys = sorted(c.keys())
    cur = [0]*len(slots)
    def rec(i):
        if i == len(slots):
            yield tuple(cur)
            return
        for k in keys:
            if c[k]:
                c[k] -= 1
                cur[i] = k
                yield from rec(i+1)
                c[k] += 1
    yield from rec(0)

def exact_E(n, log_every=1):
    # group a-labelings by AHU code
    groups = {}
    for a in product(range(n), repeat=n):
        need = fiber_need(a)
        if any(v < 0 for v in need):
            continue
        key = repr(ahu_code(a))
        if key not in groups:
            groups[key] = a  # first rep
    print(f"n={n}: {len(groups)} AHU reps", flush=True)
    best = -1
    best_pairs = []
    total_runs = 0
    t0 = time.time()
    for gi, (key, a) in enumerate(groups.items()):
        need = fiber_need(a)
        slots = []
        for qq in range(n):
            slots += [qq]*need[qq]
        fmax = -1
        fbest = None
        runs = 0; syncs = 0
        for b in multiset_perms(slots):
            runs += 1
            r = rt_forward(a, b)
            if r is not None:
                syncs += 1
                if r > fmax:
                    fmax = r; fbest = b
        total_runs += runs
        if fmax > best:
            best = fmax
            best_pairs = [(a, fbest)]
        elif fmax == best:
            best_pairs.append((a, fbest))
        if gi % 10 == 0 or gi == len(groups)-1:
            print(f"  [{gi+1}/{len(groups)}] a={a} fiber={runs} sync={syncs} fmax={fmax} global={best} elapsed={time.time()-t0:.0f}s", flush=True)
    return best, best_pairs, total_runs

if __name__ == '__main__':
    n = int(sys.argv[1])
    best, pairs, runs = exact_E(n)
    print(f"E({n})={best} runs={runs} witnesses={pairs}")
    with open(f"output/artifacts/Emax_{n}.json", "w") as f:
        json.dump({"E": best, "runs": runs, "witnesses": pairs}, f)
