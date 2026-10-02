# Independent mathematical audit — 2026-09-30

## Outcome

**PASSED** for the final finding as stated.

## Correctness — PASS

Reconstruction of PG(2,4) over F4 gives 21 points and 21 lines, each 5-regular. Independent enumeration of all C(21,8)=203490 point 8-sets gives maximum top-8 line-degree sum 24 with 7560 attaining point sets; dual enumeration in the committed verifier gives the same 24/7560 result. The KST pair-counting argument gives integer ceiling 25, and the exhaustive top-8 calculation excludes 25. The two full 21-line profiles of attaining point sets occur with counts 5040 and 2520 exactly as stated, and the explicit 24-incidence witness checks.

## Originality — PASS

Searches for the exact small-order extremal function M(8,8) in PG(2,4), its value 24, and the two extremal degree types found no earlier exact census. General finite-field incidence theorems give broader asymptotic bounds but do not imply the small-order ceiling. Residual risk is principally grey literature or a small finite-plane database.

### equivalent_formulations

Searches: "M(8,8)" "PG(2,4)"; "PG(2,4)" "24" incidences 8 points 8 lines; finite projective plane order 4 eight points eight lines

Evidence: The assigned record was the only exact semantic hit; other PG(2,4) records concern blocking sets or unrelated configurations.

Reasoning: Equivalent point-line dual formulations and top-k degree-sum formulations were searched; no earlier exact 8x8 ceiling was identified.

### broader_coverage

Searches: Vinh finite field point line incidence bound; Stevens de Zeeuw finite field incidence bound; VC-dimension finite field incidence point line

Evidence: These sources provide general/asymptotic incidence estimates; at m=n=8 they do not imply 24 and are explicitly looser than the finite-plane calculation.

Reasoning: General bounds do not cover the exact finite extremal value or its attaining types.

### exact_database_or_table

Searches: PG(2,4) incidence tables 8-subsets; projective plane order 4 subset line intersection census

Evidence: No inspected database/table supplied the 7560 attaining 8-sets or 22680 attaining point-line pairs.

Reasoning: A complete incidence table of PG(2,4) would permit mechanical recomputation, but no published target census was found.

### claim_vs_prior_implication

Searches: Kovari Sos Turan pair counting projective plane; finite projective plane exact incidence extremal 8 8

Evidence: KST/Cauchy only yields 25; the final one-unit improvement requires the finite geometry computation.

Reasoning: The prior general inequalities do not entail the exact theorem.

### source_inspections


- **Assigned PG(2,4) verifier** (2026/09/07/025/artifacts/verify.py): trigger=Critical finite exclusion of incidence 25.; material read=Complete source file.; method=Source inspection plus independent reconstruction/enumeration.; assessment=Rebuilds F4 and PG(2,4), checks regularity, enumerates both sides and verifies the degree-sequence reduction.; evidence=Independent point-side enumeration reproduced maximum 24 and 7560 attaining sets.

- **Szemerédi–Trotter type theorem and sum-product estimate in finite fields** (https://arxiv.org/abs/0711.4427): trigger=General finite-field point-line incidence prior art.; material read=Abstract and theorem scope.; method=Primary preprint abstract inspection.; assessment=General bound only; does not cover the exact PG(2,4), 8x8 ceiling.; evidence=The record's exact 24 is strictly below the general comparison bound at this scale.

### checked_sources

- arXiv:0711.4427
- arXiv:1609.06284
- arXiv:2303.00330
- assigned RESULT.md and verify.py

### residual_risks

- Unpublished finite-plane computations or differently indexed small-order tables may overlap.
- Originality is best-of-knowledge, not a priority certificate.

## Scientific value — PASS

M(8,8) is a natural extremal parameter of the smallest nontrivial finite projective plane where standard pair-counting leaves a one-incidence gap. Closing that gap and classifying extremal degree types gives a useful exact benchmark rather than an arbitrary tiny instance.

## Limitations

- The exclusion of 25 is computational, not synthetic.
- Scope is the single plane PG(2,4) and 8x8 configuration size.
- Originality has residual grey-literature risk.
