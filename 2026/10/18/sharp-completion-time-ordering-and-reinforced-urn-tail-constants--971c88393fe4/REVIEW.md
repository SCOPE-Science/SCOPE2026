# Scientific review: sharp balanced-urn completion bounds

## Correctness

**PASS.** The finite-population balancing lemma follows from a single-ball recoloring coupling and monotonicity of a ratio of binomial coefficients. Strictness uses a genuinely deficient randomly generated comparison population. The independent-draw comparison follows from the differentiated central binomial tail and the nondegenerate Dirichlet representation. For the reinforced upper tail, exact beta-binomial fixed-count asymptotics and an \(O(k^{-2a})\) bound on pairwise deficiencies yield the stated positive coefficient, with the two-color exceptional case handled separately. Summation by parts proves the fractional-moment cutoff. Exact independent recurrence checks are supportive rather than exhaustive.

## Originality

**PASS on inspected evidence, with residual uncertainty.** Jacobs, *Urns & Tubes*, arXiv:2110.02155, describes the three sampling modes but does not state the strict all-horizon multicolor completion hierarchy or the full sharp leading constant in the inspected material. Anceaume et al., arXiv:1504.03878, optimize uniform independent coupon collection of distinct types, which does not imply the cross-mode comparison or the reinforced multiple-copy tail constant. Henze and Holmes, arXiv:1911.01052, treat Pólya waiting times and moment phenomena for individual colors; they do not give the combined multicolor leading coefficient. The remaining risk is a classical general majorization theorem or non-indexed occupancy result implying a part of the claim under different terminology. No independent historical uniqueness check is claimed.

## Value

**PASS.** The problem is a natural reliability and coupon-completion comparison: the urn population begins with the same balanced physical inventory, but three standard observation mechanisms affect simultaneous coverage differently. A uniform, strict, finite-horizon comparison across all numbers of categories and feasible copy targets is a structural classification, while the precise heavy-tail constant and exact cutoff \(s<a\) distinguish the reinforced regime quantitatively from the bounded and exponential-tail alternatives. These conclusions are more informative than a single finite enumeration or routine parameter substitution.

## Limitations

The theorem is restricted to balanced integer-initialized urns with one extra same-color ball per reinforced draw, and fixed integer observation targets not exceeding initial multiplicity. No parameter-uniform asymptotics, pathwise coupling, or absolute priority is asserted. Materially similar results under different terminology remain a research-history risk.

Self-review: passed. Independent audit: not yet performed.
