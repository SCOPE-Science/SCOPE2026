"""Independent exact-integer checks for the displayed monomial construction.

Run: python3 CHECK.py
Finite tests only: the general bundle splitting is proved in RESULT.md.
"""

def powers(x, y, m, j):
    return x ** (m-j) * y ** j

def dyd(x, y, m, j):
    return 0 if j == 0 else j * x ** (m-j) * y ** (j-1)

def dxd(x, y, m, j):
    return 0 if m == j else (m-j) * x ** (m-j-1) * y ** j

def verify(k):
    m = 2*k-1
    n = 3*k+1
    d = 4*k-1
    low = 5*k-3
    high = k
    assert (low+high) == 2*(n-2)-1
    assert low*(2*k+1)+high*(2*k+2) == n*d-2
    assert n == (m+1)+(k+1)
    q1, r1 = divmod(d, 2)
    q2, r2 = divmod(d, n-2)
    assert (q1, r1, q2, r2) == (2*k-1,1,1,k)
    assert q1+q2 == (2-r1)*(n-2-r2)+1
    for x,y in [(1,0),(0,1),(1,1),(2,3),(-3,5)]:
        p = [powers(x,y,m,j) for j in range(m+1)]
        z = [powers(x*x,y*y,k,j) for j in range(k+1)]
        assert any(p) and any(z)
        for j in range(m):
            assert -y*p[j]+x*p[j+1] == 0
            assert -y*dyd(x,y,m,j)+x*dyd(x,y,m,j+1) == x**(m-j)*y**j
            assert -y*dxd(x,y,m,j)+x*dxd(x,y,m,j+1) == -x**(m-j-1)*y**(j+1)
        for j in range(k):
            assert -y*y*z[j]+x*x*z[j+1] == 0
        differential = [powers(x,y,m-1,j) for j in range(m)]
        assert any(differential)
    return f'k={k} Gr(2,{n}) degree={d} N=O({2*k+1})^{low}+O({2*k+2})^{high}: exact identities OK'

if __name__ == '__main__':
    for k in range(2,11):
        print(verify(k))
    print('ALL CHECKS PASSED (finite corroboration, not an infinite proof)')
