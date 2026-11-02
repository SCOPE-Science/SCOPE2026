# Self-review

## Correctness — PASS

**Verified claim.** The symmetry and Hilbert–Schmidt property of the killed integral operator are immediate. A nonzero eigenfunction solves an explicitly derived reflected first-order equation; differentiation twice gives a harmonic ODE, and the left endpoint gives the exact cotangent equation. Root monotonicity yields one simple eigenvalue per interval and rules out other nonzero eigenvalues. Direct differentiation plus the endpoint condition verifies the converse. The nullspace follows by differentiation, and the Doob transform is unitarily conjugate to the normalized symmetric kernel. Root ordering and the spectral theorem yield the exact Hilbert-space operator norm. The endpoint rates follow by taking limits in the root equation. The packaged checker passed 14,206 finite assertions for independent numerical identities, not as a substitute for the proof.

**Limits and risks.** Point-start total variation and parameters outside \(0<a<1\), \(\theta=-1\) are excluded. Root completeness and long-time convergence depend on the functional analytic argument, not on the sampled test grid. Independent proof auditing is not performed.

## Originality — PASS, subject to historical-priority risk

**Direct comparison.** Aurzada–Raschel (arXiv:2507.04427, first posted 2025-07-06) derive persistence generating functions and decay behavior. Aurzada–Worf (arXiv:2606.01832, first posted 2026-06-01) derive the Doob transform and principal eigenfunction; the stationary density is already implicit in its left/right eigenfunctions and symmetric specialization. Neither inspected primary text states a complete signed spectrum, infinite-dimensional nullspace, exact centered \(L^2\) operator norm for each step, or small-\(a\) rate constant for this model. The general spectral theorem alone does not calculate these values. Prior results for the different support regime \(a\ge1\) are excluded from the novelty claim. No directly covering formulation was found in targeted scholarly and mathematical-record comparisons.

**Residual risks.** A classical integral-equation or autoregressive persistence paper outside the searched corpus might contain an equivalent spectral analysis. Bibliographic searches are not a certificate of universal novelty. The leading eigenfunction and invariant-density construction are acknowledged as prior and are not claimed as independently new.

## Mathematical value — PASS

The truncated innovation support induces a nontrivial finite interval plus constant plateau, changing the operator spectrum. Exact characterization of every signed mode yields a **sharp attainable** convergence rate and shows the rare-negative-support onset \(\rho(a)\sim4a/\pi\), quantitatively addressing equilibration of a natural conditioned random process. This is more than a generic application of the spectral theorem or an arbitrarily chosen finite invariant: it resolves the spectral structure needed to analyze stationarity and relaxation in the model's distinct support phase.

Self-review: passed. Independent audit: not yet performed.
