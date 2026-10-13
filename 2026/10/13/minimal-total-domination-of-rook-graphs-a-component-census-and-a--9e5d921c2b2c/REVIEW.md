# Scientific review

## Correctness — PASS

A rook-graph total dominating set is exactly a selected bipartite edge set with no isolated selected edge and no unused row-column pair. The proof applies the deletion criterion to classify all possible occupied components; both necessity and sufficiency are checked, including the regime in which neither bipartition class has isolates. The labeled exponential formula uses the exact row, column, and edge counts of each component and disjoint counting regimes. On square boards the row-deficit argument proves the upper bound, maximum-count formula, and forbidden next-lower size without experimental extrapolation. The standalone exact scripts check the generating coefficients against exhaustive deletion tests and compare the ungraded totals to the published table.

## Originality — PASS, with residual risk

The directly closest known result is Howroyd's OEIS A384118: it reports the number of minimal total dominating sets on each rectangular rook board and a recurrence for that total. Evaluating the new formula at \(z=1\) must therefore recover prior data; these numbers alone are not claimed as new. Neither those ungraded counts, Mertens's ordinary domination polynomial, nor Kazemi–Pahlavsay–Stones's 2-tuple minimum parameter states the all-cardinalities component theorem, square-board upper gap, or maximum-size multiplicities. It is possible that the A384118 recurrence can be graded by reconstructing its component argument, or that a differently indexed enumeration already contains the polynomial. No search result establishes uniqueness or independent priority.

## Value — PASS

The exact polynomial separates minimum, intermediate, and maximal *inclusion-minimal* total dominating sets on every rectangular board. This is not merely a new tabulation of the known total: for \(5\times5\) the counts \(410\), \(5700\), and \(1200\) lie at cardinalities \(5\), \(6\), and \(8\), while cardinality \(7\) is genuinely absent. The uniform theorem \(\Gamma_t(R_{n,n})=2n-2\), its exact extremal multiplicity, and the forbidden size \(2n-3\) make the precise grading a motivated invariant of minimal total domination.

## Evidence and limitations

The primary older background is Kazemi–Pahlavsay–Stones, arXiv:1509.08208 (2015 first posting, 2016 revision); the closest ungraded table is OEIS A384118 (2025), and the ordinary domination polynomial is Mertens (2024). PDF introductions and relevant theorems were inspected, and the complete OEIS entries including programs were examined. The correctness proof is unrestricted; the separately implemented code checks are finite. Independent external mathematical review and exhaustive historical priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
