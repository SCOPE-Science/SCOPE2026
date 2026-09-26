# Independent audit — 2026/09/09/075

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I independently performed exact rational elimination on the specified 7×7 circulant theta-prime witness. Its LDL pivots are all strictly positive (last 0.000496954…); trace is one, graph-edge entries are zero, and its objective is 82827/25000 = 3.31308. The exact integer comparison (82827/25000)^4 >114 is true. Tensoring a trace-one nonnegative PSD feasible witness preserves the strong-product constraints, so the fourth-power obstruction follows. Bukh–Cox arXiv:1802.00476, Proposition 4 already proves H_f(C₇;F)=7/2 in every field, and its Theorem 3 proves multiplicativity; hence (7/2)^4=2401/16>114. The cited lower bound for ruling out rank-three matrices is a separate premise, as the record notes. This rules out the **specified** level-one routes, without bounding all methods for C₇.

## Originality — PASS

The fractional Haemers value and multiplicativity are explicitly prior work. The exact rational Schrijver witness, rank-four example logs, and combined threshold-specific certificate provide a reproducible instance not contained in the Bukh–Cox statement. No broader novelty for the underlying bound is claimed.

## Scientific value — PASS

The strict 3.31308 and fourth-power floors quantitatively eliminate the admitted 3.30/114 certificate goals for this restricted family. This guides the search for higher-level bounds, while yielding no improvement in Shannon capacity itself.

Sources: https://arxiv.org/pdf/1802.00476 ; https://doi.org/10.1109/TIT.1979.1055985 . Open prior text sufficed.
