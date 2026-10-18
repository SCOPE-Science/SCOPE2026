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

# Reproducibility and limits

Run `python verify.py` with Python 3 and mpmath installed; the provided `verification_output.txt` is the resulting reference output. The standalone program uses 65-digit precision to solve the stationary equations of the exact \(H^4\) degree-one polynomial objective at seven radial values \(1-a=10^{-2},\ldots,10^{-12}\), and tests the asymptotic coefficient and loss correction. It also verifies exact finite sixth-power baseline identities at three radial values. This is a finite consistency check, not an exhaustive proof for every exponent, degree or Blaschke parameter. The general statement is proved by localization, convexity, and uniformly controlled Taylor remainders in `RESULT.md`. No independent audit has been performed.
