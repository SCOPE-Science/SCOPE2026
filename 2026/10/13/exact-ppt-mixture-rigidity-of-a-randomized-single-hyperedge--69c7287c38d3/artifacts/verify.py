"""Reproducibility checks for the single-hyperedge determinant theorem.

Requires only the Python standard library. The all-size argument is analytic.
"""
import cmath
import itertools
import math


def det(matrix):
    n = len(matrix)
    value = 0j
    for perm in itertools.permutations(range(n)):
        parity = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        value += (-1 if parity & 1 else 1) * math.prod(matrix[i][perm[i]] for i in range(n))
    return value


def partial_transpose_pure(h):
    return [[h[2*i+l]*h[2*k+j].conjugate()
             for k in range(2) for l in range(2)]
            for i in range(2) for j in range(2)]


def parameters(n, k, theta):
    alpha = 2.0 ** (-k/2)
    beta = 2.0 ** (-(n-k)/2)
    nu = math.sqrt(1-alpha*alpha)
    w = math.sqrt(1-beta*beta)
    kap = (cmath.exp(1j*theta)-1) * 2.0 ** (-n/2)
    h = [1+kap*alpha*beta, kap*alpha*w, kap*nu*beta, kap*nu*w]
    return kap, nu, w, h


def active_pt(n, k, p, theta):
    kap, nu, w, h = parameters(n, k, theta)
    q = partial_transpose_pure(h)
    m = [[p*q[i][j] + ((1-p) if i == j == 0 else 0)
          for j in range(4)] for i in range(4)]
    expected = -p**3 * abs(kap)**4 * nu**4 * w**4
    return m, expected, h


# Check the general cofactor and determinant identity for complex 2x2 pure amplitudes.
for h in ([.7+.3j, -.2+.1j, .4-.6j, -.1+.2j],
          [1+.2j, .1-.7j, -.3+.8j, .5+.9j],
          [.2+.5j, .4-.7j, -.5+.8j, -.9-.2j]):
    q = partial_transpose_pure(h)
    dh = h[0]*h[3]-h[1]*h[2]
    assert abs(det(q) + abs(dh)**4) < 1e-10
    minor = [row[1:] for row in q[1:]]
    assert abs(det(minor)+abs(h[3])**2*abs(dh)**2) < 1e-10

# Finite independent substitution checks; not a proof for arbitrary n.
for n in range(2, 9):
    for k in range(1, n):
        for theta in (.2, 1.2, math.pi):
            for p in (.003, .2, .75, 1.0):
                block, exact, h = active_pt(n, k, p, theta)
                computed = det(block)
                assert abs(computed-exact) < 2e-12, (n,k,p,theta,computed,exact)
                assert abs(h[0]*h[3]-h[1]*h[2]-h[3]) < 1e-12
                assert exact < 0

# Separately reconstruct the full computational-basis partial transpose and
# compress onto the analytically specified active two-qubit tensor subspace.
for n in range(2, 6):
    N = 2**n
    for k in range(1, n):
        M = 2**(n-k)
        alpha = 2**(-k/2); beta = 2**(-(n-k)/2)
        nu = math.sqrt(1-alpha**2); w = math.sqrt(1-beta**2)
        aA = [2**(-k/2)]*(2**k)
        vA = [0.0]*(2**k); vA[-1]=1.0
        uA = [(vA[i]-alpha*aA[i])/nu for i in range(2**k)]
        aB = [2**(-(n-k)/2)]*M
        vB = [0.0]*M;vB[-1]=1.0
        uB = [(vB[j]-beta*aB[j])/w for j in range(M)]
        basis = [[v[i//M]*wvec[i%M] for i in range(N)]
                 for v,wvec in ((aA,aB),(aA,uB),(uA,aB),(uA,uB))]
        for theta in (.8,math.pi):
            for p in (.25,.7):
                amplitudes = [2**(-n/2)]*N
                amplitudes[-1]*=cmath.exp(1j*theta)
                def rho_entry(r,c):
                    return (1-p)/N + p*amplitudes[r]*amplitudes[c].conjugate()
                rho_pt = [[rho_entry((r//M)*M+(c%M), (c//M)*M+(r%M))
                           for c in range(N)] for r in range(N)]
                compressed = [[sum(basis[i][r]*rho_pt[r][c]*basis[j][c]
                                   for r in range(N) for c in range(N))
                               for j in range(4)] for i in range(4)]
                block,expected,h = active_pt(n,k,p,theta)
                assert max(abs(compressed[i][j]-block[i][j])
                           for i in range(4) for j in range(4)) < 1e-11

print('VERIFY_OK')
