"""Finite computational checks of an exact wheel-with-hub-leaf spectral-gap formula.

Python >=3.9, standard library only. This is not an infinite proof; see RESULT.md.
"""
import math
import random


def min_eigenvalues_sym(A):
    """Jacobi diagonalization for small real symmetric matrices."""
    M = [row[:] for row in A]
    n = len(M)
    for _ in range(30*n*n):
        p, q = 0, 1
        best = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                a = abs(M[i][j])
                if a > best:
                    best, p, q = a, i, j
        if best < 1e-13:
            return sorted(M[i][i] for i in range(n))
        # Stable annihilation (no reliance on a numerical matrix library).
        tau = (M[q][q] - M[p][p]) / (2*M[p][q])
        t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1+tau*tau)) if tau else 1.0
        cc = 1 / math.sqrt(1+t*t)
        ss = t*cc
        app, aqq, apq = M[p][p], M[q][q], M[p][q]
        M[p][p] = app - t*apq
        M[q][q] = aqq + t*apq
        M[p][q] = M[q][p] = 0.0
        for k in range(n):
            if k in (p, q):
                continue
            mp, mq = M[k][p], M[k][q]
            M[k][p] = M[p][k] = cc*mp - ss*mq
            M[k][q] = M[q][k] = ss*mp + cc*mq
    raise AssertionError('Jacobi convergence failure')


def edges(m):
    return ([(0, j) for j in range(1,m+1)],
            [(j, 1+(j%m)) for j in range(1,m+1)],
            [(0,m+1)])


def laplacian(m, spokes, rim, leaf):
    N = m+2
    L = [[0.0]*N for _ in range(N)]
    sp, ri, le = edges(m)
    for egroup, weights in [(sp,spokes), (ri,rim), (le,[leaf])]:
        for (u,v),w in zip(egroup,weights):
            L[u][u]+=w; L[v][v]+=w
            L[u][v]-=w; L[v][u]-=w
    return L


def candidate(m):
    delta=4*math.sin(math.pi/m)**2
    if m<=5:
        k=1-1/delta
        assert k>1/m**2
        d=1/math.sqrt(k)
        a=(2+d)/(m+2)
        b=(1-a)/delta
        c=((m+1)*a-1)/((m+2)*a-2)
        cost=m+1-(m*math.sqrt(k)-1)**2/(m+2)
    else:
        assert delta<=1+1e-12
        a=1.0
        b=0.0; c=1.0
        cost=m+1
    assert abs(cost-(m*(a+b)+c))<2e-12
    return a,b,c,cost


def root_small(m,a,c):
    tr=(m+1)*a+2*c
    det=(m+2)*a*c
    return 2*det/(tr+math.sqrt(max(0.,tr*tr-4*det)))


def run():
    rng=random.Random(571044)
    trials=0
    for m in range(3,21):
        delta=4*math.sin(math.pi/m)**2
        a,b,c,D=candidate(m)
        L=laplacian(m,[a]*m,[b]*m,c)
        lam=min_eigenvalues_sym(L)
        assert abs(lam[0])<2e-10
        assert abs(lam[1]-1)<3e-10, (m,lam[:3])
        assert abs(min(root_small(m,a,c),a+delta*b)-1)<1e-10
        assert abs(1/D-1/(m*(a+b)+c))<1e-12
        trials+=1
        for _ in range(15):
            x,y,z=[10**rng.uniform(-1.5,1) for dummy in range(3)]
            v=min_eigenvalues_sym(laplacian(m,[x]*m,[y]*m,z))[1]
            formula=min(root_small(m,x,z),x+delta*y)
            assert abs(v-formula)<3e-9*(1+formula),(m,v,formula)
            trials+=1
        for _ in range(10):
            ar=[rng.random()+0.05 for _ in range(m)]
            br=[rng.random()+0.05 for _ in range(m)]
            cr=rng.random()+0.05
            budget=sum(ar)+sum(br)+cr
            amax=budget/D
            v=min_eigenvalues_sym(laplacian(m,ar,br,cr))[1]
            assert v<=amax+5e-9*(1+amax),(m,v,amax)
            trials+=1
    # Exact identities for the rational cycle gaps m=3,4.
    assert abs(4*math.sin(math.pi/3)**2-3)<1e-13
    assert abs(4*math.sin(math.pi/4)**2-2)<1e-13
    assert abs(candidate(3)[3]-(13+2*math.sqrt(6))/5)<1e-12
    assert abs(candidate(4)[3]-(21+4*math.sqrt(2))/6)<1e-12
    assert candidate(5)[1]>0
    for m in range(6,21):
        assert candidate(m)[1]==0
    print('PASS: %d matrix/formula/budget comparisons; only finite checks' % trials)


if __name__=='__main__':run()
