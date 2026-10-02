# Independent scientific audit — SCOPE-20260930-2f4a2e65a3d2

Audited at: 2026-10-02T00:16:07.579488Z

Disposition: **passed**

## Correctness — PASS

Every proper color class lies inside one multipartite part. Calling a part active when it contains an odd-sized color class, the odd-neighborhood condition for every vertex is equivalent to having at least two active parts. Every odd-order part is automatically active; an even part is inactive when monochromatic and can be activated with exactly one extra color by an odd-odd bipartition. This proves \(\chi_o(K_{n_1,\ldots,n_r})=r+\max\{0,2-o\}\). Optimality then forces exactly the stated active parts, and an even \(n_i\)-set has \(2^{n_i-2}\) unordered odd-odd bipartitions, giving the three exact formulas for \(U(G)\) and the labeled factor \(k!\).

### Correctness sources

- assigned RESULT.md
- assigned verify.py
- Petruševski–Škrekovski, arXiv:2112.13710
- Caro–Petruševski–Škrekovski, arXiv:2201.03608

### Correctness risks

- The bounded exhaustive checker covers only small multipartite instances and is corroborative; the all-size theorem rests on the active-part proof.

## Originality — PASS

The foundational neighborhood-parity papers define the notion and develop general structural bounds, and later work treats products and other graph classes. Direct statement/implication searches found no earlier complete-multipartite theorem with the three parity cases, nor the exact optimal-coloring enumeration. The bipartite special cases follow from the audited general theorem, not vice versa.

### Equivalent formulations

No equivalent reformulation of the same complete-multipartite classification was located.

Searches:
- published-corpus query: odd chromatic number complete multipartite graph exact formula optimal coloring count neighborhood parity
- literature query: "odd chromatic number" "complete multipartite"

Evidence:
- The closest corpus hit was the assigned record itself; nearby records concerned unrelated complete-multipartite invariants.
- The foundational odd-coloring papers define the same neighborhood-parity notion but do not state the audited multipartite formula in the inspected material.

### Broader coverage

Those broader thematic results do not imply the audited active-part reduction or the optimal-coloring count for arbitrary complete multipartite graphs.

Searches:
- arXiv:2112.13710
- arXiv:2201.03608
- arXiv:2202.12882
- DOI:10.3934/math.2026056

Evidence:
- These sources provide the definition, general properties, graph-product results, or exact values for selected Cartesian-product families.

### Exact database or table

The result is an all-parameter structural theorem, not a recomputation of a finite table.

Searches:
- published-corpus exact query on \(\chi_o(K_{n_1,\ldots,n_r})\) and the parity parameter \(o\)

Evidence:
- No earlier table or exact-sequence record with the displayed formula or the \(U(G)\) enumeration was located.

### Claim versus prior implication

Once the active-part equivalence is proved, the chromatic number and counts follow sharply; the inspected prior theorems do not supply that equivalence.

Searches:
- comparison with the definitions and main theorem statements in arXiv:2112.13710 and arXiv:2201.03608

Evidence:
- The prior statements do not force that a complete multipartite coloring is odd exactly when at least two parts are active; that equivalence is the key new reduction.

### Sources inspected

- **Colorings with neighborhood parity condition** — https://arxiv.org/abs/2112.13710. Trigger: Primary source introducing the exact coloring notion. Material read: Accessible full article sections containing the definition, examples, and main general bounds/results. Method: Lawful open full text. Assessment: BACKGROUND_NOT_COVERING. Evidence: The inspected statements introduce odd coloring and general bounds but do not give the arbitrary complete-multipartite classification or enumeration.
- **Remarks on odd colorings of graphs** — https://arxiv.org/abs/2201.03608. Trigger: Same invariant and natural structural follow-up. Material read: Accessible full-text definitions and main structural statements. Method: Lawful open full text. Assessment: BACKGROUND_NOT_COVERING. Evidence: No theorem matching or implying the complete-multipartite active-part formula was found in the inspected text.

### Checked sources

- https://arxiv.org/abs/2112.13710
- https://arxiv.org/abs/2201.03608
- https://arxiv.org/abs/2202.12882
- https://doi.org/10.3934/math.2026056
- published-result corpus search

### Residual risks

- Originality is best-of-knowledge; an unindexed graph-class note using different terminology could contain an equivalent formula.

## Value — PASS

Complete multipartite graphs are a standard infinite family, and the result gives both the exact neighborhood-parity chromatic number and a complete count of optimal color-class partitions. The active-part characterization is a reusable structural reduction rather than a small-instance computation.

### Value sources

- arXiv:2112.13710
- arXiv:2201.03608

### Value risks

- The result is family-specific and does not directly extend to arbitrary multipartite subgraphs.

## Limitations

- Graphs are finite simple complete multipartite graphs with at least two nonempty parts.
- The exact count is for optimal color-class partitions, with labeled palettes obtained by multiplying by \(k!\).
- The finite verifier is corroborative only; the proof establishes the infinite family.
