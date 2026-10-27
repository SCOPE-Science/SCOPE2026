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

# Verification instructions and limits

The standalone file `verify.py` requires only Python 3 and its standard library. Run `python3 verify.py` and expect an output line beginning `VERIFY_OK`.

It checks, using exact arithmetic, the two claimed polynomial identities over \(\mathbb F_2\), each of the six complete base enumerations by an independent periodic-word loop, and the entire weight enumerator by binary Gaussian elimination on actual closed-neighborhood graph matrices for \(k=2,3\) and every admissible \(n\le80\), covering 150 graph instances. The matrix kernel is enumerated in its entirety for each instance, not sampled.

These finite tests verify the six boundary tables and provide an independent cross-check of the derivation. They do not alone establish the formula for unbounded \(n\). The proof derives the unbounded theorem from the exact shift-polynomial annihilator and unique decomposition into periods dividing \(h5^\delta\); this reasoning is stated in RESULT.md. No external independent validation is asserted.
