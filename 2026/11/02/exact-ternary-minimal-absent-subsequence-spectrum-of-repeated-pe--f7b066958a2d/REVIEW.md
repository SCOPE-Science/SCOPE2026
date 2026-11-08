# Independent mathematical audit

## correctness

PASS

The increasing permutation (012) repeated m times greedily embeds a target u using exactly 1+d(u) periods, where d counts adjacent weak descents (a≥b). Thus absence iff d≥m. Every letter deletion reduces d by at most one, and reduction for an internal (a,b,c) is [a≥b]+[b≥c]-[a≥c]. Therefore minimal absent iff d=m, its endpoint pairs are weak descents, and every triple has decrement 1; lengths m+1≤ℓ≤2m. Encoding successive pairs as q² states gives an injective weighted-path count v(I−M)^−1w. For q=3 the 9-state rational identity is verified by an exact polynomial-vector certificate in the package; independently reconstructed the transfer matrix and algebraically simplified v(I−M)^−1w against the displayed rational N(t,z)/D(t,z), with exact symbolic zero difference; numerator/denominator have denominator constant 1. First total counts 6,16,46,127,349,960,2640,7264. Higher q have the matrix expression, not the special small fraction. All algebra is exact, not extrapolated from 1035 finite coefficients.

## originality

PASS

Qualified PASS: Kosche–Koß–Manea–Siemer examine the same repeated permutation B_k and prove generic MAS characterization and lower bounds (not this full q3 length-layer rational form). Adamson et al. count *all* absent subsequences not minimal antichain; Manea et al. give generic enumeration. Earlier binary repeated-permutation formula does not supply q3 transition structure. Tronícek's 2023 absent-subsequence automaton and MAS-counting article is a relevant full-text priority risk; full text unavailable after arXiv/OA and institutional route returned vpn_disconnected, without bypass.

## value

PASS

Complete exact length-by-repetition distribution of a canonical nonbinary word family, with local recognition, finite-state transfer and symbolic fraction; a motivated refinement of the earlier shortest-absence counts and an explicit combinatorial benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
