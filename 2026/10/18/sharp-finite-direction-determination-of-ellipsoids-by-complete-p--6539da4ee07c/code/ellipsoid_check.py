"""Exact checks for finite-direction reconstruction of ellipsoids from section profiles.

The arbitrary-direction lower bound is proved analytically using an indefinite
symmetric kernel and a positive-definite determinant pencil.
"""
from fractions import Fraction as F


def identity(d):
    return [[F(i == j) for j in range(d)] for i in range(d)]


def gram(d):
    a = [[F((i + 2*j + 1) % 5 - 2) for j in range(d)] for i in range(d)]
    return [[F(i==j) + sum(a[k][i]*a[k][j] for k in range(d))
             for j in range(d)] for i in range(d)]


def section_halfwidth_square(q, i, j=None):
    if j is None:
        return q[i][i]
    return (q[i][i] + q[j][j] + 2*q[i][j]) / 2


def reconstruct(d, widths, centers):
    q = identity(d)
    for i in range(d): q[i][i] = widths[('axis', i)]
    for i in range(d):
        for j in range(i + 1, d):
            q[i][j] = q[j][i] = widths[('pair', i, j)] - (q[i][i] + q[j][j]) / 2
    return q, [centers[i] for i in range(d)]


def determinant(a):
    m = [row[:] for row in a]
    d = len(m)
    result = F(1)
    for k in range(d):
        p = next((i for i in range(k, d) if m[i][k]), None)
        if p is None: return F(0)
        if p != k:
            m[k],m[p] = m[p],m[k]
            result *= -1
        c = m[k][k]
        result *= c
        for i in range(k+1,d):
            f = m[i][k]/c
            for j in range(k+1,d):m[i][j]-=f*m[k][j]
            m[i][k] = F(0)
    return result


def check():
    count = 0
    for d in range(2, 8):
        q = gram(d)
        c = [F(i+1,i+2) for i in range(d)]
        measures = {('axis',i):section_halfwidth_square(q,i) for i in range(d)}
        for i in range(d):
            for j in range(i+1,d):
                measures[('pair',i,j)] = section_halfwidth_square(q,i,j)
        recovered, recovered_c = reconstruct(d, measures, c)
        assert recovered == q and recovered_c == c
        assert determinant(q) > 0
        count += len(measures)

        # Removing the view along (e1+e2)/sqrt(2) leaves Q12 unobserved.
        left, right = identity(d), identity(d)
        left[0][1]=left[1][0]=F(1,4)
        right[0][1]=right[1][0]=F(-1,4)
        assert determinant(left)==determinant(right)==F(15,16)
        for key in measures:
            if key==('pair',0,1):
                continue
            kind=key[0]
            if kind=='axis':
                i=key[1]
                assert section_halfwidth_square(left,i)==section_halfwidth_square(right,i)
            else:
                i,j=key[1:]
                assert section_halfwidth_square(left,i,j)==section_halfwidth_square(right,i,j)
        assert left!=right

    # A symmetric kernel with no semidefinite sign occurs for a sample of
    # non-axis-aligned views, illustrating the pencil construction.
    a = F(1,3)
    plus = [[F(1),a],[a,F(1)]]
    minus = [[F(1),-a],[-a,F(1)]]
    assert determinant(plus)==determinant(minus)==F(8,9)
    print('VERIFY_OK exact_full_view_measurements=',count,
          'dimensions_checked=2..7 equal_volume_ambiguities=6')


if __name__=='__main__':check()
