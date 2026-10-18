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

Standalone checker: `check_ideal_orbit_threshold.py` (Python 3.9+, no external packages). Executed successfully from this package's exact source path. It enumerates all subspaces of a six-dimensional binary vector space, selects the 45 bracket-stable ideals of the free three-generator class-two Lie algebra, and compares the complete defect-profile distribution. It constructs the action of elementary transvections generating \(\operatorname{GL}_4(\mathbb F_2)\) on all 63 nonzero alternating forms, yielding two orbits of sizes 35 (rank two) and 28 (rank four). It counts 130 rank-two and 234 rank-four projective forms over \(\mathbb F_3\), and checks full Gaussian count identities for \(q\in\{2,3,5\}\) and \(d\in\{3,4,5,6\}\). It prints `ALL_IDEAL_ORBIT_THRESHOLD_CHECKS_PASSED`.

The checker uses prime fields, not arbitrary finite extensions. The proof, rather than finite tests, establishes the statement for every prime power and every \(d\ge5\). Source search did not certify historical uniqueness. Independent audit: not performed.
