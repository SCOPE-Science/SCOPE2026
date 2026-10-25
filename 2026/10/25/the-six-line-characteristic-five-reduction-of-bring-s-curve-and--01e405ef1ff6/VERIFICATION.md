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

# Reproducible verification

From a directory containing the included files, install the declared dependency with `python -m pip install -r requirements.txt`, then run `python bring5_verify.py`. Successful exact checks print `VERIFY_OK` and `CONDUCTOR_OK`.

The standalone checker uses polynomial arithmetic modulo five, enumerates the six projective intersections and all 31 \(\mathbb F_5\)-points, computes the \(S_5\)-orbit stabilizer, and checks evaluation rank through degree four. All checks were executed successfully before this package was assembled.

These computations do not constitute an exhaustive check of all geometric points over an algebraic closure or a proof of flatness. Those conclusions depend on the explicit factorization/Bezout, exact Hilbert-series and regular-sequence arguments in the main result. The conductor proof additionally uses the transitive component action to exclude low-degree coordinate idempotents.

Scientific limitations include possible equivalent treatments under different coordinates and absence of independent verification.
