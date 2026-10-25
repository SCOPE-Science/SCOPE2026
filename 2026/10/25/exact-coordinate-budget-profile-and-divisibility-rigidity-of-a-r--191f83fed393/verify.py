#!/usr/bin/env python3
"""Independent finite arithmetic and phase checks of the regular Fourier two-row endpoint profile.
Scientific statements and exact proof are in RESULT.md; floating-point tests are supplementary.
"""
import cmath, itertools, math

def predicted(n, r):
    r = min(r, n)
    q, t = divmod(n, r)
    h = math.pi / (2*n)
    return 2 * ((r-t)*math.sin(q*h) + t*math.sin((q+1)*h)) / math.sin(h)

def cluster_bound(n, k):
    return 2 * math.sin(k*math.pi/(2*n))/math.sin(math.pi/(2*n))

def partition_optimum(n, r):
    # Separate unrestricted integer partition dynamic programming, not balanced formula.
    best = [[-1.e100]*(n+1) for _ in range(r+1)]
    best[0][0] = 0.
    for j in range(1, r+1):
        for k in range(j, n+1):
            best[j][k] = max(best[j-1][k-u] + cluster_bound(n,u)
                              for u in range(1,k-j+2))
    return best[r][n]

def constructed(n, r):
    # Balanced consecutive blocks; choose the center in each block.
    r = min(r,n)
    q,t = divmod(n,r)
    sizes = [q+1]*t+[q]*(r-t)
    angles=[]
    pos=0
    for k in sizes:
        alpha = math.pi*(pos+(k-1)/2)/n
        angles.append(-2*alpha)
        pos += k
    omega = cmath.exp(2j*math.pi/n)
    return sum(max(abs(1+cmath.exp(1j*ang)*omega**j) for ang in angles)
               for j in range(n))

checks=0
for n in range(2,51):
    for r in range(1, min(n,12)+1):
        expected=predicted(n,r)
        assert abs(partition_optimum(n,r)-expected)<2e-10*(1+n)
        assert abs(constructed(n,r)-expected)<2e-10*(1+n)
        checks+=2
        # Compare arithmetic saturation with the published endpoint constant.
        ratio=expected / predicted(n,1)
        k=min(r,n)
        universal=k*math.sin(math.pi/(2*k))
        if n % r==0:
            assert abs(ratio-universal)<3e-11
        else:
            assert ratio < universal-1e-12
        checks+=1

# Grid search evaluates the original optimization independently of the partition bound.
for n in range(3,11):
    for r,gridsize in [(1,240),(2,56),(3,18)]:
        expected=predicted(n,r)
        theta=[2*math.pi*j/gridsize for j in range(gridsize)]
        # Deterministic sparse phase grid: enough to catch upper-bound violations.
        if r==1:
            vectors=((a,) for a in theta)
        elif r==2:
            vectors=itertools.product(theta, repeat=2)
        else:
            vectors=itertools.product(theta, repeat=3)
        roots=[cmath.exp(2j*math.pi*j/n) for j in range(n)]
        for v in vectors:
            phases=[cmath.exp(1j*a) for a in v]
            val=sum(max(abs(1+phase*z) for phase in phases) for z in roots)
            assert val <= expected+1e-9
            checks+=1

assert abs(predicted(3,2)-(2+2*math.sqrt(3))) < 1e-10
print('PASS',checks,'checks: integer-partition optimum, balanced witnesses, endpoint saturation, phase grids')
