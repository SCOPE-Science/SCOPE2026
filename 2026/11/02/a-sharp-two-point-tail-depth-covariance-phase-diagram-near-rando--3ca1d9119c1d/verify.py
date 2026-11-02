#!/usr/bin/env python3
"""Exact independent checks for pairwise transient depth in uniform random mappings.
Uses integer arithmetic only and enumerates finite parent types symbolically in k.
"""
from itertools import product
from fractions import Fraction

# Coefficients in ascending powers of k for W_m, A_m, B_m.
TABLE = {
    2: ([0,2,1], [0,3,1], [0,4,1]),
    3: ([0,9,6,1], [0,17,8,1], [0,30,10,1]),
    4: ([0,64,48,12,1], [0,142,78,15,1], [0,302,120,18,1]),
    5: ([0,625,500,150,20,1], [0,1569,944,222,24,1], [0,3836,1712,315,28,1]),
}
# k-polynomials P_m satisfying Cov(H_x,H_y | conditions) = P_m(k)/(k+m)^(2m-2).
PHASE = {
    2: [-1],
    3: [-19,-2,1],
    4: [-836,24,192,46,3],
    5: [-64261,25728,40503,14072,2217,168,5],
}

checks=0

def check(cond, message):
    global checks
    checks += 1
    if not cond:raise AssertionError(message)

def value(poly,k):
    return sum(z*k**i for i,z in enumerate(poly))

def path_depths(par, root=-1):
    m=len(par)
    out=[]
    for i in range(m):
        d=0; seen=set();v=i
        while v != root:
            if v in seen: return None
            seen.add(v)
            v=par[v];d+=1
        out.append(d)
    return out

# First exact method: collapse each of k named roots to a single root symbol;
# then a type with r root arrows represents precisely k^r labeled forests.
for m in range(2,6):
    polys=[[0]*(m+1) for _ in range(3)]
    for p in product(range(-1,m),repeat=m):
        if any(p[i]==i for i in range(m)):continue
        d=path_depths(p)
        if d is None:continue
        r=p.count(-1)
        for j,coef in enumerate((1,d[0],d[0]*d[1])):
            polys[j][r] += coef
    for j in range(3):
        for t in range(m+1):
            check(polys[j][t]==TABLE[m][j][t],f'Polynomial coefficient m={m} moment={j} power={t}')
    W,A,B=polys
    for k in range(1,30):
        n=k+m
        den=value(W,k)
        check(den==k*n**(m-1), f'forest count n={n},m={m}')
        num=value(B,k)*den-value(A,k)**2
        expected=value(PHASE[m],k)*k*k*n**0 # since W^2=k^2*n^(2m-2)
        check(num==expected, f'covariance polynomial at m={m},k={k}: {num} != {expected}')
        sign=(-1 if m==2 else (-1 if k<=5 else 1) if m==3 else (-1 if k==1 else 1) if m==4 else 1)
        check((num>0)-(num<0)==sign, f'sign m={m},k={k}')

# Second exact method: enumerate all *actual* maps on n labels, without
# assuming beforehand that conditional forest laws are uniform.
for n in range(3,7):
    stats={}  # m-> [count, sum Hx, sum Hy, sum Hx*Hy]
    for f in product(range(n),repeat=n):
        on_cycle=set()
        # Directly detect cyclic vertices by full orbit recurrence.
        for start in range(n):
            visited={}; route=[]; v=start
            while v not in visited:
                visited[v]=len(route);route.append(v);v=f[v]
            on_cycle.update(route[visited[v]:])
        if 0 in on_cycle or 1 in on_cycle:continue
        k=len(on_cycle);m=n-k
        if m not in TABLE:continue
        heights=[]
        for start in (0,1):
            v=start;h=0
            while v not in on_cycle:
                v=f[v];h+=1
            heights.append(h)
        z=stats.setdefault(m,[0,0,0,0]);z[0]+=1;z[1]+=heights[0];z[2]+=heights[1];z[3]+=heights[0]*heights[1]
    for m,z in stats.items():
        k=n-m
        # Choose other m-2 transient labels and k cyclic labels among n-2,
        # then k! cycle permutations, then k*n^(m-1) forests.
        from math import comb,factorial
        check(z[0]==comb(n-2,m-2)*factorial(k)*k*n**(m-1),f'mapping conditional count n={n} m={m}')
        w,a,b=TABLE[m]
        check(Fraction(z[1],z[0])==Fraction(value(a,k),value(w,k)),f'first moment n={n} m={m}')
        check(Fraction(z[2],z[0])==Fraction(value(a,k),value(w,k)),f'symmetry n={n} m={m}')
        check(Fraction(z[3],z[0])==Fraction(value(b,k),value(w,k)),f'joint moment n={n} m={m}')
        check(Fraction(z[3],z[0])-Fraction(z[1]*z[2],z[0]**2)==Fraction(value(PHASE[m],k),n**(2*m-2)),f'covariance n={n} m={m}')

# For m>=2 and k>=1 in the phase domain: symbolic sign boundaries.
check(value(PHASE[3],5)<0 and value(PHASE[3],6)>0,'m=3 threshold')
check(value(PHASE[4],1)<0 and value(PHASE[4],2)>0,'m=4 threshold')
check(value(PHASE[5],1)>0,'m=5 minimum')
print(f'PASS: {checks} exact assertions; four polynomial moment tables and direct mappings up to n=6.')
