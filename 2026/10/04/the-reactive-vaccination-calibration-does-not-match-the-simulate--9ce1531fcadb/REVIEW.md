# Same-model review

## Correctness
PASS. The claim compares two explicit vaccination-only ODEs from the same study. Solving each equation is elementary and exact. The released implementation was inspected and uses the multiplicative term from the main article. Recalculation shows that the supplement's two rates solve the affine target-relaxation law, whereas the multiplicative law requires the single rate \(\log 2/(150\cdot0.93)\) to halve either susceptible fraction. The claim is restricted to calibration consistency and does not infer errors in fitted or simulated trajectories beyond that statement.

## Originality
PASS. Source-title, printed-rate, target-susceptibility, equation-alias, correction, and erratum searches were compared with the existing finding ledger and published records. No checked record states this exact mismatch between the supplementary calibration ODE and the main/released counterfactual ODE. The closest Texas-measles modeling literature addresses outbreak growth, spatial spread, or other vaccination scenarios and does not imply this source-specific equation comparison.

## Value
PASS. Vaccination-rate calibration is a mathematically substantive bridge between an intervention parameter and the claimed susceptible reduction. Here the bridge changes the ODE, its asymptote, and the role of vaccine efficacy. The resulting rates differ by roughly one third to two thirds from the rate that actually halves susceptibility under the simulated law, so the correction is material for interpreting or reusing the study's campaign-intensity calculation rather than a typographical normalization issue.

## Closest literature and limitations
The main article, its supplement, and the public implementation were inspected together because the mismatch exists only at their interface. A related Texas measles spatial-spread preprint does not contain the same calibration argument. The present result does not assess whether the reported intervention trajectories are epidemiologically accurate; it establishes only that the supplement's half-reduction calculation is not a calibration of the equation used for those trajectories.

Same-model review: passed. Independent audit: not yet performed.
