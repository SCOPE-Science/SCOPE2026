# Certified type-(5,5) rational approximant to |x-1/2| on [-1,1] with uniform error below 0.01

## Statement

Let \(f(x)=|x-1/2|\) on \([-1,1]\). There is an explicit real rational function
\(r(x)=P(x-1/2)/Q(x-1/2)\), with \(\deg P=\deg Q=5\), no pole on the interval, and

\[
\|f-r\|_{\infty,[-1,1]} \le 0.00878495 < 0.01.
\]

Consequently \(E_{5,5}(f)\le 0.01\).

With \(t=x-1/2\), use ascending coefficients

\[
P(t)=\sum_{k=0}^5 p_k t^k,\qquad
Q(t)=\sum_{k=0}^5 q_k t^k,
\]

where

`p = (5165/588261, -29350/900759, 5123448/301135, -3363915/284231, 116388085/763311, 4583207/428422)`

and

`q = (1, -980828/725017, 67281667/791723, -21172161/949118, 78611567/924091, 21943815/890896)`.

## Exact certificate

The certificate uses only rational arithmetic.

1. On 40,001 equally spaced nodes of \([-3/2,1/2]\), the smallest value of \(Q\) is
   0.9946050566757593... . The global derivative majorant
   \(\sum_{k=1}^5 k|q_k|(3/2)^{k-1}\), multiplied by half a grid spacing, gives the rigorous global lower bound
   \(Q(t)\ge 0.9401355692097929...>0\).

2. Split \([-3/2,1/2]\) into 2,000 cells, with the kink \(t=0\) at a cell boundary.
   On each smooth cell write
   \[
   E(t)=P(t)/Q(t)-|t|,\quad
   E''(t)=U(t)/Q(t)^4,
   \]
   where \(W=P'Q-PQ'\) and \(U=W'Q^2-2WQQ'\).
   Exact Taylor-shift majorants bound \(|E''|\) on each cell.
   The largest exact endpoint error is 0.00878086268557671... at \(t=0.139\);
   the largest Taylor correction is 0.00000408718046788004... .
   Their sum is 0.00878494986604459... .

The independent audit of 2026-09-29 replayed these two bounds from the printed rational coefficients.

## Reproducibility

Run `artifacts/verify_certificate.py`; it reads `artifacts/candidate_exact.json`.
Both files are committed in this record.

## Scope and literature context

This is a finite certified threshold witness, not an optimality theorem. The approximant was found numerically and then certified exactly; no matching lower bound for \(E_{5,5}\) is asserted.

Rational approximation of absolute-value functions is classical. Chebfun explicitly demonstrates rational minimax approximation of the same shifted function `abs(x-0.5)` at type (8,8), and separately treats high-degree minimax approximation of `abs(x)`. Those sources do not supply the rational coefficients or exact type-(5,5) certificate above. The record therefore makes only the narrow certified finite-type claim and no broad priority claim.

## References

- D. J. Newman, “Rational approximation to |x|,” Michigan Math. J. 11 (1964).
- H. Stahl, work on best uniform rational approximation and root-exponential asymptotics.
- Chebfun, “Best approximation with the REMEZ command,” rational example for `abs(x-0.5)`.
- S. Filip, Y. Nakatsukasa, N. Trefethen, Chebfun example “Rational approximation of abs(x) with minimax.”
