# Independent audit — 2026-09-30

**Record:** `2026/09/20/weak-lp-volume-ratio-exponential-all-p--cb86d86a6a44`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree:** `c159a496ce0e6fd3a1cad9ff6bce72ba18b485d3`  
**Disposition:** passed

## Correctness — PASS

PASS. The scaled weak ball is correctly equivalent to the empirical survival inequalities N_y(t)<n t^{-p}. The positive p-generalized Gaussian has p-th moment one and exactly the scaled l_p-ball entropy rate h_p, while strict Markov inequality leaves positive tail slack at every t>=1. Moving sufficiently small mass from an interval below 1 to one above 1 preserves every weak-tail inequality and has strictly positive first entropy variation. Truncating the far tail and reinserting it below 1 only decreases constrained survival probabilities and has vanishing entropy cost. On compact support, strict slack is uniform; a finite partition then converts it into robust cumulative-bin inequalities. Exact-count type sets are consequently inside the weak ball, and their Stirling exponent is the histogram entropy, which is at least the original density entropy by binwise relative entropy. This yields a strict exponential rate gain for every finite p, including 0<p<1; no convexity is used.

## Originality — PASS

PASS. Doležalová--Vybíral (2020) explicitly prove exponential growth only in their established range and state the all-finite-p extension as an open problem. The later probabilistic Lorentz-ball work of Kabluchko--Prochno--Sonnleitner concerns a different Lorentz index regime, while the 2025 entropy-number paper uses coarse volume-radius information rather than resolving this weak-Lp/classical-Lp exponential ratio. I found no later source asserting the all-finite-p result or this entropy-improving type-class mechanism. The usual caveat for an unindexed or differently formulated result remains.

## Scientific value — PASS

PASS. The theorem closes a concrete open range for every finite p and replaces a parameter-sensitive explicit subset construction with a conceptually robust entropy argument. The mechanism—strict empirical-tail slack plus local entropy increase plus type classes—is potentially reusable in other high-dimensional symmetric-body volume comparisons.

## Findings

- The p-Gaussian is at exactly the classical l_p exponential volume rate yet lies strictly inside all relevant weak-tail constraints.
- The local low-to-high mass transfer raises entropy to first order while maintaining the tail constraints for sufficiently small mass.
- The 2020 source explicitly leaves the all-finite-p assertion open.

## Independent checks

- Re-derived the weak-ball/empirical-tail equivalence including boundary conventions.
- Verified the p-Gaussian normalization, p-th moment, and entropy formula.
- Checked the survival-function perturbation, truncation, uniform-slack, and type-bin inequalities.
- Checked the histogram-entropy inequality direction using binwise KL divergence and confirmed the proof does not use p>=1.

## Literature evidence

- https://doi.org/10.1016/j.jat.2020.105407 — Doležalová and Vybíral (2020), source volume-ratio theorem and explicit open all-finite-p extension.
- https://arxiv.org/abs/2303.04728 — Kabluchko, Prochno and Sonnleitner (2023), probabilistic/maximum-entropy methods for a different Lorentz-ball family.
- https://doi.org/10.4064/sm240409-15-2 — Prochno, Sonnleitner and Vybíral (2025), entropy numbers and coarse Lorentz volume-radius context, not the audited ratio theorem.

## Limitations

- The proof is existential and does not determine the optimal exponential base or exact nth-root limit.
- No full large-deviation principle or limiting empirical distribution is proved.
- The endpoint p=infinity is outside the theorem.
- An unindexed or substantially differently formulated equivalent result cannot be ruled out absolutely.

No GitHub write was performed by this audit. The guarded change set only stages this audit evidence and updates the independent-audit channel in `VERIFICATION.md`; it leaves the research claim files unchanged.
