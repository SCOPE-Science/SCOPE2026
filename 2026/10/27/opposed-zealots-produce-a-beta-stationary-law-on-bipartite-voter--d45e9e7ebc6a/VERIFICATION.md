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

Run `python3 verify_stationarity.py` using Python 3 and no third-party packages. It forms the complete finite count-chain transition generator for each of the nine choices \(1\le a,b\le3\), solves \(\pi Q=0\) and \(\sum\pi=1\) with exact rational Gaussian elimination, and recomputes normalized first and distinct-pair second moments. All nine cases pass without tolerances. The solver uses separate full stationary equations rather than the pair-moment closure used in the proof.

The exact moment identities and the beta weak limit for every admissible integer-size sequence are proved in RESULT.md; the finite verifier is a reproducibility check, not a certificate for an infinite statement. Source originality comparisons were performed from accessible literature, but unindexed mathematically equivalent specializations remain a residual risk.

Independent audit has not been performed.
