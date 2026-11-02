"""Finite sanity checks for the mixed clique-bouquet negative-type theorem.
Run: python3 verify.py
Only Python's standard library is used. Finite tests do not prove the theorem.
"""
import itertools
import math


def q_star(sizes):
    assert len(sizes) >= 2 and min(sizes) >= 1
    def phi(q):
        return (q - 2) * sum(1/(q-1+1/k) for k in sizes)
    lo, hi = 2.0, 4.0
    assert phi(lo) < 1 and phi(hi) >= 1
    for _ in range(90):
        mid = (lo + hi) / 2
        if phi(mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def compositions(n, m, low=1):
    if m == 1:
        if n >= low:
            yield (n,)
    else:
        for k in range(low, n//m + 1):
            for rest in compositions(n-k, m-1, k):
                yield (k,) + rest


def projected_distance_power(sizes, q):
    n = sum(sizes) + 1
    blade = [-1] + [i for i,k in enumerate(sizes) for _ in range(k)]
    def d(i,j):
        if i == j: return 0.0
        return 1.0 if i == 0 or j == 0 or blade[i] == blade[j] else q
    # Basis e_i - e_0, i>0; entry d(i,j) - d(i,0) - d(0,j) + d(0,0).
    return [[d(i,j)-2.0 for j in range(1,n)] for i in range(1,n)]


def max_eigenvalue_symmetric(a):
    # Cyclic Jacobi diagonalization; independent of the scalar secular equation.
    n = len(a)
    a = [list(row) for row in a]
    for sweep in range(55):
        offmax = max((abs(a[i][j]) for i in range(n) for j in range(i+1,n)),default=0)
        if offmax < 2e-12:
            return max(a[i][i] for i in range(n))
        for i in range(n):
            for j in range(i+1,n):
                bij = a[i][j]
                if abs(bij) < 2e-14: continue
                tau = (a[j][j]-a[i][i])/(2.0*bij)
                t = (1.0 if tau >= 0 else -1.0)/(abs(tau)+math.sqrt(1.0+tau*tau))
                c = 1.0/math.sqrt(1.0+t*t)
                s = t*c
                aii,ajj = a[i][i],a[j][j]
                a[i][i] = aii-t*bij
                a[j][j] = ajj+t*bij
                a[i][j] = a[j][i] = 0.0
                for k in range(n):
                    if k in (i,j): continue
                    aik,ajk = a[i][k],a[j][k]
                    a[i][k]=a[k][i]=c*aik-s*ajk
                    a[j][k]=a[k][j]=s*aik+c*ajk
    raise AssertionError('Jacobi eigensolver failed to converge')


def check():
    cases, eigenchecks, balancechecks, witnesses = 0, 0, 0, 0
    for m in range(2,6):
        for N in range(m,min(m+8,13)):
            vectors=list(compositions(N,m))
            balanced=tuple(sorted([N//m+(i<N%m) for i in range(m)]))
            unbalanced=(1,)*(m-1)+(N-m+1,)
            qb, qu = q_star(balanced), q_star(unbalanced)
            for ks in vectors:
                q=q_star(ks)
                assert qb-2e-11 <= q <= qu+2e-11,(ks,qb,q,qu)
                balancechecks += 1
                for test_q,expect in [(1.0,'negative'),(2.0,'negative'),((2+q)/2,'negative'),(q,'zero'),(q+.03,'positive')]:
                    lam=max_eigenvalue_symmetric(projected_distance_power(ks,test_q))
                    if expect == 'negative':assert lam < -1e-8,(ks,test_q,lam)
                    elif expect == 'zero':assert abs(lam) < 2e-8,(ks,test_q,lam)
                    else:assert lam > 1e-6,(ks,test_q,lam)
                    eigenchecks += 1
                # Independent Q form at criticality, on the explicit blade-constant witness.
                vals=[1/(1+(q-1)*k) for k in ks]
                sums=[k*v for k,v in zip(ks, vals)]
                qform=-sum(k*v*v for k,v in zip(ks,vals))+(1-q)*sum(s*s for s in sums)+(q-2)*sum(sums)**2
                assert abs(qform)<1e-8,(ks,q,qform)
                witnesses += 1
                cases += 1
                for i,j in itertools.combinations(range(m),2):
                    vv=list(ks)
                    if vv[j]-vv[i]>=2:
                        vv[i]+=1; vv[j]-=1
                        assert q_star(vv) < q-1e-9,(ks,vv)
    print('PASS',cases,'nonisomorphic bouquets;',eigenchecks,'Jacobi eigenvalue checks;',
          balancechecks,'majorization-envelope checks;',witnesses,'critical null witnesses')
    for ks in [(2,2,2),(1,2,3),(1,1,4)]:
        q=q_star(ks)
        print('sample',ks,'q=',format(q,'.12f'),'p=',format(math.log2(q),'.12f'))

if __name__=='__main__': check()
