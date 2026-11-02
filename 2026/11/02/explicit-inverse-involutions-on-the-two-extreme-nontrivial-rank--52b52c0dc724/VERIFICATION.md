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

The proof in `RESULT.md` establishes the all-\(n\) claim from the necessary-and-sufficient cross-transversal criterion. Exact computations serve only as a bounded independent consistency check.

Execute `python3 verify.py` with the Python 3 standard library. The checker directly enumerates all rank-two and rank-\((n-1)\) increasing self-maps for \(2\le n\le18\), constructs their candidate partners, and tests: parametrization uniqueness; the two sandwich equations by function composition; the involution equation; fixed point if and only if idempotent; and all class/fixed-point/transposition counting identities. It prints one summary for each \(n\) and terminates with `VERIFY_OK`, as captured in `verification_output.txt`.

The script does not enumerate the inverse graph for unbounded \(n\) and does not test intermediate ranks. Its enumeration does not prove novelty, completeness of historical research, or independent certification. The definition is of inverse *matching*, not of a semigroup homomorphism or of covering by inverse subsemigroups.

Self-review: passed. Independent audit: not yet performed.
