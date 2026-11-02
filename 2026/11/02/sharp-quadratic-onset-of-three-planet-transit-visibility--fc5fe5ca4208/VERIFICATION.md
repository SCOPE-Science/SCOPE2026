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

# Reproduction and evidence
Run \(\texttt{python verify.py}\) with Python 3 in the package directory. The program uses only the standard library. It verifies cube-vertex maxima and strict adjacent-corner inequalities on six exactly represented rational matrices, calculates the eight-corner coefficient for the equal-width orthogonal example, and independently evaluates the sphere-area integral by Simpson quadrature at five decreasing excess widths.

The check printed PASS for all three groups. Numerical ratios for \(\delta=0.1,0.03,0.01,0.003,0.001\) were approximately \(1.856862602,1.706395145,1.670822450,1.658974868,1.655643574\), approaching the analytic coefficient \(3\sqrt3/\pi\approx1.653986686\). The arbitrary-orientation result is proved analytically in RESULT.md; finite examples do not establish universal quantification.

No independent audit or outside experimental validation has been performed. The calculation applies only to ideal circular-orbit transit visibility at fixed orbital planes.
