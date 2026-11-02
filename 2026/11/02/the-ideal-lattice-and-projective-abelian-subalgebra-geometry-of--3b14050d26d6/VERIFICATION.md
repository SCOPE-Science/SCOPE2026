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

# Reproduction and limits

Run `python3 verify.py` using only Python's standard library. The script implements finite-field operations for the tested fields, Lie brackets, RREF subspace enumeration, and direct closure/commutation predicates. It prints `VERIFY_OK` after all assertions succeed.

Actual successful tests: finite-field multiplication and Lie Jacobi checks; twelve parameter formula identities; exhaustive all-dimension subspace censuses at \(q=2,3\), \(m=1\) as boundary checks; exhaustive dimensions zero through two at \(q=2\), \(m=2\); all \(1,048,576\) ordered pairs of elements at \(q=2\), \(m=2\); all \(137\) predicted ideal closures for that case; projective lines and automorphism-generating maps. For \(q=2\), \(m=2\), the direct pair count is \(80896\).

These bounded computations do not exhaust subspaces of \(\mathbb F_2^{10}\) in dimensions three or larger, and do not constitute an infinite proof. The independent mathematical audit is not performed.
