---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

If every vertex on one side of a finite simple bipartite graph has degree \(d\) and the neighborhood-overlap graph on that side has maximum degree \(D\), then \(d!>e(D+1)\) guarantees a distinguishing edge order for every proper edge coloring; in particular every properly edge-colored \(d\)-regular bipartite graph is sequentially orderable for \(d\ge5\).

## Correctness — PASS

Ordering the stars on the opposite bipartition by a random vertex permutation and sorting each star internally by color makes the bad event at a degree-\(d\) vertex exactly one of \(d!\) relative neighbor orders. Relative orders on disjoint neighbor sets are mutually independent, so the neighborhood-overlap graph is a valid dependency graph. The symmetric Lovász local lemma yields the criterion. In the regular case \(D\le d(d-1)\); the inequality holds at \(d=5\) and remains true thereafter. Direct arithmetic checks confirmed the threshold values.

**Checked sources.** frozen assigned RESULT.md; Gorzkowska–Kwaśny arXiv:2609.11832v1 full PDF, including Theorem 9 and concluding open cases; Lovász local lemma

**Residual risks.** The sufficient LLL threshold is not claimed sharp.

## Originality — PASS

The full primary preprint explicitly proves the regular case only for \(d\ge6\) and states that degrees \(3,4,5\) remain open. Resultary and synonymous searches found no earlier bipartite degree-five theorem or the one-sided neighborhood-overlap criterion.

### Equivalent formulations

The record uses a different probability space than the source's random-edge-order argument and reaches the previously open degree-five bipartite case.

### Broader coverage

Thus the source does not dominate the bipartite d=5 result.

### Exact database or table

No finite table is relevant.

### Claim versus prior implication

The prior theorem does not mechanically imply the new bipartite threshold.

**Checked sources.** https://arxiv.org/pdf/2609.11832v1; Resultary semantic search

**Residual risks.** Very recent parallel work could be unindexed, but no concrete covering source was found.

## Value — PASS

The result closes the full degree-five bipartite subcase of a newly stated conjecture and packages the argument as a reusable neighborhood-overlap criterion. This is a natural structural advance rather than a single graph computation.

**Residual risks.** It does not settle arbitrary non-bipartite 5-regular graphs or degrees 3 and 4.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
