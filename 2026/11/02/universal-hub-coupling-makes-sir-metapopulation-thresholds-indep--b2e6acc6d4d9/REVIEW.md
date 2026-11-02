# Self-review

## Correctness — PASS

The exact linearized next-generation matrix is \(K=r\Phi D\Phi\) because equal populations and symmetric stochastic residence times make every present population equal. The peripheral-sum-zero subspace and the two-dimensional peripheral-mean-plus-hub space are invariant. The peripheral block has spectral radius at most \(r\); the hub block has a Rayleigh quotient at least \(r(k+\zeta)/M\), strictly larger for \(\zeta>1\). The hub block trace and determinant give the asserted radical. Diagonalizing its common-rate part and applying the rank-one positive-definiteness criterion gives the full sign and equality classification. The boundary denominator is strictly positive in the stated regime. The homogeneous-rate case and \(r\ge1\) cases are explicitly included. Tests replayed from the packaged `verify.py` are supplementary evidence, not substitutes for the complete proof. Risk: none detected for the stated domain; use with asymmetry, unequal populations or other epidemic models would be unjustified.

## Originality — PASS

The 2015 fully connected SIR-network threshold formula and the 2023 Das–Stolerman preprint's exact formulas for star, cycle, star-cycle, and selected star-triangle networks are closer than generic epidemic-threshold work. The 2023 preprint explicitly leaves broader equal-hub-flux classes as conjectures; the 2024 journal abstract likewise says extensions remain conjectural. The source's supplementary proofs address constrained families. Neither accessible primary text states the unrestricted symmetric stochastic peripheral-mobility formula. Targeted searches for SIR-network, the source authors and conjectures, rank-one/equitable decompositions, and universal spectral-invariance aliases yielded different epidemic models and transfer-matrix results, not an implication of this theorem. Priority risk: an unlocated equivalent theorem or a later inaccessible specialized proof may exist; the publisher landing page was accessible but full publisher text was not, so the lawful arXiv version and supplement supplied the paper's detailed text.

## Value — PASS

Four explicit conjectural extensions in a motivated metapopulation epidemic model are dispatched by one natural structural argument. The result upgrades graph-by-graph threshold agreement to a topology-independent closed-form reproductive threshold for every symmetric nonnegative peripheral mobility matrix, with exact minimization and equality boundaries. It distinguishes the reproduction number from transient infection trajectories, which may depend on peripheral mobility. The hypotheses are interpretable: uniform center access and common peripheral transmissibility, not a small arbitrary numerical slice.

## Verification and scientific limits

The proof uses an exact invariant decomposition; numerical and rational checks in `verify.py` covered the cases recorded in `VERIFICATION.md`. Arbitrary asymmetric flows, unequal patch populations, heterogeneous peripheral rates, and nonlinear outcome comparisons are not covered. The matrix-spectral claim is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
