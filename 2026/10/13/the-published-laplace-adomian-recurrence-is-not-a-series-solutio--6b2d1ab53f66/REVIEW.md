# Self-review

## Correctness

PASS. The source's own fractional integral equation fixes the first Caputo-series coefficient as the vector field evaluated at the initial state. Equation (5.9) changes the symptomatic hospitalization term from \(\phi_sK_3\) to \(\phi_sK_4\) and the quarantined recovery inflow from \(\rho_hK_6\) to \(\rho_hK_5\). Equation (5.10) additionally reverses the two incidence pairings, uses exposed rather than susceptible natural mortality in the susceptible recurrence, and again applies the hospitalization loss to the asymptomatic series. Exact symbolic subtraction gives nonzero generic discrepancies and the bundled checker verifies an exact positive witness.

## Originality

PASS. Laplace–Adomian decomposition and the compartmental model family are prior work. The accepted result is the source-specific coefficient-level diagnosis of equations (5.9)–(5.10). Searches by DOI, title, equation number, recurrence terminology, compartment substitutions, correction terminology, and related published findings found no equivalent source-specific correction.

## Value

PASS. The paper explicitly states that its numerical figures are generated from equation (5.10), using three terms for Figures 2–8 and iterative terms for Figure 9. Because the printed recurrence is not a recurrence for the stated model, it cannot by itself reproduce those figures as certified model approximations. This affects the paper's computational interpretation rather than merely correcting notation.

## Closest literature and limitations

The predecessor COVID-19 model distinguishes symptomatic and asymptomatic transmission and supplies the intervention architecture, but it does not analyze the later fractional article's recurrence. General decomposition-method literature likewise does not imply the state substitutions identified here.

Unavailable code could have silently used corrected equations, so the finding is limited to the published derivation and reproducibility from the printed formulas. It does not re-audit existence or uniqueness results.

Self-review: passed. Independent audit: not yet performed.
