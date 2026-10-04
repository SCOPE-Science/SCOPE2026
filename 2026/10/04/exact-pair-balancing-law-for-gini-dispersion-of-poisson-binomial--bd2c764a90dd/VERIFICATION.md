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

The theorem is analytic. The accompanying `verify_poisson_binomial_gini.py` uses exact rational arithmetic. It convolves Poisson-binomial mass functions, computes \(\Delta\) directly, and checks
\[
4(	ilde r-r)\left[(c_0-c_1)(s-r-	ilde r)+c_1ight]
\]
against the observed transfer. It also checks \(c_1\le c_0\), strict increase under genuine balancing, the CDF representation, and endpoint formulas on exhaustive small rational grids.

Replay result: `VERIFY_OK increment_checks=10241 autocorrelation_checks=238 strict_checks=8722 cdf_checks=990 grid_groups=138 grid_vectors=2776`.

Finite enumeration is supplementary; the universal theorem is the symbolic proof in `RESULT.md`.

Independent audit has not been performed.
