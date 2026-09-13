# Star-discrepancy rate for normalized cubic residues, p = 7 mod 12

## Context

For a prime p with 3 | (p-1), let C_p be the subgroup of nonzero cubic residues
mod p and E_p the one-dimensional star-discrepancy of the point set {h/p : h in C_p}
in [0,1]. The admitted target asked for a two-sided sqrt(p)-rate: an upper bound
E_p <= C p^{-1/2} log p for all large p = 7 mod 12, and a lower bound
E_p >= c p^{-1/2}/log p for infinitely many such p. This record resolves both halves,
the lower half in a stronger log-free form.

## Definitions

Let p be prime, p = 7 mod 12. Then 3 | (p-1) and N_p = (p-1)/3 is even.
Define C_p = {1 <= h < p : h^{(p-1)/3} = 1 mod p}, |C_p| = N_p, and

E_p = sup_{0<=t<=1} | (1/N_p) #{h in C_p : h/p <= t} - t |.

Let chi be a multiplicative character of order 3 mod p, tau(chi) its Gauss sum,
e_p(u) = exp(2 pi i u/p), and S_k = (1/N_p) sum_{h in C_p} e_p(kh) for p not dividing k.

## Result

There exist absolute constants C, c > 0 and P_0 such that for every prime
p >= P_0 with p = 7 mod 12,

E_p <= C (log p)/sqrt(p),

and for infinitely many primes p = 7 mod 12,

E_p >= c/sqrt(p).

In particular both halves of the admitted target hold; the lower bound is stronger
than required (c/sqrt(p) versus c/(sqrt(p) log p)).

## Proof / evidence

Upper half. On F_p^x, 1_{C} = (1 + chi + chi^2)/3, so
N S_k = (-1 + chi-bar(k) tau(chi) + chi(k) tau(chi-bar))/3, and |tau| = sqrt(p)
gives |S_k| <= 4/sqrt(p) for p >= 25. The Erdos-Turan inequality
E_p <= 6/(m+1) + (4/pi) sum_{k<=m} |S_k|/k with m = floor(sqrt(p)) yields
E_p <= C_0 (log p)/sqrt(p). The congruence condition is not needed here.

Lower half. Koksma's inequality applied to cos/sin gives E_p >= |S_h|/(8|h|) for
h != 0. Since (p-1)/3 is even, chi(-1) = 1, so C = -C and the periods N S_k are real:
with tau = r e^{i theta}, r = sqrt(p), the three values are (-1+2t)/3 etc. for
t = r cos theta and its +-2pi/3 shifts, satisfying t^2+u^2+v^2 = 3r^2/2.
Hence if 2 is a cubic non-residue mod p, max(|N S_1|,|N S_2|) >= sqrt(p)/4.
Chebotarev in L = Q(zeta_12, cbrt(2)) (degree 12 over Q) gives infinitely many
p = 7 mod 12 with 2 a cubic non-residue (a nonempty union of Frobenius classes of
density >= 1/12). For each, E_p >= max(|S_1|/8,|S_2|/16) >= c/sqrt(p), e.g. c = 1/200.

Numerical verification (supporting only): for all 108 primes p = 7 mod 12 below 3000,
E_p sqrt(p) lies in [0.43, 1.19], the Koksma and dichotomy inequalities hold with no
violations, and ~65% have 2 as a cubic non-residue, consistent with the fiber prediction
of 2/3. Script: output/artifacts/verify_numerics.py.

## Limitations

Constants C, c = 1/200 and threshold P_0 are not optimized. The Chebotarev fiber
computation is condensed; a referee may ask for the explicit Galois action to be
spelled out. Numerics below 3000 are verification only and do not replace the proof.
No claim is made outside p = 7 mod 12 or for higher power residues.

## Reproducibility

Recompute E_p and N S_k directly from the definitions using pow(h,(p-1)//3,p) == 1,
then check E_p >= max(|S_1|/8, |S_2|/16) and the dichotomy bound. Run
python3 output/artifacts/verify_numerics.py (requires sympy) to reproduce the
p < 3000 checks.

## References

Kuipers and Niederreiter, Uniform Distribution of Sequences (Erdos-Turan Thm 2.5,
Koksma inequality); standard Gauss-sum bound |tau(chi)| = sqrt(p); Chebotarev density
theorem applied to Q(zeta_12, cbrt(2)); Gaussian-period background; fused literature
search (Serpent/OpenAlex/Crossref/OpenAIRE) located no prior stating this two-sided rate.
