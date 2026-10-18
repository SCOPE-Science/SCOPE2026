#!/usr/bin/env python3
"""Independent finite-sum and finite-graph checks for a three-row strip Hodge projector.
Standard Python library only. Exact proof is in RESULT.md.
"""
from math import sqrt
from fractions import Fraction

S1, S3 = sqrt(5.0), sqrt(21.0)
q1, q3 = (3.0-S1)/2.0, (5.0-S3)/2.0

def g(lam, k):
    s = sqrt(lam*(lam+4.0))
    q = (lam+2.0-s)/2.0
    return q**abs(k)/s

def h(lam, k):
    return g(lam,k)-g(lam,k-1)

def potential(kind, k):
    a, b = g(1,k), g(3,k)
    if kind == 'vertical':
        return (.5*(a+b), -b, .5*(-a+b))
    if kind == 'outer_horizontal':
        a, b = h(1,k), h(3,k)
        return (.5*a+b/6.0, -b/3.0, -.5*a+b/6.0)
    if kind == 'middle_horizontal':
        b = h(3,k)
        return (-b/3.0, 2.0*b/3.0, -b/3.0)
    raise ValueError(kind)


def truncated_column(kind, cutoff=80):
    # For horizontal source, the transverse zero-mode adds +1/3 to
    # every horizontal row gradient at the central column bond only.
    total=0.0; diag=None
    for k in range(-cutoff,cutoff+1):
        p = potential(kind,k)
        top_mid=p[0]-p[1]
        mid_bottom=p[1]-p[2]
        total += abs(top_mid)+abs(mid_bottom)
        if kind=='vertical' and k==0: diag=top_mid
        pnext=potential(kind,k+1)
        for row in range(3):
            current=p[row]-pnext[row]
            if kind != 'vertical' and k==0: current+=1.0/3.0
            total+=abs(current)
            if k==0 and ((kind=='outer_horizontal' and row==0) or
                         (kind=='middle_horizontal' and row==1)):
                diag=current
    return total, 1.0+total-2.0*diag


def exact_limits():
    return {
        'vertical':(1.0+1.0/S1+5.0/S3, 2.0+2.0/S3),
        'outer_horizontal':(7.0/3.0+1.0/S1-1.0/S3,4.0/3.0+2.0/S1),
        'middle_horizontal':(7.0/3.0,4.0/3.0+4.0/S3),
    }


def solve_fraction(M, b):
    """Exact Gauss-Jordan, independent of Fourier formulas."""
    n=len(b)
    T=[[Fraction(M[i][j]) for j in range(n)]+[Fraction(b[i])]
       for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if T[i][j])
        if pivot!=j:T[j],T[pivot]=T[pivot],T[j]
        z=T[j][j]
        for k in range(j,n+1):T[j][k]/=z
        for i in range(n):
            if i==j or not T[i][j]:continue
            z=T[i][j]
            for k in range(j,n+1):T[i][k]-=z*T[j][k]
    return [T[i][-1] for i in range(n)]


def finite_graph_column(N, kind):
    """Project a single edge in a genuinely finite three-rail graph."""
    V=3*N
    edges=[]
    for k in range(N):
        for r in (0,1): edges.append((3*k+r,3*k+r+1,'vertical',k,r))
    for k in range(N-1):
        for r in range(3):edges.append((3*k+r,3*(k+1)+r,'horizontal',k,r))
    L=[[0]*V for _ in range(V)]
    for a,b,*_ in edges:
        L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    center=N//2
    target=next((a,b) for a,b,etype,k,r in edges if k==center and
                ((kind=='vertical' and etype=='vertical' and r==0) or
                 (kind=='outer_horizontal' and etype=='horizontal' and r==0) or
                 (kind=='middle_horizontal' and etype=='horizontal' and r==1)))
    a,b=target
    f=[0]*(V-1)
    if a<V-1:f[a]+=1
    if b<V-1:f[b]-=1
    potential=solve_fraction([row[:V-1] for row in L[:V-1]], f)
    potential+=[Fraction(0)]
    q=[potential[x]-potential[y] for x,y,*_ in edges]
    col_q=sum(map(abs,q))
    col_iq=sum(abs(Fraction(int((x,y)==target))-qv) for (x,y,*_),qv in zip(edges,q))
    return float(col_q),float(col_iq)


def run():
    limits=exact_limits()
    for kind,(q,c) in limits.items():
        val=truncated_column(kind,80)
        assert max(abs(val[0]-q),abs(val[1]-c))<2e-13,(kind,val,(q,c))
        for N in (11,15):
            # Convergence of finite central-edge current as boundaries recede.
            f=finite_graph_column(N,kind)
            assert max(abs(f[0]-q),abs(f[1]-c))<.02,(N,kind,f,(q,c))
    assert limits['outer_horizontal'][0]>limits['vertical'][0]>limits['middle_horizontal'][0]
    assert limits['vertical'][1]>limits['outer_horizontal'][1]>limits['middle_horizontal'][1]
    print('VERIFY_OK: three orbit formulas; 3 Green-kernel checks and 6 finite-graph rational Laplacian comparisons')
    print('cut endpoint =',format(limits['outer_horizontal'][0],'.13f'))
    print('cycle endpoint =',format(limits['vertical'][1],'.13f'))

if __name__=='__main__':run()
