# Scientific review: minimum maximal total visibility in the eight-cube

## Correctness — PASS

The 2023 distance-two equivalence reduces maximal total-visibility sets to independent dominating sets in two disjoint parity halves. The published code builds all 128 even-weight vertices directly, enumerates every independent anchored candidate of sizes five to eight in increasing index order, and checks domination using exactly the union of radius-two masks. Four radius-two balls cannot cover 128 vertices. Counts are zero for \(k=5,6,7\) and 142,380 for \(k=8\); the independent shortest-path checker validates a concrete size-eight witness in each parity. Even XOR transitivity and incidence double counting give \(128\cdot142,380/8=2,278,080\), whose square is the stated census. Code enumeration is a finite proof only for dimension eight, not a general pattern inference.

## Originality — PASS (with residual risks)

Brešar–Yero's 2023 Problem 1 poses the lower-visibility hypercube problem without the present dimension-eight count. The 2023 Hamming-graph characterization is used as a lemma, not relabeled as new. Korže–Vesel's 2024 exact \(\mu_{\mathrm t}(Q_8)=32\) is the **largest**, not the smallest inclusion-maximal, total-visible set. The 2025 numerical halved-cube data give ordinary domination number seven and 71,680 ordinary minimum dominating sets; the present independent domination number eight and its 2,278,080 minima are mathematically different. The length-eight radius-two covering-code literature allows both parities and also does not supply the counted independent same-parity covering families. Searching descriptions and exact numerical invariants did not locate a dominating earlier result. Residual risks: independently computed but unindexed coding-theory tables, or unpublished classifications of halved-cube maximal codes; searchable absence is not a proof of worldwide priority.

## Value — PASS

The exact minimum and census address a stated published graph-product question at the first unsolved dimension after the known dimension-seven value. The parity decomposition reveals a substantial gap between ordinary and independent domination on the halved cube; the census is not implied by either the ordinary domination number or the known upper total-visibility value. A 13-digit count of minimum objects and the profile stratification give a reproducible finite benchmark useful for later structural work. No broader-dimensional theorem is asserted.

## Limitations and relationships

The result uses a complete finite C++17 search and relies on its verifiable recursion; independent Python checks verify existence, direct shortest-path visibility and maximality but do not independently enumerate all optimizing sets. The closest inspected full texts are arXiv:2307.02951, arXiv:2307.05168 and arXiv:2405.05650; prior covering and ordinary domination tables are acknowledged. The precise value of 16 by itself could be recoverable from another coding-theoretic representation; the exact minimum census is the strongest item-specific contribution.

Self-review: passed. Independent audit: not yet performed.
