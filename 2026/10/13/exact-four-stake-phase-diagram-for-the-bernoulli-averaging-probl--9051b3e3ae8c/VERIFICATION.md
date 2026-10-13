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

The theorem is a complete finite-dimensional analytic inequality, not an experimentally extrapolated statement. The proof checks every possible type of winning singleton and winning pair as a function of threshold \(t\). The gaps in the low-threshold strips factor as
\[
(3-s)p(1-p)^3,\qquad p(1-p)^2(1-2p),\qquad p(1-p)^2(2-3p),
\]
which are nonnegative under the relevant hypotheses. Above \(1/2\), the winning-edge graph is intersecting; above \(2/3\), three winning pair/triple conditions would force total stake greater than one. These combinatorial facts yield the global bounds.

Run the standard-library-only script `verify.py` for reproducibility. It enumerates selected rational stake simplex grids and Bernoulli parameters, computes all sixteen outcomes exactly, checks the five-piece sharp bound, and tests the four explicit attaining strategies and threshold endpoints.

A successful run prints a line beginning `VERIFY_OK cases=`. The finite grid verifies only sampled configurations. It is not an exhaustive check over all real stake vectors or parameters, and all unproved extensions to five or more positive stakes are excluded.
