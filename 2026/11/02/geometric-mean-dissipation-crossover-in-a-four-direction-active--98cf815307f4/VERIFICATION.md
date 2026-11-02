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
# Reproduction and verification

The analytic result is established by stationary generator identities, the entropy balance for symmetric jump rates, exact matrix resolvents, and rational sign factorization in `RESULT.md`. These are the universal proof, rather than empirical extrapolations.

The included standalone `verify.py` requires only Python 3. Run `python3 verify.py` in the directory containing this file. Its independent \(8\times8\) linear-system solver computes the four orientation-conditioned stationary position means and the entropy-flux observable directly for 500 deterministic parameter sets. Three hundred independent exact-rational parameter sets compare the determinant-factorization and flatness identities; further boundary, orientation and geometric-mean cases check the claimed signs and invariance. The actual execution reported: `PASS: 1119 reproducible numerical and exact-rational assertions.`

The independent state-conditioned moment calculation is finite-dimensional and exact in model form; floating arithmetic is used only to corroborate it. The universal uniqueness and sign conclusions follow by the displayed positive-denominator factorization and strict monotonicity on the open angular interval, not from finite tests. No statistical parameter-identification error bars, finite-measurement stability bounds, or external scientific audit are claimed.
