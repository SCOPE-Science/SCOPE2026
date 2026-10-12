"""Numerical consistency checks for the corner-capture theorem.

Requires numpy and scipy.  Finite tests supplement, and do not replace,
the cyclotomic-field proof given in RESULT.md.
"""
import numpy as np
from scipy.linalg import expm

PRIMES = (3, 5, 7, 11, 13)


def path_adjacency(n):
    return np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1)


def group_eigenvalues(x, tol=1e-8):
    y = np.sort(np.asarray(x, dtype=float))
    groups = [[y[0]]]
    for v in y[1:]:
        if abs(v-groups[-1][-1]) < tol:
            groups[-1].append(v)
        else:
            groups.append([v])
    return groups


def predicted_rank(p, q):
    if p != q:
        return (p-1)*(q-1)
    return (p-1)**2//2 + 1


spectrum_checks = 0
for p in PRIMES:
    for q in PRIMES:
        a = 2*np.cos(np.pi*np.arange(1,p)/p)
        b = 2*np.cos(np.pi*np.arange(1,q)/q)
        sums = (a[:, None]+b[None, :]).ravel()
        groups = group_eigenvalues(sums)
        assert len(groups) == predicted_rank(p,q), (p,q,len(groups))
        spectrum_checks += 1

operator_checks = 0
for p,q in ((3,3),(3,5),(3,7),(5,5),(5,7),(7,7),(7,11)):
    H = np.kron(path_adjacency(p-1),np.eye(q-1)) + np.kron(np.eye(p-1),path_adjacency(q-1))
    n = H.shape[0]
    values,V = np.linalg.eigh(H)
    groups=group_eigenvalues(values)
    assert len(groups)==predicted_rank(p,q)
    # Every distinct eigenenergy must have a nonzero corner projection.
    positions=[]
    first=0
    for group in groups:
        size=len(group)
        power=np.sum(np.abs(V[0,first:first+size])**2)
        assert power>1e-12, (p,q,group,power)
        positions.append(power)
        first+=size
    assert abs(sum(positions)-1)<1e-10
    K=H.astype(complex)-0.35j*np.diag([1]+[0]*(n-1))
    w=np.linalg.eigvals(K)
    dark_count=np.count_nonzero(abs(w.imag)<1e-8)
    assert dark_count==n-predicted_rank(p,q), (p,q,dark_count)
    assert np.max(w.imag)<1e-8
    operator_checks+=1

# A few fully independent finite-time norm comparisons.
finite_time_checks = 0
for p,q in ((3,3),(3,5),(5,5)):
    H=np.kron(path_adjacency(p-1),np.eye(q-1)) + np.kron(np.eye(p-1),path_adjacency(q-1))
    n=H.shape[0]
    K=H.astype(complex)-0.7j*np.diag([1]+[0]*(n-1))
    w=np.linalg.eigvals(K)
    negative=-w.imag[w.imag<-1e-10]
    rate=np.min(negative)
    t=min(80000.,max(1000.,35./rate))
    U=expm(-1j*K*t)
    survival=np.sum(abs(U)**2)/n
    expected=1-predicted_rank(p,q)/n
    assert abs(survival-expected)<1e-7,(p,q,survival,expected,rate)
    finite_time_checks+=1

print(f'VERIFY_OK prime_pairs={spectrum_checks} independent_operator_tests={operator_checks} long_time_survival={finite_time_checks}')
