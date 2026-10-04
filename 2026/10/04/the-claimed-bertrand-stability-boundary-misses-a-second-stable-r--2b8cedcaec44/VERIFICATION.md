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

The bundled `verifier.py` uses exact rational polynomial arithmetic. It checks the static first-order conditions and positive demands at \((3,3)\), reconstructs the polynomial entries of the diagonal-ray Jacobian, and derives
\[
\operatorname{tr}J(t)=2-6t+\frac12t^2,
\qquad
\det J(t)=1-6t+\frac{17}{2}t^2.
\]
It then verifies the three exact Jury-factor polynomials
\[
(3t-2)^2,\qquad 8t^2,\qquad \frac{t(12-17t)}2.
\]
It checks that \(t=2/3\) gives a multiplier \(-1\), and that \(t=7/10\) lies in the second stable interval and has exact Jury margins \(1/100\), \(98/25\), and \(7/200\).

The proof of the interval characterization is symbolic algebra; the witness computation is a replay check rather than the basis for an infinite-domain inference. No nonlinear stability statement is certified at the neutral point \(t=2/3\).
