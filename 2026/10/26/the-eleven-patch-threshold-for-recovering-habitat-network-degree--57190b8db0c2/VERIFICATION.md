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

# Exact reproducibility

Execute `python3 verify_fragment.py` with Python 3.9 or later, using the Python standard library. Compare stdout to `verification_certificate.json` as JSON objects; the order of keys is not significant.

The program checks two eleven-vertex trees, enumerating all 2,048 possible retained-vertex configurations for each; compares their resulting exact quota-count polynomials with the formula independently derived from edge endpoint degrees; verifies the degree census, all degree-sum counts, and the primitive discrepancy vector; and checks 1,309 labeled subcubic Prüfer trees up to six vertices against the inversion formulas. It also verifies the common mean \(59/128\) at \(p=1/2\) and exact agreement at five rational survival parameters.

The analytic proof of the full-degree reconstruction, the one-dimensional ambiguity space, and the global eleven-vertex lower bound is in `RESULT.md`. Finite tests are additional guards, not substitutes for unbounded proofs. Source comparisons are not independent novelty certification.
