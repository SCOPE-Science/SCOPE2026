"""Exact finite checks for the integer-slope signed-remainder maps.

These checks corroborate finite Markov formulas; the all-parameter proof
and the almost-everywhere dynamical statements are mathematical arguments.
No external packages or input files are required.
"""
from fractions import Fraction as Q
from collections import deque


def edges(m, j):
    d = 2*m - 1
    left = m*j - d*(j//2)
    return tuple(range(left, left + m))


def phi(m, x):
    a = Q(2*m - 1, 2)
    y = a*x
    # Python int() truncates toward zero for a rational argument.
    return x/2 + y - int(y)


def accessible(graph, source):
    seen = {source}
    queue = deque([source])
    while queue:
        for nxt in graph[queue.popleft()]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def solve_stationary(m):
    d = 2*m - 1
    cells = tuple(range(1, 2*d - 1))
    n = len(cells)
    indexes = {j:i for i,j in enumerate(cells)}
    mat = [[Q(0) for _ in range(n+1)] for __ in range(n)]
    for i, j in enumerate(cells):
        mat[i][i] = Q(-m)
        for predecessor in cells:
            if j in edges(m, predecessor):
                mat[i][indexes[predecessor]] += 1
    mat[-1] = [Q(1) for _ in cells] + [Q(1)]
    for col in range(n):
        pivot = next((r for r in range(col,n) if mat[r][col] != 0),None)
        assert pivot is not None
        mat[col],mat[pivot] = mat[pivot],mat[col]
        a = mat[col][col]
        mat[col] = [z/a for z in mat[col]]
        for row in range(n):
            if row != col:
                factor = mat[row][col]
                if factor:
                    mat[row] = [v-factor*w for v,w in zip(mat[row],mat[col])]
    pi = [row[-1] for row in mat]
    assert sum(pi) == 1 and all(x>0 for x in pi)
    for j in cells:
        rhs = sum(pi[indexes[i]] for i in cells if j in edges(m,i))/m
        assert rhs == pi[indexes[j]], (m,j)
    return pi


def verify():
    checks = 0
    for m in range(2,41):
        d = 2*m - 1
        cells = set(range(1, 2*d-1))
        graph = {j:edges(m,j) for j in cells}
        for j, succ in graph.items():
            assert len(succ)==m and set(succ)<=cells
            checks+=1
            midpoint = Q(2*j+1,2*d)
            assert phi(m,midpoint)==m*midpoint-(j//2)
            assert phi(m,-midpoint)==-phi(m,midpoint)
            checks+=2
        hub = 2*m-2
        assert hub in graph[hub]
        assert accessible(graph,hub)==cells
        checks+=2
        assert all(hub in accessible(graph,j) for j in cells)
        checks+=len(cells)
        for num in [-250,-101,-21,-1,1,2,3,21,101,250]:
            x = Q(num,13)
            sign = 1 if x>0 else -1
            lo,hi=Q(1,d),Q(2)-Q(1,d)
            for step in range(100):
                if lo <= sign*x <= hi: break
                x=phi(m,x)
            else:
                raise AssertionError(('entry',m,num,x))
            checks+=1
    expected={
       2:[Q(1,6),Q(1,3),Q(1,3),Q(1,6)],
       3:[Q(1,30),Q(1,10),Q(1,6),Q(1,5),Q(1,5),Q(1,6),Q(1,10),Q(1,30)]
    }
    for m in range(2,9):
        pi=solve_stationary(m)
        assert pi==pi[::-1]
        assert pi[0] == pi[1]/m
        if m in expected:assert pi==expected[m]
        checks+=len(pi)+2
    # For m=2 the physical density on successive cells is 3*pi_j.
    pi=solve_stationary(2)
    assert sum(pi[1:3])==Q(2,3)
    # Direct exact cell integration is more transparent for the actual moments.
    h=[3*v for v in pi]
    mu1=sum(h[i]*(Q(i+2,3)**2-Q(i+1,3)**2)/2 for i in range(4))
    mu2=sum(h[i]*(Q(i+2,3)**3-Q(i+1,3)**3)/3 for i in range(4))
    assert mu1==1 and mu2==Q(10,9) and mu2-mu1**2==Q(1,9)
    checks+=4
    print('PASS exact finite checks:',checks)
    print('m=2 stationary cell probabilities:',pi)
    print('m=2 mean:',mu1,'variance:',mu2-mu1**2)

if __name__=='__main__':
    verify()
