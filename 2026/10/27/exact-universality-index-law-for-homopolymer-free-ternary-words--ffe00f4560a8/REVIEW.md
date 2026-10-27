# Scientific review

## Correctness — PASS
Greedy arches equal fixed-alphabet scattered-subsequence universality by a constructive embedding and a last-first-appearing-symbol obstruction. For uniformly sampled adjacent-distinct ternary words, full arch lengths are iid \(2+\operatorname{Geom}(1/2)\). Negative-binomial and binomial identities give the exact counting law. A renewal generating function proves the rational enumerator; a classical renewal CLT and partial fractions prove the asymptotic and moment constants. A standalone independent checker directly evaluates scattered-subsequence spectra through length \(11\) and runs a separate symbolic-mask DP through length \(80\).

## Originality — PASS, with residual uncertainty
General scattered subsequence universality and arch factorization are established in Barker et al. (2020) and Kosche et al. (2021). The algorithm of Adamson et al. (2023) can count universal words of a regular language, and therefore covers the generic computational counting task here. The materially inspected material does not state this ternary adjacent-distinct exact distribution, its binomial-tail closed form, or the iid renewal fluctuation law. The alternative literature might contain a semantically equivalent result under coupon-collector or proper-path-coloring terminology; indexing gaps remain.

## Mathematical value — PASS
For a constrained ternary symbolic source, these formulas determine exact all-length probabilities for full scattered-subsequence coverage, as well as the mean, variance and Gaussian scale of its universality index. The iid renewal structure and explicit binomial tail are useful structural conclusions beyond a finite census or the existence of a counting algorithm.

## Limits and closest literature
The results require linear adjacent-distinct words on a fixed three-letter alphabet; no result is claimed for other alphabets or transition rules. Closest primary papers: Barker et al., arXiv:2003.04629v1 (2020); Kosche et al., arXiv:2108.13968v1 (2021); Adamson et al., arXiv:2311.10658v1 (2023). Complete global originality is not certified, and the checker's finite comparisons do not prove the infinite identities.

Self-review: passed. Independent audit: not yet performed.
