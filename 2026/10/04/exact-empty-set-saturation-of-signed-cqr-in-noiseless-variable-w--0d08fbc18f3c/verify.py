from math import comb, floor, ceil, isclose

def cqr_for_rank(m, alpha, test_rank):
    widths = list(range(1, m + 2))
    w = widths[test_rank - 1]
    cal = widths[:test_rank - 1] + widths[test_rank:]
    scores = sorted([-x for x in cal])
    k = ceil((1 - alpha) * (m + 1) - 1e-14)
    r = floor(alpha * (m + 1) + 1e-14)
    assert k == m + 1 - r
    q = scores[k - 1]
    lo = -w - q
    hi = w + q
    empty = lo > hi
    covered = lo <= 0 <= hi
    return r, empty, covered

def check_case(m, alpha):
    r = floor(alpha * (m + 1) + 1e-14)
    assert 1 <= r <= m
    empties = 0
    covers = 0
    for rank in range(1, m + 2):
        rr, empty, covered = cqr_for_rank(m, alpha, rank)
        assert rr == r
        assert empty == (rank <= r)
        assert covered == (rank > r)
        assert not (empty and covered)
        empties += empty
        covers += covered
    assert empties == r
    assert covers == m + 1 - r
    assert isclose(empties / (m + 1), r / (m + 1), rel_tol=0, abs_tol=1e-15)
    assert isclose(covers / (m + 1), ceil((1-alpha)*(m+1)-1e-14)/(m+1), rel_tol=0, abs_tol=1e-15)

def bin_tail(m, u, r):
    return sum(comb(m,j)*(u**j)*((1-u)**(m-j)) for j in range(r,m+1))

for m, alpha in [(9,0.1),(9,0.2),(19,0.1),(24,0.2),(49,0.06),(99,0.1),(100,0.1),(100,0.37)]:
    if alpha >= 1/(m+1):
        check_case(m, alpha)

m=99; alpha=0.1; r=floor(alpha*(m+1)+1e-14)
assert r == 10
assert isclose(r/(m+1), 0.1, abs_tol=1e-15)
expected = {
    0.05: 0.026516705753822874,
    0.10: 0.535523299875549,
    0.15: 0.9404700914271256,
}
for u,v in expected.items():
    got=bin_tail(m,u,r)
    assert isclose(got,v,rel_tol=2e-14,abs_tol=2e-14), (u,got,v)
print('VERIFY_OK')
