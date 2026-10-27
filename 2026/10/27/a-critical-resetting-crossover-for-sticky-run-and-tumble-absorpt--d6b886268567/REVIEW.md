# Scientific assessment

## Correctness — PASS

The claim is restricted to the critical joint scaling \(r=R\theta^2\), \(\theta\downarrow0\), with a positive half-index bound-time coefficient. The telegraph first-hit transforms are obtained from the two backward equations and the right-moving wall return. Conditioning on the first Poisson reset gives an exact transform for each excursion, including the original-state restart shared by both protocols. The geometric number of bound visits produces the exact absorption transform. Expanding these identities at \(s=\theta^2z\) yields the proposed nonnegative Laplace limit; the Laplace continuity theorem proves distributional convergence. An explicit positive Lévy measure supports the subordinator representation, and a Tauberian theorem supplies the two different tail amplitudes. The standalone verifier passed 158 checks. Its finite calculations are supporting evidence, not substitutes for the proof.

## Originality — PASS, with residual risk

The original 2026 sticky run-and-tumble work gives the finite-parameter renewal formula and adsorption/return transforms. A closely related 2025 diffusion paper already contains the general heavy-tail minimum-exponent and equal-exponent principles, and these are not claimed. The assessed statement is the coupled rare-absorption, vanishing-bulk-reset regime yielding the specific \(z/\sqrt{z+R}\) crossover, the positive Lévy density, two protocol coefficients and discontinuous far-tail constant at \(R=0\). Targeted literature and mathematical-record searches did not identify this exact scaling law. The finite-parameter source transforms encode the model and might allow the asymptotics to be recovered; implicit coverage by general geometric-renewal scaling results is the principal unresolved priority risk. The earlier Brownian sticky-escape paper treats a different bounded-domain model.

## Value — PASS

The wall-return first-passage exponent \(1/2\) is physically singled out by run-and-tumble recurrence on a half-line, and an equally heavy bound-time law produces a genuine competition. In the joint scaling, bulk resetting changes an entire limit law, not just one moment. The result quantifies a singular noncommutation between weak-reset convergence and extreme survival times, identifies when different detachment protocols become statistically equivalent, and separates the binding and bulk-excursion mechanisms in an explicit Lévy representation. These address rare completion delays unavailable from mean first-passage statistics, which are infinite under the stated bound-time assumption.

## Evidence and limitations

Primary comparisons: Bressloff–Linn, arXiv:2602.02446v1, sections II–IV and Appendix A; Bressloff, arXiv:2503.01308v1, section 3.3 (notably equations (3.34)–(3.36)); Scher–Reuveni–Grebenkov, arXiv:2305.08701v1. The result assumes independently sampled bound durations and outcome decisions, renewal after each adsorption, Poisson tumbles/resets, and fixed parameters other than \(\theta\) and \(r\). The transform ordering is not first-order stochastic dominance. No uniform limit for diverging \(R\) and no extension to state-dependent clocks is claimed. The work has not undergone independent audit.

Self-review: passed. Independent audit: not yet performed.
