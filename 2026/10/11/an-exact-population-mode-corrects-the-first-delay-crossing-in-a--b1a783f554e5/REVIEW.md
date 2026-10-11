# Same-model review

## Correctness
PASS. The claim is restricted to the system actually displayed as equation (5.1). Exact rational substitution verifies the equilibrium. Exact determinant expansion verifies the delay-independent factor \(50\lambda+1\) and the reduced cubic-plus-quadratic delay equation. The unique positive imaginary frequency follows from a cubic whose derivative is positive for every \(u>0\); the zero-delay reduced cubic passes the exact Routh--Hurwitz test, and implicit differentiation gives a positive crossing speed. The packaged verifier independently replays these steps.

Risk: the prose parameter line above (5.1) gives a different natural-removal value from the displayed equations. The claim therefore says explicitly that it concerns the displayed system and does not infer authorial intent.

## Originality
PASS. The closest source is Wang et al. itself: it states the same displayed equations but reports a different equilibrium approximation, frequency and critical delay, and does not use the exact total-population factorization. The nondelayed Saha--Samanta model has no delay threshold. The two-delay Zhang--Yang--Xia model has different compartments and transfer terms, so its characteristic equations do not imply this correction. Searches by DOI, title, exact reported values, correction/corrigendum language, factorization language and the corrected threshold found no statement covering the claim.

Risk: absence from searched indexes is not a proof that no unindexed note or private calculation exists.

## Value
PASS. The source uses the critical delay to delimit local stability and to place its numerical simulations on opposite sides of a Hopf threshold. Correcting the first characteristic crossing from \(5.105862\) to \(5.3176961657\ldots\) changes that quantitative stability boundary, while the exact factorization explains structurally why the four-dimensional characteristic calculation contains a redundant population mode. This is a mathematically motivated correction to a published bifurcation benchmark, not a routine recomputation of an arbitrary parameter slice.

Risk: the nonlinear direction and stability of the periodic branch are not established at the corrected crossing and remain outside this claim.

## Closest literature and limitations
The direct source is Wang et al., DOI 10.3934/math.2021001. Saha--Samanta, DOI 10.1080/23737867.2019.1624204, supplies the nondelayed ancestor. Zhang--Yang--Xia, DOI 10.1155/2019/3492589, is a distinct two-delay synthetic-drug model and does not dominate the present statement. The scientific limitation is deliberately linear: the corrected first imaginary crossing is proved, while the source's nonlinear normal-form conclusions are not transferred to it without a fresh calculation.

Same-model review: passed. Independent audit: not yet performed.
