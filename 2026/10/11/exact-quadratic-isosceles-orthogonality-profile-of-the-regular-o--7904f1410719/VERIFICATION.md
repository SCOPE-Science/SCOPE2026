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

Run `python verify.py` in an environment satisfying `requirements.txt`. The script uses exact symbolic arithmetic, not floating-point sampling. It verifies the seven active-support intervals for the five dihedral vertex-separation types, the three candidate envelope branches, the exact thresholds \(2-\sqrt2\) and \(1/\sqrt2\), the parameter conversion to \(3-2\sqrt2\) and \((2\sqrt2-1)/7\), and continuity of the final profile. A successful replay prints `VERIFY_OK`.

The code does not replace the proof's convexity argument. Its scope begins after the analytic reduction to octagon vertices and checks the exact algebra and support inequalities used there.
