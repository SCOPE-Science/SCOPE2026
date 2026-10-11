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

For three supporting lines with normals \(2\pi/3\) apart and support values \(h_0,h_1,h_2\), the analytic certificate is
\[
\rho=\frac{h_0+h_1+h_2}{3},
\qquad
A=3\sqrt3\,\rho^2.
\]
For a regular \(n\)-gon of circumradius \(R\),
\[
h(\phi)=R\cos\operatorname{dist}\!\left(\phi,\frac{2\pi}{n}\mathbb Z\right).
\]

The verifier independently constructs each support line from a direct maximum over the polygon vertices, intersects line pairs, checks that all polygon vertices satisfy the three support inequalities, checks that the resulting triangle is equilateral, and compares its shoelace area with the claimed support-average formula.

It then checks the endpoint spectra for every \(3\le n\le150\) and all three congruence classes modulo \(3\). The finite checks are supplementary; the proof for every \(n\) is the exact support-phase argument in `RESULT.md`.
