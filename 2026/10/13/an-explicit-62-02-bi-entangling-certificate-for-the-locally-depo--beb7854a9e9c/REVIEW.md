# Self-review

## Correctness
PASS. The noisy CNOT is exactly a product-Pauli mixture in the CNOT Choi stabilizer basis. At \(p=(8-2\sqrt6)/5\), the fifteen positive coefficients in `decomposition.json` sum to one and reproduce all sixteen target probabilities in exact \(\mathbb Q(\sqrt6)\) arithmetic. For each affine support, the associated stabilizer-code projector has pairwise commuting local restrictions on the asserted bipartition, giving an explicit product-basis separability proof. Local post-depolarization then extends the certificate from the endpoint to every larger \(p\).

Correctness risk is concentrated in the identification of the three Choi cuts with the bi-entangling classes and in the stabilizer-projector separability lemma. Both are stated explicitly in the proof; the former is the Jamiolkowski characterization used by the source, and the latter follows by simultaneous local diagonalization rather than by a merely numerical PPT test.

## Originality
PASS. The anchor source proves only \(p\ge2/3\) by separating its inner and outer terms and explicitly says this is not a full optimization and may be improved. Targeted semantic-index and literature searches for the source identifier, CNOT/bi-entangling aliases, the exact algebraic constant, its decimal value, and the final implication statement did not locate this decomposition or a same-model \(62.02\%\) certificate. Kempe--Regev--Unger--de Wolf obtain smaller numerical bounds in an explicitly incomparable circuit model. Allison--Coffman obtain the same algebraic constant in a fermionic convex-Gaussian problem, not for CNOT bi-entangling Choi states.

Residual priority risk remains because an equivalent convex decomposition could have appeared under alternative channel-polytope terminology not returned by the targeted searches. No claim of exhaustive literature uniqueness is made.

## Value
PASS. The source itself identifies full optimization of the CNOT bi-entangling bound as an open improvement direction. The new certificate lowers the same-model sufficient noise level from \(66.67\%\) to \(62.02\%\), a nontrivial change in a fault-tolerance upper-bound benchmark, and supplies an exact reusable convex decomposition rather than a decimal-only optimization.

## Closest literature and limitations
The closest source is arXiv:quant-ph/0408076, which owns the bi-entangling framework, the exact noise model, and the prior \(2/3\) sufficient bound. arXiv:0802.1464 has a stronger-looking numerical CNOT bound but a different circuit/noise criterion and explicitly states incomparability. arXiv:2609.09467 has the identical radical constant in a different fermionic resource theory. The present result is not a global optimality theorem for the bi-entangling threshold and is specific to the CNOT.

Self-review: passed. Independent audit: not yet performed.
