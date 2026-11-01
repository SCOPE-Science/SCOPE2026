# Review: A sharp three-basis support law

## Correctness — PASS

For every complex seven-point signal, the prime cyclic Fourier minor theorem bounds each transformed zero count by the original support size minus one. An assumed total support at most \(13\) therefore gives zero sets of combined size one larger than the original support. The resulting rectangular Fourier/chirp matrix must have a nonzero kernel vector, but exhaustive rank verification in \(\mathbb F_{1009}\) finds no such rank-deficient matrix. Because \(105\) is a primitive seventh root in that field, a full-rank specialization exhibits a nonzero cyclotomic minor in characteristic zero. There are exactly \(149793\) eligible matrices, all counted by the standalone checker without sampling. The two-spike vector \(\delta_0-\delta_1\) has supports \((2,6,6)\), proving sharpness. The argument is valid for arbitrary complex coefficients, not only field-valued or unimodular coefficients. The certificate concerns only the matrices specified in the theorem.

## Originality — PASS (historical priority provisional)

Fiorentino and Weigert's 2022 article gives a general lower bound of \(12\) for the sum of the supports in three seven-dimensional standard mutually unbiased bases; the sharp \(44\) bound studied for the complete eight-basis family concerns a different statistic. The article explicitly proposes sharp bounds for triples as a future direction, while discussing numerical obstructions for some balanced configurations. Tao's prime-order theorem yields the known two-basis bound \(8\) but does not prohibit all three-basis support totals of \(13\). Searches for exact dimension-seven triple support bounds and related finite Fourier/chirp results found no prior statement determining \(14\). Related finite-parabola and Fano-frequency results use different Fourier sampling spaces and do not imply the all-complex-signal claim. An unindexed equivalent theorem or implicit stronger classification remains a residual priority risk.

## Mathematical value — PASS

The quantity is the natural exact support uncertainty for three incompatible Fourier-type measurements. The value \(14\), rather than the pairwise lower bound \(12\) or the merely integer-rounded exclusion of \(12\), is a sharp new threshold. Excluding a total of \(13\) requires joint zero-pattern constraints and is not a routine pairwise consequence. Its short exact certificate also provides a reproducible method for a precise finite-dimensional question that the focal literature explicitly isolates for future research.

## Closest literature and limits

V. Fiorentino and S. Weigert, *Uncertainty relations for the support of quantum states* (2022), especially the standard-basis definitions in §2.2, pair inequalities and triple inequality in §3, dimension-seven analysis in §§4–5 and concluding research directions; T. Tao, *An uncertainty principle for cyclic groups of prime order* (2003/2005). The result is for one explicit triple and does not assert an all-triples theorem or an equality-orbit classification. A self-review and independent integer-language replication do not constitute independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
