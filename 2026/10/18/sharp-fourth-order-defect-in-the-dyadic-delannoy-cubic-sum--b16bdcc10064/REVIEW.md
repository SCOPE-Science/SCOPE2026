# Independent mathematical audit

## correctness

PASS

PASS — Reconstructed from central Delannoy D_m=sum 2^j binom(m,j)^2 and S_n=sum_{m<n}(-1)^m(2m+1)^3D_m with n=2^r,r>=1. Verified the telescoping recurrence gives S_n=n(1-4n²)(D_n+D_{n-1})/4+n²(D_n-D_{n-1}) for even n. The uniformly convergent 2-adic interpolation d(x)=sum_j 2^j binom(x,j)^2 equals D_x at nonnegative integers, and the extended recurrence with d(-1)=-1 proves d(-n)=-D_{n-1}. The identity d(x)=1+x² sum_{j>=1}(2^j/j²)binom(x-1,j-1)^2 gives Y_n=D_n-D_{n-1}=d(n)+d(-n)=2 mod n². For X_n=D_n+D_{n-1}, Vandermonde expansion A_j=binom(n-1,j-1), B_j=binom(-n-1,j-1), and nu2 binom(2n,t)=r+1-nu2(t), with the extra A_j+B_j even, kill all layers modulo 4n except j=4; the finite j>n tail bound treats r=2,j=8 explicitly. The exceptional polynomial A4²-B4²= -2n(n²+1)(n²+11)/3 is 2n mod 4n. Thus X_n=2n³ mod 4n³, nu2 X_n=3r+1; combine with Y_n congruence to obtain nu2(S_n-2n²)=4r-1. The r=1 base n=2 is checked separately. Independent recurrence and exact sums n2..512 reproduced error ν2=4r−1 and adjacent ν2=3r+1 for r1..9, but infinite claim rests on valuation bounds.

## originality

PASS

PASS — Guo–Zeng (2012) Conjecture3.3 proposes only S_n=2n² modulo n³ at dyadic n. Wang–Zhong (2025) Theorem1.3 proves the existing modulo-n³ conjecture and Theorem3.1 contains weaker adjacent-Delannoy congruences. The new exact 2-adic valuation 4r−1 and X_n adjacent valuation 3r+1 are strictly more precise: modulo n³ at n=2^r is much weaker than the exact 2^{4r} sharp correction. No stronger same-object statement found in inspected primary sections or published Resultary matches.

## value

PASS

PASS — An exact sharp p-adic defect of a classical central Delannoy cubic moment is a natural arithmetic refinement of a previously posed and solved congruence. It identifies the first nonvanishing bit and a structural adjacent-value valuation, not merely a tiny finite table or reproduction of the old theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
