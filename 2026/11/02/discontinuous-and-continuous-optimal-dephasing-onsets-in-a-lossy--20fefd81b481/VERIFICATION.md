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

# Reproducibility checks and limits

Run `python check.py` from this same directory with SymPy, NumPy, and SciPy installed. The program constructs the nine-component Hermitian integrated-density equations and checks the displayed mean-time formula and seven density-matrix identities by exact symbolic simplification. It independently constructs the full complex \(9\times9\) Liouvillian, solves its resolvent numerically for 96 sampled parameter triples, and checks complete positivity at multiple times. It checks the derivative and threshold factorizations symbolically and tests 56 parameter configurations around the global threshold, including coexistence points. The entire program returned `TOTAL all checks PASS` when executed from the actual artifact path.

The reproducibility program is a diagnostic rather than a formal computer-assisted proof. Positivity of the capture-time mean, uniqueness of optimizer, behavior at the exact transition, and the sharp branch boundary follow from the analytic algebra and sign arguments in `RESULT.md`; finite random tests cannot establish them for all real parameter values. The numerical resolvents corroborate normalization and sink conventions but do not model experimentally correlated noise, finite temperature, or perturbations outside the specified generator. No independent external review or certification was performed.
