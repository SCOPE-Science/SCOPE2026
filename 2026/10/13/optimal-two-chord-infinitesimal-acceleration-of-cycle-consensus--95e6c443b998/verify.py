#!/usr/bin/env python3
"""Finite cross-checks of the two-chord first-order cycle eigenvalue law.

Requires Python 3 and NumPy for independent full Laplacian diagonalizations.
The mathematical proof establishes every size; this program samples and enumerates
finite cases only. No result of this program asserts an infinite theorem.
"""
import math
import numpy as np


def predicted(n):
    if n < 4:
        raise ValueError('A cycle must admit two non-edges')
    if n % 2:
        z = math.pi / (2*n)
        return (4/n)*math.cos(z)**2*(1-math.sin(z))
    if n % 4 == 0:
        return 4/n
    q = math.cos(math.pi/n)**2
    return (8/n)*q/(1+q)


def chord_list(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)
            if j-i not in (1,n-1)]


def projected_coeff(n, e, f):
    i,j = e
    k,l = f
    aa = 8/n*math.sin(math.pi*(j-i)/n)**2
    bb = 8/n*math.sin(math.pi*(l-k)/n)**2
    cc = abs(math.cos(math.pi*(i+j-k-l)/n))
    return aa, bb, cc


def optimized_pair(n,e,f):
    a,b,c=projected_coeff(n,e,f)
    den = a+b+2*math.sqrt(a*b)*c
    optimum = a*b*(1-c*c)/den
    w = (b+math.sqrt(a*b)*c)/den
    return optimum,w


def direct_projected(n,e,f,w):
    theta = np.arange(n)*(2*math.pi/n)
    U = np.stack([np.cos(theta),np.sin(theta)],axis=1)*math.sqrt(2/n)
    v=np.zeros(n);v[e[0]]=1;v[e[1]]=-1
    z=np.zeros(n);z[f[0]]=1;z[f[1]]=-1
    P=w*np.outer(U.T@v,U.T@v)+(1-w)*np.outer(U.T@z,U.T@z)
    return np.linalg.eigvalsh(P)[0]


def laplacian(n, edges_and_weights):
    out=np.zeros((n,n))
    for i in range(n):
        j=(i+1)%n
        out[i,i]+=1;out[j,j]+=1
        out[i,j]-=1;out[j,i]-=1
    for (i,j),w in edges_and_weights:
        out[i,i]+=w;out[j,j]+=w
        out[i,j]-=w;out[j,i]-=w
    return out


def main():
    pairs=0; edges=0; fullspectra=0
    for n in range(4,33):
        chords=chord_list(n)
        edges+=len(chords)
        best=-1
        winner=None
        for idx,e in enumerate(chords):
            for f in chords[idx+1:]:
                pairs+=1
                val,w=optimized_pair(n,e,f)
                if val>best:
                    best=val;winner=(e,f,w)
        theory=predicted(n)
        assert abs(best-theory)<=2e-11, (n,best,theory,winner)
        e,f,w=winner
        projection=direct_projected(n,e,f,w)
        assert abs(projection-theory)<1e-11,(n,projection,theory)
        if n<=17 or n in (18,22,25,31):
            base=4*math.sin(math.pi/n)**2
            for t in (1e-4,2e-5):
                L=laplacian(n,[(e,t*w),(f,t*(1-w))])
                eig=np.linalg.eigvalsh(L)
                assert abs(eig[1]-base-t*theory)<0.006*t,(n,t,eig[1],base,t*theory)
                fullspectra+=1
            # Any one added chord leaves the gap exactly unchanged.
            L=laplacian(n,[(e,2.7)])
            assert abs(np.linalg.eigvalsh(L)[1]-base)<1e-10,n
            fullspectra+=1
    # n=6 requires a near-diameter chord; best two diameters cannot compete.
    n=6;diams=[p for p in chord_list(n) if (p[1]-p[0])==3]
    best_diam=max(optimized_pair(n,a,b)[0] for i,a in enumerate(diams) for b in diams[i+1:])
    assert best_diam+0.1<predicted(n)
    print('VERIFY_OK: exhaustive_pairs=%d chord_edges=%d full_laplacian_spectra=%d n=4..32 all_three_residue_cases'% (pairs,edges,fullspectra))


if __name__=='__main__':
    main()
