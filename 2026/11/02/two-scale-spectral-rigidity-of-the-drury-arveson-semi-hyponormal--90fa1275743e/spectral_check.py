"""Finite-block reproducibility checks for the Drury–Arveson semi-hyponormality defect.

Requires Python 3 and NumPy.  No finite test replaces the proof for all degrees.
"""
import math
import itertools
import numpy as np


def indices(d, n):
    if d == 1:
        return [(n,)]
    return [(i,) + v for i in range(n + 1) for v in indices(d - 1, n - i)]


def degree_shift(d, n, i):
    source, target = indices(d, n), indices(d, n + 1)
    positions = {a: j for j, a in enumerate(target)}
    a = np.zeros((len(target), len(source)))
    for j, b in enumerate(source):
        c = list(b)
        c[i] += 1
        a[positions[tuple(c)], j] = math.sqrt((b[i] + 1)/(n + 1))
    return a


def matrices(d, n):
    h = math.comb(n + d - 1, d - 1)
    shifts_next = [degree_shift(d, n, i) for i in range(d)]
    shifts_prev = [degree_shift(d, n - 1, i) for i in range(d)] if n else None
    L = np.zeros((d*h, d*h))
    R = np.zeros_like(L)
    for i in range(d):
        for j in range(d):
            L[i*h:(i+1)*h,j*h:(j+1)*h] = shifts_next[j].T @ shifts_next[i]
            if n:
                R[i*h:(i+1)*h,j*h:(j+1)*h] = shifts_prev[i] @ shifts_prev[j].T
    return L,R


def spectral_check():
    assertions=0
    for d,max_n in ((2,8),(3,6),(4,4),(5,3)):
        for n in range(max_n + 1):
            L,R=matrices(d,n)
            size=L.shape[0]
            assert size == d*math.comb(n+d-1,d-1)
            assertions+=1
            if n:
                assert np.max(np.abs(L-(np.eye(size)+n*R)/(n+1))) < 4e-14
                assertions+=1
            else:
                assert np.allclose(L,np.eye(d)) and np.allclose(R,0)
                assertions+=1
            evl,Ql=np.linalg.eigh(L)
            evr,Qr=np.linalg.eigh(R)
            assert np.min(evl)>-5e-14 and np.min(evr)>-5e-14
            assertions+=1
            sqrtL=(Ql*np.sqrt(np.maximum(evl,0)))@Ql.T
            sqrtR=(Qr*np.sqrt(np.maximum(evr,0)))@Qr.T
            actual=np.linalg.eigvalsh(sqrtL-sqrtR)
            if n:
                h_prev=math.comb(n+d-2,d-1)
                positive=(n+1)**(-0.5)
                negative=math.sqrt((n+d)/(n+1))-math.sqrt((n+d-1)/n)
                expected=np.array([negative]*h_prev+[positive]*(size-h_prev))
            else:
                expected=np.ones(d)
            assert np.max(np.abs(actual-expected))<2e-7, (d,n,actual,expected)
            assertions+=1
            if n:
                assert negative<0 and positive>0
                assertions+=1
    for d in range(2,11):
        for n in range(1,100):
            hn=math.comb(n+d-1,d-1)
            hprev=math.comb(n+d-2,d-1)
            assert d*hn-hprev>0
            assertions+=1
    print(f'PASS {assertions} independent finite degree, dimension, and multiplicity assertions')


if __name__=='__main__':
    spectral_check()
