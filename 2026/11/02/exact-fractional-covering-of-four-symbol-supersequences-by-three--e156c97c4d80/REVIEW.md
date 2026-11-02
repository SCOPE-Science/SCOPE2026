# Scientific review

## Correctness — PASS

The exact finite LP and its dual use distinct deletion outputs, not deletion positions with multiplicity. All fifteen equality partitions of length four give primal coverage at least one for the displayed four-type weights. The four center types give dual mass exactly one for all alphabet sizes at least three; independent counting establishes equal primal and dual objectives. The separate binary four-center cover and four-receiver dual prove the exceptional value. The standalone checker enumerates the actual incidence relations using exact fractions for alphabet sizes three through nine and checks the binary case. The infinite-domain assertion depends on the symbolic type analysis, not extrapolation from computations.

## Originality — PASS, with residual risk

The directly relevant June 2026 paper [3] presents bounds and constructions for insertion covering, without giving the exact fractional LP optimum; the 2025 integer-density result [2] proves a strict one-third lower bound for integer covers rather than a one-quarter fractional optimum. The original 2021 insertion-covering paper [1] develops sphere bounds and constructions. Grozea's integer table [4] covers small alphabets but not the all-alphabet fractional LP. Statement-level searches for ordered-triple subsequence hypergraphs, single-insertion fractional covering and an asymptotic integrality gap did not identify a covering result. No negative uniqueness assertion follows from this search: an equivalent unpublished or unindexed LP calculation remains possible.

## Mathematical value — PASS

The exact all-alphabet fractional optimum is a natural benchmark for a covering problem with variable alphabet size. Its growth coefficient is \(1/4\), while known integer covering bounds give a strictly greater than \(1/3\) coefficient; thus the standard covering LP provably loses a constant factor in a regime where stronger methods are sought. The result is more than a numerical example or routine finite count: it gives matching symbolic dual certificates, a sharp exceptional binary boundary, and a structural obstruction to improving integer covering bounds by this LP alone.

## Sources and limitations

Primary sources: [1] https://arxiv.org/abs/1911.09944, [2] https://arxiv.org/abs/2409.06425, [3] https://arxiv.org/abs/2606.15379; integer table [4] https://www.brainsignals.de/users/cristian.grozea/combinatorial.html. The main theorem covers only three-symbol centers and exactly one insertion. It does not determine the integer optimum or the strength of semidefinite programming. Priority risk remains from unindexed calculations.

Self-review: passed. Independent audit: not yet performed.
