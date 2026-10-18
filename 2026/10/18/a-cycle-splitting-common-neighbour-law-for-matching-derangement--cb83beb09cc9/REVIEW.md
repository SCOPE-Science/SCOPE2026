# Review: cycle splitting in matching derangement graphs

## Correctness — PASS

The exact identity is obtained from the independently verified, fully specified inclusion-exclusion functional for forbidden-edge matchings and the transfer-matrix formula for even-cycle matching polynomials. The identity \(C_{2m}(z)^2-C_{4m}(z)=2z^{2m}\) has no exceptional case for \(m\ge2\), and shifting the inclusion-exclusion index leaves exactly twice the residual common-neighbour count. Positivity is proved for residual order at least four using explicit complements in order four and the minimum-degree Hamiltonicity bound thereafter; the residual orders zero and two are treated separately. The coloured-graph consequence follows from regularity and from the full automorphism group identified in Godsil–Meagher, Lemma 10.1.

The two supplied exact-integer verification implementations have been run successfully. These finite computations are corroboration, not substitutes for the quantified proof. No assertion about the full stable partition or a universal three-round upper bound is made.

## Originality — PASS, with priority risk

The highly relevant original Godsil–Meagher paper, arXiv:1506.08770, was examined for the matching derangement graph, its association scheme, and its automorphism lemma. It does not state the equal-cycle splitting law or its counting-refinement obstruction. The full-text Kersting–Mladenov–Garnett–Grohe article (AAAI 2014) concerns general colour-refinement algorithms and fractional automorphisms, rather than this perfect-matching geometry. Searches for aliases involving common neighbourhoods, perfect-matching derangements, switching even alternating cycles, association-scheme parameters, counting logic, and two-round refinement did not uncover a matching claim in the checked research records or published searches. An exact previous publication could still exist, particularly as a corollary of general association-scheme intersection-number formulae; negative searches do not prove priority.

## Value — PASS

The graph family is a natural, highly symmetric family already studied in extremal and algebraic combinatorics. The identity gives an exact local-counting change under a structurally meaningful operation on orbit labels and pinpoints the **unique residual size** at which this change vanishes. That vanishing produces a uniform infinite family of genuine orbit distinctions invisible through the second full colour-refinement round. This is a motivated structural lower bound, not a numerical coincidence or a finite-table recomputation.

The result does not claim universal colour-refinement failure or global optimality for all ranks. Its finite census is explicitly marked as finite evidence.

Self-review: passed. Independent audit: not yet performed.
