# Review of the Gaussian time–frequency localization shape theorem

## Correctness

**PASS.** The result makes a single precise statement about the principal Fock concentration eigenvalue for squared-radius, exactly area-preserving perturbations of a disk, together with the Fourier Hessian's Poisson-mode asymptotics. The exact Fock matrix follows from polar coordinates. The diagonal disk eigenvalues have a uniform isolated gap to the vacuum for every fixed positive disk area. Differentiating the coherent-projector integral justifies trace-norm differentiability and the self-adjoint perturbation formula. The resulting coefficients are derived algebraically; the strict ordering follows from a falling-factorial sum, and the asymptotics follow from a dominated geometric limit and Poisson local CLT. The standalone checker passed 249 corroborating assertions. The finite checks are not taken as proofs of infinite statements.

## Originality

**PASS, with priority risk.** The 2021 Nicola–Tilli Faber–Krahn theorem gives global disk optimality but no mode-by-mode Hessian of its optimized principal eigenvalue. The relevant Section 5 second variation in Gómez–Guerra–Ramos–Tilli concerns the *opposite partial optimization*: varying the analytic vector while reselecting its best superlevel set. This is a neighboring but differently parameterized Hessian; no statement of the Poisson ratio spectrum or its critical Gaussian edge appears in the inspected relevant results. General symbol-norm envelopes likewise do not provide it. Comparisons with searchable prior mathematical result summaries and recoverable earlier claims showed no equivalent conclusion. An implicit Schur-complement derivation from earlier results, or an unindexed explicit shape calculation, is a residual risk rather than a claim of exhaustive priority.

## Value

**PASS.** Fixed-area shape stability of the Gaussian time–frequency Faber–Krahn disk is a natural question. The exact all-mode result determines the null directions, the unique least-stable transverse angular frequency, and a sharp coefficient at every area. The area-dependent response has a new explicit crossover at angular index comparable to disk area, including the universal normal-hazard profile in the critical window. These are motivated structural data of the optimized concentration eigenvalue, not a numerical slice or a mere textbook restatement.

## Closest literature and limits

Primary comparisons: Nicola–Tilli 2021, arXiv:2106.03423 (global sharp disk); Nicola–Tilli 2022, arXiv:2207.08624 (operator norm under symbol-norm constraints); Gómez–Guerra–Ramos–Tilli 2023, arXiv:2307.09304, especially Section 5 and Lemma 5.6 (second variation after *set* optimization at fixed analytic perturbation). The present theorem is local in each fixed perturbation; it does not assert uniform large-area Taylor remainders or global set stability. Scientific priority remains provisional and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
