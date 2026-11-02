# Self-review

## Correctness — PASS

The spectral projectors for the three invariant subspaces (constant, class-constant mean zero, and class-internal mean zero) are pairwise orthogonal and resolve the whole space. Their exact eigenvalues give the displayed three classes of update-matrix entries. For orders two and four all non-edge constraints are strictly positive; in order four the within-part quadratic has strictly negative discriminant and the stability polynomial is a positive sum of squares. Hence the cross-part polynomial gives the unique fourth-order cutoff. For order three, the strictly decreasing scalar stability polynomial and the exact within-part quadratic imply independent monotone thresholds; their minimum is both necessary and sufficient. The part-size optimization and odd-dimensional inequality give all the stated boundary and extremizer claims. A standalone rational-matrix calculation passed 23,634 entry comparisons and 3,582 cutoff checks. No finite test is used as an infinite proof.

## Originality — PASS on the inspected record, with priority reservations

Horváth (1998, Sections 4–5) provides general positivity and SSP/absolute-monotonicity bounds, notably a zero *universal* positivity radius for classical RK4. The present fourth-order positive cutoff is not inconsistent with that result because it concerns the endpoints of a restricted, fixed graph family. Hadjimichael et al. (arXiv:1207.2902) optimize *method-level* SSP parameters; Higueras et al. (arXiv:1505.04024) optimize perturbations of methods; and Blanes et al. (doi:10.1051/m2an/2022042) construct distinct positivity-preserving integrators. The examined texts do not state the simultaneous exact RK2–RK4 graph-family radii, third-order order reversal or all-partition extremizers. The prior general positivity theory, stability polynomials and multipartite Laplacian decomposition are explicitly credited. Other possibly relevant graph-specific treatments remain a priority risk; absence of a retrieved match cannot establish uniqueness of discovery.

## Mathematical value — PASS

Positivity is essential when explicit time integrators approximate diffusion or Markov generators. The theorem settles an entire natural graph family for three common explicit exponential Taylor updates, including a counterintuitive order-three versus order-two reversal at five vertices and a partition-sensitive optimization. It supplies exact worst- and best-case graph structures at every applicable size, not merely one matrix calculation or a generic SSP bound.

## Closest literature and scope

Relevant foundational texts: Horváth (1998), doi:10.1016/S0168-9274(98)00050-6; Hadjimichael et al. (2012 preprint), arXiv:1207.2902; Higueras et al. (2015 preprint), arXiv:1505.04024; Blanes, Iserles and Macnamara (2022), doi:10.1051/m2an/2022042. The all-size claim assumes uniform unit edge weights, a connected complete multipartite graph and endpoint (not internal-stage) nonnegativity; it does not imply arbitrary positive-system SSP guarantees.

Self-review: passed. Independent audit: not yet performed.
