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

# Verification of the counterexample

Run `python3 artifacts/verify.py` without external libraries. The program verifies the conditional labelled comparison \(-2/9\) within either baseline group and \(-1/3\) across the two groups, reconstructing \(\tau(X_1,X_2)=-5/18\) before smoothing. The sorted pair is conditionally independent within either group and exactly discordant across groups, yielding \(\tau(X_{1:3},X_{2:3})=-1/2\). The rational bound \(3209/22500\) for exponential-mixture smoothing is checked symbolically. The script also exhausts a small integer grid of the two-coordinate rearrangement lemma for diagnostics; the universal proof is in RESULT.md and needs no grid extension. The bump's smoothness, strict positive density, and coupled-kernel inequality are proved analytically.

The displayed bound is non-sharp in general; no empirical sampling or floating-point approximation is needed. This is a self-review, not an independent audit or formal certification.
