# Independent audit — Cyclotomic Hensel roots form an exact 2-adic prime-support isometry

Audit date: 2026-10-01 (UTC) UTC

## Final claim

Squarefree cyclotomic indices define unique even 2-adic roots of Phi_n(x) = -1. The distance between two such roots is exactly controlled by the least prime on which their prime supports differ; the same roots control even-base valuations and the residue-tree branching of the resulting compact support space.

## Correctness — PASS

The proof is complete. For a squarefree index, the first two cyclotomic coefficients make Phi_n plus 1 an exact 2-adic isometry on the even 2-adics, so there is a unique even root. The standard cyclotomic identity for adjoining a new prime gives a one-prime root displacement whose 2-adic valuation is exactly that new prime; the ultrametric inequality then identifies the least prime in the symmetric difference of two supports. The nonsquarefree case follows from the radical reduction identity. A fresh modular reconstruction checked 49 squarefree roots below 81 and 1,092 pairwise distances. The committed verifier was inspected separately and reports 15,344 pair checks, 8,159 even-base checks, and ten residue-depth checks, all passing. These finite checks are corroboration, not the infinite proof.

## Originality — PASS

No prior source inspected states the canonical Hensel-root support isometry or the resulting 2-adic support geometry. Shunia's primary abstract for arXiv:2609.18480 gives prime recovery from fixed values Phi_n(2). The earlier published record on higher local cyclotomic prime extraction was inspected in full and proves corrected fixed-base valuation residuals and a binary peeling recursion. Those results do not construct the roots beta_n or imply their exact pairwise metric without the new Hensel and prime-toggle argument.

### Equivalent formulations

Searches: Resultary semantic search for cyclotomic Hensel roots, exact prime-support isometry, and 2-adic support metrics; targeted literature search for Cyclotomic Prime Extractors and local cyclotomic valuations

Evidence: The closest earlier published records recover primes from fixed cyclotomic values rather than from a canonical root-space metric.

Reasoning: Fixed-value extraction and the root isometry share first-order cyclotomic expansions, but neither statement is equivalent to the other.

### Broader coverage

Searches: Full inspection of the earlier published record Higher local cyclotomic prime extraction; Primary abstract inspection for arXiv:2609.18480

Evidence: The earlier local theorem isolates the next prime by valuations of corrected residuals at an integer base; Shunia's abstract gives binary least-prime and logarithmic recovery mechanisms.

Reasoning: Neither source supplies a theorem about unique even Hensel roots indexed by supports, pairwise root distances, or residue-tree branching, so no broader theorem located dominates the final claim.

### Exact database or table

Searches: OEIS entry for cyclotomic values at 2 was checked as a natural tabular source.

Evidence: OEIS A019320 tabulates (Phi_n(2)) values but does not encode the Hensel roots or pairwise support metric.

Reasoning: The claim is a structural (2)-adic theorem rather than a database invariant.

### Claim versus prior implication

Searches: Compared the final theorem directly with the fixed-base local residual theorem and Shunia's prime-extractor statements.

Evidence: Prior: valuations of (Phi_n(2)) or corrected (Phi_n(x)) residuals. Final: a canonical root (beta_n) and exact valuation of (beta_m-beta_n) for every pair.

Reasoning: The prior fixed-base identities do not logically identify an entire family of (2)-adic roots or establish the pairwise toggle law.

## Value — PASS

The theorem gives a structural upgrade of local cyclotomic prime extraction: every finite prime support is encoded by a canonical 2-adic point, distances recover the first differing prime, and the same points control even-base valuations and residue-tree complexity. This is a reusable geometric description rather than a finite computation or a restatement of the least-prime valuation.

## Source inspections

- **Joseph M. Shunia, Cyclotomic Prime Extractors, arXiv:2609.18480** — Material read: primary abstract and indexed summary of its local and Archimedean prime-recovery statements. Finding: Covers fixed-value extraction from (Phi_n(2)), not the Hensel-root support metric.
- **Published record Higher local cyclotomic prime extraction (2026-09-18)** — Material read: complete RESULT.md from the frozen repository. Finding: Proves exact valuations for corrected fixed-base cyclotomic residuals and a binary peeling recursion; does not construct (beta_n) or a support isometry.
- **Committed verification artifacts for the audited record** — Material read: complete verifier source and saved output. Finding: Finite exact checks agree with the theorem; they are corroborative only and are not used as an infinite proof.

## Residual risks

- The full text of Shunia's very recent preprint was not retrievable through the available route in this run, so contemporaneous unindexed overlap remains a residual originality risk. The passing judgment rests on the distinct theorem implication, not on unsuccessful search alone.

The assessment applies to the single final claim above. Computational artifacts are corroborative evidence only; they are not used as a substitute for the mathematical proof.
