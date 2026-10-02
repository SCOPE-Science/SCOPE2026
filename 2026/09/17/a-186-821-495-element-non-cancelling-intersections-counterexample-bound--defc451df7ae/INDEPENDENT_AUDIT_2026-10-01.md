# Independent audit — SCOPE-20260917-006

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For p=571, the refined first-moment argument produces an existential affine-line marking with no admissible set of size 2p through 4p, yielding through Wilhelm's construction an NCI counterexample lattice with 186,821,495 elements.

## Correctness

**PASS** — The first-moment proof was reconstructed from the incidence identities and exact probability bounds, not from the saved success log. Independent exact arithmetic gives q=1-C(552,35)/C(571,35)<353/500, S(1142)=328042/15, minimum derivative margin about 27.2677, the successive-term ratio below 1/40, geometric expectation below 14/39, and lattice size 186,821,495. Wilhelm's primary text supplies the structural implication from a marking with no admissible set in the interval to the lattice counterexample.

Residual risks:
- The marking is existential rather than explicit.
- The final lattice implication depends on Wilhelm's structural lemmas; those were checked in the accessible primary text but not re-proved from first principles here.

## Originality

**PASS** — Best-of-knowledge originality passes for the quantitative p=571 bound. Wilhelm's theorem gives the same construction only for primes at least 100,000, while targeted published-results and literature searches found no prior p=571 or stronger numerical bound. The underlying construction method is explicitly credited to Wilhelm.

### equivalent_formulations

Searches: Resultary semantic search: non-cancelling intersections Wilhelm affine plane marking p=571 186821495 elements first moment; Web search: 2608.27416 p=571 NCI counterexample

Evidence: Published-results search returned SCOPE-20260917-006 as the exact match and no independent exact p=571 result among the leading matches.; Wilhelm's arXiv:2608.27416 theorem states the construction for p at least 100,000.

Reasoning: The audited statement is the same NCI construction specialized after a sharper probabilistic estimate, but the numerical threshold p=571 is not stated by the source theorem.

### broader_coverage

Searches: arXiv:2608.27416 full accessible HTML, theorem and construction sections; arXiv:2401.16210 NCI conjecture background

Evidence: Wilhelm covers the mechanism and a much larger quantitative range; the original conjecture paper supplies the target problem, not this improved bound.

Reasoning: No broader theorem inspected forces existence for p=571.

### exact_database_or_table

Searches: Exact number searches for 186821495 and p=571 together with NCI/non-cancelling intersections

Evidence: No independent exact-table or database entry with this smaller counterexample size was located.

Reasoning: This is a theorem-level quantitative bound rather than a table lookup.

### claim_vs_prior_implication

Searches: Comparison with Wilhelm theorem p>=100000 and the p=100003 displayed example

Evidence: The source's p>=100000 hypothesis does not imply p=571; the new work is the strengthened first-moment estimate.

Reasoning: The conclusion follows from Wilhelm only after proving a new admissible-set exclusion at p=571.

### Source inspections

- **Refutation of the Non-Cancelling-Intersections Conjecture** — https://arxiv.org/abs/2608.27416
  - Trigger: Closest primary construction and quantitative theorem
  - Material read: Accessible full HTML: theorem statement, affine-plane marking construction, lattice size formula, and structural no-winning-tree implication
  - Method: full-text web inspection
  - Assessment: NOT_COVERING exact p=571 bound; provides the inherited structural mechanism
  - Evidence: Primary theorem requires p at least 100,000 and gives size p³+2p²+2.
- **A 186,821,495-element non-cancelling-intersections counterexample bound** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE006
  - Trigger: Exact published-results hit
  - Material read: Title and summary
  - Method: semantic published-results search
  - Assessment: SELF_MATCH
  - Evidence: Exact same quantitative claim.

Originality residual risks:
- The literature search cannot exclude private or unindexed contemporaneous work; Wilhelm notes contemporaneous independent activity around the general conjecture.

## Value

**PASS** — The result substantially lowers the explicit size of a counterexample lattice in a recent refutation, from a displayed construction near 10^15 elements to 186,821,495, using a rigorous strengthened threshold. The source itself identifies the quantitative size as a natural direction. This is a motivated extremal improvement, not an arbitrary parameter slice.

Residual risks:
- Minimality is not proved, so the contribution is an upper bound on counterexample size rather than an optimum.

## Scientific limitations

- The marking is existential and p=571 is not claimed minimal.
- The conceptual lattice construction is inherited from Wilhelm; the contribution is the quantitative threshold improvement.

## Disposition

**PASSED**

This audit is not peer review or external certification.
