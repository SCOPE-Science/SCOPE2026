# Scientific assessment

## Correctness — PASS

The theorem specifies exactly the real-valued propositional operations and rational input grid. Negation and clipped shifts preserve the signed-unary-literal lattice normal form, with the two shift identities proved in RESULT.md. In a minimum clause, the minimum positive offset and minimum negative offset reduce each hidden coordinate to two opposing monotone functions; their intersection is either an endpoint or a point with denominator dividing \(2d\). Independent hidden-coordinate maximization within a clause, followed by supremum/finite-maximum interchange, proves the global claim. The lower interpolant is obtained by negation. For the sharp examples the unique maximum has denominator exactly \(2d\), with the gcd verified separately for even and odd denominators. Exact finite computational checks passed, but the all-size proof is symbolic. No unproved continuum-to-grid assumption is used.

## Originality — PASS within inspected evidence

The first relevant source, Gebhart–Schröder–Wild (2026), establishes uniform interpolation for all non-expansive fuzzy modal formulae, including the propositional sublanguage, and uses arithmetic with division by two in its algorithm. That **covers the existence of interpolation** and is credited. Remark 20 concerns the denominator representation of threshold-judgement interpolants in Section 6, while Section 7 constructs pointwise formula interpolants with explicit divisions by two; neither statement is the fixed universal optimization-witness grid established here. What it does not explicitly establish in the material inspected is the **fixed worst-case precision bound** \(G_{2d}\) for arbitrarily many eliminated propositional variables, the finite substitutive witness identity, or the universal family of sharp-denominator examples. The 2025 fuzzy ALC article fixes the propositional base and reasoning procedures, not these results. Searches of published research records and relevant mathematical literature for aliases and stronger coverage yielded no decisive covering statement. Residual risks include implicit corollaries of established lattice-polynomial elimination or previously undiscovered formulations; failed search alone does not certify absolute novelty.

## Value — PASS

Uniform interpolation for real-valued fuzzy logics is a motivated information-hiding problem, and numerical precision of exact interpolants matters separately from whether interpolants exist. The claim shows that numerical denominators cannot cascade under arbitrarily deep nesting or repeated elimination: one uniform halving suffices, with a best-possible obstruction at *every* denominator. It supplies a finite exact semantic witness set, a concrete constructive algorithm, and a sharp boundary between the original and necessary numerical constants. Its scope and exponential expression-size cost are explicit. The result is more than a one-off grid computation and does not require a further modal generalization to be useful.

## Closest work and limitations

Gebhart–Schröder–Wild, *Non-Expansive Fuzzy Modal Logic Has Uniform Interpolation* (arXiv:2610.32335v1), Sections 2–3 and 6–7, especially Theorems 21 and 23, is the closest stronger **qualitative** interpolation result. Their 2025 *Non-expansive Fuzzy ALC* is the source for the natural signature. Potential alternate statements in older lattice-polynomial and fuzzy quantifier-elimination literature remain a historical-priority risk. The theorem excludes modalities and unrestricted binary Łukasiewicz addition.

Self-review: passed. Independent audit: not yet performed.
