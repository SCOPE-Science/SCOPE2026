# Scientific review: two-by-two Gaussian growth edge

## Correctness — PASS
The normalized trailing entry is computed exactly following the row interchange. Ordered first-column magnitudes have density \(2f(p)f(u)\); independent Gaussian signs give a one-half chance of reinforcing, and otherwise the growth factor is one. Splitting by which original magnitude is maximal yields two codimension-two triangular regions and one codimension-three remainder. The rescaled integrands admit an integrable Gaussian dominator. Each triangular region contributes half of \(1/(2\pi^2)\); the third is smaller order. The Gaussian double integral is evaluated explicitly. The algebraic and stochastic verifier runs successfully but is not the proof.

## Originality — PASS within documented inspection limits
The closest classical source is Trefethen–Schreiber (1990), a treatment of average-case pivot and growth statistics across dimensions. Trefethen (2026) treats an exponential-rarity result for the corner entry as dimension grows, and Urschel (2026) reports high-dimensional Gaussian partial-pivoting growth bounds. Their stated asymptotic variables and conclusions do not imply the fixed-dimension near-extremal coefficient \(1/(2\pi^2)\). Relevant exact-edge and small-dimension formulations were searched; no covering statement was identified. This is a best-knowledge priority comparison, not a proof of historical uniqueness. The complete Urschel manuscript and some specialist rare-event literature were not accessible for full inspection.

## Mathematical value — PASS
The growth factor and its deterministic Wilkinson maximum are canonical quantities in numerical linear algebra. The two-dimensional Gaussian model is the first one allowing actual elimination growth. Its exact near-maximal tail exponent and constant provide a nontrivial finite-dimensional boundary law and a quantitative rare-event benchmark, rather than a numerical anecdote or an arbitrary parametrization. The result makes no claim of directly improving a high-dimensional instability bound.

## Limitations and closest literature
The finding addresses exact-arithmetic real iid Gaussian \(2\times2\) partial pivoting, not general random matrices or backward errors. Closest inspectable primary sources: Trefethen and Schreiber, *Average-Case Stability of Gaussian Elimination* (1990), DOI 10.1137/0611023 (full text); Trefethen, *Instability of Gaussian elimination is exponentially rare* (2026), arXiv:2610.04761 (full text). Urschel, *On the Growth Factor of Random Matrices* (2026), arXiv:2610.06785 (abstract only), and Driscoll–Maki rare-event Monte Carlo (2007) remain residual historical-priority risks.

Self-review: passed. Independent audit: not yet performed.
