#!/usr/bin/env python3
"""Reproduce finite analytic-integral and Gramian checks; no external packages."""
import cmath, math

def mat_rank(a, tol=1e-9):
    a=[row[:] for row in a]
    rows=len(a); cols=len(a[0])
    pivotrow=0
    for col in range(cols):
        r=max(range(pivotrow, rows), key=lambda k: abs(a[k][col])) if pivotrow<rows else pivotrow
        if pivotrow>=rows or abs(a[r][col])<=tol:
            continue
        a[pivotrow],a[r]=a[r],a[pivotrow]
        p=a[pivotrow][col]
        for k in range(col,cols): a[pivotrow][k]/=p
        for q in range(rows):
            if q!=pivotrow:
                v=a[q][col]
                for k in range(col,cols): a[q][k]-=v*a[pivotrow][k]
        pivotrow+=1
    return pivotrow

def segment_matrix(m,edges):
    N=len(edges)-1
    B=[[0.0]*N for _ in range(2*m)]
    for j in range(1,m+1):
        for k in range(N):
            a,b=edges[k:k+2]
            B[2*j-2][k]=(math.sin(j*b)-math.sin(j*a))/j
            B[2*j-1][k]=(math.cos(j*b)-math.cos(j*a))/j
    return B

def verify():
    checks=0
    for m in range(1,9):
        N=2*m
        # Deliberately irregular knots, positive durations.
        weights=[k+1 for k in range(N)]
        total=sum(weights)
        edges=[0.0]
        for w in weights: edges.append(edges[-1]+2*math.pi*w/total)
        B=segment_matrix(m,edges)
        for row in B:
            assert abs(sum(row))<2e-12
            checks+=1
        assert mat_rank(B)<=N-1
        checks+=1
        for N in (2*m+1,2*m+2,3*m+7):
            delta=2*math.pi/N
            edges=[2*math.pi*k/N for k in range(N+1)]
            B=segment_matrix(m,edges)
            assert mat_rank(B)==2*m
            checks+=1
            for r in range(2*m):
                for s in range(2*m):
                    got=sum(B[r][k]*B[s][k] for k in range(N))/delta
                    expected=(math.pi*math.sin((r//2+1)*math.pi/N)**2/((r//2+1)*math.pi/N)**2) if r==s else 0.0
                    assert abs(got-expected)<3e-11,(m,N,r,s,got,expected)
                    checks+=1
            ratio=1/(math.sin(m*math.pi/N)/(m*math.pi/N))**2
            assert ratio>=1 and ratio<math.pi**2/4+1e-12
            checks+=1
    for m in (1,2,3,10,100,1000,10000):
        z=m*math.pi/(2*m+1)
        ratio=(z/math.sin(z))**2
        assert 1 < ratio < math.pi**2/4
        checks+=1
    assert abs((10000*math.pi/(20001)/math.sin(10000*math.pi/20001))**2-math.pi**2/4)<1e-3
    checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__': verify()
