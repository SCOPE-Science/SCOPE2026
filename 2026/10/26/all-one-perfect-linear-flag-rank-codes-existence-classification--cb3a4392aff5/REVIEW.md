# Scientific review

## Correctness

**PASS.** The corner-block support interval argument proves that every vector of flag-rank weight below \(3\) is either supported on at most two diagonal positions or on one first-superdiagonal entry with its adjacent diagonal entries. The resulting three parity-check conditions are necessary and sufficient. The standard projective-point count gives perfect syndrome coverage, while a three-direction dependency gives minimum distance exactly \(3\). The number of maps and the free postcomposition quotient by \(\mathrm{GL}(\alpha,q)\) yield the exact labeled-subspace count. The finite checker ran successfully on selected small prime fields; this does not replace the field-general proof.

## Originality

**PASS, with residual risk.** Alfarano–Neri–Zullo, arXiv:2303.16653, Proposition 4.19 and Construction C already give the central neighboring-line avoidance mechanism for three-dimensional parity-check spaces. Alfarano–Mushrraf–Zullo, arXiv:2606.12934, Theorem 5.4 gives the necessary length equation conditional on an existing distance-three code, and Theorem 5.8 constructs the codimension-three case. These ingredients are credited. Their inspected statements do not establish the all-codimension construction or the complete labeled-code count. Relevant literature searches did not identify equivalent statements; unindexed prior derivations remain possible.

## Value

**PASS.** Existence and enumeration of perfect radius-one codes are natural, not arbitrarily selected, parameters in a recently developed network-coding metric. The result closes the entire minimum-distance-three linear existence profile beyond the previously exhibited codimension, and identifies exactly which high-superdiagonal freedoms preserve perfectness. A closed formula counts all labeled code subspaces, not merely one construction.

## Limits

Only linear flag-rank minimum-distance-\(3\) codes are classified. Nonlinear codes, larger packing radii, and equivalence classes under metric isometries are not determined. The proof applies to finite fields of prime-power order; computations cover selected prime fields only. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
