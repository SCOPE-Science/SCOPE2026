# Scientific audit — 2026-09-30

## Final claim assessed

For the stated GF(3) representation of the 16-element dyadic excluded minor N4, deleting elements 0 and 1 yields a 3-connected matroid with an F7-minus minor, and every remaining element is fragile with respect to F7-minus: 2, 3, 5, 6, 7, 8 are deletion-only and 4, 9, 10, 11, 12, 13, 14, 15 are contraction-only.

## Correctness — PASS

An independent exact GF(3) reconstruction of the stated matrix reproduced rank 8 after deleting 0 and 1, minimum connectivity value 2 over every nontrivial separation, the stored seven-element F7-minus minor, and the complete 14-element fragility table. The audit re-searched every deletion and contraction side rather than trusting the saved success log.

## Originality — PASS

Brettell--Pendavingh identify N4 as the exceptional 16-element dyadic excluded minor, while Brettell--Clark--Oxley--Semple--Whittle prove a general almost-fragile structural alternative. Neither inspected primary source states this concrete deletion pair, its explicit F7-minus minor, or the full per-element fragility table. Resultary search returned only the present record for the exact N4/F7-minus query.

The comparison explicitly checked equivalent formulations, broader coverage, exact databases or tables, and implication from prior results. Structured searches, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-09-30.json`.

## Scientific value — PASS

The result supplies explicit fragile structure inside the first 16-element dyadic excluded minor, directly aligned with the structural program in which F7-minus-fragile matroids are a difficult case. The exact pair and full fragility ledger are reusable finite structure, not an arbitrary small census.

## Disposition

**PASSED**. This assessment records the mathematical status of the claim and does not assert formal verification or external certification.
