# same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately as correct, original to the best of our knowledge, and useful. This is not independent validation or peer review.

Same-model review: passed. Cross-model review: not yet performed.

## Correctness audit

The proof was checked against the following failure modes.

1. **One-sided constant.** Roth's proof of ATE McDiarmid gives the one-sided tail directly before obtaining the two-sided statement by applying it to the negative function. For an empirical indicator average, changing one coordinate changes the statistic by at most \(1/n\), so \(\sum_i c_i^2=1/n\) and each one-sided endpoint deviation is bounded by \(\exp(-2nt^2/\kappa)\).
2. **Heterogeneous marginals.** The center is \(\bar P=n^{-1}\sum_i P_i\), exactly the expectation of \(P_n\). No identical-distribution assumption is used.
3. **General bracketing step.** If \(L\subseteq A\subseteq U\) and \(\bar P(U\setminus L)\le\varepsilon\), the positive deviation of \(A\) is controlled by the positive deviation of \(U\) plus \(\varepsilon\), while the negative deviation is controlled by the negative deviation of \(L\) plus \(\varepsilon\). A union bound over the two endpoints of each finite bracket therefore gives the stated factor \(2B\).
4. **Atoms and repeated quantiles.** For \(q_j=\inf\{x:\bar F(x)\ge j/N\}\), right continuity gives \(\bar F(q_j)\ge j/N\) and the left-limit property gives \(\bar F(q_j-)\le j/N\). Grouping repeated quantiles into distinct values yields \(\bar F(b_{k+1}-)-\bar F(b_k)\le1/N\), including the two infinite endpoints.
5. **Strict versus non-strict thresholds.** This distinction is essential at atoms. The upper bracket uses \(\mathbf 1\{X_i<b_{k+1}\}\), whose mean is \(\bar F(b_{k+1}-)\), while the lower bracket uses \(\mathbf 1\{X_i\le b_k\}\), whose mean is \(\bar F(b_k)\). This avoids inserting an atom into the bracket width.
6. **Endpoint count.** The strict threshold at \(+\infty\) and the non-strict threshold at \(-\infty\) are deterministic, leaving at most \(2(N-1)\) nontrivial one-sided deviations.
7. **Recovery of Roth's constant.** With \(N=\lceil2/r\rceil\), one has \(1/N\le r/2\) and \(N-1<2/r\), giving \((4/r)\exp[-nr^2/(2\kappa)]\).
8. **Optimized exponent.** Taking \(N=n\) gives \(2(n-1)\exp[-2n(r-1/n)^2/\kappa]\). For fixed \(r\) and fixed \(\kappa\), dividing its logarithm by \(n\) yields the rate \(-2r^2/\kappa\).
9. **Finite support.** If the average marginal measure is supported on a finite set, nonnegativity implies every marginal is supported there. Both CDFs are constant between support points and coincide at the empty/full infopoints, so only \(M-1\) nontrivial thresholds need a two-sided union bound.

No hidden regularity of \(\bar F\) is used in Theorem 2.

## Originality audit

### Existing SCOPE records

Searches of the current archive for approximate tensorization, empirical processes, DKW, continuity, bracketing, and empirical CDF concentration did not locate a SCOPE record covering this result. A recent probability record on infinitely exchangeable Bernoulli tails concerns a different problem.

### External literature checked

- **Roth (2026), arXiv:2606.12720v1.** The full accessible text of Theorem 4.9 and its proof was inspected. The theorem explicitly assumes that the average marginal CDF is continuous. Its proof uses equal-mass anchor points available under continuity, derives the intermediate union-bound estimate, and then fixes \(N=\lceil2/r\rceil\), \(t=r/2\). No atom-safe generalized-quantile version or optimized-in-\(N\) statement was located.
- **Bobkov--Götze (2010), arXiv:1011.6165 / Bernoulli 16.** This work treats dependent empirical distribution functions under Poincare/log-Sobolev conditions. The relevant comparison theorem, as explicitly restated in Roth, assumes a Lipschitz average CDF and has an \(r^3\) exponent. The primary article was not separately full-text-inspected for every ancillary statement, so a limited residual risk remains there, but its assumptions and main theorem do not directly cover the ATE result here.
- **Kontorovich--Weiss (2014), arXiv:1207.4678 / J. Appl. Prob. 51.** Their DKW-type result uses Markov contraction/geometric ergodicity and extends to countable state spaces. This confirms that discontinuous state spaces can be handled under other dependency structures, but those assumptions do not imply the stated arbitrary-ATE theorem.
- **Jerison (2026), arXiv:2606.30866.** This recent DKW result is for regenerative Markov chains and supplies data-dependent confidence bands. It is structurally different from ATE and does not cover the theorem here.
- **Caputo--Menz--Tetali (2015), arXiv:1405.0608, and later entropy-factorization literature.** These works establish ATE for weakly dependent discrete systems, especially spin systems. This makes removal of a continuous-CDF restriction scientifically relevant rather than merely cosmetic.
- **Massart (1990).** The classical i.i.d. DKW inequality is valid without continuity; continuity is related to sharpness/equality, not validity. No novelty is claimed for allowing atoms in the i.i.d. setting.
- Searches combining approximate tensorization with empirical-process bracketing, VC classes, Glivenko--Cantelli, uniform laws, empirical CDFs, atoms, and DKW did not locate an existing statement matching Theorem 1 or Theorem 2.

The bracketing argument itself is standard and is explicitly described as such. The originality claim is only for the located ATE formulation and its consequences: a finite-bracketing inequality under ATE, an atom-safe DKW extension of Roth's theorem, and the free-resolution bound that sharpens the stated fixed-deviation exponential rate.

No single inaccessible source emerged as a uniquely high-risk candidate. The main residual risk is that a general theorem in the broad empirical-process, transportation-inequality, or dependent-concentration literature may imply an equivalent bound in different notation. Accordingly, originality is asserted only **to the best of our knowledge**.

## Value audit

The result improves both assumptions and bounds around a recent ATE-based DKW theorem. Removing continuity admits discrete and mixed marginals, which is especially natural because much of the ATE literature concerns discrete spin systems. Keeping the bracket resolution free produces a strictly stronger finite-sample family of bounds and changes the fixed-deviation exponential rate from the stated \(-r^2/(2\kappa)\) to \(-2r^2/\kappa\), a factor-four improvement in the exponent. The general finite-bracketing theorem also makes the same mechanism reusable for empirical set classes beyond one-dimensional thresholds.

The result does not claim minimax optimality, and it does not remove the logarithmic loss in the shrinking-deviation regime for general distributions. For finite support, however, the direct support-point bound eliminates that bracketing loss.
