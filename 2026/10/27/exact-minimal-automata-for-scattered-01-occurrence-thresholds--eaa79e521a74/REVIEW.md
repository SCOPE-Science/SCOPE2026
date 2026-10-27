# Scientific review

## Correctness — PASS
The concatenation identity is an exact partition of index pairs. The three exceptional residuals are exhaustive outside the positive deficit region. In that region the expression \(h(v)+z(t(v)-1)\ge d\) makes the \(z\ge d\) collapse exact. The separating suffixes \(0^d1\), \(11\), and \(1 0^{d-z_2}1\) prove all remaining classes inequivalent. Every class is reachable. This reconstructs the proof for all \(k\ge1\), including \(k=1\), with no reliance on finite enumeration. The packaged Python checker independently confirms minimization for forty thresholds and more than 1.55 million direct concatenation checks.

## Originality — PASS, subject to bibliographic risk
The closest full scientific comparison is Mansour–Rastegar–Roitershtein (arXiv:1905.05646), Section 2.2: it defines a fine equivalence relation preserving every bounded occurrence count for arbitrary patterns, rather than determining the coarser Myhill–Nerode quotient for the predicate \(N_{01}\ge k\). Atanasiu–Poovanandran–Teh (arXiv:1808.04102) treats Parikh matrices under taking powers; Fazekas–Huang (arXiv:2407.04462) treats generalized occurrence-count matrices. Neither inspected primary source states the present quadratic minimal-state formula. These are statement-level contrasts, not a claim that absence from a search proves novelty. Residual risk: an uncatalogued explicit specialization or general state-minimization theorem may cover the same formula.

## Value — PASS
The natural Parikh-matrix entry \(N_{01}\) gives an elementary but useful threshold language. Its exact minimal-state cost is a structural automata invariant, not merely a generic recognition construction: distinct raw counters collapse on a sharp diagonal, leaving \(\lfloor k^2/4\rfloor+3\) reachable distinguishable classes. The uniform formula and the complete residual classification establish an explicit complexity benchmark for pattern-count threshold recognition.

## Verification limits
The finite checker verifies bounded thresholds and direct concatenation counts; the infinity of positive thresholds follows from the symbolic proof. Published mathematical work establishing bounded-occurrence automata is acknowledged rather than re-claimed. No independently commissioned audit is asserted.

Self-review: passed. Independent audit: not yet performed.
