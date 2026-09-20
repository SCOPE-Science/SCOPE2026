# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The main statement follows from an explicit coordinate decomposition rather than an existence argument. For delta=v-w, the coordinates split into gcd(n,delta) disjoint additive cycles. On each cycle the first canonical map is literally the ordinary odd chi map after reindexing. For the second canonical map, reversal followed by bitwise complementation is an affine involution that conjugates its block rule to ordinary chi. The two parameter cases in the classification theorem of Feng--Wang--Yu--Zhang reduce to these canonical maps by explicit input and output shifts.

The exact affine-class count follows because ell=n/gcd(n,delta) ranges over all divisors ell>1 of the odd part n0, all maps with the same ell reduce to the same Cartesian product, and different ell have different inverse algebraic degrees (ell+1)/2. Algebraic degree of a vectorial map is preserved under invertible affine maps on either side.

The dynamical consequences are restricted to the canonical maps, where genuine conjugacy is available. This avoids incorrectly transferring iteration data through general left-right affine equivalence. The DDT and Walsh formulas are direct products block by block; maximizing over the number of active blocks gives the stated exact scaling.

A standalone exhaustive verifier checks representative dimensions, both canonical conjugacies, the inverse formula, fixed points, order, inverse degree for small feasible cases, the complete classified normal-form reduction in dimension six, and one DDT/Walsh factorization instance. All checks pass. These computations support but do not replace the symbolic proof.

## Originality

**PASS, to the best of our knowledge.** The primary source Feng--Wang--Yu--Zhang, arXiv:2609.19548v1, was inspected beyond the abstract. It proves the complete permutation classification, introduces the two canonical families, partitions indices into additive cycles in the proof machinery, and ends with the remark that the behavior of the iterates of the two canonical families is similar. It does not state the affine Cartesian-product decomposition, an exact affine-class count, the inverse degree of the new family, or the DDT/Walsh factorization consequences.

The ordinary chi literature was checked for the properties imported by the theorem. Schoone--Daemen give the exact order of odd chi and the inverse algebraic degree; these are treated as prior results, not as new claims. Lyu et al., arXiv:2509.20880 / IEEE TIT 2026, study a different generalized chi family and explicitly note a prior CHICHI construction that is EA-equivalent to a concatenation of chi maps. This shows that affine decomposition is a known cryptographic viewpoint, but it does not cover the Feng--Wang--Yu--Zhang family introduced later.

Searches using the new family name and notation together with `direct product`, `Cartesian product`, `parallel copies`, `affine equivalent`, `inverse degree`, `gcd`, and equivalent descriptions did not locate a prior statement of the result. The current SCOPE archive was also checked for the source identifier, generalized-chi terminology, affine-product terminology, and Boolean-permutation terminology; no overlapping record was found.

The main residual originality risk is chronological: arXiv:2609.19548v1 was submitted on 17 September 2026. Its authors already observe similar iterate behavior, and the product decomposition is short once the additive coordinate cycles are reindexed. A near-simultaneous observation, an unindexed note, or a later revision of that preprint could therefore cover the same refinement. The originality claim is deliberately limited to the structural reduction and its stated consequences.

No inaccessible paper was identified as a particularly plausible direct source for this exact result. Older adjacent constructions concern different generalized-chi families and cannot literally contain a theorem about the family first introduced in arXiv:2609.19548, although they remain relevant conceptual prior art.

## Value

**PASS.** The source classification counts many parameter choices but leaves their internal structure largely implicit. The product theorem collapses them to one ordinary odd chi block length ell, yielding exactly tau(n0)-1 affine types instead of a parameter-level list. It immediately determines inverse degree and, for the canonical maps, order and fixed-point/cycle data. It also shows that the normalized maximum differential probability and linear correlation of the larger map are exactly those of chi_ell, a concrete cryptographic consequence of the structural reduction.

The result does not claim a break of any complete primitive. A surrounding linear layer can mix the independent nonlinear blocks, and the theorem concerns the nonlinear permutation layer itself.

## Verdict

Correctness: PASS.  
Originality: PASS, to the best of our knowledge.  
Value: PASS.

**Same-model review: passed. Independent audit: not yet performed.**
