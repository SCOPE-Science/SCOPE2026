# Independent mathematical audit — SCOPE-20260920-49d1af418189

Audited at: 2026-10-01T18:05:11.787582Z

Disposition: **passed**

## Correctness — PASS

If a b-coloring uses \(q\) colors, at least \(q\) vertices have degree at least \(q-1\), and connectedness forces every other vertex to have degree at least one; hence \(2m\ge q(q-1)+(n-q)\), yielding \((q-1)^2\le n+2r-1\). The sparse construction completes any connected \(k\)-vertex core of cycle rank \(r\) with exactly the leaves needed to make each core vertex a b-vertex; the dense construction starts from \(K_k\) and adds edges while preserving a \(k\)-chromatic subgraph. Inverting the sharp bound gives the threshold formula, and equality in the sparse degree sum forces the stated leaf-completion structure. The finite atlas and witness checks agree with the symbolic proof.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify.py
- Irving-Manlove 1999
- Jakovac-Peterin survey 2018

### Correctness risks

- The dense-regime minimum-order equality graphs are not classified.

## Originality — PASS

The primary survey records the Irving-Manlove high-degree bound and a classical size-only square-root bound, but not the connected joint order-size extremum. Resultary returned no earlier SCOPE record with the exact fixed-\((n,r)\) formula or threshold classification. The 2026 Zaker paper addresses independence/chromatic-number bounds rather than cycle rank.

### Equivalent formulations

No equivalent joint order-size or cycle-rank theorem was located.

### Broader coverage

Those broader b-chromatic bounds do not imply sharpness for every feasible \((n,r)\) or the minimum-order equality structure.

### Exact database or table

The result is a closed extremal formula, not a recomputation of a known table.

### Claim versus prior implication

The final theorem is not mechanically implied by the cited prior bounds.

### Sources inspected

- The b-chromatic number and related topics—A survey — https://doi.org/10.1016/j.dam.2017.08.008. NOT_COVERING: The survey gives the size-only square-root estimate and other bounds, but no exact connected fixed-order/fixed-cycle-rank extremum.
- Improved bounds on the b-chromatic number using the independence and chromatic numbers — https://arxiv.org/abs/2606.07461. NOT_COVERING: Its bounds depend on independence and chromatic numbers, not cyclomatic number.

### Checked sources

- https://doi.org/10.1016/j.dam.2017.08.008
- https://doi.org/10.1016/S0166-218X(98)00146-2
- https://doi.org/10.1016/S0012-365X(01)00469-1
- https://arxiv.org/abs/2606.07461
- Resultary semantic search

### Residual risks

- The full 2002 Kouider-Maheo article was not inspected in full; the relevant bounds were checked through the comprehensive 2018 survey.

## Value — PASS

This is a natural exact two-parameter extremal problem for a standard graph-coloring invariant. The theorem gives the complete maximum for every feasible order/cycle-rank pair, an exact inverse realization threshold, and a sparse equality classification.

### Value sources

- Jakovac-Peterin survey 2018
- assigned RESULT.md

### Value risks

- The dense equality class remains open.

## Limitations

- Dense-regime minimum-order extremals are not classified.
- Originality is best-of-knowledge with residual risk from differently indexed older work.
