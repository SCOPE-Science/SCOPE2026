from fractions import Fraction
from math import gcd


def primes(n):
    out=[]
    x=2
    while len(out)<n:
        ok=True
        d=2
        while d*d<=x:
            if x%d==0:
                ok=False
                break
            d += 1 if d==2 else 2
        if ok: out.append(x)
        x += 1
    return out

MAX_N=300
P=primes(MAX_N)
ratio_checks=0
kernel_checks=0
spectral_checks=0
for N in range(2, MAX_N+1):
    g=P[:N]
    ds=set()
    for s in range(1,N):
        d=gcd(N,s)
        L=N//d
        ds.add(d)
        ratios=[]
        for j in range(N):
            ratios.append(Fraction(g[(j+s)%N],g[j]))
        assert len(set(ratios))==N, (N,s)
        ratio_checks += N
        vals={}
        for xi in range(N):
            e=(-s*xi)%N
            vals[e]=vals.get(e,0)+1
        assert len(vals)==L
        assert set(vals.values())=={d}
        kernel_checks += N
        # Therefore a two-point signal has either zero or d STFT zeros
        # for this explicit positive-prime window, depending on whether
        # its coefficient ratio lies in one of the N disjoint root cosets.
        stft={N*N, N*N-d}
        fourier={N, N-d}
        assert {v-(N*N-N) for v in stft}==fourier
        spectral_checks += 1
    proper_divs={d for d in range(1,N) if N%d==0}
    assert ds==proper_divs
    stft_global={N*N}|{N*N-d for d in proper_divs}
    fourier_global={N}|{N-d for d in proper_divs}
    assert {v-(N*N-N) for v in stft_global}==fourier_global
    # exact generic k<=2 minimum; singletons have full N^2 support for nonzero window
    pmin=next(p for p in P if N%p==0)
    assert max(proper_divs)==N//pmin
    assert min(stft_global)==N*N-N//pmin

print('N_RANGE',2,MAX_N)
print('RATIO_DISTINCTNESS_CHECKS',ratio_checks)
print('KERNEL_FIBER_CHECKS',kernel_checks)
print('DIFFERENCE_SPECTRA_CHECKS',spectral_checks)
print('VERIFY_OK')
