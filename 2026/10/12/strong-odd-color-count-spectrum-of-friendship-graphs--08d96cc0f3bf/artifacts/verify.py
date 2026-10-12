from collections import defaultdict

def partitions(n):
    # Restricted-growth strings, one representative of each set partition.
    a=[0]*n
    yield tuple(a)
    def rec(pos, mx):
        if pos==n:
            yield tuple(a); return
        for v in range(mx+2):
            a[pos]=v
            yield from rec(pos+1,max(mx,v))
    # First coordinate fixed at 0; avoid duplicate all-zero emitted above.
    def rec2(pos,mx):
        if pos==n:
            if any(a): yield tuple(a)
            return
        for v in range(mx+2):
            a[pos]=v
            yield from rec2(pos+1,max(mx,v))
    yield from rec2(1,0)

def realized_outer_counts(k):
    n=2*k
    got=set(); tested=0
    for p in partitions(n):
        tested+=1
        # Outer edge i is (2i,2i+1), hence endpoints must differ.
        if any(p[2*i]==p[2*i+1] for i in range(k)):
            continue
        cnt=defaultdict(int)
        for c in p: cnt[c]+=1
        if all(v%2==1 for v in cnt.values()):
            got.add(len(cnt))
    return got,tested

total=0
for k in range(2,6):
    got,tested=realized_outer_counts(k); total+=tested
    expected=set(range(2 if k%2 else 4,2*k+1,2))
    assert got==expected,(k,got,expected)
    total_colors={q+1 for q in got}
    expected_total=set(range(3 if k%2 else 5,2*k+2,2))
    assert total_colors==expected_total
    print(f'F_{k}: outer_counts={sorted(got)} total_colors={sorted(total_colors)} partitions={tested}')
print(f'ALL CHECKS PASSED; k_range=2..5; canonical_partitions_checked={total}')
