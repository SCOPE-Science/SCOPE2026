#!/usr/bin/env python3
"""Standalone checks for a priced wheel's optimal algebraic connectivity.

Only Python's standard library is needed. Numerical finite checks supplement,
but do not replace, the all-parameter analytic proof in RESULT.md.
"""
import math
import random
from fractions import Fraction

CHECKS = 0

def require(ok, note=''):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(note or 'validation failed')


def alpha(n):
    return 2.0 - 2.0*math.cos(2.0*math.pi/n)


def candidate(n, P, Q, budget):
    a1 = alpha(n)
    if Q < P*a1:
        rim = budget/(P*a1+n*Q)
        spoke = a1*rim/n
        gap = (n+1)*spoke
    else:
        rim = 0.0
        spoke = budget/(n*P)
        gap = spoke
    return spoke, rim, gap


def mat(n, spokes, rims):
    N = n+1
    A = [[0.0]*N for _ in range(N)]
    def edge(i,j,w):
        A[i][i] += w
        A[j][j] += w
        A[i][j] -= w
        A[j][i] -= w
    for i in range(n):
        edge(n,i,spokes[i])
        edge(i,(i+1)%n,rims[i])
    return A


def eigenvalues(S):
    """Classical Jacobi rotations for small real symmetric matrices."""
    A = [r.copy() for r in S]
    d = len(A)
    for iteration in range(200*d*d):
        i,j = max(((i,j) for i in range(d) for j in range(i+1,d)),
                  key=lambda ij: abs(A[ij[0]][ij[1]]))
        if abs(A[i][j]) < 1e-12:
            return sorted(A[k][k] for k in range(d))
        angle = .5 * math.atan2(2*A[i][j], A[j][j]-A[i][i])
        c,s = math.cos(angle),math.sin(angle)
        aii,ajj,aij = A[i][i],A[j][j],A[i][j]
        A[i][i] = c*c*aii-2*c*s*aij+s*s*ajj
        A[j][j] = s*s*aii+2*c*s*aij+c*c*ajj
        A[i][j]=A[j][i]=0.
        for k in range(d):
            if k==i or k==j: continue
            uki,ukj=A[k][i],A[k][j]
            A[k][i]=A[i][k]=c*uki-s*ukj
            A[k][j]=A[j][k]=s*uki+c*ukj
    raise RuntimeError('Jacobi did not converge')


def exact_small_checks():
    for n,aa in [(3,3),(4,2),(6,1)]:
        require(abs(alpha(n)-aa)<2e-14,'exact cosine')
        for P,Q,B in [(1,1,7),(2,1,13),(1,4,13)]:
            aa = Fraction(aa)
            P,Q,B=map(Fraction,(P,Q,B))
            if Q<P*aa:
                y=B/(P*aa+n*Q)
                x=aa*y/n
                target=(n+1)*x
            else:
                y=Fraction(0)
                x=B/(n*P)
                target=x
            require(n*(P*x+Q*y)==B,'exact budget')
            require(min((n+1)*x,x+aa*y)==target,'exact gap')


def analytic_and_matrix_checks():
    rng=random.Random(20261027)
    for n in range(3,15):
        for Q in (.1,.5,1.,2.,5.,15.):
            P=1.37
            B=2.1
            x,y,gap=candidate(n,P,Q,B)
            require(abs(n*(P*x+Q*y)-B)<2e-12,'cost')
            require(abs(gap-min((n+1)*x,x+alpha(n)*y))<2e-12,
                    'two orbit eigenvalues')
            ev=eigenvalues(mat(n,[x]*n,[y]*n))
            require(abs(ev[0])<1e-9,'zero eigen')
            require(abs(ev[1]-gap)<1e-9,'matrix spectral gap')
            for _ in range(5):
                raw=[rng.random()+.03 for i in range(2*n)]
                scale=B/(P*sum(raw[:n])+Q*sum(raw[n:]))
                raw=[v*scale for v in raw]
                trial=eigenvalues(mat(n,raw[:n],raw[n:]))[1]
                require(trial<=gap+2e-9,'unrestricted trial may not win')
            if Q<P*alpha(n):
                require(x>0 and y>0,'retained rim')
                require(abs((n+1)*x-(x+alpha(n)*y))<1e-10,
                        'eigenvalue crossing')
            else:
                require(y==0.0,'deleted rim')


def critical_line_checks():
    for n in range(3,13):
        P,B=2.0,1.0
        Q=P*alpha(n)
        base=B/(n*P)
        amax=B/(P*(n+1)*alpha(n))
        for portion in (0.,.1,.5,.9,1.):
            y=amax*portion
            x=base-alpha(n)*y
            eig=eigenvalues(mat(n,[x]*n,[y]*n))[1]
            require(abs(eig-base)<1e-9,'boundary continuum')


def asymptotic_checks():
    for kappa in (1.,10.,4*math.pi**2,100.):
        for n in (1000,4000):
            x,y,g=candidate(n,1.,kappa/(n*n),1.)
            limit=max(1.,4*math.pi**2/kappa)
            require(abs(n*g/limit-1)<.05,'asymptotic window')
    require(alpha(5)>1 and abs(alpha(6)-1)<1e-13 and alpha(7)<1,
            'equal-price five/six/seven transition')

if __name__=='__main__':
    exact_small_checks()
    analytic_and_matrix_checks()
    critical_line_checks()
    asymptotic_checks()
    print('VERIFY_OK',CHECKS,'assertions')
