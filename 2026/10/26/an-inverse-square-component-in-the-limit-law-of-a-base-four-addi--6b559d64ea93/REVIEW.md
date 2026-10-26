# Mathematical review: limiting counting ratio for a base-four additive complement

## Correctness — PASS

The claim concerns the exact digit pair \(A=\{\sum\epsilon_j4^j\}\), \(B=2A\). Base-four digit uniqueness proves an exact complement and the counting lower bound. The finite CDFs of its normalized counting functions approximate the two Cantor CDFs with uniform \(2^{-k}\) errors. The explicit coupling between a uniform integer in \(\{1,\ldots,4^k\}\) and a uniform real point, together with a harmonic-sum calculation, proves \(W_1=O(k2^{-k})\). The known finite-digit argument gives the necessary global ratio range \([1,3/2]\). Since \(C\cup2C\) has Lebesgue measure zero, the complement is a full-measure union of intervals on which the CDF product is constant; inverse change of variables proves an absolutely continuous law and the exact density series. Two explicitly disjoint geometric gap families give density \(2/t^2\) on \((1,3/2)\) and exactly \(2/3\) of its mass. The depth-\(L\) cylinder cover bounds the missing CDF mass by \(2^{-L}\). The standalone exact-arithmetic `verify.py` checks the finite ingredients. No finite calculation is presented as a proof of an infinite statement.

## Originality — PASS, subject to external priority review

The September 12, 2026 Yang–Zhao paper gives a universal limsup threshold, not a sampled-ratio distribution. Zhang's October 21, 2026 paper explicitly proves sharpness of the same base-four pair at \(3/2\), which is recognized as prior knowledge, not a novelty claim. Ma's 2022 paper gives additive-complement constructions and limsup formulas; the inspected text does not state a limiting density. The new statement specifies a Wasserstein convergence rate, exact countable density, the \(2/3\)-mass inverse-square subcomponent and certified finite CDF approximations; none follows merely from the previously known limsup \(3/2\). Searches comparing aliases such as four-adic digit tilings, Cantor probability-factorization and additive-complement count ratios did not locate an equivalent published assertion. The full 2011 Chen–Fang article was not accessible and is a genuine residual risk; other unindexed distribution theorems may also subsume the result. The failure to locate them is not treated as a proof of global uniqueness or independent priority.

## Mathematical value — PASS

The counting ratio of a pair of additive complements is central to the contemporary sharp-threshold problem, but a limsup does not reveal what happens for a randomly sampled integer. The theorem determines the complete distribution in an explicit convergent form with quantitative convergence, and identifies a large, exact inverse-square component of mass \(2/3\) that would be invisible from an extremal bound. Its complementary \(1/3\) mass is still absolutely continuous, and every CDF value has an exact rational error enclosure. The setting is a standard published extremal example, not an arbitrarily parameterized finite computation.

## Closest literature and scientific limits

Sources inspected materially: Yang and Zhao (arXiv:2609.13900v1, introduction, theorem and sections 2–4); Zhang (arXiv:2610.29963v1, theorem, proof text and section 6 of the eight-page PDF); Ma (arXiv:2205.04128v1, theorem and construction sections). Chen and Fang, *On additive complements, II* (2011) was confirmed bibliographically but its full text was not accessible for a direct statement comparison. The claim is for one fixed digit complement, not all additive complements. An elementary closed form for the remaining density and an independent priority determination are not claimed.

Self-review: passed. Independent audit: not yet performed.
