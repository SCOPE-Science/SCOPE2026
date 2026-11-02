# Self-review: critical group of the McGee cage

## Correctness — PASS

The theorem concerns one completely specified 24-vertex, 36-edge cubic graph and an integral Laplacian cokernel. An exact 471-step list of row/column operations in `certificate.json` reduces the 23-by-23 reduced Laplacian to nineteen units followed by invariant factors \(11,44,132,2640\). Each operation is unimodular, so replay establishes the integral group structure, not just a determinant or floating-point calculation. The independent edge-list verification produces the same prime-power elementary divisors and a Bareiss determinant of \(168{,}664{,}320\). Both checks passed. The conclusion is finite and does not assert a family theorem.

## Originality — PASS, qualified

McGee (1960, DOI: 10.4153/CMB-1960-018-1) gives the classical graph, not its sandpile factors. MathWorld gives its LCF and adjacency spectrum. House of Graphs graph 1223 **already states the spanning-tree count** of \(168{,}664{,}320\), and that number is not asserted as a new finding. The new claim is the full four-factor integral critical group. General graph-Jacobian theory and results for complete multipartite, Cartesian-product and Cayley graphs do not imply these specific factors. Searches under critical/sandpile/Jacobian/Smith aliases and the exact numbers, as well as public research-record comparisons, revealed no covering statement. The complete text of Balasubramanian (2025, DOI: 10.1007/s10910-025-01747-4) was inaccessible; the abstract concerns spectra, but noncoverage of its full text is **not** claimed. Residual risk: an older or unindexed table may already have the factorization.

## Value — PASS

This group is the integral flow/cut discriminant and chip-firing class group of the canonical unique cubic \((3,7)\)-cage. Its four generators, exponent \(2640\), and four independent order-eleven directions are finer arithmetic data than the already-known spanning-tree product. They answer a natural exact graph-invariant question and enable modular-harmonic and chip-firing comparisons in an extremal regular graph. The contribution is narrow but self-contained; no unsupported general theorem is claimed.

## Checked literature and limits

The original McGee article was inspected throughout, including figures. The full accessible MathWorld entry, indexed House of Graphs invariant list, foundational graph-Jacobian abstract, and a publisher preview of the cage-spectral paper were compared. The potentially overlapping full publisher text remains unread; inaccessible content was not treated as confirmed noncoverage. Computations were exact and reproducible, but this review is not an independent scholarly examination.

Self-review: passed. Independent audit: not yet performed.
