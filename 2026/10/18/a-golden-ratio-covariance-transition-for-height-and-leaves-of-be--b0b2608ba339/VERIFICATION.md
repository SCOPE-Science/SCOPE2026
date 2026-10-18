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
# Reproducibility

Execute `python3 verify.py` from a directory containing the extracted files. No third-party Python dependencies, network access, or random seeds are required.

The checker reconstructs the actual rooted tree from the attachment word and separately reconstructs its height and leaf count from the increment formulas. It exhaustively tests every attachment word for \(3\le n\le12\) at five exact rational attachment parameters and compares exact means and second moments with a state-based recursion. It also checks limiting covariance predictions using deterministic moment propagation through \(n=3000\) for six parameters and validates the exact determinant identity at five rational parameters. In the completed run, all **288** assertions passed.

This finite verification is not an exhaustive enumeration for arbitrary \(n\); it cannot establish functional weak convergence or literature originality. Those require the analytical covariance-sum proof, the standard finite-state functional central limit theorem, and the documented source comparisons. The code models only iid two-choice attachment and the precise rooted definitions from the finding.
