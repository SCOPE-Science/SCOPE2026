# Independent audit — Deflation-history contamination can make weighted-mass ACA arbitrarily suboptimal

Audit date: 2026-10-01 (UTC) UTC

## Final claim

An explicit positive-semidefinite family makes weighted-mass diagonal ACA choose a second pivot with Frobenius residual N when another legal second pivot after the same first step leaves residual 1. The pathology comes from using original-matrix correlations after the responsible component has already been deflated.

## Correctness — PASS

The positive-semidefinite construction checks exactly. The initial score makes the distinguished index q the unique first pivot, and its Schur-complement update removes the added rank-one term and leaves the prescribed block residual. At that same residual, the original-matrix correlation makes the bad index the unique second pivot, leaving Frobenius norm N; any good block pivot leaves norm 1. The displayed two-by-two spectrum gives the stated best rank-two SVD error. A fresh implementation reproduced the pivot sequence and residuals at N equal to 2, 7, 64, and 257, and the committed verifier source and saved output were inspected.

## Originality — PASS

The motivating ACA preprint's primary abstract introduces the geometry-aware weighted-mass rule and reports empirical performance, but no source located states this deflation-history counterexample or an unbounded fixed-rank factor for that rule. Resultary searches returned the audited record itself and only different ACA/pivoted-Cholesky obstructions, such as complete-pivot Frobenius growth. Those results concern different pivot scores and do not imply the source-specific stale-correlation construction.

### Equivalent formulations

Searches: Resultary semantic search for weighted-mass ACA, deflation history, stale correlation, and fixed-rank suboptimality; targeted web search for the weighted-mass rule in arXiv:2609.17947

Evidence: No equivalent theorem was returned; the primary abstract presents the rule as a heuristic motivated by exterior algebra and experiments.

Reasoning: Generic ACA worst-case bounds do not amount to a counterexample to this specific residual/original-matrix mixed score.

### Broader coverage

Searches: Search of published records for pivoted-Cholesky and ACA counterexamples; Comparison with complete-pivot ACA Frobenius-growth record

Evidence: Prior records cover largest-entry or complete-pivot behavior, randomized Cholesky, and maximum-volume rules, not this weighted-mass score.

Reasoning: No broader theorem located directly applies to the mixed score and forces the same rank-two pathology.

### Exact database or table

Searches: No canonical finite database or table exists for worst-case pivot trajectories of this newly proposed heuristic.

Evidence: The claim is analytic and parameterized by every (N), not a tabulated benchmark.

Reasoning: Database comparison is inapplicable.

### Claim versus prior implication

Searches: Compared the source rule and known pivoted-Cholesky guarantees with the explicit construction.

Evidence: The source paper motivates the score but does not establish residual-state invariance or a worst-case approximation factor.

Reasoning: Existing guarantees for other pivot rules do not imply failure of this distinct rule.

## Value — PASS

This isolates a substantive algorithmic design defect in a new heuristic: the next pivot is not a function of the current residual, and an already removed component whose norm is asymptotically negligible can force an arbitrarily bad fixed-rank choice. The theorem quantifies both approximation loss and one-step-gain loss, so it is more than a toy counterexample.

## Source inspections

- **Trevor Loe, Longxiu Huang, Deanna Needell, A Geometric View of Adaptive Cross Approximation via Exterior Algebra, arXiv:2609.17947** — Material read: primary abstract and bibliographic record. Finding: Introduces the geometry-aware weighted-mass pivoting rule and reports experiments; the accessible primary material does not state the audited failure theorem.
- **Published record Sharp one-step Frobenius growth under complete-pivot ACA** — Material read: Resultary title/summary and repository comparison target. Finding: Concerns largest-entry complete-pivot behavior rather than weighted-mass deflation-history contamination.
- **Committed verification artifacts for the audited record** — Material read: complete verifier source and saved output. Finding: Numerically reproduces the exact construction; the audit separately checked the algebra.

## Residual risks

- The full arXiv:2609.17947 manuscript was not retrievable through the available route in this run, so a very recent source-text overlap is a residual risk. The accessible abstract and the theorem's source-specific construction make exact coverage unlikely, but the risk is recorded explicitly.

The assessment applies to the single final claim above. Computational artifacts are corroborative evidence only; they are not used as a substitute for the mathematical proof.
