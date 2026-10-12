# Self-review

## Correctness — PASS
The finite claim was reconstructed from the definitions. Pairwise compatibility was independently computed from deletion-shadow disjointness and from longest-common-subsequence length, with agreement on all pairs. Exhaustive enumeration of every six-subset found exactly six codes, exhaustive enumeration of every seven-subset found none, and an independent maximal-clique search returned the same six maxima. The orbit, checksum, shadow-profile, and coverage claims were recomputed from the final list.

## Originality — PASS
The closest inspected source, Sloane's arXiv survey, records the exact optimum \(A(5,1)=6\) and the VT construction but does not enumerate all length-five optimum codes. Kulkarni--Kiyavash provide the general hypergraph formulation and finite upper bounds but no equality census at this parameter. Perfect-code theory cannot imply the complete result because four of the six maximum codes found here are nonperfect. Targeted searches for exact enumeration, deletion-graph maximum independent sets, VT equality cases, and perfect/nonperfect length-five optima produced no implication-equivalent published finding.

## Value — PASS
This is the first block length where the classical zero-syndrome VT family is nonlinear. The classification shows that the equality set is already structurally richer than the VT construction: only two of six maxima are perfect and the remaining four are optimal without perfect coverage. That is a natural complete finite classification rather than an arbitrary parameter slice.

## Closest literature and limitations
Sloane's survey is closest for the exact optimum and small-length context. Kulkarni--Kiyavash are closest for the general finite optimization framework. The result is limited to binary length \(5\), one deletion, and the natural complement/reversal action; an obscure unindexed historical enumeration remains a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
