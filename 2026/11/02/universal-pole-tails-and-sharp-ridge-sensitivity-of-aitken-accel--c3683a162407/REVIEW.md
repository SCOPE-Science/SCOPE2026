# Scientific review

## Correctness — PASS
The Aitken reduction is algebraically exact for nested \(1,2,4\) Gaussian-probe means. Positive quadratic-Gaussian densities have exponential tails and an integrable origin singularity, while the two-probe sum density is bounded. Conditioning on the first two probes gives the rigorous denominator-pole tail via an approximate-identity argument, and the ridge argument uses a second approximate-identity kernel. The explicit rational integrals were reconstructed independently and checked by the standalone verifier. The Monte Carlo experiment is corroboration, not proof.

## Originality — PASS, qualified
The central 2023 Aitken trace paper was materially read, including its algorithm, distinction between deterministic probing and random comparison method, and conclusions; it does not assert these stochastic moment or ridge constants. Basic Aitken pole sensitivity and Gaussian trace probes are established. The closest stochastic prior is Fika's 2018 inverse-trace extrapolation chapter: its abstract confirms stochastic variants but the full text was inaccessible, leaving a material priority risk rather than a claimed negative full-text finding. A semantic database search found related ratio-tail results on different estimators, not a stated or mathematically dominating result for these nested trace means.

## Value — PASS
The gap is motivated by extrapolating progressively refined matrix-trace estimates. The theorem shows that finite-moment unbiased Gaussian inputs can lose even the first absolute moment after a natural three-level acceleration, universally across nonzero PSD matrices. It also quantifies exactly the inverse-ridge risk of a standard smooth denominator guard; the \(2\times2\) isotropic instance supplies closed calibration constants. This distinguishes deterministic-probing acceleration from an unsafe unguarded Monte Carlo transplant and informs numerical diagnostics.

## Closest sources and remaining limitations
Kalantzis--Kollias--Ubaru--Salonidis 2023 studies deterministic probing, not accelerated nested Gaussian Monte Carlo. Avron--Toledo 2011 covers unaccelerated random trace means. Fika 2018 analyzes extrapolated inverse-trace approaches and may contain relevant specialized results not inspected in full; no first-priority novelty claim against that inaccessible text is warranted. Classical rational-transform pole warnings alone do not provide the matrix-universal constants. The result does not treat Rademacher probes, adaptive stopping, or deterministic hierarchical probing.

Self-review: passed. Independent audit: not yet performed.
