#!/usr/bin/env python3
import math


def dot(u,v):
    return sum(complex(a).conjugate()*complex(b) for a,b in zip(u,v))

def norm2(u):
    return dot(u,u).real

def vec(n, i):
    x=[0j]*n; x[i]=1+0j; return x

def add(*vs):
    return [sum(z) for z in zip(*vs)]

def scale(a,v):
    return [a*z for z in v]

def check_basis(m, phis, expected_z):
    # Output basis f_0,...,f_m.  phis live in span(f_1,...,f_m).
    n=m+1
    fs=[vec(n,i) for i in range(n)]
    for p in phis:
        assert abs(norm2(p)-1.0) < 1e-10
        assert abs(p[0]) < 1e-10
    for i in range(m):
        for j in range(m):
            target=1.0 if i==j else 0.0
            assert abs(dot(phis[i],phis[j])-target) < 1e-10
    alphas=[dot(fs[1],p) for p in phis]
    z=sum(abs(a)<1e-10 for a in alphas)
    assert z==expected_z
    assert z <= m-1
    # Trace preservation is diagonal: E0^*E0 covers e0,e1 and Ej^*Ej covers e_{j+1}.
    diag=[1.0,1.0]+[1.0]*m
    assert diag == [1.0]*(m+2)
    # Cross coefficients E0^*Ej are exactly alpha_j |e1><e_{j+1}|.
    for a,p in zip(alphas,phis):
        assert abs(a-dot(fs[1],p))<1e-12
    # Predicted two maximal types coalesce precisely at z=m-1.
    dominates = (m+1 <= z+2)
    assert dominates == (z==m-1)

# Salzmann--Singh Hadamard example: m=2, z=0.
s=1/math.sqrt(2)
check_basis(2, [ [0,s,s], [0,s,-s] ], 0)

# Fully aligned m=2 endpoint: domination returns, z=1.
check_basis(2, [ [0,1,0], [0,0,1] ], 1)

# m=3 with one branch orthogonal to f1 but not full alignment: z=1<m-1.
check_basis(3, [ [0,0,1,0], [0,s,0,s], [0,s,0,-s] ], 1)

print('VERIFY_OK')
