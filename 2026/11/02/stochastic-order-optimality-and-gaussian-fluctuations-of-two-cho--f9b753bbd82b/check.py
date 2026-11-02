"""Reproducible exact checks for controlled two-choice cycle-cover laws.

Uses only the Python standard library. Proofs for all sizes are in RESULT.md;
finite-state checks are tests, not substitutes for those arguments.
"""
from fractions import Fraction as Q
from math import isclose

P = Q(3, 4)
R = Q(1, 4)
checks = 0


def assert_it(condition, detail):
    global checks
    assert condition, detail
    checks += 1


def finite_horizon_exit(L, max_time=48):
    # State j=1,...,L is a position in the visited interval;
    # states 0 and L+1 are absorbing (new vertices).
    survival = [Q(0)] + [Q(1)] * L + [Q(0)]
    m = (L + 1) // 2
    for t in range(max_time):
        assert_it(all(survival[j] == survival[L+1-j]
                      for j in range(L+2)), (L, t, 'symmetry'))
        d = [survival[j]-survival[j-1] for j in range(1, m+1)]
        assert_it(all(x >= 0 for x in d), (L, t, 'monotonicity'))
        assert_it(all(d[j+1] <= 3*d[j] for j in range(len(d)-1)),
                  (L, t, 'cone'))
        new = [Q(0)]
        for j in range(1, L+1):
            a, b = survival[j-1], survival[j+1]
            optimal = P*min(a, b) + R*max(a, b)
            # Fixed nearer-end policy, including a symmetric central tie.
            if j < (L+1)/2:
                candidate = P*a + R*b
            elif j > (L+1)/2:
                candidate = P*b + R*a
            else:
                candidate = (a+b)/2
            assert_it(optimal == candidate, (L, t, j, 'policy dominance'))
            new.append(optimal)
        survival = new + [Q(0)]


def tridiagonal(A, b):
    n = len(b)
    diag, upper, lower = [], [], []
    for i in range(n):
        diag.append(A[i][i])
        if i < n-1: upper.append(A[i][i+1])
        if i > 0: lower.append(A[i][i-1])
    rhs = list(b)
    for i in range(1, n):
        t = lower[i-1] / diag[i-1]
        diag[i] -= t*upper[i-1]
        rhs[i] -= t*rhs[i-1]
    x = [Q(0)]*n
    x[-1] = rhs[-1] / diag[-1]
    for i in range(n-2,-1,-1):
        x[i] = (rhs[i]-upper[i]*x[i+1])/diag[i]
    return x


def exact_moments(L):
    m = (L+1)//2
    M = [[Q(int(i==j)) for j in range(m)] for i in range(m)]
    for j in range(1, m+1):
        if j < m:
            if j > 1: M[j-1][j-2] -= P
            M[j-1][j] -= R
        elif L % 2:
            if j > 1: M[j-1][j-2] -= 1
        else:
            if j > 1: M[j-1][j-2] -= P
            M[j-1][j-1] -= R
    means = tridiagonal(M, [Q(1)]*m)
    second = tridiagonal(M, [2*z-1 for z in means])
    return means[0], second[0]-means[0]**2


def expected_stage(L):
    if L % 2:
        return Q(2)-Q(1, 3**((L-1)//2))
    return Q(2)-Q(2, 3**(L//2))


for L in range(1, 27):
    finite_horizon_exit(L)

variance_sum = Q(0)
for L in range(1, 83):
    mean, variance = exact_moments(L)
    assert_it(mean == expected_stage(L), (L, 'mean', mean))
    assert_it(variance >= 0, (L, 'negative variance'))
    m = (L+1)//2
    if L % 2:
        closed_var = Q(6) - Q(8*m-4, 3**(m-1)) - Q(2, 9**(m-1))
    else:
        closed_var = Q(6) - Q(16*m-2, 3**m) - Q(8, 9**m)
    assert_it(variance == closed_var, (L, 'exact closed variance'))
    if L > 1: assert_it(variance < 6, (L, 'upper variance', variance))
    variance_sum += variance
    if L in (1, 2, 3, 4, 6, 10, 20, 40, 80):
        print('stage', L, 'E=', float(mean), 'Var=', float(variance))

for n in range(3, 83):
    o, e = n//2, (n-1)//2
    known_mean = Q(2*n)-Q(9, 2)+Q(3,2*3**o)+Q(1,3**e)
    assert_it(sum(expected_stage(L) for L in range(1,n)) == known_mean,
              (n, 'exact cover mean'))

assert_it(abs(float(exact_moments(82)[1])-6) < 1e-15, 'large-L variance limit')
assert_it(float(variance_sum) > 0, 'positive total variance')
print('PASSED', checks, 'exact assertions')
print('total_variance_stages_1_through_82',float(variance_sum))

# Independent whole-cycle finite-horizon Bellman replay, not using interval
# distance folding or the first/second-moment recurrence.
def contiguous(mask, n):
    if mask == (1 << n)-1:
        return True
    boundaries = sum(((mask >> j)&1) != ((mask >> ((j+1)%n))&1)
                     for j in range(n))
    return boundaries == 2


def distance_to_unvisited(x, direction, mask, n):
    j=x
    for k in range(1,n+1):
        j=(j+direction)%n
        if not (mask >> j)&1:
            return k
    return n+1


for n in range(3, 9):
    all_mask=(1<<n)-1
    states=[(mask,x) for mask in range(1,all_mask+1)
            if contiguous(mask,n)
            for x in range(n) if (mask >> x)&1]
    opt = {(mask,x):Q(int(mask!=all_mask)) for mask,x in states}
    fixed = dict(opt)
    for t in range(1,35):
        no, nf = {}, {}
        for mask,x in states:
            if mask==all_mask:
                no[(mask,x)]=nf[(mask,x)]=Q(0)
                continue
            a=(x-1)%n; b=(x+1)%n
            sa=mask | (1<<a); sb=mask | (1<<b)
            va=opt[(sa,a)]; vb=opt[(sb,b)]
            no[(mask,x)] = P*min(va,vb)+R*max(va,vb)
            fa=fixed[(sa,a)]; fb=fixed[(sb,b)]
            da=distance_to_unvisited(x,-1,mask,n)
            db=distance_to_unvisited(x, 1,mask,n)
            if da < db: v=P*fa+R*fb
            elif da > db: v=P*fb+R*fa
            else: v=(fa+fb)/2
            nf[(mask,x)] = v
            assert_it(v==no[(mask,x)],('full-cycle',n,t,mask,x))
        opt,fixed=no,nf
print('PASSED',checks,'exact assertions including whole-cycle finite-horizon tests')
