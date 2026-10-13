# Self-review

## Correctness — PASS
The constrained overlap graph and cyclic-rotation lower bound are explicit. All possible equality cases are one-per-necklace transversals, and every such choice is exhaustively inspected: from 2 up to 262,144 candidates according to length. Acyclicity and longest paths are checked by two independently coded algorithms (topological sorting with dynamic programming; DFS cycle detection with memoized depth). Their exact optimizer catalogues agree at every length, including all 240 length-eight sets. This is a finite proof; no unjustified extrapolation is made to longer lengths.

## Originality — PASS, subject to bibliographic residual risk
Champarnaud–Hansel–Perrin's unrestricted and restricted-language theorem already yields the minimum cardinalities and lists the golden-mean necklace counts; these are explicitly prior results. Moreno's golden-mean de Bruijn sequence counts are different from optimizer counts. The claimed new finite census of every minimum unavoidable set and the entire remaining-path histogram for lengths two through eight is not supplied by the inspected primary texts or the indexed mathematical findings. An unindexed dataset and incompletely accessible literature are residual risks; failed searches do not establish priority.

## Value — PASS
In sequence selection under a prescribed `11` run constraint, two unavoidable sets of equal smallest possible cardinality can have very different sharp finite hitting guarantees. The full length-eight distribution proves that the sharp best guarantee is 23 symbols, attained by exactly 16 of 240 designs; worst minimum-cardinality designs guarantee only 30. The exact finite classification and catalogue refine a classical existence theorem into a concrete design spectrum and benchmark.

## Closest literature and limits
Champarnaud–Hansel–Perrin (2004), restricted-language existence theorem and necklace table; Moreno (2003), golden-mean shift graph and distinct de Bruijn sequence enumeration; Zheng–Kingsford–Marçais (2020), unrestricted UHS and residual-path motivation; Marçais–DeBlasio–Kingsford (2023/2024), full-alphabet minimum-decycling-set algorithms. The exact count and path profiles are proved for lengths 2–8 only; prior data not indexed or not fully accessible remain a novelty risk.

Self-review: passed. Independent audit: not yet performed.
