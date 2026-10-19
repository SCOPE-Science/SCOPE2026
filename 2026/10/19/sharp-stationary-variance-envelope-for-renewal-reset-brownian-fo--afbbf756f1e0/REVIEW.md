# Scientific review

## Correctness — PASS

The stationary renewal occupation formula gives the exact lag covariance \(C_Y(h)=D\mathbb E[(T-|h|)_+^2]/m\). The exponential harmonic Green function reduces the position variance to a single waiting-time Laplace transform. Strict ordinary Jensen and strict Jensen under the size-biased waiting law establish the distinct open endpoints at nondegenerate second moment. Positive two-point waiting times match both prescribed moments exactly; continuity and limiting constructions show that they realize the full interior and approach each unattained endpoint. The proof treats deterministic waiting as its own equality case. The independently executable `verify.py` supports the formulas by exact-identity, covariance quadrature, and phase-integral comparisons; finite tests are not substituted for the proof.

## Originality — PASS, with qualified priority risk

The closest source is Guéneau, Majumdar, and Schehr (arXiv:2306.09453), whose Sections 2–5 develop the resetting-noise harmonic-trap model, general recurrence machinery, a periodic-reset-epoch variance, and Poissonian results. The inspected text does not state the time-stationary arbitrary-renewal Brownian-force covariance and **complete sharp variance interval with fixed first and second waiting moments**. General arbitrary-waiting-time resetting by Eule and Metzger (arXiv:1510.07876) resets particle position, while den Hollander et al. (arXiv:1801.09909) study additive functionals under Poissonian Brownian resets. These comparisons concern mathematical implications, not titles alone. Classical moment-transform inequalities and size-bias Jensen are acknowledged ingredients, not separately novel claims. An existing stronger theorem for moment-constrained Laplace transforms or a generalized renewal-filter process could subsume part of the result.

## Scientific value — PASS

Holding both the mean renewal cadence and variability of intervals fixed is a natural control constraint for a correlated stochastic force, and stationary position variance is a direct transport observable. The theorem completely classifies attainable variance, resolves whether extremes are physically realized with positive waits, and constructively synthesizes any intermediate variance using only two waiting-time values. Its covariance convex-order statement explains the direction of fluctuation change at every lag, extending the calculation beyond a single number. The observable is phase-stationary; its deterministic-periodic specialization must not be confused with a reset-epoch variance.

## Closest literature and limitations

References and inspected sections: https://arxiv.org/pdf/2306.09453 (Sections 2–5, Eq. 11, Appendix C); https://arxiv.org/pdf/1510.07876 (model, Eq. 6); https://arxiv.org/pdf/1801.09909 (model and Theorem II.1). No assertion of broad literature exhaustiveness or independent priority certification is made. Results require strictly positive finite-second-moment renewal durations; the endpoints are limiting only.

Self-review: passed. Independent audit: not yet performed.
