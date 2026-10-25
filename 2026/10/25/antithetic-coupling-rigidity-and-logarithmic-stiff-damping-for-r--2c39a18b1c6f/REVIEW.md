# Scientific review: antithetic coupling of randomized implicit stages

## Correctness — PASS

The countable-integer-step limiting argument proves that any samplewise unconditionally contractive uniform-marginal coupling must satisfy \(U+V=1\) almost surely. The exact complementary-stage transfer and its scalar modulus identity establish sufficiency. An operator polarization identity evaluated on arbitrary vectors proves contractivity for every finite-dimensional complex dissipative matrix, including nonnormal ones; no unsupported scalar-to-matrix inference is used. The two rational integrals for the second moment and the sharp expansion were verified both symbolically and by high-precision quadrature. The numerical matrix experiments are corroboration only, not universal proof.

## Originality — PASS (best-knowledge)

The closest primary antecedent, Bochacik–Przybyłowicz (arXiv:2404.19059v1), establishes stability for independent uniform stage choices, not the uniqueness of an across-step coupling under samplewise stability. The closest structural antecedent, Blanes–Casas–Murua (arXiv:0812.0377), covers classical adjoint compositions and order cancellation, both explicitly excluded from the novel claim. Broad published-finding corpus queries for complementary stage pairing, randomized implicit Runge–Kutta stage couplings, contractivity, and stiff damping found no result implying this exact rigidity and asymptotic law. Potential equivalent formulations in older adjoint-coupling and copula-based stability literature remain a residual risk; a failed search does not establish originality conclusively.

## Value — PASS

Coupling-induced stability is a meaningful gap for randomized integrators: two schemes can have identical one-step uniform stage distributions but qualitatively different samplewise stability. The uniqueness identifies the only admissible all-step-size contractive coupling, extends the implication beyond normal matrices, and gives an exact nonuniform stiff-damping obstruction. It is a structural sampling result plus a sharp rate, not a restatement of a second-order adjoint-composition calculation.

## Limitations

This is a modified correlated-stage method. It does not assert that the original independently randomized scheme has samplewise all-step-size stability; it does not prove nonlinear B-stability, or any L-stability. Source comparisons support best-knowledge originality and are not exhaustive proof of absence of prior work.

Self-review: passed. Independent audit: not yet performed.
