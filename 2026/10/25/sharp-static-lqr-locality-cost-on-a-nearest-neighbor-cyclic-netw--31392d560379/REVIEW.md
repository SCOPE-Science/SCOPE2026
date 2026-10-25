# Scientific review

## Correctness — PASS

The Riccati scalar polynomial, positive state-cost spectrum, Bellman completion-of-squares identity for arbitrary stable static feedback, covariance lower bound, and graph-radius Frobenius projection imply a universal lower cost bound. The Laurent square-root singularity of the centralized gain at \(z=-2\) implies Fourier coefficients of size \(j^{-3/2}2^{-j}\) and a squared tail of sharp order \(r^{-3}4^{-r}\). A symmetric finite-range Fourier truncation is stable for large radius and attains the same order. The direct floating-point checker verifies independent finite instances but does not establish the universal theorem.

## Originality — PASS (subject to residual bibliographic uncertainty)

Zhou–Matias, arXiv:2610.11699v1, establishes upper spatiotemporal response decay and logarithmic sufficient communication ranges. Shin et al., arXiv:2204.05551v2, establishes exponential upper performance gaps for truncated static LQR gains. The new contribution is a lower bound over *every* stable static radius-constrained gain, combined with an exact nontrivial polynomial prefactor for this nearest-neighbor cyclic family. Closely related older spatially invariant Riccati analysis is acknowledged; two plausible sources were not fully inspected, as recorded in the structured review. A failed literature search is not proof of novelty.

## Mathematical value — PASS

The lower bound demonstrates unavoidable stationary LQR excess cost of static locality, and the matching upper construction gives an exact second-order logarithmic formula for the spatial radius needed to meet a target tolerance. It supplies a nontrivial boundary against arbitrary nontranslation-invariant static policies rather than only showing a known Fourier truncation is accurate.

## Scope and risk

The result is restricted to the specified stable discrete-time model, static state feedback and fixed-radius-then-size limit. It neither gives a universal limit coefficient for the optimal static cost nor bounds dynamic distributed controllers. Relevant full-text bibliographic coverage remains imperfect, as itemized in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
