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
# Verification

The theorem is analytic. The accompanying script uses exact rational arithmetic.

For every tested \(n\), it verifies the three pointwise certificates on the entire parity lattice:
\[
r\ge\frac{r^2}{n},
\qquad
r\ge\frac{r^2+n}{n+1},
\qquad
r\le\frac{r^2+ab}{a+b},
\]
using the appropriate lower certificate for the parity of \(n\).

It constructs the lower and upper endpoint laws for \(|S|\), symmetrizes them, converts to
\[
K=\frac{n+S}{2},
\]
and checks exactly
\[
\mathbb E K=\frac n2,
\qquad
\mathbb E[K(K-1)]=\frac{n(n-1)}4.
\]

For moderate \(n\), the script also enumerates every feasible two-point law on the absolute-sum parity lattice with second moment \(n\) and confirms the claimed extrema.

Finite enumeration is a replay, not the proof of the universal theorem.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK pointwise_checks=12509998 construction_checks=9998 extreme_pair_checks=299 feasible_pair_laws=151864`.
