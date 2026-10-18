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

# Reproduction

Save `verification.py` alongside this document and execute `python verification.py` with Python 3.10 or later. No packages are required. The program computes all exact branchwise fixed points and primitive two-cycle points using `fractions.Fraction`, reconstructs knots from fixed points (even branch count), or from fixed points plus the least exact-period-two point (odd branch count), and confirms every tested identity without floating-point rounding. It produces `Exact deterministic rational samples passed: 271`.

The test comprises 260 independently specified rational knot vectors with branch counts \(2\) through \(14\), six admissible odd-fiber perturbations, and five explicit three-branch fiber examples. It is not a proof of the universal real-parameter claim; the full proof is in `RESULT.md`. No independent external verification or historical-priority audit has been performed.
