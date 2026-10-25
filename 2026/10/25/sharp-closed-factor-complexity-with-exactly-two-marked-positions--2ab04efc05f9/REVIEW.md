# Scientific assessment

## Correctness

**PASS.** All factor types are handled. A factor with both marked symbols has a marker-bearing border exactly when both outer zero-gaps are at most the middle gap; a zero-only border supplies the diagonal cases. Closed palindromes contribute exactly the word length, and the off-diagonal marker-bearing factors contribute the product correction. The max problem is an exact two-integer optimization, not an inference from finite data. The bundled checker independently reconstructs 680 complete closed-factor sets through length 16, confirms all maxima through length 100, and checks the zero/one-marker boundary through length 34. Main limitation: no separate formal proof certification.

## Originality

**PASS with residual priority uncertainty.** Badkobeh–Fici–Lipták establish the general closed-factor theory, the empty-word convention, and the possibility of quadratic behavior; their unrestricted length table and a block-rich construction do not imply the sharp two-one formula or optimizer list. The 2016 closed-factorization paper concerns substring algorithms, but its full manuscript could not be examined, so an undocumented special-case theorem cannot be ruled out. A search across complete-return, periodic-like, closed-factor, and fixed-Hamming-weight terminology, indexed related results, and the accessible original research records found no dominating statement. Negative searches alone do not prove novelty.

## Value

**PASS.** The exact formula yields a complete sparse-family classification with sharp all-length maximizers and identifies the minimum number of minority-symbol occurrences needed for quadratic closed-factor richness. This strengthens the qualitative interpretation of the classical quadratic construction: a single marker gives linear complexity, but two markers already produce a quadratic family. The exact constrained extremum and limiting average are natural quantities independently motivated by closed-factor complexity, rather than arbitrary finite table entries.

## Sources and limits

Primary: G. Badkobeh, G. Fici, and Zs. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395 (2013). Relevant but not fully accessible: G. Badkobeh et al., *Closed factorization*, Discrete Applied Mathematics 212 (2016), 23–29, doi:10.1016/j.dam.2016.04.009. Prior results on unrestricted maxima do not settle the fixed-weight-two question. The bounded primary-text access risk remains explicit, and independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
