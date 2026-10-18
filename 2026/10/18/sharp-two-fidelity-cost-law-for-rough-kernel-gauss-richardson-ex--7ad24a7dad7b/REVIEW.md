# Scientific review: sharp two-fidelity cost law for rough-kernel GRE

## Correctness (PASS)

The result follows from direct inversion of the two-point nonstationary GRE covariance, the exact reciprocal-cost parametrization, and the global inequality \(1/(1-e^{-t})\leq1+1/t\). The resulting precision upper bound is uniform over all admissible, possibly budget-dependent design ratios; maximizing \(w(1-w^2)\) gives the sharp coefficient. A fixed admissible ratio realizes the bound, and uniqueness of the scalar maximizer proves rigidity of asymptotically optimal designs. The symbolic/numeric replay supplies 114 supplementary checks, while the proof supplies the infinite-horizon and all-design arguments.

## Originality (PASS, qualified)

The nearest work is Oates et al. (arXiv:2401.07562v1), whose Section 2.7, Eq. (16) and Example 10 introduce the *same* first-order bias envelope, reciprocal fidelity cost and rough Matérn family, but consider a finite 20-candidate design search. The source does not give the sharp continuous two-fidelity asymptotic \(12\sqrt3/(\ell C^3)\) or unique limit ratio \(2+\sqrt3\). The classical stationary Ornstein–Uhlenbeck constant-trend design problem does not directly imply a result for multiplicatively fidelity-scaled errors and cost-limited simulations. The later sparse GRE work emphasizes extrapolation dimensionality and learned model structure; the accessible material did not identify this exact law. Targeted searches of published mathematical records and direct comparisons with the closest literature disclosed no matching statement or stronger theorem whose hypotheses imply it. This is a best-knowledge originality assessment, not proof of priority; generalized correlated-design theory or uninspected sections could contain an equivalent derivation.

## Value (PASS)

Two simulations at a natural pair of fidelities deliver an entire additional inverse-budget power over one simulation in a concrete first-order GRE setting, despite a rough \(\nu=1/2\) kernel. The exact asymptotic coefficient and unique fidelity ratio resolve a continuous design question that a fixed candidate grid cannot capture and clarify a published finite-grid observation about greedy allocation. This is a fixed-scale posterior-variance result, not a claim about actual deterministic simulation errors, empirical coverage, unrestricted numbers of experiments, or other kernels.

## Literature comparison and residual limits

Relevant sources include Oates et al. (2024), arXiv:2401.07562v1, sections 2.1–2.2 and 2.7; Zagoraiou and Baldi Antognini (2008), DOI 10.1002/asmb.749 (only abstract and bibliographic material accessible); and Oates, Howey and Karvonen (2026), arXiv:2604.02072 (abstract and publicly retrieved design-section excerpt, not full manuscript). The general covariance and cost-design objective are prior work. The closed sharp asymptotic for the two-point, first-order, exponential-kernel specification is the assessed contribution. Limits of incomplete literature coverage and non-independent review remain.

Self-review: passed. Independent audit: not yet performed.
