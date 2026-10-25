# Scientific review

## Correctness — PASS

The Zak transform of the unnormalized piecewise-exponential window is an absolutely convergent pair of geometric series. At modulation step \(1/2\) the frame operator diagonalizes as the sum of two Zak squared moduli, with no missing density factor. Strict convexity in the cosine frequency variable forces the two spectral frequencies. At the positive-frequency endpoint the multiplier is a strictly convex sum of exponentials and has equal endpoint values, giving the exact maximum. At the negative-frequency endpoint its Gram determinant is \((1-rs)^2/((1+r^2)^2(1+s^2)^2)>0\), and differentiation gives a quadratic with one positive root strictly inside the Zak period. This proves the minimum, its uniqueness, and positivity for every \(a,b>0\). The packaged Python script returns `CHECK_OK`; this is a reproducibility check, not an infinite proof.

## Originality — PASS, with priority risk

The 2026 frame-set theorem (arXiv:2608.04992) establishes qualitative existence for totally positive windows, not these sharp bounds. Faulhuber–Shafkulovska (arXiv:2204.02917, Section 8) develop sharp bounds for symmetric two-sided exponentials and lattice optimization, making \(a=b\) a **known special case**. Kloos–Stöckler (arXiv:1311.7359) give Zak-transform and frame-existence results, including even-window lower-bound estimates, not a complete unequal-rate frame spectrum. Closest mathematical-index comparisons concern shift-invariant translation sampling of asymmetric exponentials or compactly supported spline Gabor frames: neither conclusion implies optimal frequency-and-space Zak spectral extrema for unequal exponential rates. The complete 1996 Janssen text could not be accessed; that is an explicit residual priority uncertainty, not proof of noncoverage. No independent originality audit was conducted.

## Value — PASS

The exact constants quantify stability of time-frequency synthesis at the first overcritical integer lattice density across the natural independent two-rate window family. Unequal rates move the sharp lower Zak fiber, a phenomenon absent from known symmetric formulas. The two-parameter closed form and equality locations allow exact conditioning without numerical spectral optimization. The family restriction is mathematically meaningful and is not presented as a classification of all totally positive windows.

## Scientific limits

Neither arbitrary nonrectangular lattices nor other redundancies are addressed. Inaccessible historical full text leaves finite priority risk. The script samples only finitely many rates/fibers; the analytical inequalities prove the theorem for all rates.

Self-review: passed. Independent audit: not yet performed.
