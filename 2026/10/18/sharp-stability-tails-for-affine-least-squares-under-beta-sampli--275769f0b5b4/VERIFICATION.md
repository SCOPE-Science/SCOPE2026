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

Run `python verify.py` with Python 3, NumPy and SciPy installed. The recorded output is embedded in `verification_output.txt` and can be regenerated from the code, which uses a fixed deterministic seed.

The checker reconstructs \(G_n\), its trace and determinant, tests the exact small-eigenvalue/tube-event equivalence against explicit Gram eigenvalues, verifies leading uniform-sampling coefficients, checks the analytically derived two-point corner constant, and simulates two million independent three-point samples as a coarse tail sanity check. Direct quadrature in dimension two independently checks the large-threshold normalization. The analytic proof, not finite simulation or recorded output, establishes the asymptotic regimes, infinite moments and all-parameter quantifiers.

Known limits: the two-million-draw experiment is subject to Monte Carlo error and finite-threshold bias; no numerical experiment proves exactness for every \(n,\alpha,\beta\). The originality and value assessments are internal scientific reviews only, not independent certification.
