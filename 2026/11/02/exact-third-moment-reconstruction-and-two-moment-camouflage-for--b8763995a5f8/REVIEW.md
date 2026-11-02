# Scientific review — two-loop intrinsic distance moments

## Correctness

**PASS.** The graph is precisely two positive circles joined at a unique articulation; the proof separates same-loop circular distances, each uniform on half the corresponding circumference, from cross-loop sums of two independent uniforms. This gives the exact first, second and third moments for all positive real loop lengths. The cubic contrast is \(\Delta=(ab/(a+b))^3/32\), so solving the positive quadratic \(z^2-Lz+Lc=0\) recovers the unordered lengths. The discriminant gives necessary and sufficient feasibility with correct strict and closed endpoints. The modulus follows from concavity of the real cube root; two strictly positive graph families with fixed mean prove its exponent sharp. Rational and independently integrated checks in `verify_figure8.py` passed. Finite checks are not a proof of the quantifiers.

## Originality

**PASS, with historical-priority risk.** The known general forward-moment framework of Wei–Walteros–Batta (2019/2020), Garijo–Márquez–Silveira's cactus mean formula (2023), and prior metric-flower first/second-moment identities are explicitly acknowledged. In particular, the two-moment identity is already algebraically implied by broader prior formulas, and is not claimed new. The retained result is the exact inverse feasibility classification, reconstruction from mean and third moment, minimal consecutive-moment cutoff, and sharp contrast-based recovery exponent. Dey–Shi–Wang's persistence distortion and Aanjaneya et al.'s point-cloud reconstruction use different and richer observables. Accessible relevant sections were inspected; the complete Doyle–Graver (1982) article remained inaccessible. Search nonmatches are treated as provisional evidence, not certification.

## Mathematical value

**PASS.** The inverse problem asks which geometric parameters can be recovered from the smallest number of unlabelled random-distance moments. The theorem proves a surprising information obstruction: a branched two-cycle graph and a simple circle agree on the first two moments, and a continuum of two-loop lengths also agree. It gives the exact third-order remedy with constructive formulas, a complete feasible data region, equality and degeneracy cases, and an optimal modulus for a natural recovered invariant. This is a complete, motivated low-dimensional inverse classification rather than an arbitrary new forward moment coefficient.

## Limits and closest literature

The forward moments are not novel; no full-graph reconstruction beyond the explicitly described two-loop class is claimed. No finite-sample robustness or optimal individual-loop modulus at equal loops is proved. Relevant comparisons: Dey–Shi–Wang, arXiv:1503.07414; Wei–Walteros–Batta, DOI 10.1002/net.21919; Garijo–Márquez–Silveira, DOI 10.1007/s00025-023-01902-w; Aanjaneya et al., DOI 10.1142/S0218195912600072; Doyle–Graver, DOI 10.1002/jgt.3190060410. A previously obtained general metric-flower result implies the first two formulas, but not the new inverse criterion from the third moment. The possibility of an equivalent inverse theorem in older literature remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
