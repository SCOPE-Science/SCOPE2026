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

The standalone script `check_hankel.py` uses only the Python standard library. Run it as `python3 check_hankel.py` in the same directory as this file. It re-evaluates weighted Bergman moments using log-gamma, checks the norm-and-projection identity against an independently written orthogonal decomposition, verifies unweighted norming indices using exact rational numbers, tests the unique critical branch across sample weights, and checks the small-positive-weight exponential displacement. The observed output was `WEIGHTED_HANKEL_CHECKS_PASS 10717`.

The finite checks do not prove the limiting statement for arbitrary real weights, degrees or near-critical couplings. These are established by the exact moment formula, uniform escape-of-index analysis, derivative signs and logarithmic critical equation in `RESULT.md`. Independent audit has not been performed.
