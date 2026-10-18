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

# Independent reproducibility instructions

The principal claim is an all-dimensional exact identity, a strict inequality in the dimension parameter, and a sharp asymptotic expansion. The text in `RESULT.md` contains the analytical proof. The additional script `verify.py` requires Python, `mpmath` and `sympy`, and can be run as `python verify.py` in the extracted directory. Its numerical quadrature checks are supplementary; no finite computation proves an infinite-dimensional assertion.

The script checks that the Taylor coefficients of \(\exp((\operatorname{erf}^{-1}u)^2)\) through degree four equal \(1,\pi/4,7\pi^2/96\) in even degrees; compares numerical quadratures in dimensions two through five with standard independently known exact volumes, including the correctly rescaled OEIS values for four and five dimensions; verifies a decreasing numerical sequence through forty dimensions; and tests the asymptotic remainder for several dimensions through 320. The analytical beta coupling and the uniform Taylor remainder estimate, not the observed numbers, prove strict monotonicity and the \(O(n^{-6})\) error.

To independently reconstruct the proof, check the minimum-coordinate chamber integral, the spherical-to-Gaussian independence relation, the normalization to unit-ball volume, the exact beta moments, and the bound \(\operatorname{erfc}(t)\le e^{-t^2}\) for \(t\ge0\). Also distinguish volume of the cylinder intersection from volume of the polar convex hull of coordinate disks. No independent scientific audit is represented by these instructions.
