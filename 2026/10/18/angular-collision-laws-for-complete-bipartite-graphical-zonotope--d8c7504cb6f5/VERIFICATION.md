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

# Reproducibility and verification

The formula for the collision probability follows from alternating block decompositions of orientations. The exhaustive checker `angular_collision_checker.py` computes orientation signatures directly from labeled permutations, independently forms the weighted binary-run census, and computes formal-series coefficients by convolution. It compares all three rational results on 15 tested bipartitions (2,818 distinct orientation signatures), and checks the exact minimum/maximum cone angles and counts. It verifies the reference case \(C_{2,2}=7/72\) and nine further rational coefficient evaluations with long-side sizes 30, 60, and 120. Run with `python angular_collision_checker.py` using a current Python 3 interpreter and only its standard library. The argument in `RESULT.md` proves the all-parameter statements; the finite checks do not constitute independent validation or an exhaustive all-dimensional proof.
