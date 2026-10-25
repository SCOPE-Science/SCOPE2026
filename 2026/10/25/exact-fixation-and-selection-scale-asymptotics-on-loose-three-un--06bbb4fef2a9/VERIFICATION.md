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

The standalone `verify.py` reconstructs the *labeled* Markov chain for the group-overwrite rule and solves exact-rational absorption equations for \(m=1,2\). Four fitness inputs \(r\in\{1/2,1,2,3\}\) at each size verify the two single-mutant initialization orbits. It independently checks 48 exact harmonic-formula cases across \(1\le m\le8\), including neutrality. The \(m=2\) Moran gap factorization is verified by integer polynomial convolution, not by sampling alone.

To reproduce: place `verify.py` beside this file and run `python verify.py` with Python 3. It requires no nonstandard libraries. Analytical proofs of almost-sure absorption, the all-\(m\) harmonic reduction, and the large-size limits are in RESULT.md. Finite computational checks do not prove asymptotics or exhaustive uniqueness beyond the proven formulas. No independent audit is represented by these checks.
