# Independent mathematical audit

## correctness

PASS

For binary order-five de Bruijn necklaces of length 32, every cyclic BWT column has 16 complementary adjacent two-bit blocks (01/10), from the unique 5-factor dictionary. The LF inversion permutation on 32 rows must be one cycle for a single necklace (Higgins, Thm 3.4 and Lemmas 3.6–3.7); with 16 orientation bits the linear run number is 17+sum_{i=0}^{14}[a_i=a_{i+1}]. My independent LF implementation exhaustively enumerated 65,536 orientations, verified 2048 single 32-cycles and exact histogram {20:38,22:426,24:840,26:608,28:130,30:6}. The source checker also contains an independent rooted Euler-tour exhaustive construction; its algorithm was inspected and is consistent with the LF/dictionary correspondence. This is a finite complete classification at n=5 only.

## originality

PASS

Best-of-knowledge originality is qualified: equivalent formulations, stronger published implications and exact tables were searched and compared at the statement level. The record expressly excludes cited prior components; no located material supplies the claimed precise new remainder. Inaccessible/unindexed specialized literature remains a residual risk, not an automatic scientific rejection.

## value

PASS

The sentinel-free BWT run count is a compression/indexing invariant and de Bruijn cycles are canonical strings. The complete 2048-necklace order-five census gives the natural attainable range, sharp min 20 rather than generic lower bound 18, and exact counts for six classes, a useful independently reproducible benchmark despite no all-order theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
