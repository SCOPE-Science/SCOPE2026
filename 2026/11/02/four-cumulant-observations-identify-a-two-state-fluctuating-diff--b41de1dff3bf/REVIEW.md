# Scientific review

## Correctness — PASS

The model is stationary with ordered positive diffusivities and positive rates. Conditional Gaussianity converts displacement cumulants of orders two, four, and six into cumulants of integrated diffusivity. The two-state Markov property gives the exact centered two-time covariance and three-time moment; explicit positive integrals establish the formulas. The positive derivative of the time-ratio elasticity follows from the strict inequality \(2\cosh z>2+z^2\). This proves one-to-one rate identification for any two distinct positive times. Two-point moment algebra reconstructs the rest, and an admissible one-parameter family establishes lower-order nonidentifiability. The continuous-dimension lower bound uses invariance of domain. The separately implemented generator-hierarchy verifier passed 802 deterministic assertions. Numerical checks are not substitutes for the proof.

## Originality — PASS, qualified

Hidalgo-Soria–Barkai–Burov's two-state occupation-time law already addresses the same physical model and its forward displacement law. Guéneau–Majumdar–Schehr (2025) explicitly provides arbitrary finite-time moments and the complete forward transform for an equivalent two-state case; those formulas are stronger than our **forward moment evaluation**. The claim accepted here is narrowly the explicit global four-scalar inverse theorem, the strict all-positive-times ratio monotonicity, and the exact second/fourth-data nonidentifiability fiber. Full-text inspection located forward moments, occupations, and switching reduction, but not this inverse characterization. This is a derivative extension, not a claim to discover the model, moment generating function, or finite-time moments. Residual risk: an independently published inverse observation theorem or a direct corollary in related identifiability literature could already subsume the result.

## Mathematical value — PASS

A natural experimental information question remains even if the entire forward characteristic function is known: which smallest preselected finite collection of displacement cumulants identifies all hidden environmental parameters, and what fails at lower order? The theorem answers this with four scalar values and explicit inversion, proves universal strict rate-ratio monotonicity for arbitrary sampling durations, and exhibits a genuine continuous indistinguishability family from all second/fourth data. It does not assert statistical efficiency or stability with finite, noisy data. The value is exact structural experimental identifiability, not a new forward process law.

## Nearest literature and residual limits

- arXiv:2012.11265, Sections I.1, I.3.2 and Appendix A: full occupation-time forward distribution for asymmetric exponential switching.
- arXiv:2501.13754, End Matter and supplementary Sections III–IV: exact finite-time moments and full two-state forward characteristic function; closest stronger forward coverage.
- arXiv:1907.06819, Sections II–III: alternating fluctuating diffusivity and integral-diffusivity relaxations.
- arXiv:2410.11333, Sections 1–4: a distinct regime-observed high-frequency statistical inference setting.

Independent literature priority and finite-sample inference properties are not certified.

Self-review: passed. Independent audit: not yet performed.
