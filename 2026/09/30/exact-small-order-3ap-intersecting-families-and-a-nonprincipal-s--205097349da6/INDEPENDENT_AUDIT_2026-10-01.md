# Independent mathematical audit — Exact small-order 3AP-intersecting families and a nonprincipal sharp construction

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** For a pair with exactly three arithmetic-progression completions, any two subsets containing the pair and at least two completion points share a completion, so their intersection contains a progression; the construction has exactly the conjectured size. For orders three through ten, the inspected verifier constructs the exact compatibility graph and enumerates every maximal clique. The independent replay reproduced the conjectured maximum at every order, total maximum-family counts 1, 2, 4, 6, 10, 14, 19, 24, and nonprincipal counts 0, 0, 0, 0, 1, 2, 3, 4, with every maximum family matching the predicted principal or pair-majority construction.

Checked sources: Assigned RESULT.md; verify.py and census.json; Independent complete replay for orders three through ten; Keevash 2026 complete preprint.

Residual correctness risks: The repository has one exhaustive algorithm for the finite classification; the audit reran it rather than implementing a second algorithm..

## Originality

**PASS.** Keevash's complete 2026 preprint states the Simonovits--Sos conjectured bound, gives a fixed-progression star as the evident sharp example, and proves only a weaker general density bound. It contains neither the exact small-order classifications nor the pair-majority construction. No earlier matching finite classification or nonprincipal equality family was located.

### Equivalent formulations

Searches/sources: Published-record search for exact small-order 3AP-intersecting families and pair-majority constructions; arXiv:2609.18870; Chung--Graham--Frankl--Shearer 1986.

Evidence: The exact archive match was the audited theorem. Keevash defines the same problem and conjectured optimum. The complete Keevash preprint names only fixed-progressions as the obvious sharp examples.

No equivalent nonprincipal construction or finite classification was found.

### Broader coverage

Searches/sources: Keevash bounded-codegree hypergraph-intersection theorem; General intersection theorems cited there.

Evidence: Keevash proves only a density bounded away from one half, much weaker than the conjectured one-eighth density. The general theorem does not classify equality.

No inspected broader result implies the exact cases or the new equality construction.

### Exact database or table

Searches/sources: Published archive exact search for orders three through ten; Search for nonprincipal equality examples for the Simonovits--Sos problem.

Evidence: No earlier finite table or pair-majority construction was located.

The census is not a recomputation of an identified known table.

### Claim versus prior implication

Searches/sources: Does Keevash's density theorem imply the exact conjectured bound in small orders?; Does the fixed-progression example imply the pair-majority family?.

Evidence: The density theorem is strictly weaker and gives no exact small-order conclusion. The pair-majority family uses a different codegree-three mechanism and has no common fixed progression.

Both finite exactness and the nonprincipal construction require additional arguments.

### Source inspections

- **A non-trivial bound for 3AP-intersecting families** — PRIMARY_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2609.18870
  Trigger: Exact same problem and conjectured bound.
  Material read: All three pages of the primary preprint, including the full theorem and proof.
  Method: authorized institutional full-text extraction after open-access text retrieval failed
  Evidence: The complete paper proves a weaker density theorem and contains no exact small-order classification or pair-majority construction.

Residual originality risks:
- Unpublished or unindexed computations of the first few cases cannot be ruled out by corpus search alone.

## Scientific value

**PASS.** The result not only verifies the conjectured optimum through order ten but also gives a nonprincipal sharp construction valid from order seven onward. That infinite construction changes the equality landscape of the open problem: any future equality theorem must allow more than fixed-progression stars.

Residual value risks: The general upper bound and complete equality classification beyond order ten remain open..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
