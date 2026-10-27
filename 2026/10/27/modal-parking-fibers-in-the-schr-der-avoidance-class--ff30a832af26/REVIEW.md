# Scientific review: modal parking fibers in the Schröder avoidance class

## Correctness — PASS

The claim concerns the maximum \(M_n\) of the established parking-permutation fiber product over \(\operatorname{Av}_n(1234,2134)\). The central new step is an **exact**, not one-sided, decomposition at the global maximum of a permutation. The left segment avoids \(123\) and \(213\); the unrestricted-right-segment factorization follows because the global maximum blocks all leftward suffix lengths. A skew value separation supplies an avoiding construction attaining each candidate recurrence term. This establishes the max-product recurrence for every \(n\). The proof then eliminates all composition parts outside \(\{3,5\}\) for \(n\ge8\) via explicit strictly improving replacements, and uses \(20^3>6^5\) to obtain the unique optimal residue representation. Boundary orders \(1\) through \(7\) are treated separately. The supplied checker independently enumerates all avoiding permutations through order nine, directly simulates preferences through order five, and compares the formula against the recurrence through order 150. Computation is only corroboration; the unrestricted proof is in RESULT.md.

## Originality — PASS (bounded published-record comparison)

Martinez–Zeilberger, arXiv:2609.28650v1 (2026-09-23), explicitly studies these same forbidden outcome patterns, introduces parking-table weights, and gives a scheme for the **sum** over their weights. The present theorem determines their **maximum**, including a finite reduction to weighted compositions and an eventual exact five-step law. This maximum is not implied by knowledge of the total count. The earlier general fiber-product identity (Colmenarejo et al., arXiv:2009.01124) and unconditional permutation probability formula (Pinsky, arXiv:2404.11529) do not optimize over this avoidance class. Searches of accessible published mathematical records, primary literature, mathematical search results and the precise initial sequence found no matching stronger claim. Accessible past mathematical records concerning different pattern classes and parking-polytope geometry do not subsume the theorem. The motivating preprint's main-result section could not be reopened in full during the review; that access limitation and the possibility of unindexed equivalent literature remain explicit residual risks. No absence-of-hits search is treated as proof of uniqueness.

## Mathematical value — PASS

The mode of an outcome distribution is a basic extremal statistic not supplied by a total enumeration. For the naturally selected Schröder avoidance class, the result gives an exact value at **every** order, an explicit construction, the eventual five-step multiplier, and the exponential growth rate. The argument explains why a maximum problem on permutations reduces to an optimized composition problem and why blocks of sizes three and five ultimately govern the answer. This is not a numerical extrapolation from a finite table or a mere reformulation of the known fiber product.

## Closest sources and limits

- L. Martinez and D. Zeilberger, *A parking function analog of the Schröder numbers*, arXiv:2609.28650v1, https://arxiv.org/abs/2609.28650 , introductory definitions, Lemma 2.1, total-enumeration objective.
- L. Colmenarejo et al., *Counting k-Naples parking functions through permutations and the k-Naples area statistic*, arXiv:2009.01124, https://arxiv.org/abs/2009.01124 , general product formula.
- R. G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529, https://arxiv.org/abs/2404.11529 , unconditional permutation distribution.

Bibliographic priority cannot be fully guaranteed by accessible searches. The formula does not classify all maximizing permutations or extend to other parking rules. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
