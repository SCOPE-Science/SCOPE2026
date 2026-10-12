"""Independent finite-dimensional checks for the Dicke amplitude-damping QFI formula."""
from itertools import combinations
from math import comb
import numpy as np


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def lam(n, k, s, j, p):
    r = k - s
    if not (0 <= s <= k and 0 <= j <= min(s, n-s, r, n-r)):
        return 0.0
    return (p**r * (1-p)**s / comb(n,k)
            * comb(n-s-j, r-j) * comb(n-r-j, s-j))


def fast_qfi(n,k,p):
    result = 0.0
    for s in range(n):
        for j in range(min(s,n-s-1)+1):
            left, right = lam(n,k,s,j,p), lam(n,k,s+1,j,p)
            if left + right > 1e-14:
                d = comb(n,j)-choose(n,j-1)
                result += (d * (s+1-j)*(n-s-j)
                           * (left-right)**2/(left+right))
    return result


def dense_qfi(n,k,p):
    dim = 1<<n
    indices = [i for i in range(dim) if i.bit_count()==k]
    rho = np.zeros((dim,dim),dtype=float)
    for x in indices:
        for y in indices:
            common = x & y
            mask = common
            while True:
                loss_count = mask.bit_count()
                rho[x ^ mask, y ^ mask] += (p**loss_count
                        * (1-p)**(k-loss_count) / len(indices))
                if mask == 0: break
                mask = (mask-1) & common
    assert abs(np.trace(rho)-1)<1e-12
    generator = np.zeros_like(rho)
    for x in range(dim):
        for i in range(n):
            generator[x, x^(1<<i)]+=0.5
    eig, vectors = np.linalg.eigh(rho)
    G = vectors.T @ generator @ vectors
    total=0.0
    for a in range(dim):
        for b in range(dim):
            if eig[a]+eig[b]>1e-12:
                total += 2*(eig[a]-eig[b])**2/(eig[a]+eig[b])*G[a,b]**2
    return total


def incidence_spectrum(n,k,s,p):
    r=k-s
    if r<0: return True
    ss = list(combinations(range(n),s))
    rr = list(combinations(range(n),r))
    B=np.array([[int(not (set(S)&set(R))) for R in rr] for S in ss],dtype=float)
    actual=np.linalg.eigvalsh((p**r*(1-p)**s/comb(n,k)) * (B @ B.T))
    expected=[]
    for j in range(min(s,n-s)+1):
        expected.extend([lam(n,k,s,j,p)]*(comb(n,j)-choose(n,j-1)))
    assert len(expected)==len(actual)
    return np.max(abs(actual-np.sort(expected)))<1e-10


def main():
    qfi_cases=0
    maximum_error=0.0
    for n in range(3,8):
        for k in range(2,n):
            for p in (0.0,0.2,0.53,0.9,1.0):
                err=abs(fast_qfi(n,k,p)-dense_qfi(n,k,p))
                maximum_error=max(maximum_error,err)
                assert err<1e-9,(n,k,p,err)
                qfi_cases+=1
    Gram_cases=0
    for n in range(4,9):
        for k in range(2,n):
            for s in range(k+1):
                assert incidence_spectrum(n,k,s,0.37),(n,k,s)
                Gram_cases+=1
    endpoints=0
    for n in range(4,24):
        for k in range(2,n):
            assert abs(fast_qfi(n,k,0)-n-2*k*(n-k))<1e-8
            assert abs(fast_qfi(n,k,1)-n)<1e-8
            endpoints+=1
    assert abs(fast_qfi(8,4,0.5)-4.0)<1e-10
    late_slope=0
    for n,k in ((4,2),(5,3),(8,4),(12,5)):
        survival=1e-7
        measured=(fast_qfi(n,k,1-survival)-n)/survival
        expected=-2*k*(n-k+2)
        assert abs(measured-expected)<1e-3,(n,k,measured,expected)
        late_slope+=1
    print('VERIFY_OK dense_qfi=%s inclusion_spectra=%s endpoints=%s late_slope=%s max_error=%.3g'
          %(qfi_cases,Gram_cases,endpoints,late_slope,maximum_error))

if __name__=='__main__':
    main()
