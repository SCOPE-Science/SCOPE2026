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

The finite checker `verify.py` was executed with standard Python and no third-party dependencies. It directly enumerated lower and upper parameter subsets, checked closure and comparability constraints, and tested the actions of all index permutations. For dimensions \(2\) through \(6\), there were \(872\) permutations; both untwisted and duality-twisted fixed-type formulas passed for every permutation. The checker separately counted ordinary and duality-extended orbits via Burnside for all five dimensions, and enumerated actual orbit sets directly for dimensions \(2\) through \(4\).

The saved `verification-output.txt` gives the exact output of this run. The tested dimensions do not constitute a proof for unbounded \(n\); the general proof is the structural partition and even-cycle argument in `RESULT.md`. No separate independent audit or external certification was performed.
