# Independent mathematical audit — SCOPE-20260920-fc9ef1319daf

Final disposition: **PASS**.

## Correctness
**PASS** — The contradiction is exact. In Martín Duro's Type-II case the two one-dimensional modules fix each three-dimensional simple, so the relevant grouplike stabilizer has order two. For an irreducible character of a semisimple Hopf algebra, the standard Nichols-Zoeller consequence gives that the stabilizer order divides the square of the character degree. Hence two would have to divide nine. Dualizing handles a right-versus-left tensor convention without changing the contradiction. The source classification then removes its sole stated exception below dimension 32.

## Originality
**PASS** — The complete primary classification retains the dimension-24 Type-II case as its sole exception, and the primary stabilizer theorem supplies the classical divisibility input but not this correction. Targeted current searches found no separate correction or stronger published result eliminating the exception. The contribution is therefore the specific application closing the published case, not the general stabilizer theorem.

### Equivalent formulations
The correction was compared in the source's own representation-ring/stabilizer language.

### Broader coverage
The final correction requires combining the source's specific Type-II action with the classical stabilizer constraint; no inspected source had already made that combination.

### Exact database or table
The classification table is explicitly the object corrected; its unique exception is not a known valid example.

### Claim versus prior implication
The mathematical proof is short, yet it is a correction to a published conclusion rather than a previously stated corollary.

## Value
**PASS** — A one-line obstruction can still be valuable when it removes the unique exception in a published finite-dimensional classification. Here it upgrades the source conclusion to an unconditional dimension-at-most-31 theorem and corrects a concrete realizability oversight.

## Source inspections
- **The Knutson Index of the Representation Ring** (https://arxiv.org/abs/2211.08123): full primary text around Corollary 2.32 and the dimension-24 Type-I/Type-II analysis Method: primary full-text inspection. Assessment: PRIMARY_SOURCE_RETAINS_THE_EXCEPTION. Evidence: The paper explicitly treats Type II as the sole possible non-Knutson case below dimension 32 and states that the one-dimensional modules act trivially on the three-dimensional simples.
- **On fusion categories with few irreducible degrees** (https://arxiv.org/abs/1103.2340): full primary PDF section defining the character stabilizer and stating that its order divides the square of the character degree Method: primary full-text inspection. Assessment: CLASSICAL_INPUT_NOT_PRIOR_CORRECTION. Evidence: The theorem gives the divisibility needed for the contradiction but does not discuss the Knutson classification.

## Checked sources
- https://arxiv.org/abs/2211.08123
- https://arxiv.org/abs/1103.2340

## Residual risks
- An unindexed erratum or informal correction to the 2024 classification could exist.
- The dimension-at-most-31 conclusion inherits the correctness of the source's remaining case analysis.
