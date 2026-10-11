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

The universal claim is proved analytically in `RESULT.md`. The included `verify.py` performs exact finite symbolic checks on the explicit quartic data only.

It checks that the two base quartic polynomials have zero Euclidean Laplacian, evaluates exact uniform-sphere moments by the monomial double-factorial formula, verifies
\[\mathbb E f(U)^2=\mathbb E g(U)^2=64/315,\qquad \mathbb E f(U)^3=\mathbb E g(U)^3=0,\]
reproduces
\[\mathbb E f(U)^4=4096/36465,\qquad \mathbb E g(U)^4=241664/2501499,\]
and confirms the positive difference \(65536/4169165\). It also checks that inserting the common second moment into the analytic area and volume formulas gives the coefficient \(256\pi/35\).

The script does not numerically certify convexity for all directions and does not replace the compactness/positive-curvature argument establishing an admissible \(\varepsilon_0>0\). No brightness-law claim is verified or made.
