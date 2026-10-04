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
The source formulas used in the proof were checked in the full arXiv text: the upper and lower flight formulas, the Poincaré map, the boundary condition, and the explicit statement that the boundary derivative test is unavailable.

At the singular equality, direct substitution gives the exact signed-distance map
\[
u^+=\sqrt{u(u+2\rho)}.
\]
The positive-time conditions are verified separately, so the fixed point is a physical grazing cycle rather than an extraneous root of a squared equation.

For the iterate asymptotic, normalization by \(\rho\) gives
\[
v_{n+1}=\sqrt{v_n^2+2v_n}.
\]
The exact increment tends to one and has expansion
\[
v_{n+1}-v_n=1-\frac{1}{2v_n}+O(v_n^{-2}).
\]
Monotonicity, Stolz-Cesàro, a harmonic lower bound, and a summable-error correction then give
\[
v_n=n-\frac12\log n+C+o(1).
\]

No finite numerical experiment is used as proof. A symbolic expansion was used only as a consistency check on the algebraic asymptotic expansion. The unresolved scientific limit is literature completeness outside the inspected and indexed grazing-map sources.
