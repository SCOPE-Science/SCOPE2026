# Independent mathematical audit — SCOPE-20260920-1fb45117f7e9

Final disposition: **PASS**.

## Correctness
**PASS** — For periodic conservative flux, integration by parts gives the centered energy identity \(E'=-\nu\|u_{xx}\|_2^2+\|u_x\|_2^2\). At \(\nu=1\), Fourier expansion shows the dissipation vanishes exactly on constants plus first harmonics. Recurrence and monotonicity force a recurrent orbit to remain in that kernel. Substitution of \(m+A\cos(x-\theta(t))\) then forces \(f'\) to be constant on the entire attained interval, and the converse follows by direct substitution. The invariant-measure statement follows by integrating the nonnegative dissipation. For classical quadratic flux there is no nontrivial affine interval, so standard precompactness plus LaSalle yields critical attraction; the strict and unstable regimes follow from Poincaré and the first Fourier mode.

## Originality
**PASS** — The closest accessible stability result proves global asymptotic stability of the constant-equilibrium set only in the strict regime \(\nu>1\) and instability for \(\nu<1\); it does not state the critical zero-dissipation recurrent-set classification. Targeted current searches found no published result with the affine-flux if-and-only-if traveling-wave obstruction or invariant-measure rigidity. Several older KS sources could not all be inspected in complete theorem-level text, so the classical special case remains a best-of-knowledge originality claim with explicit residual risk.

### Equivalent formulations
The exact equality-set dynamics were searched in both stability and traveling-wave formulations.

### Broader coverage
Broader dynamical theory supplies inputs, not the full critical equality classification.

### Exact database or table
No finite database is intrinsic; this was a prior-theorem search.

### Claim versus prior implication
The final theorem is not mechanically implied by the standard endpoint-adjacent results.

## Value
**PASS** — The theorem resolves the nonhyperbolic boundary left open by the standard strict energy estimate and identifies exactly what can obstruct decay for a whole conservative-flux class. The affine-flux classification and invariant-measure consequence are structural dynamical statements, not merely an endpoint calculation.

## Source inspections
- **Linearized Stability of Partial Differential Equations with Application to Stabilization of the Kuramoto-Sivashinsky Equation** (https://doi.org/10.1137/140993417): accessible abstract and theorem-level description of stability for \(\nu>1\) and instability for \(\nu<1\) Method: primary-source theorem comparison. Assessment: STRICT_REGIMES_NOT_CRITICAL_CLASSIFICATION. Evidence: The accessible statement does not provide the zero-dissipation invariant-set calculation at equality.
- **The Well-Posedness of the Kuramoto-Sivashinsky Equation** (https://doi.org/10.1137/0517063): primary bibliographic and theorem-level material on one-dimensional periodic well-posedness Method: primary-source context inspection. Assessment: SUPPORTING_INPUT_NOT_COVERING_RECURRENCE_THEOREM. Evidence: It supplies the analytic framework, not the critical recurrence classification.

## Checked sources
- https://doi.org/10.1137/140993417
- https://doi.org/10.1137/0517063

## Residual risks
- Complete theorem-level texts of several older KS papers were not all inspected, so an equivalent classical \(\nu=1\) observation under different terminology remains possible.
- The general-flux statements require the regularity stated in the package; global attraction is asserted unconditionally only for the classical one-dimensional periodic KS flow.
