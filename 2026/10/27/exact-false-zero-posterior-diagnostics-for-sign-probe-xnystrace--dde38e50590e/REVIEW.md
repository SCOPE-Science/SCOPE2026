# Scientific review: sign-probe XNysTrace posterior diagnostics

## Correctness — PASS

The Nyström approximation is defined by the Moore–Penrose pseudoinverse and remains meaningful for repeated sign columns. Its active-range projection reduces all dimensions to two projective signs. A monochromatic leave-one-out sketch has residual trace \(c\), and each corresponding basic estimate is \(T-cst\), where \(s,t\) are sketch and held-out signs. A mixed sketch spans the full active range and returns exactly \(T\). Counting the two monochromatic sign patterns, the \(2m\) one-minority patterns, and all remaining patterns proves the complete joint distribution for every \(m\ge3\); two probes give the distinct special case. The exact-rational standalone checker independently enumerates four eigenvalue profiles and all projective-sign configurations for \(2\le m\le9\). That finite test is not the proof of the general statement.

## Originality — PASS (best-knowledge assessment)

The defining XNysTrace formulas and the general pairwise-correlation error identity are prior work of Epperly, Tropp and Webber, arXiv:2301.07825, equations (7)–(9), Section 3.1 Proposition 2, and Section 5.6. Epperly's 2025 dissertation, Chapter 15 Proposition 15.4, repeats the identity and documents empirical underestimation. The material inspected contains no exact two-sign projective classification, finite-sample three-atom joint law, \(1/2\) correlation, or \(m+1\) calibration factor. The current result is not the general correlation identity itself: it determines its matrix- and probe-specific correlation analytically, as well as the stronger false-zero probability. Prior work on exchangeable diagonal estimation studies a different output and loss. The primary-source and research-record comparison did not uncover a dominating theorem. Risk: an equivalent calculation may be present in unindexed discrete-sketch or resampling literature.

## Value — PASS

The natural smallest nontrivial PSD rank with fair-sign probes exhibits a precise limitation of an a posteriori diagnostic used for adaptive stopping. Its squared diagnostic can report zero even when the trace is wrong, and its expectation is underestimated by the unbounded factor \(m+1\) for all \(m\ge3\). The complete law distinguishes false-zero probability, which decreases exponentially, from the relative diagnostic calibration error, which increases with sample count. The result motivates distinguishing correlation, confidence, and absolute risk in sign-probe trace estimation rather than proposing a general failure of the algorithm.

## Limits and closest literature

The estimator is the mathematical pseudoinverse version, not every optimized implementation; rank-deficient sketch Gram matrices matter. Gaussian probe behavior and finite-precision error are excluded. The primary comparison is Epperly–Tropp–Webber, *XTrace: Making the most of every sample in stochastic trace estimation* (arXiv:2301.07825); additional comparison is Epperly's 2025 Caltech dissertation, Chapters 14–15. A related exchangeable XDiag risk calculation does not cover scalar XNysTrace posterior diagnostics. Independent specialist inspection is still outstanding.

Self-review: passed. Independent audit: not yet performed.
