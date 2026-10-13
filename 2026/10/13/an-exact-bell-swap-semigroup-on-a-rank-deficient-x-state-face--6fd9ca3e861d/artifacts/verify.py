#!/usr/bin/env python3
import cmath

TOL = 2e-12


def rho(a, c, d, w):
    return [
        [complex(a), 0j, 0j, complex(w)],
        [0j, 0j, 0j, 0j],
        [0j, 0j, complex(c), 0j],
        [complex(w).conjugate(), 0j, 0j, complex(d)],
    ]


def idx(i, j):
    return 2 * i + j


def bell_swap_left_right(r1, r2):
    # Direct contraction of systems A,B and C,D against
    # |Phi+>_{B,C} = (|00>+|11>)/sqrt(2), without using the closed formula.
    out = [[0j for _ in range(4)] for _ in range(4)]
    for a in range(2):
        for d in range(2):
            for A in range(2):
                for D in range(2):
                    s = 0j
                    for b in range(2):
                        for B in range(2):
                            s += 0.5 * r1[idx(a,b)][idx(A,B)] * r2[idx(b,d)][idx(B,D)]
                    out[idx(a,d)][idx(A,D)] = s
    return out


def matmul2(x, y):
    return [
        [x[0][0]*y[0][0] + x[0][1]*y[1][0], x[0][0]*y[0][1] + x[0][1]*y[1][1]],
        [x[1][0]*y[0][0] + x[1][1]*y[1][0], x[1][0]*y[0][1] + x[1][1]*y[1][1]],
    ]


def formula(links):
    # T_L ... T_1, with T_k=[[a_k,c_k],[0,d_k]].
    T = [[1.0, 0.0], [0.0, 1.0]]
    W = 1+0j
    for a,c,d,w in links:
        Tk = [[a,c],[0.0,d]]
        T = matmul2(Tk, T)
        W *= w
    A, C, D = T[0][0], T[0][1], T[1][1]
    fac = 2.0**(1-len(links))
    return [[fac*z for z in row] for row in rho(A,C,D,W)], (A,C,D,W)


def direct(links):
    out = rho(*links[0])
    for link in links[1:]:
        out = bell_swap_left_right(out, rho(*link))
    return out


def maxerr(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(4) for j in range(4))


def trace(m):
    return sum(m[i][i].real for i in range(4))


def check_case(links):
    f, (A,C,D,W) = formula(links)
    q = direct(links)
    assert maxerr(f,q) < TOL
    Z=A+C+D
    p=2.0**(1-len(links))*Z
    assert abs(trace(q)-p) < TOL
    assert Z > 0
    concurrence = 2*abs(W)/Z
    # Negative eigenvalue of the partial-transpose 2x2 block [[0,W],[W*,C]]/Z.
    lam_minus = (C-(C*C+4*abs(W)**2)**0.5)/(2*Z)
    if all(abs(x[3]) > 0 for x in links):
        assert concurrence > 0
        assert lam_minus < 0


cases = [
    [(0.40,0.15,0.45,0.20+0.05j)],
    [(0.40,0.15,0.45,0.20+0.05j), (0.35,0.25,0.40,-0.12+0.08j)],
    [(0.40,0.15,0.45,0.20+0.05j), (0.35,0.25,0.40,-0.12+0.08j), (0.30,0.20,0.50,0.10-0.09j)],
]
for case in cases:
    check_case(case)

# Check the two-parameter family used in arXiv:2609.11021.
s=0.6
kappa=0.7
L=5
link=(0.5,(1-s)/2,s/2,kappa*(s**0.5)/2)
f,(A,C,D,W)=formula([link]*L)
Z=A+C+D
an=A/Z
cn=C/Z
dn=D/Z
wn=W/Z
assert abs(an-0.5) < TOL
assert abs(cn-(1-s**L)/2) < TOL
assert abs(dn-s**L/2) < TOL
assert abs(wn-kappa**L*(s**L)**0.5/2) < TOL
assert abs(2*abs(wn)-(kappa*s**0.5)**L) < TOL

print('VERIFY_OK')
