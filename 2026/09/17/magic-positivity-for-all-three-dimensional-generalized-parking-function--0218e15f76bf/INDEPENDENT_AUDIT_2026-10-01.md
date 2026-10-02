# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260917-004`

## Correctness — PASS

The dimension-three proof reconstructs from the primary recursion rather than from finite testing. The full primary preprint text was inspected through the lattice-slice recursion, the arbitrary-parameter Ehrhart construction, and the dilation lemma. Substituting the dilation parameters into the dimension-three recursion and changing to the degree-three magic basis independently reproduces the four coefficients in RESULT. After \(A=a-1\), \(B=b-1\), and \(C=c-1\), every coefficient of the displayed numerators is nonnegative, so all magic coefficients are nonnegative for every positive integer triple. The package verifier was also read completely and its symbolic identities agree with this independent derivation; its 500 lattice enumerations are corroboration only.

### Correctness sources

- Hill–Luo–Trinh–Vindas-Meléndez, arXiv:2607.15503, especially Theorems 2.2, 3.5, 4.1, Lemma 5.1 and the magic-positivity discussion
- assigned RESULT.md
- artifacts/verify.py
- independent symbolic reconstruction of the cubic magic coefficients

### Correctness risks

- The theorem is only dimension three; nothing here proves the arbitrary-dimension conjecture.

## Originality — PASS

The motivating primary paper proves magic positivity for the two-parameter family \(X_n(a,b,\ldots,b)\) and explicitly leaves arbitrary parameter vectors as Conjecture 8.1. A fresh published-findings search found the audited theorem itself but no independent result covering all triples \(X_3(a,b,c)\). The primary paper's finite checks on small triples are not an infinite theorem, and its arbitrary-parameter Ehrhart formula does not force magic-basis coefficient signs without the new specialization and expansion.

### equivalent_formulations

Searches:
- semantic search for magic positivity of \(X_3(a,b,c)\) with arbitrary positive parameters
- exact-title and generalized-parking-polytope searches
- inspection of Conjecture 8.1 in arXiv:2607.15503

Evidence:
- The exact matching published finding was the audited record; no separate covering theorem appeared in the fresh search.
- The primary paper explicitly says the arbitrary-\(\mathbf b\) magic-positivity question remains open.

Reasoning:
Equivalent formulations via arbitrary length-three parameter vectors and degree-three magic-basis nonnegativity were checked.

### broader_coverage

Searches:
- Hill–Luo–Trinh–Vindas-Meléndez two-parameter theorem
- arbitrary-parameter Ehrhart formula for generalized parking-function polytopes

Evidence:
- Theorem 7.2 in the source treats \(X_n(a,b,\ldots,b)\), while Theorem 5.9 supplies an Ehrhart formula for arbitrary parameters.

Reasoning:
Neither broader result states nor mechanically implies positivity of the four magic coefficients for every arbitrary triple.

### exact_database_or_table

Searches:
- published computational checks for small generalized parking-function triples

Evidence:
- The source reports finite computational evidence for bounded parameter triples, not a complete table or theorem over all positive triples.

Reasoning:
Finite checks cannot establish the infinite three-parameter statement.

### claim_vs_prior_implication

Searches:
- comparison of source Conjecture 8.1 with the audited coefficient formulas

Evidence:
- The source leaves the general statement conjectural; the audited cubic expansion resolves the first open arbitrary-parameter dimension.

Reasoning:
The final claim is not a corollary of a prior sign theorem located in the search.

### source_inspections
- **Lattice Slices, Ehrhart Polynomials, and Magic Positivity of Generalized Parking-Function Polytopes** — https://arxiv.org/abs/2607.15503. Trigger: Primary source of the recursion and open magic-positivity conjecture. Material read: Full preprint text through pages 1–12, including Theorems 2.2, 3.5, 4.1, Lemma 5.1, and the statement of the two-parameter magic theorem/open conjecture. Method: Primary full-text theorem and formula comparison. Assessment: The source supplies the exact recursion and leaves arbitrary parameter vectors open; it does not cover the audited all-triples theorem. Evidence: Theorem 7.2 is two-parameter and Conjecture 8.1 asks for arbitrary \(\mathbf b\).
- **Assigned symbolic verifier** — artifacts/verify.py. Trigger: Critical coefficient formulas. Material read: Complete source file. Method: Line-by-line inspection plus independent symbolic re-derivation. Assessment: The shifted magic coefficients are reproduced exactly; finite lattice enumeration is correctly used only as corroboration. Evidence: Independent algebra returns the same four coefficient expressions.

### checked_sources

- https://arxiv.org/abs/2607.15503
- assigned RESULT.md and artifacts/verify.py
- fresh semantic published-findings search

### residual_risks

- Because the proof is short once the source recursion is known and the motivating preprint is recent, an unindexed contemporaneous independent proof remains possible.

## Scientific value — PASS

This is the natural first open arbitrary-parameter dimension of a published conjecture. It replaces bounded experiments by a complete infinite three-parameter theorem and exposes explicit coefficient polynomials that explain positivity structurally. That is a meaningful classification boundary rather than an arbitrary finite slice.

### Value sources

- arXiv:2607.15503, Conjecture 8.1 and the two-parameter classification
- audited exact coefficient formulas

### Value risks

- The result does not extend the conjecture beyond dimension three.

## Limitations

- The accepted theorem is limited to parameter vectors of length three.
- Originality is best-of-knowledge rather than a historical priority certificate.
- Finite enumeration in the package is corroborative; the acceptance rests on the symbolic all-parameter proof.

## Disposition

**PASSED**
