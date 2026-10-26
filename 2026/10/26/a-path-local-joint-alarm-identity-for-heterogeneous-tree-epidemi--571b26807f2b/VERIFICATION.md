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

Run `python verify_tree_joint_path_identity.py` using Python 3 and its standard library. The program prints one JSON object recording whether every exact-rational comparison passed. Expected counts: 290 tree/parameter scenarios, 2,712 unordered monitor-pair comparisons, 206,368 weighted source–edge–pair configuration evaluations. The source distribution is the nonuniform vector with coordinates proportional to \(1,2,\ldots,n\); edge weights are separately chosen from a heterogeneous rational family and the uniform \(1/2\) family. It uses explicit edge-configuration enumeration to calculate joint alarm probabilities and a path-only calculation for the proposed identity.

The mathematical proof covers **all** finite trees, **all** probabilities in \((0,1)\), **all** probability distributions of the unique source, and every distinct monitor pair; the finite checks only test samples of this domain. Bapat and Sivasubramanian's previously published inverse formula is independently rederived in `RESULT.md` and its novelty is not claimed. No independently performed audit or certification is asserted.
