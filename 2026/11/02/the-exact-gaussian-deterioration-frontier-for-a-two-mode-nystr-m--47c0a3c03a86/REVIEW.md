# Scientific review

## Correctness — PASS

The one-pass Nyström eigenpair is reconstructed directly from the rank-one matrix \(A\omega(\omega^{\mathsf T}A\omega)^{-1}\omega^{\mathsf T}A\). The rank-one SPD spectral correction has trace \(L+m+(c-1)R\) and determinant \(cLm\). The exact condition-number comparison factors into the cubic \(Q_{a,b}\), with a strictly positive prefactor and the correct reversed sign. Descartes' rule and endpoint signs prove uniqueness of the threshold. The two Gaussian events are tails of the absolute normal ratio, and the high-contrast limit follows from coefficient convergence and a positive-root sign bracket. The embedded numerical checker passes 793 finite cross-checks; the general result depends on the analytical proof.

## Originality — PASS under reviewed sources

The 2026 EDA paper's sections 3.1–3.2.3, Algorithm 3.1, 4.2.1, and appendices introduce the Nyström construction, covariance-informed sketch, and scale but do not give the exact two-mode deterioration law. The full 2024 Carson–Daužickaitė article supplies finite-precision approximation/conditioning bounds and considers a different scaling. Giraud–Gratton's accessible author report analyzes perturbation sensitivity rather than the Gaussian law. Frangella–Tropp–Udell give condition-number guarantees for their differently scaled Nyström PCG scheme; available access for that paper comprised its abstract rather than a verified full-text priority exclusion.

An earlier exact Gaussian alignment frontier exists for the **Rayleigh** eigenvalue correction to a top-eigenvalue-plus-identity spectrum; it is explicitly excluded from novelty. The present harmonic Nyström correction with two strictly positive eigenvalues and the \(A+A^2\) sampling law gives different equations and a distinct order-\(a^{-2}\) conclusion. Published semantic comparisons found no dominating result, but do not establish global uniqueness. Remaining risks include specialized older randomized preconditioning analyses, inaccessible material, and independent priority verification.

## Mathematical value — PASS

The informed Gaussian covariance is motivated by a concrete 2026 data-assimilation preconditioning proposal. An analytic baseline with the ideal target scale still has a nonzero probability of becoming worse conditioned. The unique cubic and its exact Gaussian tail quantify that risk, while the one-power improvement between the two natural sketch laws provides an interpretable design benchmark. This is not simply a textbook restatement of angular sensitivity: it compares two proposed sketch geometries with provably distinct rare-event exponents.

## Limits

Exactly two dimensions, positive distinct modes, one Nyström vector, a fixed oracle target scale, exact Gaussian distributions and exact arithmetic. No broad claim about PCG convergence, matrix-free execution, higher ranks, non-Gaussian perturbations or actual ensemble covariance. Independent literature-priority and mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
