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

# Verification record

Reproduce with `python3 verify.py`, using Python 3's standard library only. The checker enumerates every invertible \(2\times2\) matrix over each of the three prime fields \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\), constructs representatives of all three Frobenius splitting types, computes all their determinant-twisted cubic orbits, and checks that these orbits are disjoint and exhaustive among squarefree cubic forms. For each representative, it enumerates all \(q^3\) symmetric scalar forms, partitions them by the exact cubic stabilizer, and counts the full-algebra stabilizer orders \(1,2,3,6\). It also checks directly on basis pairs the covariance of the traceless multiplication under each invertible change of basis.

Observed class-count totals: \(155\) for \(q=5\), \(399\) for \(q=7\), and \(1463\) for \(q=11\). Observed automorphism-size distributions in the order \((1,2,3,6)\) are \((100,45,5,5)\), \((294,91,7,7)\), and \((1210,231,11,11)\). Each agrees with the symbolic theorem, and execution terminates with `VERIFY_OK`.

These are complete **finite** verifications for the selected prime fields. The proof's Frobenius descent and representation-theoretic fixed-space arguments, not extrapolation from these checks, establish the infinite family covering all prime powers of characteristic greater than three. No computer algebra system, independent reviewer, or external validation is asserted.
