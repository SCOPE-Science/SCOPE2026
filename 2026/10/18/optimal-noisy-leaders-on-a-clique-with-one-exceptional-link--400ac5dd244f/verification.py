"""Reproduce exact-rational checks for weighted-clique leader placement.

All arithmetic uses fractions.Fraction. The finite tests supplement the
all-parameter matrix-inversion argument; they are not a substitute for it.
"""
from fractions import Fraction as Q
from itertools import combinations


def inverse(A):
    n = len(A)
    M = [[Q(x) for x in row] + [Q(i == j) for j in range(n)]
         for i, row in enumerate(A)]
    for i in range(n):
        k = next(k for k in range(i, n) if M[k][i])
        M[i], M[k] = M[k], M[i]
        pivot = M[i][i]
        M[i] = [x / pivot for x in M[i]]
        for k in range(n):
            if k != i:
                factor = M[k][i]
                M[k] = [x - factor*y for x, y in zip(M[k], M[i])]
    return [row[n:] for row in M]


def direct_cost(n, gain, edge_weight, selected):
    A = [[Q(n-1) if i == j else Q(-1) for j in range(n)]
         for i in range(n)]
    z = edge_weight - 1
    A[0][0] += z
    A[1][1] += z
    A[0][1] -= z
    A[1][0] -= z
    for i in selected:
        A[i][i] += gain
    B = inverse(A)
    return sum(B[i][i] for i in range(n))


def parameters(n, number_leaders, gain):
    q = number_leaders
    a, c = Q(1, n), Q(1, n) / (1+gain / n)
    r = [2*a, a+c+(a-c)/q, 2*c]
    s = [2*a*a,
         c*c*(1-Q(1,q)) + a*a*(1+Q(1,q)+Q(n,q*q)),
         2*c*c]
    return r, s


def predicted_increment(n, q, gain, edge_weight, j):
    r, s = parameters(n, q, gain)
    t = 1-edge_weight
    return t*s[j] / (1-t*r[j])


def expected_classes(n, q, gain, edge_weight):
    possible = {j for j in (0,1,2) if j <= q and q-j <= n-2}
    if edge_weight == 1:
        return possible
    if edge_weight < 1:
        return {0 if q == 1 else 2}
    if q == n:
        return {2}
    if q == 1 or q == n-1:
        return {1}
    r, s = parameters(n,q,gain)
    D = s[1]-s[0]
    H = s[1]*r[0]-s[0]*r[1]
    comparison = D+(edge_weight-1)*H
    return {1} if comparison>0 else ({0} if comparison<0 else {0,1})


def run():
    subsets_checked = 0
    instances = 0
    for n in range(3,9):
        for q in range(1,n+1):
            for gain in (Q(1,2), Q(3), Q(10)):
                for w in (Q(1,3), Q(1), Q(7,3), Q(19), Q(27,22)):
                    classes={}
                    increments={}
                    for selected in combinations(range(n), q):
                        j=len(set(selected)&{0,1})
                        exact=direct_cost(n,gain,w,selected)
                        incr=predicted_increment(n,q,gain,w,j)
                        base=exact-incr
                        if j in classes:
                            assert exact==classes[j]
                        else:
                            classes[j]=exact
                        if increments:
                            assert next(iter(increments.values()))==base
                        increments[j]=base
                        subsets_checked+=1
                    minimum=min(classes.values())
                    minimizers={j for j,v in classes.items() if v==minimum}
                    assert minimizers==expected_classes(n,q,gain,w), (n,q,gain,w,minimizers)
                    instances+=1
    print('PASS: %d parameter instances and %d leader subsets checked exactly.' % (instances,subsets_checked))
    n,q,gain=5,3,Q(10)
    r,s=parameters(n,q,gain)
    D=s[1]-s[0]; H=s[1]*r[0]-s[0]*r[1]
    assert D==Q(-1,675) and H==Q(22,3375)
    critical=1-D/H
    assert critical==Q(27,22)
    assert expected_classes(n,q,gain,Q(11,10))=={0}
    assert expected_classes(n,q,gain,Q(2))=={1}
    assert expected_classes(n,q,gain,critical)=={0,1}
    print('PASS: K_5, q=3, gain=10: transition at exact edge weight 27/22.')

if __name__=='__main__':
    run()
