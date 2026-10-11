"""Exact finite checks for the Euclidean diameter transition of simplex shuffles.

The symbolic argument for arbitrary dimensions is given in RESULT.md.  The
exhaustive checks here test small matrices and an independent vertex model.
"""
from fractions import Fraction as F
from itertools import combinations


def sign_profile(m, n, bits):
    rows = [n] * m
    cols = [-m] * n
    for i in range(m):
        for j in range(n):
            if bits & (1 << (i * n + j)):
                rows[i] -= 2
                cols[j] += 2
    return rows, cols


def maximum_sign(m, n, alpha, beta):
    """Exact diameter squared by maximizing over segment-endpoint differences."""
    best = None
    for mask in range(1 << (m*n)):
        r, c = sign_profile(m, n, mask)
        span_r = max(r)-min(r)
        span_c = max(c)-min(c)
        db = n*m*m-sum(z*z for z in c)
        da = m*n*n-sum(z*z for z in r)
        assert db >= 2*(m-1)*span_r
        assert da >= 2*(n-1)*span_c
        val = sum(z*z for z in r+c)+2*alpha*span_r+2*beta*span_c + 2*alpha*alpha+2*beta*beta
        if best is None or val > best:
            best = val
    return best


def vertex_profiles(m, n, alpha, beta):
    """Independently form all coordinate multisets via strict mixed orders."""
    profiles = set()
    for positions in combinations(range(m+n), m):
        a_positions = set(positions)
        ca = cb = 0
        va, vb = [], []
        for place in range(m+n-1, -1, -1):
            if place in a_positions:
                va.append(F(cb) + (alpha if ca == m-1 else 0))
                ca += 1
            else:
                vb.append(F(ca) + (beta if cb == n-1 else 0))
                cb += 1
        profiles.add((tuple(sorted(va)), tuple(sorted(vb))))
    return profiles


def maximum_vertices(m, n, alpha, beta):
    """Independently maximize squared distances between vertex coordinate orbits.

    For each pair of coordinate multisets, opposite sorting maximizes squared
    Euclidean separation by the rearrangement inequality.
    """
    pp = list(vertex_profiles(m, n, alpha, beta))
    best = F(0)
    for a, b in pp:
        for c, d in pp:
            val = sum((a[i]-c[m-1-i])**2 for i in range(m)) + sum((b[j]-d[n-1-j])**2 for j in range(n))
            best = max(best, val)
    return best


def test():
    sign_cases = 0
    vertex_cases = 0
    for m, n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)]:
        assert m>=2 and n>=2
        alpha_values = [F(0),F(1,2),F(m-1),F(m),F(m+1,2)]
        beta_values = [F(0),F(1,2),F(n-1),F(n),F(n+1,2)]
        choices = [(F(0),F(0)),(F(1),F(1)),
                   (F(m-1),F(n-1)), (F(m),F(0)),
                   (F(0),F(n)),(F(m+1,2),F(n+1,2)),
                   (F(m-1,2),F(n-1,2))]
        for alpha,beta in choices:
            exact = maximum_sign(m,n,alpha,beta)
            baseline = F(m*n*(m+n))+2*alpha*alpha+2*beta*beta
            in_region = 0<=alpha<=m-1 and 0<=beta<=n-1
            assert (exact == baseline) == in_region, (m,n,alpha,beta,exact,baseline)
            sign_cases+=1
            from_vertices=maximum_vertices(m,n,alpha,beta)
            assert exact==from_vertices,(m,n,alpha,beta,exact,from_vertices)
            vertex_cases+=1
    print('VERIFY_OK sign_matrix_cases=%d independently_reconstructed_vertex_cases=%d' % (sign_cases,vertex_cases))

if __name__=='__main__':
    test()
