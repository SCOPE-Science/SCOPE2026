# Same-model review

## Correctness

**PASS.** Direct propagation gives the exact two-step distribution \((\cos^2\theta/2,\sin^2\theta,\cos^2\theta/2)\) and the exact three-step distribution \((\cos^4\theta/2,(1-\cos^4\theta)/2,(1-\cos^4\theta)/2,\cos^4\theta/2)\). Shannon entropy on three or four accessible sites is globally maximized exactly by the uniform distribution. This yields the unique angles \(\arcsin(1/\sqrt3)\) and \(\arccos(2^{-1/4})\). The Hadamard values are strictly smaller. At one step the position law is exactly uniform for every coin angle, making two steps the earliest strict failure.

## Originality

**PASS, narrowly scoped.** The direct source states that the Hadamard coin has maximum measurement entropy and supports the claim with much larger-step plots. Its erratum does not alter that conclusion. Ide--Konno--Machida later state the finite-time numerical suggestion explicitly “for any \(n\).” Targeted searches for the two exact optimizer angles, uniform short-time distributions, and corrections to the Hadamard-maximality statement did not locate the displayed result.

Residual risk remains because the two- and three-step distributions are elementary and may have been noted in unindexed material. The accepted originality claim is only the exact short-time optimizer and earliest strict counterexample, not a general entropy-maximization theorem for quantum walks.

## Value

**PASS.** The result resolves the earliest boundary cases of a published finite-time entropy-maximality statement and shows that the discrepancy is structurally large: non-Hadamard coins attain the absolute information-theoretic upper bound by making all accessible positions uniform. This is directly relevant to using coin parameters to optimize finite-time spreading or uncertainty, and it prevents large-step numerical plots from being extrapolated to every step number.

Same-model review: passed. Independent audit: not yet performed.
