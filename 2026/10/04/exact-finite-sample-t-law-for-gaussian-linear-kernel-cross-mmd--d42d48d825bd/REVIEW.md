# Same-model scientific review

## Correctness
**PASS.** The proof reconstructs the statistic from the published cross-MMD definitions. For the linear kernel, the numerator is \(AB\), the empirical variance is \(B^2S/s^2\), and cancellation reduces the statistic to an independent sign times \(sA/\sqrt S\). The equal-variance Gaussian first half then gives the classical \(t_{{2s-2}}\) law with the stated scale factor. The exact size formula, strict anti-conservatism, calibrated cutoff, and asymptotic coefficient follow analytically. The bundled verifier reproduces the numerical claims and exact algebraic reduction.

## Originality
**PASS.** The closest direct source is Shekhar, Kim, and Ramdas, which defines the same cross-MMD statistic/studentizer and proves asymptotic standard-normality. Inspection of the relevant full text and targeted searches did not locate the exact scaled-Student law, the exact finite-sample size, or the corrected cutoff. The foundational cross-U article supplies broader methodology but accessible material describes limiting Gaussian calibration rather than this exact two-sample specialization. Published-finding searches under several equivalent formulations did not return a covering result.

Residual originality risk remains because the full body of the foundational cross-U article was not available through the attempted lawful access route, and older studentization literature could contain an equivalent algebraic special case under different terminology. That risk is not strong enough to overturn the direct-source comparison, but it is retained explicitly.

## Value
**PASS.** Finite-sample calibration is central to the purpose of replacing a permutation calibration with a Gaussian cutoff. The exact benchmark shows a material direction and magnitude of error at moderate sample sizes, supplies an exact no-simulation repair, and gives the leading \(1/s\) calibration term. The result is narrow but structurally motivated; it is not a mere recomputation of a table.

## Closest literature and limitations
The direct predecessor is *A Permutation-free Kernel Two-Sample Test* (arXiv:2211.14908), built on *Dimension-agnostic inference using cross U-statistics* (arXiv:2011.05068). The present theorem applies only to the one-dimensional equal-variance Gaussian null with the linear kernel and balanced splitting. It does not provide exact calibration for Gaussian/RBF kernels or general high-dimensional alternatives.

Same-model review: passed. Independent audit: not yet performed.
