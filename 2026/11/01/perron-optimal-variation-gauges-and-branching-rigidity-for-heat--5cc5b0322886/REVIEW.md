# Scientific assessment

## Correctness — PASS

For a tree the incidence map onto edge gradients is surjective, so the induced variation seminorm is exactly a weighted \(\ell^1\) matrix norm for the edge generator \(Q=-BB^{\mathsf T}C\). Its diagonal entries are \(-2c_e\), and each off-diagonal absolute value is \(A_{ef}c_f\). This gives the exact logarithmic norm and optimal prefactor-one exponential envelope. Component indicators realize each column derivative. Collatz–Wielandt gives the optimal strictly positive gauge and the symmetric conjugate eigenvalue; inertia and explicit induced subgraph witnesses give the path/claw/other sign trichotomy. Consistent path orientation makes the edge generator Metzler and establishes equality of the optimized decay exponent and the weighted vertex spectral gap. Tests: 1,890 numerical weighted-tree cases, 4,400 exact-rational edge-column identities, 23 independent path-gap comparisons. Residual mathematical risk is limited to implementation and presentation, not unresolved proof lemmas; finite tests are not substituted for the proof.

## Originality — PASS, with residual risk

The material read from arXiv:1306.2561v1 and arXiv:1509.07981v1 concerns pointwise/quadratic heat-gradient estimates and Harnack bounds for positive functions; it does not state a global weighted absolute edge-gradient matrix logarithmic norm for every real input. The material read from arXiv:1502.07770v1 concerns static tree-TV minimization algorithms. published-finding corpus searches for tree heat BV contraction, optimal Perron variation weights, and the path/claw rigidity did not surface a materially equivalent theorem. Accessible historical claims on clique bouquets and cycles classify different graph classes with fixed unit conductances and do not imply the all-tree, arbitrarily weighted optimal-gauge theorem. Standard matrix-measure/Perron ingredients are acknowledged. An older unindexed application of these classical principles to heat gradients could already prove the tree classification; such implicit prior coverage is the chief residual risk.

## Value — PASS

The theorem solves a natural design question: can reweighting the measured variation, or changing positive diffusion rates, force all-time variation stability on a branched network? It gives a complete answer for every tree rather than a small numerical instance, and sharpens it to an exactly optimizable prefactor-one growth exponent. A conductance-independent path/claw barrier, the uniqueness of the claw variation gauge, and the path equality with the spectral gap link nonlinear-looking edge variation to semigroup and Perron structure. These are useful even without a general-graph extension.

## Literature and limitations

The earliest qualifying source is the 2013-06-11 first preprint of Bauer et al. Results for static TV regularization or pointwise heat gradient estimates must not be conflated with uniform decrease of \(\sum_e w_e|(Bf)_e|\) for every signed signal. The theorem does not cover graphs with cycles or normalized heat generators with vertex masses. The optimal exponent is a sharp small-time and all-time **prefactor-one** bound, not an exact finite-time norm formula.

Self-review: passed. Independent audit: not yet performed.
