"""Reproducible exact-arithmetic checks for wall-occupation fluctuations.

Uses only the Python standard library.  A discrete ballistic clock approximates
continuum deterministic flights; it is an independent finite-state check, not
an infinite-dimensional proof.
"""
from fractions import Fraction as Q


def linear_solve(a, b):
    n = len(b)
    mat = [[Q(x) for x in row] + [Q(b[i])] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if mat[r][col]), None)
        assert pivot is not None, ('singular', col)
        mat[col], mat[pivot] = mat[pivot], mat[col]
        c = mat[col][col]
        mat[col] = [x / c for x in mat[col]]
        for r in range(n):
            if r != col:
                c = mat[r][col]
                if c:
                    mat[r] = [mat[r][j] - c * mat[col][j] for j in range(n + 1)]
    ans = [row[-1] for row in mat]
    assert all(sum(Q(a[i][j]) * ans[j] for j in range(n)) == b[i]
               for i in range(n))
    return ans


def finite_chain(ncells, speed=Q(1), gamma=Q(1), length=Q(1)):
    n = 2 * (ncells + 1)
    mat = [[Q(0) for _ in range(n)] for _ in range(n)]
    def at(i, spin): return 2 * i + spin
    hop = speed * ncells / length
    for i in range(ncells + 1):
        for s in (0, 1):
            u = at(i, s)
            j = at(i, 1-s)
            mat[u][j] += gamma
            mat[u][u] -= gamma
            if s == 1 and i < ncells:
                j = at(i+1,s)
                mat[u][j] += hop
                mat[u][u] -= hop
            if s == 0 and i > 0:
                j = at(i-1,s)
                mat[u][j] += hop
                mat[u][u] -= hop
    transpose = [[mat[j][i] for j in range(n)] for i in range(n)]
    transpose[-1] = [Q(1)] * n
    pi = linear_solve(transpose, [Q(0)] * (n - 1) + [Q(1)])
    assert all(x > 0 for x in pi)
    assert sum(pi) == 1
    left = [Q(0)] * n
    right = [Q(0)] * n
    left[at(0, 0)] = Q(1)
    right[at(ncells, 1)] = Q(1)

    def avar(f):
        mean = sum(x*y for x,y in zip(pi, f))
        rhs = [x-mean for x in f]
        a = [[-mat[i][j] for j in range(n)] for i in range(n)]
        a[-1] = pi[:]
        rhs[-1] = Q(0)
        g = linear_solve(a, rhs)
        assert sum(x*y for x,y in zip(pi,g)) == 0
        for i in range(n):
            assert sum(-mat[i][j]*g[j] for j in range(n)) == f[i]-mean
        return sum(2*pi[i]*(f[i]-mean)*g[i] for i in range(n))

    return (sum(pi[i]*(left[i]+right[i]) for i in range(n)),
            avar([left[i]+right[i] for i in range(n)]),
            avar([right[i]-left[i] for i in range(n)]))


def continuum(k, speed=Q(1), gamma=None, length=Q(1)):
    if gamma is None: gamma = k*speed/length
    m = 1/(1+k)
    sum_var = length/speed * k*(k+3)/(3*(1+k)**3)
    difference_var = 1/gamma
    rho = k*k*(k+3)/(3*(1+k)**3)
    return m, sum_var, difference_var, rho


def verify():
    checks = 0
    for k in (Q(1,5), Q(1), Q(3), Q(10)):
        m, vs, vd, rho = continuum(k)
        assert vs == rho * vd
        checks += 1
        assert Q(0) < rho < Q(1,3)
        checks += 1
        # Exact rational polynomial identity for derivative of rho(k).
        numerator = k*k*(k+3)
        denominator = 3*(1+k)**3
        nprime = 3*k*k + 6*k
        dprime = 9*(1+k)**2
        assert (nprime*denominator-numerator*dprime)/(denominator**2) == 2*k/(1+k)**4
        checks += 1
        assert -1 < (rho-1)/(rho+1) < Q(-1,2)
        checks += 1
        # Check the analytic Poisson solution at rational interior locations.
        length = Q(1); speed = Q(1); gamma=k
        q = m/2
        pbulk = gamma/(2*(speed+gamma*length))
        C = -2*m*m*length/speed*(k*k/Q(12)+k/Q(4)+Q(1,2))
        def u(x):return C+2*gamma*m/speed**2*(x-length/Q(2))**2
        def w(x):return 2*m/speed*(x-length/Q(2))
        def gp(x):return (u(x)+w(x))/2
        def gm(x):return (u(x)-w(x))/2
        gwall=gp(length)
        assert gwall==gm(Q(0))==length/speed*m*m*k*(k+3)/6
        checks+=1
        assert gamma*(gp(length)-gm(length)) == 1-m
        assert -gamma*(gp(Q(0))-gm(Q(0))) == 1-m
        checks+=2
        for x in (Q(0),Q(1,7),Q(1,3),Q(1,2),Q(6,7),Q(1)):
            du=4*gamma*m/speed**2*(x-length/Q(2))
            dw=2*m/speed
            assert -speed*(du+dw)/2+gamma*w(x)==-m
            assert speed*(du-dw)/2-gamma*w(x)==-m
            checks+=2
        # Integral of u(x) over the continuum interior and wall mass.
        int_u=C*length+gamma*m*length**3/(6*speed**2)
        assert pbulk*int_u+2*q*gwall==0
        assert vs==2*m*gwall
        checks+=2
    # Discrete finite-state approximation independently solves stationary law
    # and 2 Poisson equations, with exact rational elimination.
    for k in (Q(1,5),Q(1),Q(3)):
        m,vs,vd,_=continuum(k)
        errors=[]
        for n in (4,8,16):
            mm,ss,dd=finite_chain(n,gamma=k)
            errors.append(abs(ss-vs)+abs(dd-vd)+abs(mm-m))
            assert ss>0 and dd>0 and mm>0
            checks+=3
        assert errors[0]>errors[1]>errors[2]
        checks+=1
        assert errors[2] < errors[0]/3
        checks+=1
        print('k=',k, 'exact=',tuple(map(float,(m,vs,vd))),
              'discrete errors=',tuple(map(float, errors)))
    print('PASS:',checks,'exact-arithmetic assertions')

if __name__=='__main__':verify()
