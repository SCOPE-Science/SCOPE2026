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

The analytic proof in `RESULT.md` establishes the statements for all real \(B>0\) and \(I>3B/2\). The companion standard-library-only `verify.py` independently evaluates exact branch identities with `fractions.Fraction`, propagates the three-component transfer recursion for 21 time indices per parameter sample, and checks eventual parity complement at 97 rational mirror separations. It checks six ratios \(I/B\in\{8/5,39/20,2,11/5,3,10\}\) at two positive values of \(B\), for a total of 12 parameter instances, 252 transfer-time identities, and 1164 exact mirror pairs.

Run from the extracted package: `python verify.py`. The expected output is `PASS: 12 parameter instances, 252 transfer time-step checks, 1164 mirror pair tests`. These tests corroborate finite instances and do not replace the all-parameter proof. No external certification or independent audit has been performed.
