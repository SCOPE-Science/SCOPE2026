# Independent mathematical audit

## correctness

PASS

Both the retained finite formulas and the narrowed sharp supercritical finding are correct. The inverse squared radius is the least eigenvalue of the restricted quadratic form; it is one minus the top eigenvalue of a projected two-column Gram matrix. The fixed-normal identity thus also works at rank deficiency. Schur complementation when d₂−s>0 proves the Dirichlet CDF event; rank-one interlacing gives R≥b with equality for e₁-perpendicular. Coupling with one Gaussian sequence gives √N(U₁,U₂)→G and positivity of the scaling limit even when c₁=∞, since the determinant is c₂⁻²G₁². At t>c₂, taking the Schur complement at t⁻² and conditioning on G₂ gives the exact erf expression; t times the integrand is dominated for t≥√2 c₂ by √(2/π)√(1+2c₂²G₂²). Its limiting constant is positive and finite, so layer-cake proves the full positive-moment threshold. Bounded truncations under weak convergence prove divergence of the normalized expectations without an illicit exchange of limits. The frozen check_two_spike.py and VERIFICATION.md were inspected, not executed; the reported finite eigenvalue checks are not proofs of the limiting assertions.

## originality

PASS

The original attribution of a distinct exact finite-dimensional distribution FAILS: an inspected prior theorem gives the very same law, not just estimates or a methodological analogue. Assiotis–Najnudel Definition 1.1 explicitly allows repeated eigenvalues, and Proposition 1.7 identifies the real Haar compression with θ=1/2. The factorization below gives exact coverage at every assigned N. The corrected RESULT.md reclassifies the finite law as a specialization, retains the scaling calculation for context, and makes the sharp supercritical tail and its moment/optimal-radius consequences the surviving finding. That claim passes the bounded prior comparison; the cited general law does not itself carry out this large-N, then large-t, endpoint analysis.

## value

PASS

The routine specialization of the exact finite kernel is not the reason for acceptance. The repaired result computes the sharp large-radius coefficient and its moment threshold in a natural critical/supercritical measurement model. An optimal one-hyperplane normalized radius stays bounded, while uniform random choice has diverging normalized mean even though each member of the sequence is bounded. The constant and this distinction complement general high-probability radius estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
