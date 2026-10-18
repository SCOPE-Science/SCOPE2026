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

# Exact reproduction and limitations
Run `python3 verify.py` (uses only Python standard library) to check \(31\) points of \(\mathbf P^2(\mathbf F_5)\), the \(16\) Gauss tangents of the quartic, all \(28\) even-contact lines and their Frobenius cycles in \(\mathbf F_{625}\). The expected final line is `ALL_CHECKS_PASS`.

Run `python3 verify_prime_fields.py` (again standard library only) to verify the all-\(q\) incidence formula numerically for \(q=5,7,11,13\). The final line should be `ALL_PRIME_TESTS_PASS`. This checker is separately implemented and does not import the quartic checker. The exact outputs of both programs are included as text files.

The proof for all prime powers follows from the cited point-optimal classification and algebraic counting, not these finite checks. The complete F5 bitangent list is analytically exhaustive by line-coordinate support and square-comparison; its Galois action is a finite, exactly checked calculation. No external independent validation has been performed.
