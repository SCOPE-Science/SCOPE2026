# Independent mathematical audit

## correctness

PASS

Each length-19 unfolding of a binary order-four de Bruijn cycle has 16 distinct length-four factors at starts 0..15. A full attractor must intersect each unique corresponding window; each position meets at most four windows. Exactly four positions therefore force the unique window-hitting set S4={3,7,11,15}. The fixed S5={3,6,9,12,15} hits every length-four window. Factors longer than four automatically have an occurrence intersected by any set that hits all length-four windows, so finite factor checks 1..4 suffice for full attractors. Independently enumerated all 2^16 binary 16-words, obtained 256 cyclic de Bruijn roots and 16 cycles, then compared full distinct factor sets for all roots: exactly 192 S4-successes, 64 failures all covered by S5; per-cycle count histogram 4 cycles with 16, 8 with 12, 4 with 8 successful cuts. Thus finite exhaustion proves the complete stated first-composite-order census, with no infinite extrapolation.

## originality

PASS

Mantaci et al., A Combinatorial View on String Attractors, Section 6.2 Proposition 41, gives general de Bruijn attractor bounds and one binary order-four example attaining four positions. Whittington, Online String Attractors Section 5/Theorem 29, discusses an online/linear formulation and Lyndon-generated de Bruijn optimality at prime orders. Neither provides the 16-cycle/256-cut composite order-four full census, unique optimal placement, universal five-set or 192/64 profile in the inspected mathematical material. Published Resultary string-attractor censuses concern length-12 arbitrary words, Thue–Morse or pseudostandard words, not these length-19 de Bruijn unfoldings.

## value

PASS

Order four is the first composite binary de Bruijn order, and the gap between the theoretical order-size attractor lower bound four and actual optimal size across all rooted cuts is a natural complete boundary classification. Exact counts and universal four/five placements give reproducible counterexamples to the belief that every cut attains the lower bound, while identifying at least eight optimal cuts on every cycle. This is a meaningful complete finite structural result rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
