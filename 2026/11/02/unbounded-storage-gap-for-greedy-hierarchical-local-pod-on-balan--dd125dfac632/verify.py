"""Exact reconstruction checks for a row-local POD hierarchical storage example.

Requires only Python 3 standard library. No random sampling is needed.
"""
from fractions import Fraction

checks = 0

def check(expr, message):
    global checks
    assert expr, message
    checks += 1


def rank_and_squares(mode_indices, b):
    """Each group has b identical rows e_j+e_(r+j)."""
    counts = {j: mode_indices.count(j) for j in set(mode_indices)}
    return len(counts), sorted((2*b*v for v in counts.values()), reverse=True)


def nodes(indices):
    yield indices
    if len(indices) > 1:
        mid = len(indices)//2
        yield from nodes(indices[:mid])
        yield from nodes(indices[mid:])


def test(r, materialize=False):
    assert r >= 2 and r & (r-1) == 0
    b = r*r
    n = 2*r
    m = 2*r*b
    eps2 = Fraction(1, 16*r*r)
    groups = list(range(r))*2
    check(len(groups)*b == m, "row count")
    check(n > r, "true low-rank compression")
    check(groups[:r] == groups[r:], "both root children retain all temporal modes")
    check(len(set(groups)) == r, "global temporal rank")

    # All dyadic nodes exactly realize the method's rank rule (Eq. 25).
    for node in nodes(groups):
        rank, eigvals = rank_and_squares(node,b)
        allocated = len(node)*b*n*eps2
        check(rank >= 1, "rank positive")
        check(min(eigvals) > allocated, "full local rank is forced by positive NRMSE tolerance")
        check(len(eigvals) == rank, "singular-value multiplicity")
        if len(node) <= r:
            check(len(set(node)) == len(node), "descendant has distinct modes")
            check(set(eigvals) == {2*b}, "descendant positive Gram eigenvalues")
        else:
            check(set(eigvals) == {4*b}, "root positive Gram eigenvalues")

    parent_cost = r*(m+n+1)
    children_cost = r*(m+2*n+2)
    leaves_cost = 2*r*(b+n+1)
    check(children_cost > parent_cost, "greedy must refuse root bisection")
    check(parent_cost > leaves_cost, "entire hierarchy offers strict saving")
    check(parent_cost < m*n, "unsplit POD genuinely compresses compared with raw entries")
    check(leaves_cost < parent_cost, "leaf POD genuinely compresses")

    # Dynamic programming: exact optimum among all recursive dyadic partitions.
    def best(subgroups):
        rank,_ = rank_and_squares(subgroups,b)
        cost = rank*(len(subgroups)*b+n+1)
        if len(subgroups)==1:
            return cost
        half=len(subgroups)//2
        return min(cost,best(subgroups[:half])+best(subgroups[half:]))
    check(best(groups) == leaves_cost, "exact global tree optimum is the fine partition")

    # Check actual Gram entries rather than trusting rank formulas (small sizes).
    if materialize:
        A=[]
        for j in groups:
            row=[0]*n
            row[j]=1
            row[r+j]=1
            A += [row[: ] for _ in range(b)]
        check(len(A)==m, "constructed row count")
        for subgroup in (groups,groups[:r],groups[:max(1,r//2)]):
            rows=A[:len(subgroup)*b]
            G=[[sum(row[i]*row[j] for row in rows) for j in range(n)] for i in range(n)]
            count={j:subgroup.count(j) for j in range(r)}
            for i in range(n):
                for j in range(n):
                    expected=b*count.get(i%r,0) if i%r==j%r else 0
                    check(G[i][j]==expected, "exact matrix Gram identity")

    return parent_cost, children_cost, leaves_cost, Fraction(parent_cost,leaves_cost)

if __name__ == "__main__":
    for r in (2,4,8,16,32):
        p,c,l,rat=test(r,materialize=r<=8)
        print(f"r={r}: greedy={p}, first_children={c}, optimum={l}, ratio={rat} ({float(rat):.6f})")
    check(test(64)[-1]>50, "unbounded-ratio trend at r=64")
    print(f"PASS: {checks} exact assertions; universal result relies on algebra, not these finite tests")
