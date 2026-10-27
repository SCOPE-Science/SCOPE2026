# Self-review

## Correctness — PASS

Both sides of the sharp threshold are proved: for every allowed shift, a maximal-sum argument eliminates cycles using exponent at least two and an alternating-matching argument eliminates cycles on the first two sums; for every excluded shift, the explicitly indexed \(2(b+1)\)-vertex sequence is a simple cycle. The published forest criterion [1, Theorem E] connects the graph statement with all positive pattern lengths, while [1, Theorem 7.4] gives a strictly larger complexity value at the displayed pattern size. The bases \(b=2\) and \(b\ge3\), the threshold equality case, all nonnegative integer endpoints, and the unbounded zero gaps have been checked. The accompanying finite verifier checks graph edges and cycles but cannot itself certify the infinite theorem.

## Originality — PASS within checked evidence

The closest primary source is [1]. Its Theorem E gives an iff graph framework; Proposition 7.12 supplies a strong sufficient gap hypothesis; Example 7.13 already identifies the unshifted base-two and base-three cases. The precise sharp shift threshold, arithmetic converse, and explicit boundary cycles were not found in its inspected sections. This is a new complete specialization with proof, not a claim to the general graph criterion or those known examples. Searches over indexed mathematical results yielded a distinct logarithmic support-envelope result for a negative shift, not this nonnegative-shift classification. The two-dimensional background paper [2] does not imply it. An unindexed equivalent proof remains a priority risk.

## Mathematical value — PASS

The theorem completes a natural parameter perturbation of canonical lacunary binary words, including a sharp arithmetic transition for every base, concrete forbidden cycles at and above threshold, and an explicit positive complexity gap. This supplies usable family-level structure for an invariant introduced and classified abstractly in recent literature, beyond a single example or routine numeric increment.

## Limitations

The invariant is Abelian maximal pattern complexity of nonnegative-shifted powers only. The result does not determine the full complexity profile of nonextremal shifts, or shortest possible cycles. Published [1] is relied upon for the graph-word equivalence and quantitative cycle implication. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Q. Zeng, Y. Xue and C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059v2, especially Theorems E and 7.4, Proposition 7.12, Example 7.13.

[2] Q. Zeng, Y. Xue and C. Zeng, *Abelian maximal pattern complexity of two-dimensional words*, arXiv:2608.21084.
