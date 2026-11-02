"""Reproduce exact identities and finite numerical tests for single-capped path mixing."""
from fractions import Fraction as F
from math import sqrt, isqrt
from random import Random


def center(m, d):
    p = [d[0] * 0]
    for v in d:
        p.append(p[-1] + v)
    mean = sum(a * b for a, b in zip(m, p)) / sum(m)
    x = [v - mean for v in p]
    V = sum(a * b * b for a, b in zip(m, x))
    S = []
    partial = 0
    for a, b in zip(m[:-1], x[:-1]):
        partial += a * b
        S.append(-partial)
    return x, V, S


def capped_design(m, c, B, k, U):
    q = [sqrt(t) for t in c]
    _, V0, S0 = center(m, q)
    lam0 = B / V0
    w0 = [lam0 * S0[i] / q[i] for i in range(len(q))]
    if U >= w0[k]:
        return lam0, w0, q[k], w0[k]
    dc = q[:]
    dc[k] = 0.0
    _, Vc, Sc_vec = center(m, dc)
    Sc = Sc_vec[k]
    massL, massR = sum(m[:k+1]), sum(m[k+1:])
    C = massL * massR / sum(m)
    E = B - c[k] * U
    discr = (U*Vc - C*E)**2 + 4*U*Sc**2*E
    z = (C*E-U*Vc+sqrt(discr))/(2*U*Sc)
    d = q[:]
    d[k] = z
    x, V, S = center(m, d)
    lam = U*z/S[k]
    w = [lam*S[i]/d[i] for i in range(len(d))]
    w[k] = U
    assert z > q[k]
    assert abs(lam - U*z/(Sc+C*z)) < 2e-9*max(1,lam)
    assert abs(V - (Vc+2*Sc*z+C*z*z)) < 2e-8*max(1,V)
    return lam, w, z, w0[k]


def jacobi_eigenvalues(matrix):
    n = len(matrix)
    A = [r[:] for r in matrix]
    scale = max(1., max(abs(z) for row in A for z in row))
    for _ in range(60*n*n):
        _, p, q = max((abs(A[i][j]), i, j) for i in range(n) for j in range(i+1,n))
        if abs(A[p][q]) < 2e-12 * scale:
            break
        b = A[p][q]
        tau = (A[q][q]-A[p][p])/(2*b)
        t = (1. if tau >= 0 else -1.)/(abs(tau)+sqrt(1+tau*tau))
        cc = 1/sqrt(1+t*t)
        ss = t*cc
        app, aqq = A[p][p], A[q][q]
        A[p][p], A[q][q] = app-t*b, aqq+t*b
        A[p][q] = A[q][p] = 0.
        for h in range(n):
            if h in (p,q):
                continue
            ap, aq = A[h][p], A[h][q]
            A[h][p]=A[p][h]=cc*ap-ss*aq
            A[h][q]=A[q][h]=ss*ap+cc*aq
    else:
        raise AssertionError('Jacobi eigensolver did not converge')
    return sorted(A[i][i] for i in range(n))


def gap(m, w):
    n = len(m)
    A = [[0. for _ in range(n)] for _ in range(n)]
    for j, v in enumerate(w):
        A[j][j] += v/m[j]
        A[j+1][j+1] += v/m[j+1]
        A[j][j+1]=A[j+1][j]=-v/sqrt(m[j]*m[j+1])
    return jacobi_eigenvalues(A)[1]


def exact_tests():
    rng = Random(20261031)
    tests = 0
    for n in range(3, 10):
        for _ in range(35):
            m = [F(rng.randint(1, 7), rng.randint(1, 4)) for _ in range(n)]
            q = [F(rng.randint(1, 5), rng.randint(1, 4)) for _ in range(n-1)]
            c = [v*v for v in q]
            k = rng.randrange(n-1)
            U = F(rng.randint(1,7),rng.randint(1,5))
            z = q[k] + F(rng.randint(1,9),rng.randint(1,5))
            dc=q[:];dc[k]=F(0)
            _, Vc, Sc_arr = center(m, dc)
            Sc=Sc_arr[k]
            ml=sum(m[:k+1]);mr=sum(m[k+1:]);C=ml*mr/sum(m)
            d=q[:];d[k]=z
            x,V,S=center(m,d)
            lam=U*z/S[k]
            w=[lam*S[i]/q[i] if i!=k else U for i in range(n-1)]
            B=sum(c[i]*w[i] for i in range(n-1))
            E=B-c[k]*U
            assert Sc>0 and Vc>0 and C>0 and E>0
            assert V==Vc+2*Sc*z+C*z*z
            assert S[k]==Sc+C*z
            assert U*Sc*z*z+(U*Vc-C*E)*z-Sc*E==0
            assert sum(c[i]*w[i] for i in range(n-1))==B
            assert all(v>0 for v in w)
            assert sum(m[i]*x[i] for i in range(n))==0
            for i in range(n):
                lhs=(w[i-1]*(x[i]-x[i-1]) if i>0 else F(0))+(w[i]*(x[i]-x[i+1]) if i<n-1 else F(0))
                assert lhs==lam*m[i]*x[i]
            _,V0,S0=center(m,q)
            assert U < B*S0[k]/(V0*q[k])
            tests+=1
    return tests


def numeric_tests():
    rng = Random(144231)
    tests = competitors = 0
    for n in range(3, 12):
        for _ in range(65):
            m=[rng.uniform(.25,5) for _ in range(n)]
            c=[rng.uniform(.2,4) for _ in range(n-1)]
            B=rng.uniform(.5,10)
            k=rng.randrange(n-1)
            _, _, _, threshold = capped_design(m,c,B,k,1.e8)
            U=threshold * rng.uniform(.08,1.8)
            lam,w,z,threshold2=capped_design(m,c,B,k,U)
            assert abs(threshold-threshold2)<1e-8
            assert all(v>0 for v in w)
            assert sum(w[i]*c[i] for i in range(n-1)) <= B+1.e-8
            assert w[k] <= U + 1.e-9
            spectral=gap(m,w)
            assert abs(spectral-lam) < 1e-8*max(1,lam), (n,m,c,k,U,lam,spectral)
            if U < threshold:
                for _ in range(12):
                    vals=[rng.expovariate(1) for _ in range(n-1)]
                    ww=[B*vals[i]/(c[i]*sum(vals)) for i in range(n-1)]
                    if ww[k]>U:
                        ww[k]=U
                        other=sum(c[i]*ww[i] for i in range(n-1) if i!=k)
                        ww=[v*(B-c[k]*U)/other if i!=k else U for i,v in enumerate(ww)]
                    assert gap(m,ww) <= lam+1e-8, (n,lam,gap(m,ww))
                    competitors+=1
            tests+=1
    lam,w,z,threshold=capped_design([1.]*4,[1.]*3,1.,1,.2)
    assert abs(threshold-.4)<1e-12
    assert all(abs(w[i]-v)<1e-10 for i,v in enumerate([.4,.2,.4]))
    assert abs(lam-(3-sqrt(5))/5)<1e-10
    assert abs(z-(1+sqrt(5)))<1e-10
    return tests, competitors


if __name__=='__main__':
    e=exact_tests()
    n,c=numeric_tests()
    print('PASS:',e,'exact rational constructed cases,',n,'finite numerical spectral cases,',c,'feasible comparisons; one algebraic radical example.')
