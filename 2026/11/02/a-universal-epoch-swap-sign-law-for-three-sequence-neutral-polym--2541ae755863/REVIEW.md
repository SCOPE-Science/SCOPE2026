# Scientific review

## Correctness — PASS

The lineage-count process under variable pair-coalescence hazard gives \(\Pr(K_t=3)=e^{-3H(t)}\) and \(\Pr(K_t=2)=\tfrac32(e^{-H(t)}-e^{-3H(t)})\). Counting descendant classes leads to exact linear forms in two exponential survival integrals. Swapping the two intact hazard blocks preserves cumulative hazard at the end and hence cancels the shared prefix and tail. An independently checked two-block integral factorization yields \(\Delta_1>0\) and the exact doubleton sign criterion. Each of the two geometric factors in \(R(s)\) is strictly decreasing; its endpoint values establish uniqueness and the equality boundary. The proof treats zero prior hazard and all positive block durations. `checker.py` provides exact algebraic and independent quadrature spot checks. Finite computations are not used as a proof for all parameters.

## Originality — PASS within inspected sources, provisional

Polanski and Kimmel (2003) and Rosen et al. (2018) already give general variable-demography expected SFS representations, so computation of an SFS for specified epochs is not new. The inspected portions of those primary full texts, including the original formula and SFS geometry arguments, do not state the complete **sign** and unique threshold for transposing intact adjacent epochs with arbitrary independent lengths and arbitrary common surrounding history. Eriksson et al. (2009) concern total genealogical branch lengths; Jenkins et al. (2013) emphasize triallelic sites and second moments. The requested comparison and the global accumulated-hazard cutoff are not stated in those inspected results. Searches of published research records and prior work identified no matching comparison; this cannot prove worldwide uniqueness. Priority risk remains from broader coalescent rearrangement and sensitivity results, particularly those not indexed by the search terms.

## Value — PASS

The sign of an expected site-frequency component under rearranged demographic epochs is a natural interpretive question: aggregate coalescent exposure and the two block sizes do not determine the temporal order. The result gives a fully quantified answer, including a surprising opposite direction for singleton and doubleton counts, an exact global cutoff, a minimal sample size, and robustness to arbitrary identical prehistory and tail. The result is a theoretical genetic-demography benchmark; it is not a claim about normalized SFS, high-sample inference, or practical identification from three observed sequences.

## Limitations and further scrutiny

The infinite-sites neutral Kingman assumptions and constant mutation rate are essential. The general SFS representation is established prior art, so external expertise could determine that the comparison is subsumed by an existing rearrangement theorem. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
