# Scientific review: sharp quadratic Hankel kernel-testing constant

## Correctness — PASS

The finite Hankel matrix is \(\left(\begin{smallmatrix}\overline a&\overline b\\\overline b&0\end{smallmatrix}\right)\). Its largest singular value and kernel-testing profile follow by direct matrix multiplication. After normalization \(A=1-B^2\), the complete global inequality reduces to \(\max_r F(B,r)\ge25/27\). The proof checks two explicit radii rather than assuming a numerical maximizer: \(r=B\) for \(B\le1/2\), and \(r=1/\sqrt6\) for \(B\ge1/2\). The second bound has a unique equality at \(B=\sqrt{2/3}\). A separate exact quartic factorization proves that at this parameter no untested radius is better, establishing both sharpness and all equality cases. The phase adjustment is valid for arbitrary complex coefficients. At pure monomials the ratio is one. The reproducible finite checker passes, but its grid is not used as proof.

## Originality — PASS, best knowledge

The first-public motivating source (Dyakonov, arXiv:2609.33242v1, 2026-09-27; inspected in the later full version) gives a qualitative quadratic counterexample and a later equality classification, not an optimal degree-two quantitative constant. Two closely relevant published mathematical records classify zero-gap polynomial and finite-rank cases. A recoverable two-monomial historical result supplies local asymptotic strictness, not the global optimum across all coefficient ratios. A logarithmic-Hankel record computes a different, infinite-rank single-symbol gap. Searches for quantitative Garsia/Nehari comparisons, two-by-two Hankel testing, the exact coefficient ratio and the constant did not locate a dominating statement. The distinct normalized parameters and implications were compared, not merely paper titles. A possible older rephrasing as a finite-matrix testing problem remains a real priority risk.

## Mathematical value — PASS

Dyakonov explicitly singles out two-term quadratic symbols as elementary failures of the strong reproducing kernel thesis. The precise worst-case defect on **all** such symbols is a natural sharp uniform invariant of the first nontrivial polynomial class. The optimal constant and unique projective modulus ratio quantify how far a kernel-only test can understate an operator norm. This is a complete exact extremal calculation, not an arbitrarily selected coefficient or a deduction of the already-known equality classification. The result does not claim high-degree or nonpolynomial extensions.

## Closest sources and remaining limits

The full 2026 motivating paper was inspected at its Hankel definition, kernel/Garsia identity, the explicit quadratic counterexample, and the later addendum. Full published-finding corpus documents for the polynomial and finite-rank classifications were inspected. Earlier Treil, Bonsall, and Brevig results were checked through accessible mathematical records and abstracts; their entire original full texts were not independently inspected during this review. This access limit remains an originality risk, although the available statements concern general boundedness or distinct minimal/maximal norm questions.

Self-review: passed. Independent audit: not yet performed.
