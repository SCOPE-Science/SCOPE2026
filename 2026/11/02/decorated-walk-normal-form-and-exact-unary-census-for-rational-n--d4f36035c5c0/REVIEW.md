# Review: Decorated-walk normal form and exact unary census

## Correctness — PASS

For any positive denominator \(d\), structural induction gives affine pieces with slopes in \(\{-1,0,1\}\) and integral-grid intercepts. Their pairwise crossing locations lie on the half-grid, which forces the three same-height decorations and the unique increasing/decreasing transitions. Conversely, Ovchinnikov's representation theorem expresses any permitted continuous decorated walk as a min-max polynomial of its affine pieces, each of which clips to an available shifted literal. The transfer matrix counts the resulting unique paths; a weighted-walk maximal inequality proves \(|\mathcal T_d|=5^d(d+O(\sqrt d))\). The independent grammar-closure checker matches transfer-matrix and decorated-path enumerations through \(d=3\). The proof, not finite tests, covers all denominators.

## Originality — PASS within inspected evidence

The 2025 source introduces non-expansive constant-shift fuzzy logic and gives decision procedures. The 2026 interpolation source establishes qualitative interpolation and syntactic normal forms but not exact unary cardinalities. Ovchinnikov's 2002 max-min representation is a critical credited proof input, not the claimed new census. The closest accessible earlier half-grid result establishes the existence of grid optimizers, which does not imply the classification of all definable functions. Searches for equivalent unary free algebras, exact number sequences, boundary-weighted walks and stronger general statements did not identify a covering theorem. Equivalent work under different terminology remains a historical-priority risk.

## Mathematical value — PASS

The fixed-denominator, one-variable semantic term algebra is a natural quantitative measure of expressivity for a widely studied non-expansive fuzzy propositional base. The complete decorated-path normal form gives exact, all-size cardinalities and a sharp asymptotic rate, distinguishing semantic possibilities from unbounded formula syntax and offering canonical finite encodings.

## Scientific limitations

No claim is made for arbitrary rational constants, additional binary operations, modalities, or multiple variables. The computational tests cover only small denominators and do not independently certify the infinite theorem; exact coverage of all historical literature is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
