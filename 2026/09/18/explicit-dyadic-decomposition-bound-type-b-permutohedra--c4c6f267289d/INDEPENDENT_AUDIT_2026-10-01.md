# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-c4c6f267289d`

## Correctness — PASS

The proof reconstructs. For a linearly independent set of type-B roots, the signed-incidence support decomposes after unit pivots into unbalanced cycle blocks whose Smith torsion is elementary of order two, so twice the saturated root lattice lies in the generated lattice. Vallée's deletion-contraction join geometry supplies independent root-spanned direction spaces. Hence a genuinely two-sided join adds at most one factor two to the quotient exponent, while a join with a point adds none. The recurrence gives exponent at most \(2^{\max(0,\lfloor(d-1)/2\rfloor)}\). Multiplying barycentric coordinates by that annihilator makes them integral and yields the stated dyadic decomposition. The tetrahedral type-D example is non-IDP and gives the lower bound one from dimension three onward; products with cubes preserve that obstruction.

### Correctness sources

- Mathieu Vallée, arXiv:2609.18331, deletion-contraction triangulation and dyadic decomposition corollary
- Bolker–Zaslavsky 2006 half-integrality framework
- assigned RESULT.md

### Correctness risks

- The upper bound is not claimed optimal for dimensions at least five.
- The argument concerns quotient exponent, not normalized volume/order.

## Originality — PASS

Vallée proves existence of an ambient-dimension dyadic exponent by taking a maximum normalized volume over finitely many simplices, but does not give the audited intrinsic-dimension bound or quotient-exponent recurrence. The half-integrality of signed/bidirected incidence systems is classical, so originality lies in tracking exponent through Vallée's joins and obtaining the explicit bound plus sharp values in dimensions three and four.

### equivalent_formulations

Searches:
- arXiv:2609.18331 full text, dyadic decomposition and deletion-contraction sections
- exact phrase/search for the floor intrinsic-dimension exponent

Evidence:
- Vallée's corollary chooses an exponent from a finite maximum of normalized volumes rather than the stated floor bound.
- No inspected source states the audited exponent recurrence.

Reasoning:
Equivalent formulations as an annihilator bound on simplex edge-lattice quotients and as a uniform dyadic decomposition exponent were compared.

### broader_coverage

Searches:
- Vallée's full type-B generalized-permutohedron theorem
- Bolker–Zaslavsky half-integrality

Evidence:
- The broader triangulation theorem gives dyadic triangulations but not this quantitative exponent; half-integrality supplies only the one-step lattice ingredient.

Reasoning:
Neither broader result mechanically yields the floor bound without the new join-depth analysis.

### exact_database_or_table

Searches:
- Morales arXiv:2609.02778 and the standard tetrahedral nonnormality example

Evidence:
- The tetrahedron supplies the lower obstruction but no table of uniform dyadic exponents was located.

Reasoning:
The exact upper bound is not a database/table lookup.

### claim_vs_prior_implication

Searches:
- direct implication comparison with Vallée Corollary 3.7

Evidence:
- Vallée's existence exponent may be much larger because normalized volume is quotient order, whereas the audited argument tracks quotient exponent.

Reasoning:
Existence of some dyadic power does not imply the displayed explicit intrinsic-dimension power.

### source_inspections
- **Regular dyadic triangulations of delta-matroid polytopes** — https://arxiv.org/abs/2609.18331. Trigger: Same object and triangulation mechanism. Material read: Full accessible preprint sections on root minors, deletion/contraction, coordinate dicing, dyadic triangulations, and the uniform decomposition corollary. Method: Primary full-text theorem and proof comparison. Assessment: Provides the recursive triangulation and qualitative dyadic decomposition, but not the audited explicit exponent. Evidence: Its uniform exponent is chosen from maximal normalized simplex volume over finitely many delta-matroids.
- **A simple algorithm that proves half-integrality of bidirected network programming** — https://doi.org/10.1002/net.20117. Trigger: Classical lattice ingredient behind type-B roots. Material read: Published theorem/scope material. Method: Prior-lemma comparison. Assessment: Covers half-integrality, not the triangulation-recursion exponent theorem. Evidence: The half-integral basis property matches the elementary two-torsion ingredient.

### checked_sources

- https://arxiv.org/abs/2609.18331
- https://doi.org/10.1002/net.20117
- https://arxiv.org/abs/2609.02778
- assigned RESULT.md

### residual_risks

- The motivating preprint is extremely recent, so unindexed parallel work remains possible.

## Scientific value — PASS

An explicit intrinsic-dimension saturation bound materially strengthens a finiteness-only decomposition theorem, and the exact low-dimensional values identify a natural boundary where ordinary IDP first fails. Tracking exponent rather than quotient order is structurally useful for future decomposition bounds.

### Value sources

- Vallée's qualitative dyadic decomposition theorem
- the type-D tetrahedral obstruction

### Value risks

- Optimality remains open for dimensions at least five.

## Limitations

- The bound is not claimed optimal for dimensions at least five.
- The result is about dyadic decomposition, not ordinary normality or IDP.
- Originality is best-of-knowledge because the motivating preprint is recent.

## Disposition

**PASSED**
