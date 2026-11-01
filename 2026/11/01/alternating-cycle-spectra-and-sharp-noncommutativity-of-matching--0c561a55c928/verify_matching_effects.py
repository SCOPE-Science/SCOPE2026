"""Reproducible checks for pair-matching Parseval-frame commutators.

Requires Python 3 and NumPy. Tests are finite corroboration of the analytic proof.
"""
import math
from functools import lru_cache
import numpy as np

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    u = vertices[0]
    return tuple(((u, v),) + tail for j, v in enumerate(vertices[1:])
                 for tail in matchings(vertices[1:j+1]+vertices[j+2:]))

def swap_matrix(n, match):
    S = np.zeros((n, n), dtype=np.int64)
    for a, b in match:
        S[a, b] = S[b, a] = 1
    return S

def lengths_by_alternation(n, ma, mb):
    a = {x:y for x,y in ma for x,y in ((x,y),(y,x))}
    b = {x:y for x,y in mb for x,y in ((x,y),(y,x))}
    seen = set()
    out = []
    for v in range(n):
        if v in seen:
            continue
        stack = [v]
        comp = set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend((a[x], b[x]))
        seen |= comp
        assert len(comp)%2==0
        out.append(len(comp)//2)
    assert sum(out)==n//2
    return out

def predicted_spectrum(n, lengths):
    vals = []
    for k in lengths:
        for j in range(k):
            vals.extend([2*math.sin(2*math.pi*j/k)/(n-2)**2]*2)
    vals.remove(next(t for t in vals if abs(t)<1e-12))  # remove constant mode
    return sorted(vals)

def predicted_norm(n, lengths):
    return max(abs(2*math.sin(2*math.pi*j/k)/(n-2)**2)
               for k in lengths for j in range(k))

def count_commuting(m):
    return sum(math.factorial(m)//(math.factorial(m-2*t)*math.factorial(t))
               for t in range(m//2+1))

def count_maximizing(m):
    # Integer recurrence for the labelled component assembly on m base pairs.
    @lru_cache(None)
    def rec(remaining, has_eight_multiple):
        if remaining==0:
            return int(has_eight_multiple)
        # component containing a distinguished base pair, with k vertices total.
        ans = 0
        for k in range(1,remaining+1):
            options = 1 if k==1 else 2**(k-1)*math.factorial(k-1)
            ans += math.comb(remaining-1,k-1)*options*rec(remaining-k,has_eight_multiple or k%4==0)
        return ans
    return rec(m,False)


def verify(n, spectral=True):
    ma=tuple((2*i,2*i+1) for i in range(n//2))
    SM=swap_matrix(n, ma)
    J=np.ones((n,n),dtype=np.int64)
    A=n*(np.eye(n,dtype=np.int64)+SM)-2*J
    I=np.eye(n)
    total=0
    comm=0
    maximizing=0
    for mb in matchings(tuple(range(n))):
        SB=swap_matrix(n,mb)
        B=n*(np.eye(n,dtype=np.int64)+SB)-2*J
        C=A@B-B@A
        # The exact integer identity, independent of numerical eigensolvers.
        assert np.array_equal(C,n*n*(SM@SB-SB@SM))
        lens=lengths_by_alternation(n,ma,mb)
        should_zero=all(k<=2 for k in lens)
        assert (not np.any(C)) == should_zero
        actual_max=any(k%4==0 for k in lens)
        comm += should_zero
        maximizing += actual_max
        if spectral:
            obs=list(np.linalg.eigvalsh(1j*C.astype(float)/(n*n*(n-2)**2)))
            obs.pop(next(j for j,x in enumerate(obs) if abs(x)<1e-12))
            obs=np.array(sorted(obs))
            # i*C has real spectrum = -imaginary part for C's imaginary spectrum.
            expected=np.array(predicted_spectrum(n,lens))
            assert np.allclose(obs,expected,atol=2e-10), (n,ma,mb,lens,obs,expected)
            norm=predicted_norm(n,lens)
            assert np.isclose(np.max(abs(obs)),norm,atol=1e-10)
        total+=1
    assert total==math.prod(range(n-1,0,-2))
    assert comm==count_commuting(n//2), (n,comm,count_commuting(n//2))
    assert maximizing==count_maximizing(n//2), (n,maximizing,count_maximizing(n//2))
    if n>=8:
        assert maximizing>0
    else:
        assert maximizing==0
    print(f'n={n} total={total}, commuting={comm}, maximizing={maximizing}, spectra={spectral}')


def verify_frame(n):
    V=np.eye(n)-np.ones((n,n))/n
    S=np.zeros((n,n))
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            v=(V[:,i]+V[:,j])/math.sqrt(n-2)
            S+=np.outer(v,v)
            edges.append((i,j,v))
    assert np.allclose(S,V,atol=1e-12)
    M=tuple((2*i,2*i+1) for i in range(n//2))
    D=sum((np.outer(v,v) for i,j,v in edges if (i,j) in M),start=np.zeros((n,n)))
    SM=swap_matrix(n,M)
    exact=(np.eye(n)+SM-2*np.ones((n,n))/n)/(n-2)
    assert np.allclose(D,exact,atol=1e-12)
    assert np.allclose(D@D,2/(n-2)*D,atol=1e-12)

if __name__=='__main__':
    for n in (4,6,8,10):
        verify_frame(n)
        verify(n,spectral=True)
    for n in (12,):
        verify_frame(n)
        verify(n,spectral=False)
    print('VERIFICATION_OK')
