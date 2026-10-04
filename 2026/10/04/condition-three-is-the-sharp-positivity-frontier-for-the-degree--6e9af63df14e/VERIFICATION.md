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
The checker uses only exact rational arithmetic and the Python standard library.

It evaluates the defining scaled Chebyshev polynomial
\[
p_3(\lambda)
=
\frac{
T_3((L+\mu-2\lambda)/(L-\mu))
}{
T_3((L+\mu)/(L-\mu))
}
\]
and verifies that
\[
\frac{1-p_3(\lambda)}{\lambda}
=
\frac{
2[16\lambda^2-24(L+\mu)\lambda+9L^2+30L\mu+9\mu^2]
}{
(L+\mu)(L^2+14L\mu+\mu^2)
}
\]
at many exact rational inputs.

It reconstructs the sharpness family and verifies its off-diagonal formula exactly. It also rebuilds the complete \(\kappa=4\) witness, its degree-three Chebyshev solution matrix, the negative final coordinate, and the strictly positive exact solution.

The universal Stieltjes frontier and the two-dimensional immunity theorem are analytic matrix arguments in RESULT.md; the finite replay is corroborative only.
