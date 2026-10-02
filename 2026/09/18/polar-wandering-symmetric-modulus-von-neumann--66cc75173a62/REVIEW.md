# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: **PASS**. The positive block matrix \(\begin{bmatrix}|X_j^*|&X_j\X_j^*&|X_j|\end{bmatrix}\) is standard and summing, polar-conjugating, and testing on \((h,-h)\) gives \(U^*PU+Q\ge 2|X|\ge2a1\). A nonzero vector in the intersection of the two strict low-spectral subspaces would make both quadratic-form terms strictly below \(a\), contradicting that inequality. In a finite von Neumann algebra, modularity of center-valued dimension then gives \(2\operatorname{Tr}_Z(E)\le1\). When the polar unitary is a scalar multiple of a symmetry, conjugating and adding the two inequalities gives \(\mathsf S+V\mathsf SV\ge |X|+|X^*|\ge2a1\), proving the doubled threshold. Boundary cutoffs are open, so equality at the threshold causes no gap in the argument.

Originality: **PASS**. The recent matrix papers supply finite-dimensional eigenvalue inequalities for the symmetric modulus, but the audited claim is the projection relation itself and its center-valued finite-von-Neumann consequence. No inspected source or earlier published record was found to state or mechanically imply that projection-wandering formulation. The main residual risk is that the most recent matrix source could not be obtained in full text through the lawful retrieval paths available during this audit.

Scientific value: **PASS**. The statement isolates a structural mechanism behind a sharp median matrix inequality and extends it to type-II finite von Neumann algebras through center-valued comparison. The distinction between the general half-threshold and the polar-Hermitian full threshold, together with sharp finite-dimensional examples, gives a natural reusable operator-algebraic fact rather than a cosmetic reformulation.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
