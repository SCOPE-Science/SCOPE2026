#!/usr/bin/env python3
"""Reproduce the numerical checks for a sparse-node trigonometric quadrature theorem.

Uses only Python's standard library. The proof is in RESULT.md; these
finite computations are diagnostic and do not certify all odd orders.
"""
import cmath
import math

PI = math.pi
CHECKS = 0


def check(condition, description):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description)


def close(x, y, tol=2e-10):
    return abs(x-y) <= tol * max(1, abs(x), abs(y))


def cardinal(K, j, theta):
    h = 2*PI/K
    z = theta-j*h
    den = math.sin(z/2)
    if abs(den) < 1e-12:
        return 1.0
    return math.sin(K*z/2)/(K*den)


def direct_solve(A, b):
    n = len(b)
    a = [[complex(z) for z in row] + [complex(v)] for row, v in zip(A,b)]
    for c in range(n):
        p = max(range(c,n), key=lambda r:abs(a[r][c]))
        if abs(a[p][c]) <= 1e-13:
            raise ArithmeticError('Unexpected singular Fourier system')
        a[c], a[p] = a[p], a[c]
        pv = a[c][c]
        for j in range(c, n+1):
            a[c][j] /= pv
        for r in range(c+1,n):
            v = a[r][c]
            for j in range(c,n+1):
                a[r][j] -= v*a[c][j]
    x = [0j]*n
    for c in range(n-1,-1,-1):
        x[c] = a[c][n]-sum(a[c][j]*x[j] for j in range(c+1,n))
    return x


def independent_fourier_weights(K, shifts):
    h = 2*PI/K
    nodes = [(j+shifts.get(j,0))*h for j in range(K)]
    ks = list(range(-(K//2),K//2+1))
    a = [[cmath.exp(1j*k*x) for x in nodes] for k in ks]
    b = [2*PI if k==0 else 0 for k in ks]
    return direct_solve(a,b)


def one_site_weights(K, delta):
    h=2*PI/K
    if delta==0:
        return [h]*K
    t=PI/K
    s=math.sin(PI*delta)
    u=delta*t
    w=[0.0]*K
    w[0]=2*PI*math.sin(u)/s
    for j in range(1,K):
        w[j]=h*(1-(-1)**(j+1)*math.sin(u)/math.sin((j-delta)*t))
    return w


def two_site_weights(K, delta):
    h=2*PI/K
    if delta==0:
        return [h]*K
    t=PI/K
    u=delta*t
    v=(1-delta)*t
    s=math.sin(PI*delta)
    s0=s/K*(1/math.sin(u)-1/math.sin((2-delta)*t))
    w=[0.0]*K
    w[0]=w[2]=h/s0
    for j in range(K):
        if j in (0,2):
            continue
        sj=cardinal(K,j,delta*h)+cardinal(K,j,(2-delta)*h)
        w[j]=h*(1-sj/s0)
    return w


def delta_critical(K):
    t=PI/K
    return 1-math.asin(math.sqrt(1-math.cos(t)))/t


def center_weight(K, delta):
    h=2*PI/K
    t=PI/K
    v=(1-delta)*t
    return h*(1+math.cos(t)-math.sin(t)**2/math.sin(v)**2)/math.cos(t)


def main():
    for K in (5,7,9,11,15,21,31,51,101,501):
        critical=delta_critical(K)
        check(0.25 < critical < 1-1/math.sqrt(2),f'frontier range K={K}')
        for delta in (0,0.03,0.1,0.249,0.25,0.28,0.29,0.30,0.40,0.49):
            a=one_site_weights(K,delta)
            check(all(z>0 for z in a),f'one-site positivity K={K} d={delta}')
            check(close(sum(a),2*PI),f'one-site mass K={K} d={delta}')
            b=two_site_weights(K,delta)
            check(close(sum(b),2*PI),f'two-site mass K={K} d={delta}')
            check(close(b[1],center_weight(K,delta)),f'center formula K={K} d={delta}')
            check(all(b[j]>0 for j in range(K) if j!=1),f'other sites positive K={K} d={delta}')
            if abs(delta-critical)>1e-5:
                check((b[1]>0) == (delta<critical),f'sign frontier K={K} d={delta}')
            check(close(sum(map(abs,b)),2*PI+2*max(0,-b[1])),f'abs norm K={K} d={delta}')
        check(close(center_weight(K,critical),0),f'zero frontier K={K}')
        for delta in (0.13,0.22,0.37,0.49):
            w=two_site_weights(K,delta)
            h=2*PI/K
            check(close(w[0],w[2]),f'symmetric moved weights K={K}')
            # Equivalent analytic Dirichlet-kernel expression for the other fixed nodes
            t=PI/K; v=(1-delta)*t; s=math.sin(PI*delta)
            s0=2*s*math.sin(v)*math.cos(t)/(K*(math.sin(t)**2-math.sin(v)**2))
            check(close(w[0],h/s0),f'moved weight formula K={K} d={delta}')
            for k in range(-K//2+1,K//2+1):
                j=(1+k)%K
                if j in (0,2):continue
                sk=2*(-1)**k*s*math.sin(v)*math.cos(k*t)/(K*(math.sin(v)**2-math.sin(k*t)**2))
                check(close(w[j],h*(1-sk/s0)),f'S_k formula K={K} k={k} d={delta}')
    last=0.24
    for K in (5,7,9,11,15,21,31,51,101,501,1001):
        d=delta_critical(K)
        check(d>last,f'monotone K={K}')
        last=d
    check(abs(delta_critical(1001)-(1-1/math.sqrt(2)))<1e-6,'limit')
    # An independent complex-valued Fourier moment solver checks the formulas
    # without using the rank-two cardinal update.
    for K in (5,7,9,11,15,21):
        for d in (0,0.1,0.25,0.3,0.45):
            for shifts,construct in [({0:d},one_site_weights),({0:d,2:-d},two_site_weights)]:
                direct=independent_fourier_weights(K,shifts)
                predicted=construct(K,d)
                for j,(x,y) in enumerate(zip(direct,predicted)):
                    check(close(x,y,2e-9),f'Fourier weights K={K} d={d} j={j}')
                    check(abs(x.imag)<2e-9,f'reality K={K} d={d} j={j}')
    print(f'PASS: {CHECKS} grouped reproducible assertions')

if __name__=='__main__':
    main()
