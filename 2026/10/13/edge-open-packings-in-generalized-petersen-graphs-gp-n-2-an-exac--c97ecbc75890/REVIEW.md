# Scientific review

## Correctness — PASS

The edge-open-packing condition is reduced to an explicitly tabulated finite-range conflict condition for \(GP(n,2)\) at every \(n\ge9\), with boundary orders \(5\)–\(8\) handled directly. The deterministic verifier reconstructs exactly \(120\) compatible four-mask states, exactly \(291\) transitions, and checks \(291\) integral inequalities \(h(s)\ge h(t)+9w-7\). These inequalities telescope on every cyclic word to give the upper bound \(\lfloor7n/9\rfloor\). Thirteen direct-checkable base words and the shared-prefix closed-walk operation attain it at all orders. The exact branch recurrence proves the four boundary optima without relying on heuristic optimization. Source file and captured output are included; small finite experiments are not mistaken for the infinite proof. Risk: the user should independently replay the executable certificate and inspect the local table if formal assurance is required.

## Originality — PASS

The 2022 foundational full text determines the Petersen \(GP(5,2)\) value \(3\), already subsumed by the new theorem, and treats several other graph families. The 2024 bounds/complexity full text and the 2024 graph-products full text address general bounds and other families; neither yields an exact \(GP(n,2)\) law. The 2025 general characterization via quantified structural conditions likewise contains no evaluated \(GP(n,2)\) formula and does not bypass checking the underlying packing constraints. A cubic general bound of order \(n\) is strictly weaker than the exact \(\lfloor7n/9\rfloor\) law for large \(n\). The closest retrieved mathematical database entries concern vertex open-packing spread or unrelated packing complexes, not this precise edge invariant on this graph family. Equivalence checks included original graph names, edge-open packing, injective edge-color class, and induced star-forest terminology. No search proves global uniqueness; an older unindexed induced-star-forest result remains a genuine residual risk.

## Value — PASS

This is an all-orders exact extremal invariant on a classical connected cubic graph family, with a nontrivial slope \(7/9\), an exact period-nine construction, and a finite reusable local-potential method. It strictly improves generic cubic bounds and includes—but is not merely—the known Petersen case. The result could serve as a benchmark for edge-open packing and injective edge-coloring studies, without claiming to solve those coloring problems.

## Literature compared and limitations

- G. Chelladurai, K. Kalimuthu, S. Soundararajan, *Edge open packing sets in graphs*, DOI `10.1051/ro/2022171`: full text inspected, including Proposition 2.5; the \(GP(5,2)\) value is prior work.
- B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750: full text inspected; algorithmic hardness and general bounds do not determine the new formula.
- B. Brešar, T. Dravec, T. Hedžet, B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020: full text inspected; product/hypercube results do not imply this graph-specific extremum.

- A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935: full text inspected; exact generic characterization requires checking structural conditions on the family and does not determine the numerical formula.

The result does not enumerate all extremal packings, treat other generalized Petersen step sizes, or assert that the search establishes absolute novelty.

Self-review: passed. Independent audit: not yet performed.
