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
The universal theorem is analytic.

For
\[
A_\sigma=W-\sigma D
=
aI+b(S+S^{-1}),
\qquad
a=\frac56+2\sigma,
\qquad
b=\frac1{12}-\sigma,
\]
the regime \(\sigma\ge1/12\) has \(b\le0\) and exact diagonal-dominance margin
\[
a-2|b|=1.
\]
This gives inverse positivity.

For \(0<\sigma<1/12\), the inverse Green kernel is
\[
g_j=C r^{|j|},
\qquad -1<r<0.
\]
The distance-two coefficient of the full backward-Euler map is
\[
(B_\sigma e_0)_2
=
-\frac{12C\sigma r^2}{1-12\sigma}<0.
\]
Thus every strictly positive sub-threshold step fails positivity.

The embedded `verify.py` independently reconstructs the four-point periodic matrices using exact `Fraction` arithmetic and verifies the negative component at \(\sigma=1/100\). It also checks the algebraic threshold identities and representative infinite-lattice kernel signs. Those finite checks corroborate the formulas but are not used as a substitute for the infinite-lattice proof.

The exact finite-grid threshold for arbitrary size, boundary closures, higher dimensions, variable coefficients, nonlinear diffusion, and Crank--Nicolson are not established here.
