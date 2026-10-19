"""Independent finite tests for the odd squared-cycle fastest-mixing formula.

Dependencies: Python 3, numpy, scipy. Analytical proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.optimize import linprog

checks = 0

def check(statement, message):
    global checks
    assert statement, message
    checks += 1


def formula(n):
    check(n >= 7 and n % 2 == 1, 'domain')
    c1 = math.cos(2 * math.pi / n)
    cK = -math.cos(math.pi / n)
    j = (n + 1) // 4
    d = math.cos(2 * math.pi * j / n)
    R = -2 * (c1 + cK)
    F = lambda c: 2 * R * (1 - c) + 4 * (1 - c * c)
    E, M = F(c1), F(d)
    b = 2 / (E + M)
    a = R * b
    mu = (M - E) / (M + E)
    return a, b, mu, j, R, E, M


def spectral_formula(n, a, b):
    return [1-2*a*(1-math.cos(2*math.pi*k/n))-
            2*b*(1-math.cos(4*math.pi*k/n))
            for k in range(1, (n+1)//2)]


def matrix(n, a, b):
    P = np.eye(n) * (1 - 2*a - 2*b)
    for i in range(n):
        for offset, val in ((1,a),(-1,a),(2,b),(-2,b)):
            P[i,(i+offset)%n] += val
    return P


def general_slem(P):
    w = np.linalg.eigvalsh(P)
    return float(np.max(np.abs(w[:-1])))


def independent_lp(n):
    k = np.arange(1,(n+1)//2)
    A = 1-np.cos(2*np.pi*k/n)
    B = 1-np.cos(4*np.pi*k/n)
    C = np.column_stack([2*A,2*B])
    inequalities = np.vstack([np.column_stack([-C,-np.ones(len(k))]),
                              np.column_stack([C,-np.ones(len(k))]),
                              np.array([1.,1.,0.])])
    bounds = np.r_[np.full(len(k),-1.),np.ones(len(k)),0.5]
    result=linprog([0,0,1],A_ub=inequalities,b_ub=bounds,
                   bounds=[(0,None)]*3,method='highs')
    check(result.success, f'linear program n={n}')
    return result.x


for n in range(7, 102, 2):
    a,b,mu,j,R,E,M = formula(n)
    check(0 < a < b and 0 < b < 0.5 and 0 < mu < 1, f'positivity n={n}')
    check(1 - 2*(a+b) > 0, f'positive hold n={n}')
    check(E < M, f'endpoint interior n={n}')
    check(abs(R - a/b) < 2e-11, f'ratio n={n}')
    check(abs(E-(2*R*(1+math.cos(math.pi/n)) +4*(1-math.cos(math.pi/n)**2)))<2e-10,
          f'endpoints n={n}')
    eigenvalues=spectral_formula(n,a,b)
    check(abs(max(map(abs,eigenvalues))-mu)<2e-11, f'SLEM n={n}')
    check(abs(eigenvalues[0]-mu)<2e-11, f'low-frequency contact n={n}')
    check(abs(eigenvalues[-1]-mu)<2e-11, f'antipodal contact n={n}')
    check(abs(eigenvalues[j-1]+mu)<2e-11, f'mid-frequency contact n={n}')
    la,lb,lmu=independent_lp(n)
    check(abs(la-a)<2e-7 and abs(lb-b)<2e-7 and abs(lmu-mu)<2e-7,
          f'independent optimization n={n}')
    if n <= 31:
        P=matrix(n,a,b)
        check(np.max(np.abs(P-P.T)) < 1e-13, f'symmetry n={n}')
        check(np.min(P)>-1e-13, f'stoch positivity n={n}')
        check(np.max(np.abs(P.sum(axis=1)-1))<1e-13, f'row sums n={n}')
        check(abs(general_slem(P)-mu)<1e-10, f'full matrix n={n}')

rng=np.random.default_rng(3602026)
for n in (7,9,11,13,15):
    a,b,mu,*_=formula(n)
    edges=sorted({tuple(sorted((i,(i+shift)%n)))
                  for i in range(n) for shift in (1,2)})
    for trial in range(100):
        P=np.zeros((n,n),dtype=float)
        for i,j in edges:
            v=.02 + .18*rng.random()
            P[i,j]=P[j,i]=v
        for i in range(n):
            P[i,i]=1-sum(P[i,j] for j in range(n) if j!=i)
        check(min(np.diag(P))>0 and abs(np.sum(P)-n)<1e-10,
              f'asymmetric feasible n={n} trial={trial}')
        check(general_slem(P)+1e-10>=mu,
              f'asymmetric comparison n={n} trial={trial}')

for n in (501,1001,2001):
    a,b,mu,j,R,E,M=formula(n)
    z=(math.pi/n)**2
    check(abs(a/z-1.5)<0.015, f'a asymptotic n={n}')
    check(abs((.5-b)/z-21/8)<0.015, f'b asymptotic n={n}')
    check(abs((1-2*(a+b))/z-9/4)<0.015, f'hold asymptotic n={n}')
    check(abs((1-mu)/z-8)<0.025, f'gap asymptotic n={n}')
    C=math.cos(math.pi/n)
    c1=math.cos(2*math.pi/n)
    pure=(c1+C)/(2-c1+C)
    check(abs((1-mu)/(1-pure)-4)<0.015,
          f'fourfold spectral-gap improvement n={n}')
print('PASS',checks,'checks')
