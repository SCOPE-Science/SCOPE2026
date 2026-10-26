# Scientific review: two-season Ricker pulse placement

## Correctness

PASS. The two final stocks are strictly positive on the domain. Direct composition cancels the final-season uncrowded multiplier and yields the exact logarithmic ratio. The derivative of the positive function \(h(z)=e^{-sz}-e^{-z}\) changes sign once and only once, giving exactly zero, one tangential, or two crossing stocks. Its nondegenerate maximum also gives the stated fold asymptotics. The one-step strict inequality and the exact rational sign witness were reconstructed separately. `verify.py` passed 8,000 seeded algebraic/numerical identity comparisons, including 2,207 bracketed two-root cases. Those computations are secondary checks, not an exhaustive proof.

## Originality

PASS subject to material historical limitations. Ricker (1954) introduced the overcompensatory stock–recruitment setting; Jonzén–Lundberg (1999) compared chronological density-dependent events; Abrams (2009) reviewed the hydra effect and equilibrium responses; Liz–Hilker (2014), particularly its sections 2.1–2.2, compared recurring annual early/late harvest models; Grey et al. (2021) studied different variable within-season harvest controls. The inspected material does not present the new claim's exact two-consecutive-season **single** pulse comparison, two initial-stock thresholds, sharp cross-season pressure boundary, terminal multiplier independence, and critical fold. This does not prove global uniqueness. Jonzén–Lundberg (1999) and Ricker (1954) could not be read in complete primary text, while a wider Ricker-map timing or nonlinear rearrangement theorem could logically imply the result. These are substantive residual risks but no decisive covering claim was found in reviewed evidence.

## Value

PASS. The theorem gives a complete and testable intervention-timing phase diagram in an established population-management model, not a standalone algebraic curiosity. The two reversals cannot occur when there is only one recruitment step; the boundary is sharp for every admissible parameter combination; later-season density regulation but not its uncrowded reproductive multiplier changes the boundary. A concrete parameter choice places the reversal inside the locally stable unharvested Ricker regime, so the phenomenon does not merely restate instability or chaotic hydra effects. Its precise two-season scope is also a limitation: no many-season global policy follows.

## Closest sources and unresolved risk

Full accessible science from Abrams (2009), Liz–Hilker (2014) and Grey et al. (2021) was compared with the claim's objects, date of the single harvest, season composition, objectives, and quantifiers. The 1999 Jonzén–Lundberg original was located but its full text could not be opened; the original 1954 paper's abstract and bibliographic information were obtained, not the whole article. The possibility of an uninspected broader composition theorem remains. No assertion of independent assessment is made.

Self-review: passed. Independent audit: not yet performed.
