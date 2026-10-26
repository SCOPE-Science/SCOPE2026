# Scientific review

## Correctness

PASS. Exact equilibrium elimination and strict-sign contradictions exclude every positive two-group equilibrium in the example; the complete Jacobian has six strictly negative eigenvalues at the surviving partial-endemic equilibrium. The supercritical spectral radius and all critical algebra were independently checked by the companion symbolic program. The general sufficient result uses the positive left Perron vector to construct an inward-pointing truncated cube, a Brouwer/projection zero, and irreducible propagation to exclude any boundary zero. Its continuity, positive-denominator and positive-creation assumptions are explicit. Computational checks corroborate rather than replace the infinite-dimensional parameter theorem.

## Originality

PASS, with priority risk. The motivating published paper, equation (2), Theorem 5 and Conjecture 6 were inspected in full: it proposes the broader implication but establishes it only under a stronger row-sum condition. The example has smallest next-generation row sum \(3/4\), so its stable partially endemic branch is not ruled out by that theorem. The earlier single-community adaptive article and multigroup compartment literature do not state a corresponding directed-link-erasure counterexample. The main claim is about the unrestricted conjecture **and** its precise positive-creation sufficient replacement, not about the familiar static SIS threshold. Searches cannot exclude all unindexed equivalent discoveries.

## Value

PASS. This answers a concrete outstanding existence question by exhibiting a substantive model boundary: a locally unstable disease-free state and irreducible potential contact network can coexist with a stable *partially* infected equilibrium because adaptive contact creation turns off an essential edge. It also gives a general constructive condition restoring existence, useful for deciding which behavioral response assumptions matter in multigroup epidemic models. The negative example is not an arbitrary numerical slice: it uses only two groups, positive rates, and smooth monotone behavior, directly matching the motivating model's assumptions.

## Literature and limitations

The closest source is Achterberg–Sensi–Sottile, *Chaos* 35, 033127 (2025), doi:10.1063/5.0246228, particularly Theorem 5 and Conjecture 6. The condition is sufficient but not necessary, and no uniqueness or global convergence theorem is asserted. Search completeness and independent validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
