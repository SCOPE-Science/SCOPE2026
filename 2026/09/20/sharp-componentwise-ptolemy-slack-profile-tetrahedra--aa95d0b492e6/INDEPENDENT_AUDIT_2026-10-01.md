# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-aa95d0b492e6`

## Correctness — PASS

The proof reconstructs exactly. Crelle's triangle has sides equal to the three opposite-edge products and area \(6RV\); factored Heron therefore gives \(L\sigma_x\sigma_y\sigma_z=576R^2V^2\), while the three slacks sum to \(L\). The stated disphenoid coordinates realize every positive probability vector of normalized slacks. Holding one normalized slack \(t\) fixed leaves two positive companions exactly when \(t(1-t)^2\ge\eta\), yielding the complete interval between the two roots and full attainability. The displayed defect identity follows by substituting Mazur's centroid-circumcenter identity and the three opposite-edge square decompositions. Degenerate tetrahedra occur only as limits.

### Correctness sources

- assigned RESULT.md
- Mazur 2018 full four-page paper
- Crelle/Heron identity as reproduced in Mazur 2018

### Correctness risks

- The simple lower bound is asymptotically sharp only along degenerating families; the exact interval is the stronger statement.

## Originality — PASS

The classical \(d_3\ge72V^2\) inequality and the ingredients behind the defect identity are prior work and are not counted as the originality-bearing part. Mazur's complete paper explicitly gives Crelle's triangle, the Heron product identity, \(8R^2\ge L\), and the centroid-circumcenter formula. It does not give the slack-simplex surjectivity, the exact fixed-\(\eta\) component interval, or realization of every intermediate value. Fresh Resultary searches returned no stronger theorem covering those complete-profile statements.

### equivalent_formulations

Searches:
- Resultary semantic query: Crelle triangle tetrahedron d3 72 V^2 exact defect centroid circumcenter disphenoid slack simplex
- Mazur 2018 DOI 10.1080/00029890.2018.1411741

Evidence:
- Mazur's Theorem 1 is the product inequality and Theorem 3 is \(8R^2\ge L\); neither parameterizes the normalized slack simplex.
- The audited disphenoid map is onto the entire open simplex and the one-coordinate feasibility condition is exact.

Reasoning:
Equivalent formulations through the Crelle-triangle semiperimeter slacks, normalized barycentric coordinates, and Heron factors were compared.

### broader_coverage

Searches:
- Mazur 2018 full text
- Mazur–Petrenko arXiv:1102.4662
- current Resultary tetrahedral-inequality findings

Evidence:
- The strongest inspected prior theorem supplies the classical product lower bound and equality case, not the complete fixed-product coordinate profile.

Reasoning:
The profile and surjectivity are strictly more informative than the scalar product inequality even though they use its classical ingredients.

### exact_database_or_table

Searches:
- current Resultary tetrahedron/Ptolemy findings

Evidence:
- No exact table or database of normalized slack triples was found; theorem-level searches returned only the audited record as an exact match.

Reasoning:
This is a continuous realizability/profile theorem rather than a finite database claim.

### claim_vs_prior_implication

Searches:
- claim-by-claim implication from Mazur's Heron and centroid identities

Evidence:
- The exact defect decomposition is mechanically obtainable from Mazur's displayed identities and is therefore treated as covered context.
- The surjectivity and complete interval require the additional disphenoid realization and finite-fiber discriminant analysis.

Reasoning:
Partial coverage of one companion identity does not imply the final package's complete profile.

### source_inspections

- **An Inequality for the Volume of a Tetrahedron** — https://doi.org/10.1080/00029890.2018.1411741. Trigger: Closest primary source for the \(d_3\) inequality and centroid identity. Material read: Complete four-page author-hosted paper, including Theorems 1 and 3, Proposition 2, and the proofs of Crelle's theorem and the centroid identity. Method: Full primary statement-and-proof comparison. Assessment: PARTIAL COVERAGE only. Evidence: The paper proves the product inequality and \(8R^2\ge a+b+c\), but has no normalized slack-simplex realization or fixed-product coordinate interval.

### checked_sources

- Mazur 2018 full text
- Mazur–Petrenko arXiv:1102.4662
- current Resultary semantic search
- assigned RESULT.md

### residual_risks

- Because the surviving profile is an elementary symmetric-variable consequence plus an explicit realization, equivalent older solid-geometry folklore under different terminology remains possible.

## Scientific value — PASS

A complete realizability theorem and sharp coordinate profile for a classical tetrahedral inequality is a natural structural refinement: it specifies every possible component slack at fixed scale-invariant Crelle data and proves there is no hidden geometric realizability gap. The result is more than recomputing the classical scalar inequality.

### Value sources

- classical Crelle triangle problem
- assigned disphenoid realization and exact profile

### Value risks

- The defect identity alone would be too close to Mazur's existing proof framework; value rests on the complete profile and realizability.

## Limitations

- Nondegenerate Euclidean tetrahedra only; degenerate cases are limits.
- The profile controls opposite-edge-product slacks, not the six individual edges.
- The defect identity is not treated as independently original from Mazur's framework.
- Originality is best-of-knowledge with explicit folklore risk.

## Disposition

**PASSED**
