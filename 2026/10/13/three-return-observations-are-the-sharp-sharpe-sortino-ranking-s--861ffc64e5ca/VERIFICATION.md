---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The proof uses exact finite-sample formulas.

For two observations, every admissible return sample has the form
\[
(-a,b),
\qquad
0<a<b.
\]
Writing
\[
r=\frac ba,
\]
the population-standard-deviation Sharpe ratio is
\[
S=\frac{r-1}{r+1},
\]
and lower-partial-second-moment Sortino is
\[
Q=\frac{r-1}{\sqrt2}.
\]
Both are strictly increasing in \(r\), proving the support-two obstruction.

For the sharp witness
\[
A=(-1,1,9),
\qquad
B=(-2,5,6),
\]
the embedded verifier checks
\[
\mu(A)=\mu(B)=3,
\]
\[
\sigma_A^2=\frac{56}{3},
\qquad
\sigma_B^2=\frac{38}{3},
\]
\[
S(A)^2=\frac{27}{56},
\qquad
S(B)^2=\frac{27}{38},
\]
and
\[
Q(A)^2=27,
\qquad
Q(B)^2=\frac{27}{4}.
\]

It separately checks the denominator convention that averages downside squares only over below-target observations.

Padding both samples with their common mean gives, for every \(n\ge3\),
\[
\sigma^2(A_n)=\frac{56}{n},
\qquad
\sigma^2(B_n)=\frac{38}{n},
\]
and
\[
\delta^2(A_n)=\frac1n,
\qquad
\delta^2(B_n)=\frac4n.
\]

Run:

`python3 verify_sharpe_sortino_minimal_support.py`

The first output line must be:

`VERIFY_OK`

The script replays the persistent family through \(n=500\). The universal support-two obstruction and all-\(n\) formulas are proved algebraically in `RESULT.md`.
