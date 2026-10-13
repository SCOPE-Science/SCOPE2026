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

The mathematical proof is symbolic and valid for every integer \(n\ge3\). Its critical steps were checked separately:

1. If at least three white vertices remain on one bipartition side, no blue vertex on the opposite side can force into it; forces from the other direction cannot change that obstruction.
2. A minimum set must therefore leave exactly two white vertices on each side.
3. Equal omitted-index pairs admit no initial force.
4. Distinct omitted-index pairs admit the explicit force sequence \(b_x\to a_y\), \(a_z\to b_w\), \(a_w\to b_z\), \(b_z\to a_x\), with the possible equality \(w=y\) handled because \(a_y\) is blue after the first force.
5. Counting ordered distinct omitted 2-subsets gives \(\binom n2(\binom n2-1)\).

The included checker exhaustively verifies the standard zero forcing process for every \(3\le n\le9\), independently computes the minimum size, and compares every size-\(2n-4\) subset with the stated characterization. Replay output:

`VERIFY_OK n_range=3..9 subset_checks=346739 basis_checks=6671 max_order=18`

Finite exhaustive verification is not used as proof for unbounded \(n\). The scalar equality is also cross-checked against the previously published tensor-product theorem \(Z(P_t\times K_n)=(n-2)t\) for even \(t\), specialized to \(t=2\).
