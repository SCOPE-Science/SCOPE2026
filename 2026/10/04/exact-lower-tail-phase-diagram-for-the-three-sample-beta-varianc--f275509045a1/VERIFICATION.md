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

The analytic verification uses the orthogonal diagonal coordinates in `RESULT.md`. The transverse disk for \(S^2\le y\) has area \(2\pi y\), and the coordinate Jacobian is \(\sqrt3\). This fixes the regular coefficient before any endpoint analysis.

For the critical normalization check, Royen's Theorem 3 uses \(Q=2S^2\). At \(n=3\) and \(p=2/3\), its coefficient is \(4\pi\sqrt3/27\) in \(F_Q(x)\sim Cx\log(1/x)\). Therefore \(F_{S^2}(y)=F_Q(2y)\) has coefficient \(8\pi\sqrt3/27\) in front of \(y\log(1/y)\). The present formula gives the same number because \(B(2/3,1)=3/2\).

The standalone script `verify.py` checks that exact normalization identity numerically to machine precision, checks the uniform-parent coefficient \(2\sqrt3\pi\), and checks the exponent ordering on representative parameter values below and above the threshold. These are normalization and algebra checks only. They do not constitute a proof of the asymptotic limits; the proof is the localization argument in `RESULT.md`.

Unproved limits: no second-order term, explicit error rate, simplification of \(J_m\), or extension to \(n\ne3\) is asserted.
