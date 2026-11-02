# Review of a sharp uniqueness threshold in randomized apportionment

## Correctness — PASS

The claim concerns exactly three different lower-quota strata with strictly ordered residues within each. Zero envy is equivalent to selecting top-residue suffixes in each stratum. The normalized probability vector obeys an explicit zero-one marginal matrix. For all four possible three-part size patterns with at most five parties, all nontrivial surplus sizes are covered by thirteen nonzero maximal minors, each of determinant \(+1\) or \(-1\). Boundary surplus sizes admit only one deterministic outcome. The six-party witness uses two distinct probability tables; exact marginal checks give low/high round-up probabilities \((1/5,4/5)\) in every block. Both an independent computer algebra rank check and the packaged standard-library exact-rational verifier corroborated the determinants. No infinite-size assertion is made.

## Originality — PASS, with residual priority risk

La Commare, Tucker-Foltz and Verdugo (arXiv:2610.24217), especially Sections 2.2 and 4.2 and Proposition 4.2, provide the correct block-flow existence formulation but neither the complete below-six rank classification nor the minimum size for failure of distributional uniqueness. Earlier exact two-block uniqueness and six-party three-pair feasibility/transportation results are adjacent but do not supply the universal five-party three-stratum uniqueness theorem; the six-party behavior is acknowledged as established context. The claim is not new polynomial-time feasibility, and the overlapping block-specific existence criteria are not claimed as new. Unindexed equivalent work remains possible.

## Value — PASS

Uniqueness is an operationally relevant feature: when a perfectly fair proportional quota lottery exists, it is determined by the parties' marginal entitlements, without any further choice of correlation policy. The result determines the first possible party count at which multiple such choices can exist with precisely three lower-quota strata. The sharp, finite structural cutoff distinguishes a rigid small market from a genuine transportation degree of freedom, rather than merely presenting one numerical counterexample.

## Scope and limitations

The theorem is conditional on existence and requires exactly three distinct floor values, strictly ordered residues within each stratum, quota-respecting roundings, integer total seats, and exact ex-ante proportionality. It does not characterize models with ties, more floor levels, or nonzero unavoidable envy. Scientific priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
