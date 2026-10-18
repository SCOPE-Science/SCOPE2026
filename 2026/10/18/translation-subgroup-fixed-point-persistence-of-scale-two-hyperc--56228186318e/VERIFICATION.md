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

# Verification of translation-subgroup fixed-point classification

The finite check is the standalone dependency-free `verify.py`, run with ordinary Python 3. It enumerates every subgroup of ranks one and two of \((\mathbb F_2)^n\), and every subgroup of rank three for the obstruction test, for the four dimensions \(3\leq n\leq6\). Every cyclic/rank-two subgroup is classified by the exact maximum Hamming distances between original cube vertices in its cosets; the resulting orbit complex is checked at thresholds \(0\), \(1\), and \(2\).

For admissible rank-one subgroups the check reconstructs the full compatibility graph and verifies the expected vertex and edge counts, regularity, connectedness, and exact binomial graph-distance profile at every vertex. Its Euler characteristic matches \(1+(n-3)2^{n-2}\) independent cycles. The proof separately gives an explicit linear graph isomorphism, so these finite graph invariants are not substituted for an isomorphism theorem. For rank two, the code checks exactly \(2^{n-2}\) isolated orbit-vertices; for rank three it confirms every subgroup contains an inadmissible weight-three-or-greater vector. For weight-one rank-one subgroups, the code also verifies that the scale-one isolated vertices are precisely the scale-two graph vertices.

The attached `verification_output.txt` records the successful actual execution. No claim is made that finite checks establish the infinite theorem. That theorem is proved combinatorially using the barycentric fixed-orbit homeomorphism, Hamming distance constraints, subspace classification, and an explicit binary basis change. The verification does not include any independent external audit; its front matter records that status exactly.
