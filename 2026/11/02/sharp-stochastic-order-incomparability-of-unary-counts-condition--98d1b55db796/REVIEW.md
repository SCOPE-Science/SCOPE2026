# Self-review

## Correctness — PASS

The model is a uniform plane tree of \(n+1\) vertices conditional on root degree \(k\), bijective to a uniform ordered \(k\)-forest on \(n\) vertices. The generalized cycle lemma gives the factor \(k/n\), the degree-word generating function gives the complete mass function, the path-composition count identifies the maximum unary event, and the one-edge remainder rules out the next-lower count. The ratio is algebraically \((2n-k-1)/(k+1)\), strictly greater than one for \(k\le n-2\), and the two adjacent thresholds go in opposite directions. A separate boundary argument covers \(k=n-1\). The delivered Python verifier passed 26,310 exact checks, including independent tree enumeration. Finite checks are corroboration, not an infinite proof. No unproved nonstandard combinatorial assertion is needed beyond the classical cyclic lemma with its stated admissibility condition.

## Originality — PASS, with historical-priority risk

The classical forest count and degree-profile coefficient are acknowledged and not claimed as new. The claim assessed for originality is the exact all-parameter stochastic incomparability, adjacent threshold witnesses and one deterministic exception. The 2011 random-forest reference and the 2013 degree-count reference contain general models and asymptotic conclusions; their inspected relevant passages did not provide this finite cross-root-degree comparison. The accessible abstract of the 1999 degree-distribution work addresses asymptotics, but its full text was not read. An earlier general degree-count formula might imply the result on specialization, and the literature search is not a proof of novelty; this remains a substantive priority risk. That risk should be checked independently before publication.

## Mathematical value — PASS

Unary nodes are precisely the degree-one subdivision vertices in a rooted tree, so they determine contraction of maximal chains. Root degree is the natural forest-component parameter. The theorem gives a complete distributional boundary: balancing the forest into more components increases the probability of a near-maximal unary count but eliminates the previous maximum. This structural conflict is not visible from mean-only analysis or the distributional ordering of leaves. It holds uniformly over all tree sizes and every adjacent root-degree pair, rather than being a single small counterexample.

## Scope and limitations

Only adjacent root-degree comparisons and nonroot unary counts are classified. The accessible relevant primary sections were read and compared; a plausible 1999 full text remains unavailable, and implicit theorem coverage is not excluded. Self-review is not independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
