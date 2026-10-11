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
# Reproducibility and limitations

Run `python verification/verify.py` in the extracted directory. The script requires Python 3 and SymPy, and uses exact symbolic arithmetic, not floating-point thresholds, for the contact and covariance identities. It checks the graph adjacency, projected eigenspaces, weighted mean, full covariance, inverse-covariance norms of every listed vertex, algebraic root equation, and positive determinant for \(m=2,3,4,5\). The observed output was four `PASS` records followed by `ALL_CHECKS_PASS`.

The general proof is the weighted covariance contact certificate and the determinant–trace lower bound in `RESULT.md`. Repeating finitely many symbolic instances does not independently certify infinitely many dimensions or uniqueness relative to all competitors. Independent audit has not been performed. The scripts and proof use the intrinsic Euclidean structure of the original PQ embedding, and make no lattice-isometry claim for integral equivalents.
