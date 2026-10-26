"""Independent finite certificates for closed Johnson-neighborhood VC dimension.
Only standard-library Python required; run `python verify.py`.
"""
from itertools import combinations, product
from math import comb

# All set partitions of m labeled positions, in restricted-growth form.
def partitions(m):
    if not m:
        yield ()
        return
    def go(xs, high):
        if len(xs) == m:
            yield tuple(xs)
            return
        for j in range(high + 2):
            yield from go(xs + [j], max(high, j))
    yield from go([0], 0)


def saturated_traces(edges, center_in_sample):
    """Superfamily of all traces on edges of a row-column grid near C.

    Every center at Johnson distance 0,1,2,>=3 from C gives respectively
    all, row-column cross, 2-by-2 rectangle, or empty on B_1(C).
    Two unused row/column coordinates suffice for all possible traces.
    """
    m = len(edges)
    nr = 1 + max(i for i,j in edges) + 2
    nc = 1 + max(j for i,j in edges) + 2
    full = (1 << m) - 1
    cb = (1 << m) if center_in_sample else 0
    traces = {0, full | cb}
    for a in range(nr):
        for b in range(nc):
            traces.add(cb | sum(1 << t for t,(i,j) in enumerate(edges)
                                  if i == a or j == b))
    for aa in combinations(range(nr),2):
        for bb in combinations(range(nc),2):
            traces.add(sum(1 << t for t,(i,j) in enumerate(edges)
                           if i in aa and j in bb))
    return traces


def upper_kernel(m, center_in_sample):
    all_parts = list(partitions(m))
    feasible = 0
    max_traces = 0
    for row_partition, col_partition in product(all_parts, repeat=2):
        edges = tuple(zip(row_partition, col_partition))
        if len(set(edges)) != m:
            continue
        feasible += 1
        num = len(saturated_traces(edges, center_in_sample))
        max_traces = max(max_traces, num)
        assert num < 2 ** (m + int(center_in_sample)), (
            'five-point counterexample', edges, center_in_sample, num)
    assert (m, center_in_sample, feasible, max_traces) in [
        (5, False, 1153, 24), (4, True, 113, 25)]
    print('KERNEL', 'five_neighbors' if not center_in_sample else 'center_plus_four',
          'partitions', feasible, 'maximum_traces', max_traces, 'PASS')


def bitmask(x):
    return sum(1 << i for i in x)


def base_case(n,k,vc):
    verts = [bitmask(c) for c in combinations(range(n),k)]
    fixed = verts[0]
    anchor = [v for v in verts if (v ^ fixed).bit_count() <= 2]
    balls = [sum(1 << i for i,v in enumerate(anchor)
                 if (v ^ center).bit_count() <= 2)
             for center in verts]
    def traces(xs):
        return {sum(1 << p for p,i in enumerate(xs) if (b >> i) & 1)
                for b in balls}
    # By vertex transitivity, every shattered set can be moved into anchor.
    assert all(len(traces(xs)) < 2**(vc+1)
               for xs in combinations(range(len(anchor)), vc+1))
    if vc:
        witness = next((xs for xs in combinations(range(len(anchor)),vc)
                        if len(traces(xs)) == 2**vc), None)
        assert witness is not None
        chosen = [anchor[i] for i in witness]
        centers = []
        for target in range(2**vc):
            hit = next(c for c in verts if
                       sum(1 << p for p,v in enumerate(chosen)
                           if (v ^ c).bit_count() <= 2) == target)
            centers.append(hit)
        # Replay the entire explicit witness chart without using `traces`.
        for target, center in enumerate(centers):
            got = sum(1 << p for p,v in enumerate(chosen)
                      if (v ^ center).bit_count() <= 2)
            assert got == target
        pretty = lambda v: ''.join(str(i+1) for i in range(n) if (v>>i)&1)
        print('BASE',n,k,'VC',vc,'nonexistence_tests',comb(len(anchor),vc+1),
              'witness',','.join(map(pretty,chosen)),
              'center_chart',','.join(map(pretty,centers)),'PASS')
    else:
        assert len({b for b in balls}) == 1
        print('BASE',n,k,'VC',vc,'PASS')



def check_local_trace_geometry():
    # Independent Johnson-distance check of the four claimed trace shapes.
    for n,k in [(4,2),(6,3),(7,3),(8,2)]:
        C = bitmask(range(k))
        R = range(k)
        T = range(k,n)
        cells = [(a,b, C ^ (1<<a) ^ (1<<b))
                 for a in R for b in T]
        for tup in combinations(range(n),k):
            D=bitmask(tup)
            dist=(D^C).bit_count()//2
            actual={ (a,b) for a,b,v in cells
                     if (v^D).bit_count()<=2 }
            if dist==0:
                predicted={(a,b) for a,b,v in cells}
            elif dist==1:
                removed=[a for a in R if not (D>>a)&1]
                added=[b for b in T if (D>>b)&1]
                predicted={(a,b) for a,b,v in cells
                           if a==removed[0] or b==added[0]}
            elif dist==2:
                removed={a for a in R if not (D>>a)&1}
                added={b for b in T if (D>>b)&1}
                predicted={(a,b) for a,b,v in cells
                           if a in removed and b in added}
            else:
                predicted=set()
            assert actual==predicted, (n,k,tup,actual,predicted)
        print('LOCAL_TRACE_GEOMETRY',n,k,'PASS')

def main():
    check_local_trace_geometry()
    upper_kernel(5, False)
    upper_kernel(4, True)
    for n,k,vc in [(4,2,1),(5,2,2),(6,2,3),(7,2,3),
                   (8,2,4),(6,3,3),(7,3,4)]:
        base_case(n,k,vc)
    print('VERIFY_OK complete_finite_kernel=PASS small_cases=PASS witnesses=PASS')

if __name__ == '__main__':
    main()
