# Independent audit — 2026-09-30

**Record:** `SCOPE-20260910-023`

## Correctness — PASS

A fresh catalecticant construction independently verified that all six stated cubic operators annihilate the family, the indicated 14-by-14 middle catalecticant minor is the nonzero constant 86369107968, and the quotient multiplication matrix for L0 has a 10-by-10 minor equal to 1 and rank 10. These facts force h_3=14, identify the fixed six-dimensional Ann_3, and give maximal rank from degree 2 to 3. The committed symbolic Gram determinants are positive for every real parameter pair, giving the remaining uniform Hilbert ranks; Gorenstein duality then closes the WLP maps. The stated uniform non-compressedness and uniform WLP conclusions are correct.

## Originality — PASS

Abdallah–Schenck's full text treats codimension 4 and socle degree 6 as an unresolved WLP boundary: they report no failures and explicitly say it would be interesting to determine whether WLP always holds there. Their paper does not contain this two-parameter inverse system or its fixed annihilator/minor certificate. Searches for the exact sextic expression and its Hilbert/WLP data found no prior source beyond this record.

### Structured originality checks

- **equivalent_formulations:** Checked the apolar inverse-system formulation, catalecticant-rank formulation of the Hilbert function, and maximal-rank multiplication formulation of WLP.
- **broader_coverage:** Prior work gives general positive/negative results around codimension 4 and nearby socle degrees, but does not prove all degree-6 algebras have WLP and does not specialize to this exact family.
- **exact_database_or_table:** Exact-expression and invariant searches found no published table containing this family or its fixed Ann_3/Hilbert data. Nearby published findings concern different apolar forms and do not imply this result.
- **claim_vs_prior_implication:** The global degree-6 WLP statement is explicitly left open in the inspected primary source, so it cannot imply the family theorem. The record's constant-minor and annihilator calculations are additional information, not a restatement of a prior theorem.

## Scientific value — PASS

The result gives a uniform positive two-parameter family exactly in a recognized codimension-4, socle-degree-6 WLP gap, together with explicit structural reasons for both non-compressedness and Lefschetz behavior. That is a motivated family-level theorem rather than an isolated point computation, and it provides useful evidence and guardrails for the broader open cell.

## Source inspections

- **Abdallah–Schenck, Free resolutions and Lefschetz properties of some Artin Gorenstein rings of codimension four** — Full HTML, including the introduction and Section 3.3 on codimension 4, socle degree 6. The source states that no WLP failures were found for degree 6 and poses the universal question; it does not contain the present family. https://arxiv.org/html/2208.01536v2
- **Published-findings semantic search** — Top semantically related apolar/WLP findings. Nearby findings concern different forms or general Jordan constraints; none supplies this exact family theorem. https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE023

## Residual risks

- The result does not resolve the general codimension-4, socle-degree-6 WLP question.
- The committed RESULT.md names output/artifacts paths, while the audited tree stores the verifier files under artifacts/. This is a reproducibility-path documentation defect, not a defect in the theorem.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
