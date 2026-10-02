# Independent audit — 2026-10-01

**Record:** `SCOPE-20260911-043`

## Correctness — PASS

The headline mod-2 cohomology-ring computation was independently reconstructed from the public graph model without loading the committed pickle files. Direct enumeration of disjoint-closure four-particle Abrams cells gave counts (126,350,320,108,11); rebuilding the barycentric face poset gave 915 vertices, 6948 edges, 15440 triangles, and 13632 tetrahedra. Fresh F2 elimination gave ranks 914, 6031, and 9408 and hence Betti numbers (1,3,1). An independently chosen H1 basis was then used to recompute all nine Alexander-Whitney products, and every product reduced to zero modulo coboundaries. Thus the vanishing pairing is not dependent on the archived basis or pickle witnesses.

## Originality — PASS

The inspected graph-braid literature gives presentations, RAAG/Massey-product criteria, chain models, and Betti-number data, but no source found states the complete mod-2 H1-by-H1 cup pairing for four unordered points on this theta graph. The Ko-La-Park paper is structurally related to four-braid groups and theta subgraphs but its principal theorems concern presentations, RAAG obstructions, and Massey products rather than this exact cup matrix. Published-record searches returned this exact record and nearby homology results, not a prior ring computation.

### Structured originality checks

- **equivalent_formulations:** Searches: theta graph four-braid cohomology ring cup product; Conf_4 theta graph mod 2 H1 H1 H2. Evidence: No prior source with the exact nine-product vanishing statement was identified. Reasoning: The cup-length-two negation and zero bilinear pairing are equivalent here because H1 has dimension three and H2 dimension one; the searched formulations did not reveal prior coverage.
- **broader_coverage:** Searches: Graph 4-braid groups and Massey products theta; graph configuration cohomology rings theta. Evidence: Ko-La-Park covers broad four-braid structural questions; Drummond-Cole supplies Betti-number data for small graphs; Swiatkowski-based work covers homology. Reasoning: These sources do not mechanically determine the cup pairing. Betti numbers alone do not determine the ring, and presentation/Massey criteria do not supply this exact F2 multiplication table.
- **exact_database_or_table:** Searches: published-result semantic search exact theta cup pairing; Betti numbers small graphs theta four particles. Evidence: The exact semantic match was the audited record; related entries concerned H2 torsion or ordered H2 rather than cup multiplication. Reasoning: No prior exact ring table or cup-matrix row was located.
- **claim_vs_prior_implication:** Searches: Abrams model cohomology cup product theta; Ko-La-Park theta four braid. Evidence: Existing models make the finite computation possible but do not state a general theorem forcing all products to vanish. Reasoning: The result requires graph-specific cochain-level calculation; it is not a short parameter specialization of a published multiplication formula.

## Scientific value — PASS

The result determines genuine multiplicative structure beyond Betti numbers: H2 is nonzero while every degree-one product vanishes. This is a natural invariant for the four-point theta configuration space and gives a precise boundary for cup-length-based and formality-related questions without overclaiming other coefficients or Massey products.

## Source inspections

- **Ko, La, Park, Graph 4-braid groups and Massey products** (arXiv:1407.3723). Full HTML/abstract-indexed article, with searches for theta and cohomology terminology. Assessment: RELATED_NOT_COVERING_EXACT_CLAIM. The main results concern commutator presentations, RAAG criteria, and triple Massey products; no exact mod-2 H1-by-H1 cup matrix for this theta configuration was located.
- **Drummond-Cole, Betti numbers of unordered configuration spaces of small graphs** (arXiv:1906.00692). Abstract describing the small-graph Betti database. Assessment: PARTIAL_NUMERICAL_CONTEXT_ONLY. Betti-number data can support dimensions but does not determine the cup product; no exact cup table was found.

## Residual risks

- The committed binary pickle artifacts were deliberately not deserialized during the fresh audit; correctness was instead rebuilt from model.json, which is stronger against artifact-trust concerns but does not byte-verify those pickles.
- Novelty is best-knowledge based; no general published theorem forcing this exact cup matrix was found.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
