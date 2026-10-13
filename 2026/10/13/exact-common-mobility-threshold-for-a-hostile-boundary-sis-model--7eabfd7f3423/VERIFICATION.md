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
The universal proof is analytic.

For each nonzero test function,
\[
C=A r^2+B r
\]
defines its unique positive threshold \(r\). Hence its reproduction quotient is above one exactly for \(d<r\).

At the global threshold \(d_c=\sup r\), the upper estimate
\[
\frac{C}{d^2A+dB}\le\frac{d_c}{d}
\]
holds for \(d>d_c\), while a sequence with \(r\to d_c\) gives
\[
\frac{C}{d_c^2A+d_cB}\ge\left(\frac{r}{d_c}\right)^2\to1.
\]
This proves the boundary equality without assuming that the supremum is attained.

The bundled checker verifies these algebraic implications with exact rational arithmetic for many positive triples \((A,B,C)\), and checks the monotonicity scaling inequality. No finite calculation is used as a substitute for the PDE or variational argument.
