# Scientific review: complete split-graph majority dynamics

## Correctness

**PASS.** The proof derives exact microscopic update equations from degrees \(2n-1\) (clique) and \(n\) (independent set), splits all initial populations by their sum relative to \(n\), and distinguishes the balanced two-cycle with a fixed count profile from fixed microscopic configurations. This yields the global identity \(F_n^4=F_n^2\), fixed and primitive-periodic populations, sharp entry bounds and a necessary-and-sufficient basin inequality. Vandermonde's identity and paired triangular binomial sums give the exact basin count; Stirling's formula gives the stated expansions. The packaged verifier independently enumerates \(349{,}524\) labelled configurations for \(1\le n\le9\) and cross-checks the population formulas through \(n=150\). A finite test is not a substitute for the universal proof.

## Originality

**PASS, with documented historical risk.** The general period-at-most-two property is already known from Goles--Olivos and is explicitly excluded as a novel contribution. The accessible 2013 Tamuz--Tessler and 2014 Benjamini et al. primary texts concern general information retention, infinite-graph recurrence and random graphs, not the all-size balanced complete-split orbit census or one-quarter basin law. The nearest identified comparable graph classifications involve crown graphs, two joined cliques with only matching links, or complete tripartite graphs; their neighbor-count maps and asymptotic basin laws do not imply the present formula. A complete multipartite parity-automaton result applies an XOR update, not majority. Searches by graph family, rule, equivalent join representation and binomial formulas found no stronger source establishing the entire new claim. Full text of Goles--Olivos (1980) remained inaccessible, and unindexed equivalent work remains possible.

## Mathematical value

**PASS.** The exact orbit count exhibits an exponential parity fracture, while a nonvanishing and asymptotically identical \(1/4\) fraction of initial states is attracted to oscillations in both parities. This mismatch between recurrent-set size and attraction-basin measure is a natural qualitative issue in deterministic opinion dynamics. The result supplies an all-size sharp convergence cutoff, a complete recurrent census and exact finite-size basin probability without arbitrary parameter slicing.

## Limitations and comparison risk

The claimed new content is restricted to balanced complete split graphs and deterministic tie retention. The historical 1980 full text was not inspectable; its accessible abstract establishes a different, general result, not a documented enumeration. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
