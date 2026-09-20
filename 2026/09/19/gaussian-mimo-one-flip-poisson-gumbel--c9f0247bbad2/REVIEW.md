# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The one-bit objective gap is exact:
\[
f(x^{(i)})-f(x^\star)=4\left[(\rho/N)\|h_i\|^2+\sqrt{\rho/N}\,h_i^Tw\right].
\]
Conditioning on the common noise vector makes the improving-neighbor indicators independent because the channel columns are independent. Chi-square concentration places both \(\|w\|^2\) and \(\|h_i\|^2\) at their dimensions with relative error \(N^{-1/4}\), whose effect on the Gaussian tail exponent is \(O((\log N)N^{-1/4})=o(1)\). Hence the conditional success probability is uniformly \((1+o(1))Q(\sqrt{\alpha_N\rho_N})\) on a noise event of probability \(1-o(1)\). Mills' ratio gives the stated constant \(e^{-c/2}/(2\sqrt\pi)\), and conditional binomial-to-Poisson convergence completes the proof. The Gumbel centering follows algebraically from the zero-count probability. The minimax corollary is a standard uniform-prior MAP lower bound and is stated only as a lower bound.

The finite simulation artifact independently checks the limiting constant and zero-count probability for square and rectangular examples; it is supporting evidence rather than a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** The primary motivating source, Papailiopoulos (arXiv:2609.19405), was inspected beyond the abstract. It explicitly derives the heuristic scale from \(NQ(\sqrt\rho)\), proves failure below \(2\log N-\log\log N-s_N\) for diverging \(s_N\), and states that its theorem does not determine the complete lower-order window. No Poisson limit for the count of improving one-bit neighbors, no Gumbel law for the local-stability threshold, and no rectangular \(\alpha\rho\) formulation were found there.

The closest identified prior limiting-law result is Hu--Lu (arXiv:2006.08416), which proves a Poisson/Gumbel transition for the box-relaxation decoder. Its statistic and threshold are different: the square-model refined threshold is \(4\log N-2\log\log N+O(1)\), not the one-bit maximum-likelihood obstruction at \(2\log N-\log\log N+O(1)\).

Targeted searches included combinations of “one-bit neighbor”, “Hamming-one”, “local minimum”, “Poisson”, “Gumbel”, “Gaussian binary MIMO”, and the exact \(2\log N-\log\log N\) scale. No equivalent result was located. The current SCOPE archive was also searched by the motivating arXiv identifier and by MIMO / one-bit-local-minimum terminology, with no overlap found. Because the theorem is a short extreme-value refinement of a heuristic already visible in a very recent preprint, folklore and near-simultaneous priority risk are material; the novelty claim is restricted accordingly.

No highly relevant inaccessible paper was identified whose title or available description specifically suggests this one-bit critical-window law. This does not eliminate unindexed or unstated prior coverage.

## Value

**PASS.** The result replaces a divergent-slack one-bit converse by the exact \(O(1)\) critical-window law, identifies the full limiting distribution of the planted word's local-stability SNR, extends the obstruction to bounded rectangular aspect ratios through the effective parameter \(\alpha\rho\), and gives an explicit constant-window minimax error lower bound. It also sharply separates what is resolved locally from the still-open question of whether farther Hamming competitors alter the full ML critical window.

## Limitations checked

The proof does not control competitors at Hamming distance at least two and therefore cannot be advertised as an exact ML threshold. It does not establish a new polynomial-time recovery theorem, nor does it cover correlated/non-Gaussian channels, coded MIMO, or finite-precision complexity.
