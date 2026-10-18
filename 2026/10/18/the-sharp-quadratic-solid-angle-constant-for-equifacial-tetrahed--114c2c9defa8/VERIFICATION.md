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

The exact coordinate model for all equifacial tetrahedra is given in `RESULT.md`. Its edge determinant yields \(V=8xyz/3\) and its longest edge yields \(\delta=2\sqrt{y^2+z^2}\) after ordering \(x\le y\le z\). The van Oosterom--Strackee formula gives \(\tan(\Omega/2)=2xyz/Q\), with \(Q\) specified in `RESULT.md`. The analytic inequalities and equality-boundary analysis are proved there.

Run `python3 verify.py` using Python 3 and no third-party packages. Expected: `DISPHENOID_SHARP_SOLID_ANGLE_CHECKS_OK`. The code executes independent finite consistency checks for ordered integer triples, checks a polynomial identity over exact rational numbers, reconstructs a sample tetrahedron determinant, and checks approach to the sharp constant along four increasingly thin specimens. These checks supplement, but do not replace, the universal proof. Numerical diagnostics do not establish originality, universal truth, or independent validation.
