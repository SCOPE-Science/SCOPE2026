"""Exact finite-coefficient checks and asymptotic numerical diagnostics.

Standard-library-only checker for the neutral heterochaos baker correlation.
The infinite asymptotic theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb, sqrt, pi


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def killed_transition(n, j, k):
    """n-step fair walk on positive integers, killed at zero."""
    if (n + k - j) % 2:
        return Q(0)
    return Q(binom(n, (n + k - j) // 2) - binom(n, (n - k - j) // 2), 2**n)


def direct_exact(n):
    """Infinite wavelet sum reduced to finite sum plus exact geometric tail."""
    low = Q(0)
    for j in range(1, n + 1):
        for k in range(1, j + n + 1):
            low += Q(1, 2**(j+k)) * killed_transition(n, j, k)
    return low / 4 + Q(5**n, 12 * 16**n)


def generating_coefficients(N):
    """Algebraic generating function G=(1/3-t/(2-t))/(4-5z)."""
    t = [Q(0)] * (N + 1)
    for m in range((N - 1)//2 + 1):
        t[2*m+1] = Q(binom(2*m,m), (m+1)*2**(2*m+1))
    h = [Q(0)] * (N+1)
    g = [Q(0)] * (N+1)
    for n in range(N+1):
        if n:
            h[n] = (t[n] + sum((t[j]*h[n-j] for j in range(1, n+1)), Q(0)))/2
        d = (Q(1,3) if n == 0 else Q(0)) - h[n]
        g[n] = (d + (5*g[n-1] if n else Q(0))) / 4
    return g


def numeric_covariances(sample_times=(300,301,800,801)):
    max_n=max(sample_times)
    L=max_n+180
    vec=[-2.0**(-j-1) for j in range(1,L+1)]
    weights=vec.copy()
    out={}
    for n in range(max_n+1):
        if n in sample_times:
            v=sum(a*b for a,b in zip(weights,vec))
            lead=sqrt(2/pi)*(1+((-1)**n)/81)*n**(-1.5)
            out[n]=(v,lead,abs(v/lead-1))
        if n < max_n:
            nxt=[0.0]*L
            nxt[0]=vec[1]/2
            for i in range(1,L-1):
                nxt[i]=(vec[i-1]+vec[i+1])/2
            nxt[-1]=vec[-2]/2
            vec=nxt
    return out


def run():
    N=24
    gf=generating_coefficients(N)
    for n in range(N+1):
        assert gf[n]==direct_exact(n), (n,gf[n],direct_exact(n))
    assert gf[:4]==[Q(1,12),Q(1,24),Q(7,192),Q(5,192)]
    asym=numeric_covariances()
    for n,(_,_,error) in asym.items():
        assert error < 0.07, (n,error)
    print(f"PASS: {N+1} exact coefficient identities (algebraic vs reflected walks)")
    print("Initial covariances:",[(i,str(gf[i])) for i in range(7)])
    print("Large-time numerical consistency:",asym)
    print("NOTE: infinite-series identity and asymptotic singularity transfer need the analytic proof.")


if __name__=='__main__':
    run()
