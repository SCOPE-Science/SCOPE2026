# Independent mathematical audit — 2026-10-01

## Final claim assessed

Powered-Bohr upper bounds and duality for the ell_p shift calculus

## Correctness — PASS

PASS. The norm transference step is valid: a finite polynomial of either unilateral shift is a compression of the corresponding bilateral convolution operator, while finitely supported bilateral test vectors can be translated away from the boundary, so the unilateral and bilateral polynomial norms coincide. Banach adjoint duality therefore gives \(R_p=R_{p'}\). Testing Taylor truncations of the disk automorphism \(\phi_a(z)=(a-z)/(1-az)\) on a far basis vector produces disjoint coordinates and exactly the stated powered coefficient sum, yielding the \(eta_q\) upper bound. The endpoint \(\ell_1\) and \(\ell_\infty\) norms reduce exactly to the classical Bohr sum, while \(p=2\) is von Neumann's inequality. The two first-order expansions around \(q=2\) correctly bracket the linear defect by \((\log2)/2\) and \((\log3)/2\).

## Originality — PASS

PASS to the best of current knowledge. Kania's recent primary paper supplies the shift construction and the interpolation lower bound but its accessible primary statement does not contain the dual-exponent identity, powered-Bohr obstruction, endpoint limits, or Hilbert-point linear defect. Kayumov--Ponnusamy's 2019 primary paper was inspected through its journal page and full-document metadata: it proves the scalar powered Bohr radius for Schur functions, not an operator \(\ell_p\)-shift radius. Resultary searches for the operator radius, duality and powered-Bohr transfer returned this record as the only exact match. The Kania PDF could not be retrieved in verified full text during this run, so an unindexed overlap inside that very recent paper remains an explicit residual risk.

### equivalent_formulations

Searches: ell_p unilateral shift contractivity radius powered Bohr duality; R_p R_p' canonical shift polynomial calculus

Evidence: The exact semantic search returned the audited record; scalar Bohr results concern coefficient sums rather than operator norms.

Reasoning: The bilateral-convolution formulation is equivalent to the shift formulation but does not turn the scalar powered-Bohr theorem into the claimed operator statement without the new test/transference argument.

### broader_coverage

Searches: Kania spectral constants algebraic numerical ranges canonical left shift; Kayumov Ponnusamy powered Bohr inequality

Evidence: Kania supplies the shift setting and lower bound; Kayumov--Ponnusamy supply the scalar obstruction.

Reasoning: Neither inspected statement dominates the combined duality and operator upper-bound theorem.

### exact_database_or_table

Searches: Resultary semantic search powered Bohr ell_p shift radius

Evidence: No table/database is natural for this analytic radius; no earlier exact published record was found.

Reasoning: The relevant check is theorem-level literature comparison.

### claim_vs_prior_implication

Searches: arXiv:2609.18963 shift interpolation radius; doi:10.5186/aasfm.2019.4416 powered Bohr

Evidence: The two prior ingredients live in distinct operator and scalar settings.

Reasoning: The Möbius-truncation test and unilateral/bilateral duality bridge are additional arguments; the final bounds are not a mere parameter substitution.

## Scientific value — PASS

PASS. The result turns a one-sided interpolation estimate for a newly introduced shift radius into a quantitative two-sided theory, identifies the Hilbert exponent as the unique full-radius point, gives exact duality and endpoint limits, and pins down the first-order scale of the defect near \(p=2\). Those are natural structural properties of the new invariant rather than arbitrary evaluations.

## Source inspections

- **Spectral constants for algebraic numerical ranges** — https://arxiv.org/abs/2609.18963. Material read: Primary abstract/indexed statement; repeated full-text retrieval attempts did not yield a verified PDF. Assessment: PLAUSIBLE_PRIMARY_SOURCE_WITH_ACCESS_LIMITATION. Evidence: The accessible statement describes the canonical left-shift construction and contractive polynomial calculus but not the audited powered-Bohr/duality theorem.
- **On a powered Bohr inequality** — https://doi.org/10.5186/aasfm.2019.4416. Material read: Journal landing page, abstract, and public PDF metadata identifying the powered coefficient sum and exact automorphism radius problem. Assessment: SCALAR_PRIOR_INGREDIENT_NOT_OPERATOR_COVERAGE. Evidence: The paper concerns Schur-function coefficient sums for exponents between one and two, not the \(\ell_p\) unilateral-shift contractivity radius.

## Limitations and residual risks

The theorem does not identify the exact radius for \(1<p<\infty\), \(p
e2\), and the shift-specific transference argument should not be generalized to arbitrary contractions.

- The full Kania PDF was not obtained in verified text during this run, so hidden overlap in that extremely recent preprint remains possible.
- The exact interior value of \(R_p\) remains open; the audit validates only the stated bounds and limiting geometry.

## Disposition

**passed**
