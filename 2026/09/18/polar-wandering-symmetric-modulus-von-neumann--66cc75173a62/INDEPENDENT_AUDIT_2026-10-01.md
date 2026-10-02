# Independent audit — 2026-10-01

## Final claim

Polar-wandering spectral projections for symmetric moduli in von Neumann algebras

## Correctness — PASS

The positive block matrix \(\begin{bmatrix}|X_j^*|&X_j\X_j^*&|X_j|\end{bmatrix}\) is standard and summing, polar-conjugating, and testing on \((h,-h)\) gives \(U^*PU+Q\ge 2|X|\ge2a1\). A nonzero vector in the intersection of the two strict low-spectral subspaces would make both quadratic-form terms strictly below \(a\), contradicting that inequality. In a finite von Neumann algebra, modularity of center-valued dimension then gives \(2\operatorname{Tr}_Z(E)\le1\). When the polar unitary is a scalar multiple of a symmetry, conjugating and adding the two inequalities gives \(\mathsf S+V\mathsf SV\ge |X|+|X^*|\ge2a1\), proving the doubled threshold. Boundary cutoffs are open, so equality at the threshold causes no gap in the argument.

## Originality — PASS

The recent matrix papers supply finite-dimensional eigenvalue inequalities for the symmetric modulus, but the audited claim is the projection relation itself and its center-valued finite-von-Neumann consequence. No inspected source or earlier published record was found to state or mechanically imply that projection-wandering formulation. The main residual risk is that the most recent matrix source could not be obtained in full text through the lawful retrieval paths available during this audit.

### Equivalent formulations

Searches/sources: Aouichaoui–Lee 2026 symmetric modulus median inequality; Bourin–Lee 2026 operator symmetric modulus.

Evidence: The located results are formulated as finite-matrix eigenvalue/triangle inequalities.

Reasoning: Eigenvalue median bounds follow from a half-dimension projection statement in matrices, but the converse does not supply the meet-zero identity or a center-valued statement in finite factors.

### Broader coverage

Searches/sources: positive 2x2 operator matrices tau-measurable operators; symmetric modulus von Neumann algebra inequalities.

Evidence: General positive-block and measurable-operator literature supplies the block positivity technology.

Reasoning: Those general tools do not by themselves state the polar-translated low spectral projection disjointness or its sharp thresholds.

### Exact database or table

Searches/sources: published SCOPE record index: polar wandering symmetric modulus center-valued trace.

Evidence: The only exact matching published record was the audited record itself.

Reasoning: No exact database/table coverage was located; this is only best-of-knowledge evidence, not a proof of novelty.

### Claim versus prior implication

Searches/sources: Aouichaoui–Lee Theorem 3.1 context; Bourin–Lee symmetric modulus inequalities.

Evidence: The prior matrix theorem gives a scalar ordered-eigenvalue consequence at the same threshold.

Reasoning: That consequence does not imply a specific polar-unitary meet-zero relation in arbitrary von Neumann algebras, so prior implication is not decisive coverage.

## Scientific value — PASS

The statement isolates a structural mechanism behind a sharp median matrix inequality and extends it to type-II finite von Neumann algebras through center-valued comparison. The distinction between the general half-threshold and the polar-Hermitian full threshold, together with sharp finite-dimensional examples, gives a natural reusable operator-algebraic fact rather than a cosmetic reformulation.

## Sources inspected

- **Mohamed Amine Aouichaoui and Eun-Young Lee, Solutions to some open problems in matrix analysis** (https://arxiv.org/abs/2609.20094): RELATED_NOT_DECISIVE_COVERAGE. The located theorem is a finite-matrix eigenvalue statement, not the audited projection-wandering or center-valued theorem.
- **Jean-Christophe Bourin and Eun-Young Lee, Triangle inequalities for the operator symmetric modulus** (https://arxiv.org/abs/2602.19607): GENERAL_MATRIX_FRAMEWORK. The paper develops finite-matrix symmetric-modulus inequalities but does not furnish the audited finite-von-Neumann projection statement.

## Residual risks and limitations

- The newest finite-matrix paper was not available in verified full text in this audit, leaving a bounded literature-access risk.
- No claim is made for arbitrary unbounded measurable operators or for a normalized half-dimension statement in properly infinite algebras.

## Disposition

**passed**
