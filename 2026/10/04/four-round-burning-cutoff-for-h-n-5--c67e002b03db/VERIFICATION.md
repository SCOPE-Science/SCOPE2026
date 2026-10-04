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

`verify.py` is a standalone exact checker using only the Python standard library. It constructs each graph from the rim and diagonal definition, computes shortest-path distances by breadth-first search, and checks all displayed positive burning sequences.

For \(n=7\), it exhausts every ordered pair of centers for radii \(2\) and \(1\); the minimum uncovered count is \(2\), so a final singleton cannot yield a three-round burning. For \(n=16,17,18\), it exhausts every ordered triple of centers for radii \(3,2,1\); the respective minimum uncovered counts are \(2,4,5\). These covering obstructions are stronger than needed because they ignore source-validity restrictions.

For the infinite ranges, the proof uses the maximum-degree-three ball cap \(|B_r|\le3\cdot2^r-2\). The checker verifies the resulting three-round capacity \(15\) and four-round capacity \(37\). No finite experiment is used to extrapolate the cases \(n\ge19\).

The checker does not determine exact burning numbers for \(n\ge16\); it verifies only the lower bound needed for the stated cutoff.
