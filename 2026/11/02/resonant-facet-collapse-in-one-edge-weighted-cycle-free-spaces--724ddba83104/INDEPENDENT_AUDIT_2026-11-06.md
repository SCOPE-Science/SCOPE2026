# Independent mathematical audit

## correctness

PASS

For the n-cycle with edge lengths (1,...,1,t), the zero-sum edge-increment model Q_{n,t}={sum x_i=0, |x_i|<=1 for i<n, |x_n|<=t} is exactly the dual Lipschitz ball. A vertex of a one-hyperplane box section has at most one slack coordinate; partition by special-coordinate slack, ordinary-coordinate slack, or all-tight, carefully using strict inequalities to avoid double counts. This yields all three binomial sums for 0<t<n-1. At t>=n-1 the special bound is redundant and Q is an (n-1)-cube with 2^(n-1) vertices. For smaller t, all edge molecules are genuine primal extreme points; fully tight dual vertices are precisely integer parity resonances and expose n rather than n-1 primal vertices. Counting them gives U_n(s)=2*binom(n-1,(n-1+s)/2). Chamber binomial difference identities show the exact even and odd maximizers and the n/2 even-cycle drop at t=1. Independently enumerated rational vertices by fixing n-1 signed coordinates and deduplicating for n=4..8 and seven parameter values, agreeing exactly with the formula. The all-real, all-n assertion rests on polyhedral and binomial proof, not the finite checks.

## originality

PASS

Jevtić–Timotijević–Živaljević 2018 classifies generic weighted-cycle KR polytopes, excluding the exact half-perimeter resonances. Braun–Bruegge 2022 gives unweighted cycle facet counts (t=1) and unicyclic-graph extrema, but not fixed-cycle weighted wall multiplicities. The assessed non-simplicial resonance counts and all-t phase diagram are additional statements; generic chamber formulas and unweighted endpoint counts are explicitly prior or derived.

## value

PASS

The generic Bier-sphere correspondence deliberately excludes the resonance walls; determining exactly which facets cease to be simplices, how many n-vertex facets occur, and the complete sharp phase diagram solves a natural structural gap. The unbounded factor n/2 loss at even unweighted cycles is substantial rather than a small known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
