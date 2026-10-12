# Scientific review: exact limited domination of rectangular rook graphs

## Correctness — PASS
The argument uses the exact outside-neighbor identity \((n-\rho_i)+(m-\kappa_j)\) for selected squares. Domination forces one whole orientation to have no empty line, and summing the induced occupancy lower bound gives the stated minimum. Whole-row or whole-column constructions attain the bound in every parameter range, including both endpoints. Equality in the occupancy inequalities proves the exhaustive low-capacity optimizer classification. A separate exhaustive adjacency-based program checks 14 complete boards, 93 capacity instances and all optimum counts at low capacity, finding no discrepancy. Computation is supportive rather than an infinite proof.

## Originality — PASS (with identified residual risks)
Božović et al., arXiv:2606.22422, define the invariant and give complete-graph values. Tepeh, arXiv:2606.22428, gives the relevant Cartesian-product **upper** bound (Theorem 7) and a single sharp diagonal family \(K_{k+2}\square K_{k+2}\) (Proposition 8) in the materially inspected first version. Neither assertion yields the matching lower bound for arbitrary rook graphs or the present optimizer classification. The revised October 2026 version was identified but its complete text remained inaccessible, and older unindexed \((1,t)\)-domination formulations could conceivably duplicate the claim. Those are documented risks, not assurances of global novelty.

## Value — PASS
Rectangular rook graphs form a canonical infinite Cartesian-product family singled out by the motivating paper. Rather than giving another isolated tightness example, the theorem settles the product bound on the entire three-parameter family and identifies all low-capacity extremizers. The resulting line-occupancy rigidity explains why no irregular selection can improve on complete coordinate slabs in that range. This is a natural completion of the paper's specific square extremum, with clear scope limits.

Self-review: passed. Independent audit: not yet performed.
