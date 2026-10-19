# Scientific review

## Correctness — PASS

The proof has four self-contained steps: existence of the normalized expectation by superadditivity; an exact geometric waiting-time factorization for a fixed target word; an independent-source union bound yielding a finite-parameter upper envelope; and a strict-gap expansion for the uniquely most likely letter. The ratio expansion uses \(t_d=(\log d)/(d\Delta)\), controls every less frequent letter by \(O(d^{-1})\), and checks positivity of the logarithmic denominator. A separate law-of-large-numbers argument proves the lower baseline. Explicit exhaustive finite experiments test the embedding and event inequalities, but are not used to prove an infinite limit.

## Originality — PASS within inspected evidence

The closest theorem by Li, Ren, and Wen (arXiv:2504.10425, full openly available article inspected) treats independent *uniform* sources and proves an excess of order \(d^{-1/2}\) for the binary case. Neither its main statements nor its relevant proof sections cover the present **strictly nonuniform** source or its \((\log d)/d\) upper scale. Nikolić et al. (doi:10.3390/math9131515) treat nonuniform input probabilities in finite-instance LCS search and an embedding recurrence, rather than the many-string normalized expectation; direct access to their article was rate-limited, but substantial indexed text was examined. Relevant existing findings on random *substrings*, deterministic periodic-word LCS, and subsequence universality do not imply a many-i.i.d.-string biased LCS bound. These are comparison-of-claims judgments, not deductions from titles or an assertion that an unsuccessful search establishes uniqueness.

## Value — PASS

The originating multiword LCS question establishes a square-root-order excess in the uniform binary case. The strict-bias theorem proves a qualitatively smaller excess for every fixed nonuniform i.i.d. source with a unique maximizer, and gives a usable explicit finite-\(d\) variational bound. It identifies a natural boundary between distinct source regimes, with an analytic coefficient controlling the upper limit. This is a motivated asymptotic result, not a renamed finite computation.

## Residual limitations

The displayed coefficient is not proved optimal, there is no matching lower rate, and finite enumeration cannot show an infinite asymptotic. Tied maximal symbol probabilities are outside the theorem. Earlier unindexed equivalent analyses and inaccessible material remain possible historical-priority risks; the relevant nonuniform-LCS paper's direct page fetch was rate-limited. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
