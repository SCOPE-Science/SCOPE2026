# Scientific review

## Correctness — PASS

The claim holds for every \(a,b,c,d\in(0,1)\). The lifted four-state transition matrix is primitive, and its unique stationary distribution is \((u,1,1,v)/(u+v+2)\), with \(u=(1-b)/a\), \(v=c/(1-d)\). Four positive first-step recurrences for each of the two targets yield all eight hitting means. Substitution into stationary target weighting gives the two exact squared-parameter gaps and proves the necessary and sufficient equality conditions; the converse also follows directly from the two-state first-order formula. The denominator and every prefactor are positive. The theorem is analytical; 268 independent exact-rational linear-system checks are supplementary, not a proof by finite testing. The saved source and output were inspected and replayed. The strict-positive hitting convention is essential and is stated consistently.

## Originality — PASS, qualified

Han (2026, arXiv:2607.12303v1, Section 5, Remark 5.1) explicitly asks under what conditions the full-history expected marginal mixing times are constant and provides the first-order sufficient condition. The two sharp nonnegative memory gaps and the positive binary necessity implication are not stated there. Fasino–Tonetto–Tudisco (2021, Sections 4–5) derives random-target identities for an equilibrium-averaged second-order construction subject to return-time regularity, not for every fixed initial two-symbol history. Xu (2026, Section 6) gives general mean first-passage equations but not this marginal-target constancy criterion. Kemeny–Snell covers only the already-known first-order direction. Comparison with relevant mathematical claims found no implication covering both new quadratic formulas or the binary necessity theorem. Non-indexed historical-priority overlap, especially a general algebraic formula whose binary specialization yields these squares, remains possible and is not ruled out by negative searches.

## Mathematical value — PASS

This is a natural complete classification of the smallest nontrivial case of a concrete, recently published open constancy question about a stationary random target. It identifies *which* conditional memories force a specific signed discrepancy, and provides two exact quantitative equations, even when the stationary one-symbol target distribution is balanced. The result distinguishes marginal random-target hitting statistics from the classical lifted-state random-target lemma. It does not purport to solve higher-order or many-state versions of the question.

## Scientific limitations

The kernel must be strictly positive, the alphabet binary, the Markov order at most two, and the target distributed according to the unique stationary marginal. Finite exact checks do not establish the infinite parameter assertion. Primary-source comparison included the relevant full mathematical arguments of Han and Xu and the random-target theorem of Fasino et al.; unindexed prior coverage remains a residual historical-priority risk. No external independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
