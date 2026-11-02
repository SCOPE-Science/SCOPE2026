# Scientific assessment: sharp cycle-length positivity frontiers for classical RK4

## Correctness — PASS

The theorem is an exact classification for the clearly specified column-convention generator \(Q_n=P_n-I_n\), all cycle lengths \(n\ge2\), orders \(1\) through \(4\), and all nonnegative steps. Direct binomial expansion gives the residue coefficients, and the separate proof of no later positivity windows rests on a coefficient strictly negative for every step above one (long cycles) or a unique increasing-polynomial zero (short cycles). For dimension two, the projection formula works for every Markov generator, including absorbing cases; the strict positivity of the fourth Taylor polynomial on the negative real axis is established by Taylor's remainder. The three-state example is a rational certificate: negative diagonal \(-1/128\) and exact nonstationary eigenvalue modulus \(79/128\). All stated boundaries were checked independently by a standard-library, exact-rational verifier (4,070 check groups). Finite checks confirm algebraic identities but are not treated as proof for all cycles and times.

## Originality — PASS (qualified)

The 2021 positivity-preserving Markov/graph-Laplacian literature establishes the general need for positivity and discusses classical RK4 as a baseline but does not give these exact directed-cycle thresholds. Established SSP theory provides global convex monotonicity bounds and notes classical four-stage RK4 has zero nonlinear SSP coefficient; this does not imply the fixed-generator coefficient thresholds or the three-state stable-but-negative certificate. Perturbed RK theory changes the method, whereas the finding classifies an unperturbed RK4 end-step. Related analyses of Crank–Nicolson, Padé methods, and other Markov integrators have different stability functions and thus do not logically subsume this table. The scalar negative-real-axis RK4 stability endpoint and the general distinction between spectral and positivity stability are prior facts. Residual publication-priority risk: specialized circulant Markov time-stepping or polynomial semigroup positivity literature might already contain an equivalent theorem; broad search and source inspection are not proof of novelty.

## Value — PASS

This is a complete, sharp classification for a fundamental family of periodic, constant-rate Markov generators. It identifies a counterintuitive three-cycle positivity horizon larger than the two-cycle's, explains why all longer cycles hit the Euler frontier, and gives the smallest possible Markov dimension where a classical RK4 step is spectrally contracting but assigns a negative transition weight. A naive check of spectral stability would approve the explicit rational failure example. This supplies an interpretable benchmark for numerical master equations, rather than an arbitrary slice of a polynomial calculation. No claims are made for general generators, nonlinear problems, intermediate stages, or arbitrary Runge–Kutta schemes.

## Closest primary literature and limitations

[1] Blanes, Iserles and Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242, posted 2021-02-16 (full HTML sections 1–5 inspected, including RK4 comparisons): establishes the model class and positivity concern, not this classification.

[2] Gottlieb, Grant and Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and Optimal Nonlinear Order*, arXiv:1403.6519 (sections 1, 3–5 inspected): studies method-level SSP coefficients, not end-step probabilities on directed cycles.

[3] Higueras, Ketcheson and Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024 (sections 1–3 inspected): uses modified tableau monotonicity, not the same unperturbed cyclic Markov end-steps.

Scientific limitations are generator-specific scope, non-roundoff arithmetic, and absence of independent validation. Specialized equivalent prior literature remains a risk.

Self-review: passed. Independent audit: not yet performed.
