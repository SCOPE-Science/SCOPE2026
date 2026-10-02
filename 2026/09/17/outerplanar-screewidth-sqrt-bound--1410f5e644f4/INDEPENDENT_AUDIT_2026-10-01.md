---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

Every connected simple outerplanar graph on \(n\) vertices has screewidth at most \(40\sqrt n\); together with the fan lower bound, the maximum screewidth among \(n\)-vertex outerplanar graphs is \(\Theta(\sqrt n)\).

## Correctness — PASS

The separator recursion was reconstructed in the tree-cut language. After passing to a maximal outerplanar supergraph, a centroid edge of the subcubic weak dual gives a two-vertex separator whose components have size at most \(3n/4\). If a component boundary is large, Rivera Laboy's bounded-boundary separator lemma supplies a replacement bag of size below \(\sqrt{2n}\) with every component boundary at most \((2+\sqrt2)\sqrt n+4\). Recursing on the connected components, each old link or node adhesion gains at most that component boundary, while the central node adhesion is empty because distinct components have no cross-edges. The numerical recurrence \(40\sqrt{3n/4}+(2+\sqrt2)\sqrt n+4\le40\sqrt n\) was independently checked for all integers \(n\ge6\). Fan scramble number gives the matching order lower bound because scramble number is at most screewidth.

**Evidence.** RESULT.md; Rivera Laboy, arXiv:2609.03755v2; Cenek et al., arXiv:2209.01459

**Residual risk.** The constant 40 is deliberately nonoptimal; the theorem concerns screewidth, not gonality.

## Originality — PASS

Rivera Laboy's full v2 paper was inspected. It proves the outerplanar scramble-number bound, notes that fan and wheel upper bounds can also be obtained via screewidth, and then explicitly asks as Question 5.1 whether outerplanar screewidth is \(O(\sqrt n)\). Searches found no earlier resolution or stronger outerplanar screewidth theorem; the public open-problem index still lists this question. The package therefore answers the exact stated question rather than merely renaming the scramble result.

**Equivalent formulations.** A scramble-number upper bound does not imply the desired screewidth upper bound because the known inequality runs in the opposite direction for obtaining an upper bound.

**Broader coverage.** Treewidth two alone does not bound screewidth by a constant; fans already have square-root order.

**Exact database or table.** The proof needs a recursive decomposition.

**Claim versus prior implication.** The audited recursion is the missing implication needed to answer Question 5.1.

### Source inspections

- **Rivera Laboy, arXiv:2609.03755v2** — full 13-page paper, including fan computation, separator lemmas, outerplanar theorem, and page 13 Question 5.1. Explicitly leaves outerplanar \(O(\sqrt n)\) screewidth open.
- **Cenek et al., arXiv:2209.01459** — indexed theorem-level descriptions used for screewidth/scramble relations. Provides the screewidth framework and inequalities, not the outerplanar theorem.

**Checked sources.** https://arxiv.org/abs/2609.03755; https://arxiv.org/abs/2209.01459; recent web search for outerplanar screewidth

**Residual risk.** The source question is extremely recent, so simultaneous unindexed work remains possible; no such resolution was found.

## Value — PASS

The theorem directly answers an explicit current open question and determines the correct extremal order \(\Theta(\sqrt n)\) on a natural graph class. The result is structural and all-order, not a finite census or constant optimization.

**Residual risk.** The explicit leading constant remains open to substantial improvement.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
