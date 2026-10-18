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

# Reproducibility of the integral leaf-transfer theorem

Execute `python3 verify.py` with a standard Python 3 installation; no third-party modules or downloads are needed. The verification script regenerates all unlabelled trees of orders one through nine using recursive leaf addition and a centroid canonical encoding, and computes every vertex-root Kalman determinant exactly using fraction-free integer elimination. It checks the sharp nine-vertex example, the mod-two parity annihilator, 326 direct unit-leaf determinant comparisons, and explicit block-column identities for the conductances 1, 2, and 3 on all rooted free trees through order six.

Expected final line: `VERIFY_OK tree_types_1_through_9=95 rooted_cases=749 leaf_invariance_tests=326 nonunit_min_size=9 magnitude=2 lattice_parity=verified`.

The finite census proves only the claimed finite minimum because its leaf-generator and canonical duplicate removal cover all free trees in the specified range. The statement for arbitrary graph order instead follows from the algebraic block-recurrence proof in `RESULT.md`. These checks are finite exact arithmetic, not an independent external audit. Historical priority remains unresolved beyond the stated inspected literature.
