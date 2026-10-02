# Independent mathematical audit — SCOPE-20260917-009

Audit date: 2026-10-01 (UTC) UTC.

Outcome: **PASSED**.

## Final claim assessed

Weighted-histogram certificates for the edge multiset dimension of Q7–Q10.

## Correctness

**PASS** — The certificate principle follows from exact shell capacities and double-counting of edge-distance totals. A fresh bounded-composition enumeration independently reproduced every displayed \(L\) and \(T\) value for \(d=7,8,9,10\), including the tightest cases \(909>896\), \(5770>5616\), \(8476>8460\), and \(12732>12540\). Thus distinct admissible histograms cannot supply a resolving set at the excluded landmark sizes.

## Originality

**PASS** — Allikvere's full 2026 paper gives explicit resolving-set upper bounds 63, 115, 246, and 492 for \(Q_7,\ldots,Q_{10}\), proves only \(6\le \operatorname{edim}_m(Q_6)\le15\), and explicitly leaves exact minimum sizes open. Resultary search found the present \(Q_7\)–\(Q_{10}\) lower-bound record and the earlier \(Q_6\ge8\) record, but no stronger published lower bounds implying these four \(d+2\) certificates.

## Value

**PASS** — These are exact lower-bound advances for the first finite hypercubes in a newly classified parameter, on a problem whose primary source explicitly leaves exact minima open. Four consecutive dimension-specific certificates are a motivated finite boundary contribution even though they do not determine the exact values.

## Source inspections

- **J. Allikvere, The edge multiset dimension of hypercubes, arXiv:2608.09983v1 (2026).** Primary full text inspected through the finite certificates and lower-bound section. It gives resolving sets of sizes 63, 115, 246, and 492 for \(Q_7,\ldots,Q_{10}\), and only proves \(6\le \operatorname{edim}_m(Q_6)\le15\); exact minima are left open. Consequence: Does not imply the new \(d+2\) lower bounds.
- **Resultary semantic search for edge multiset dimension of \(Q_7,\ldots,Q_{10}\).** The current record and the earlier \(Q_6\ge8\) certificate were the directly relevant hits; no stronger published lower-bound record was located. Consequence: No published Resultary domination located.

## Residual risks

- The archived package lacks the original local verifier files, but every displayed certificate number was independently recomputed from the mathematical definition.
- Exact values of the four edge multiset dimensions remain open.

The accompanying JSON audit records the implication comparisons and exact coverage analysis in structured form.
