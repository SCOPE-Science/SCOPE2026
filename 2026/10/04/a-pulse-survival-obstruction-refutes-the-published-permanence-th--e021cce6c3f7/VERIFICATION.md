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
The main argument is analytic.

For the printed short-mackerel equation,
\[
\dot x_2
=
x_2\left(
B+\frac{rbx_1}{k_2+x_1}-Ax_2
\right),
\]
one has
\[
\dot x_2\le(B+rb)x_2.
\]
Combining this with
\[
x_2(nT^+)=(1-\omega)x_2(nT)
\]
gives the exact pulse-to-pulse upper multiplier
\[
q=(1-\omega)e^{(B+rb)T}.
\]
Thus \(q<1\) forces \(x_2\to0\). The equality case is also excluded from permanence because \(x_1\) has a finite logistic upper bound, making the Holling gain eventually strictly less than \(rb\).

The bundled checker verifies all numerical and logical inequalities used in the explicit counterexample, including every hypothesis listed in Theorem 3.8 and
\[
q\approx0.6085676604<1.
\]

No simulation or finite enumeration is used to prove extinction.
