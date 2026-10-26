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

# Verification of the finite-field bitangent classification

The mathematical proof in `RESULT.md` gives explicit line families, a square-of-a-quadratic identity, an exhaustive geometric count by the 28 odd theta characteristics, and an exact Frobenius calculation. The computation below is an independent finite test of the rational-line counts and of the elementary sixteen-case cycle table, not an infinite-field certification.

Run `python3 verify_diagonal_bitangents.py` with the Python standard library. It enumerates all projective lines over odd prime fields \(p\in\{3,5,7,11,13,17,19,23,29,31,37\}\), for every coefficient fourth-power class triple. The actual test criterion is whether the quartic restricted to a line is a scalar square of a binary quadratic. It compares the result with the theorem's fourth-root formula. A second implementation over \(\mathbb F_9\), represented as \(\mathbb F_3[i]\) with \(i^2=-1\), tests all 64 coefficient-class triples independently. The program checks each sixteen-pair Frobenius classification against its stated distinct cycle profiles. It returns `VERIFY_OK` and `GF9_VERIFY_OK` if all assertions succeed.

All required computations were executed successfully on the embedded program. There is no claim that finite checks exhaust every odd prime power. Independent audit: not performed.
