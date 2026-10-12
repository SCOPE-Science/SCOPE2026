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

The symbolic proof has three independent regimes determined by the center label. The critical checks are: the precise forbidden blade family when the center is \(2\); the two forbidden blade families when the center is \(0\) or \(1\); and the fact that \(r\ge2\) makes the center condition automatic in the latter regime.

`artifacts/verify.py` constructs each tested heterogeneous windmill, enumerates every labeling by \(\{0,1,2,3\}\), tests the double Roman definition directly from graph neighborhoods, and compares the resulting coefficient vector to the closed polynomial computed independently by polynomial convolution. It also verifies the minimum weight and its multiplicity.

The packaged finite test covers blade profiles \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), and \((2,3,3)\), through graph order \(9\). This finite range is a stress test and boundary check, not evidence for the universal quantifier beyond those instances.
