# Independent audit — SCOPE-20260919-c9f0247bbad2

Audited: 2026-10-01 UTC.

Disposition: **passed**.

## Final claim

In rectangular iid-real-Gaussian binary MIMO, at \(\alpha_N\rho_N=2\log N-\log\log N+c+o(1)\), the number of improving Hamming-one neighbors converges to Poisson with mean \(e^{-c/2}/(2\sqrt{\pi})\), equivalently yielding the stated Gumbel one-flip stability threshold and a minimax block-error lower bound.

## Correctness (C) — PASS

For a one-bit flip, the exact objective gap reduces to a quadratic column-norm term plus a Gaussian inner product. Conditional on the common noise vector, the channel columns are independent, so the improvement indicators are iid Bernoulli. Uniform chi-square concentration for both the noise norm and a fresh column norm is strong enough on the \(1/N\) tail scale because \(N^{-1/4}\log N\to0\). Mills’ ratio gives \(NQ(\sqrt{2\log N-\log\log N+c})\to e^{-c/2}/(2\sqrt{\pi})\), and the conditional binomial law therefore converges to Poisson. Each gap changes sign at most once as \(\rho\) increases, so the zero-count probability gives the Gumbel threshold. The minimax lower bound follows from the uniform-prior MAP argument.

**Sources checked.** assigned RESULT.md and check_poisson.py at the audited tree; Papailiopoulos arXiv:2609.19405 abstract for the diverging-slack one-bit converse

**Risks / limits.** The theorem concerns only Hamming-one competitors; it does not determine the full ML critical window.

## Originality (O) — PASS

Papailiopoulos states a one-bit ML converse only below \(2\log N-\log\log N-s_N\) for diverging \(s_N\), while the audited claim resolves the constant window and its limiting count law. Hu–Lu’s Poisson/Gumbel theorem concerns errors of the box-relaxation decoder, a different statistic and threshold. Resultary did not surface an earlier SCOPE claim implying this exact Hamming-one Poisson law.

**Sources checked.** arXiv:2609.19405 abstract and bibliographic record; Hu and Lu, arXiv:2006.08416 / IEEE JSAIT 2020; Resultary semantic search for Gaussian MIMO one-bit Poisson/Gumbel

**Risks / limits.** The full text of arXiv:2609.19405 was not retrievable through the lawful full-text routes attempted. Because its public abstract explicitly states the converse with diverging slack, an unstated constant-window theorem inside remains a residual but not decisive risk.

## Value (V) — PASS

The exact constant-width transition and limiting law sharpen a natural first-order ML threshold obstruction and quantify the probability of local instability precisely where the motivating result leaves a lower-order gap. The result also cleanly separates what one-bit competitors explain from what any unresolved multi-bit obstruction must supply.

**Sources checked.** motivating ML-threshold theorem and the audited critical-window proof

**Risks / limits.** No claim is made that one-flip stability equals global ML recovery.

## Originality comparison

**Equivalent formulations.** The Poisson count statement, the zero-count local-minimum probability, and the Gumbel distribution of the monotone one-flip stability threshold are equivalent formulations of the same Hamming-one extreme-value limit.

**Broader coverage.** Papailiopoulos covers only a diverging-slack one-bit converse; Hu–Lu covers a different box-relaxation error process. Neither implication dominates the constant-window Hamming-one count.

**Exact database or table checks.**

- Resultary: Gaussian binary MIMO one-bit local minimum Poisson Gumbel 2 log N log log N — The audited record was the sole direct hit; no earlier equivalent SCOPE theorem was surfaced.

- primary-literature search: Poisson Hamming-one MIMO Gaussian one-flip Gumbel — Located Papailiopoulos and Hu–Lu; their stated theorems concern, respectively, diverging slack and box-relaxation errors.

**Claim versus prior implication.** Neither prior statement implies the constant-window Poisson law: the diverging-slack probability-one result loses the \(O(1)\) centering, while the box-relaxation statistic is algorithmically and probabilistically different.

## Source inspections

- Assigned package and both committed simulation files inspected from the frozen Git tree.

- Papailiopoulos abstract inspected; full text unavailable after lawful attempts.

- Hu–Lu abstract/bibliographic record inspected.

## Residual risks

- Near-simultaneous or folklore derivations remain possible because the conditional-independence proof is short and the motivating preprint is very recent.

## Scope boundary

Only Hamming-distance-one competitors are classified. The result assumes iid real Gaussian channels and Gaussian noise with aspect ratio bounded away from zero and infinity; it does not establish the full ML lower-order threshold.
