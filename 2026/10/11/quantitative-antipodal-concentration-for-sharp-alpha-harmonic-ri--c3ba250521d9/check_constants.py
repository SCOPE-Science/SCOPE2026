#!/usr/bin/env python3
"""Finite consistency checks for gamma/hypergeometric normalizations; not a proof."""
from mpmath import mp
mp.dps = 60
cases = [(2, 0), (2, mp.mpf('0.75')), (3, mp.mpf('-0.5')),
         (3, 0), (5, 2), (8, mp.mpf('-0.9'))]
for n, alpha in cases:
    assert alpha > max(-1, -(n-1)/2)
    cn = mp.gamma((n+alpha)/2) * mp.gamma(1+alpha/2) / (mp.gamma(n/2)*mp.gamma(1+alpha))
    Rn = mp.gamma(n/2)/(mp.sqrt(mp.pi)*mp.gamma((n-1)/2))
    b0 = mp.beta(mp.mpf(n-1)/4, (alpha+1+mp.mpf(n-1)/2)/2)
    a = -(alpha+mp.mpf(n-1)/2)/2
    b = -(alpha+1)/2
    c = mp.mpf(n+1)/4
    F1 = mp.hyp2f1(a,b,c,1)
    Fq = mp.hyp2f1(a,b,c,mp.mpf(1)/4)
    A_exact = cn * Rn * mp.beta(mp.mpf(n-1)/4, mp.mpf(1)/2) * F1
    A = cn*Rn*mp.power(2,alpha+mp.mpf(n-1)/2)*b0
    B = cn*mp.power(2,alpha+mp.mpf(n-1)/2-1)*b0
    C = mp.power(2,2*alpha+n-2)*cn**2*Rn*b0**2
    tol = mp.mpf('1e-45')
    assert abs(A/A_exact-1) < tol, (n,alpha,'A')
    assert abs(A*B/C-1) < tol, (n,alpha,'AB')
    assert F1 > Fq > 0, (n,alpha,'F')
    delta = mp.mpf(1)/2
    k = 4*A*cn/(3*mp.power(2,n+alpha))*(1-Fq/F1)*(
       delta**2*(1-delta**2/4))**(mp.mpf(n-1)/4)
    assert k>0, (n,alpha,'kappa')
    print(f'n={n}, alpha={alpha}, F(1/4)/F(1)={mp.nstr(Fq/F1,14)}, kappa(1/2)={mp.nstr(k,14)}')
print('PASS: six finite consistency cases. Universal proof is analytic.')
