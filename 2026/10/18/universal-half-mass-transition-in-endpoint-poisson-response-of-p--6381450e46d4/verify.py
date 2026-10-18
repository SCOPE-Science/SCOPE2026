"""Reproducible checks for sharp pendant-vertex Poisson response.

Run with Python 3 (standard library only): python verify.py
These finite checks support, but do not prove, the universal statements.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import cos, pi, sqrt


def inverse(matrix):
    n=len(matrix)
    augmented=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if augmented[i][j])
        augmented[j],augmented[pivot]=augmented[pivot],augmented[j]
        z=augmented[j][j]
        augmented[j]=[x/z for x in augmented[j]]
        for i in range(n):
            if i!=j:
                fac=augmented[i][j]
                if fac:
                    augmented[i]=[a-fac*b for a,b in zip(augmented[i],augmented[j])]
    return [row[n:] for row in augmented]


def graph_laplacian(m,p,head_edges):
    n=m+p
    edges=list(head_edges)+([(0,m)]+[(m+k,m+k+1) for k in range(p-1)] if p else [])
    a=[[Q(0) for j in range(n)] for i in range(n)]
    for i,j in edges:
        a[i][i]+=1;a[j][j]+=1;a[i][j]-=1;a[j][i]-=1
    return a


def green(laplacian):
    n=len(laplacian)
    b=[[laplacian[i][j]+Q(1,n) for j in range(n)] for i in range(n)]
    inv=inverse(b)
    return [[v-Q(1,n) for v in row] for row in inv]


def median_norm(values):
    ordered=sorted(values)
    middle=ordered[(len(values)-1)//2]
    return sum(abs(x-middle) for x in ordered)


def tail_coefficients(m,p):
    n=m+p
    return [Q(m*k,n)+Q(k*(k-1),2*n) for k in range(1,p+1)]


def clique_tip_formula(m,p):
    n=m+p
    return median_norm([Q(-1,n)]*(m-1)+[Q(0)]+tail_coefficients(m,p))


def continuum(lam):
    if lam<=0.5:
        return 0.125-lam**3/3
    return (1-lam)**2*(1+2*lam)/6

checks=0
# Exact rational comparisons with the full pseudoinverse, for every tested size.
for m in range(2,8):
    for p in range(1,9):
        edges=list(combinations(range(m),2))
        g=green(graph_laplacian(m,p,edges))
        actual=median_norm(g[-1])
        expected=clique_tip_formula(m,p)
        assert actual==expected,(m,p,actual,expected)
        checks+=1

# Independent finite linear-programming test: enumerate all zero-sum cube vertices.
# With an even number of sites, every extreme point is a balanced sign vector.
# With an odd number, precisely one coordinate is zero and the others are balanced signs.
for m in range(2,6):
    for p in range(1,7):
        n=m+p
        if n>10:continue
        g=green(graph_laplacian(m,p,list(combinations(range(m),2))))[-1]
        brute=Q(0)
        if n%2==0:
            for plus in combinations(range(n),n//2):
                pos=set(plus)
                v=sum(g[i]*(1 if i in pos else -1) for i in range(n))
                brute=max(brute,abs(v))
        else:
            for zero in range(n):
                remaining=[i for i in range(n) if i!=zero]
                for plus in combinations(remaining,(n-1)//2):
                    pos=set(plus)
                    v=sum(g[i]*(0 if i==zero else (1 if i in pos else -1)) for i in range(n))
                    brute=max(brute,abs(v))
        assert brute==clique_tip_formula(m,p),(m,p,brute)
        checks+=1

# Test the head-to-path reduction with nonclique heads, computing their own Green functions.
for m in range(3,8):
    heads={
        'path':[(i,i+1) for i in range(m-1)],
        'cycle':[(i,(i+1)%m) for i in range(m)],
        'clique':list(combinations(range(m),2)),
        'star':[(0,i) for i in range(1,m)],
    }
    for edge_set in heads.values():
        head_g=green(graph_laplacian(m,0,edge_set))
        # Validate the full row formula through exact vector coefficients.
        for p in range(1,6):
            n=m+p
            g=green(graph_laplacian(m,p,edge_set))
            b=tail_coefficients(m,p)
            head_row=[Q(m,n)*(head_g[0][i]-head_g[0][0]) for i in range(m)]
            # Path response coefficients b, and head v0 term reconstructed in zero-sum gauge.
            # Relative to the head root, subtracting coefficients from all columns is harmless.
            for j in range(m):
                assert g[-1][j]-g[-1][0]==head_row[j],(m,p,j)
                checks+=1
            for k in range(p):
                assert g[-1][m+k]-g[-1][0]==b[k],(m,p,k)
                checks+=1

# Spectral-gap error control on several different connected head geometries.
for m in range(3,9):
    heads={
        'path': ([(i,i+1) for i in range(m-1)],2-2*cos(pi/m)),
        'cycle': ([(i,(i+1)%m) for i in range(m)],2-2*cos(2*pi/m)),
        'clique': (list(combinations(range(m),2)),float(m)),
        'star': ([(0,i) for i in range(1,m)],1.0),
    }
    for edge_set,gap in heads.values():
        for p in range(1,7):
            n=m+p
            full=median_norm(green(graph_laplacian(m,p,edge_set))[-1])
            ideal=median_norm([Q(0)]*m+tail_coefficients(m,p))
            upper=m/n*(m+sqrt(m))/gap
            assert float(abs(full-ideal)) <= upper+1e-9
            checks+=1

# Closed continuum median profile versus discrete collapsed-head median.
for n in [20,40,80,160,320,640]:
    for m in range(2,n):
        p=n-m
        t0=median_norm([Q(0)]*m+tail_coefficients(m,p))
        err=abs(float(t0)/n**2-continuum(m/n))
        assert err<=1.001/n,(n,m,err)
        checks+=1

# Asymptotic examples for the two regimes of clique attachment.
for p in [32,64,128,256]:
    dilute=clique_tip_formula(2,p)/p**2
    dominant=clique_tip_formula(40*p,p)/p**2
    assert abs(float(dilute)-.125)<3/p
    assert abs(float(dominant)-.5)<.02
    checks+=2

print(f'PASS: {checks} exact-rational and continuum-consistency comparisons.')
