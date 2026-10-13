# Scientific assessment

## Correctness: PASS
The finite Markov generator has an explicitly derived closed system of three stationary occupation moments. Exact elimination yields the current formula. Both denominator-positivity decompositions cover all positive rates and boundary-density endpoints; an independent symbolic identity yields the all-drive reversal law with a strictly positive factor. `verify.py` separately constructs and solves the four-state generator in exact rational arithmetic for 1,600 combinations and checks both formulas. These checks supplement the universal proof.

## Originality: PASS with explicitly limited source access
The closest motivating 2026 boundary-gradient paper addresses general site disorder using approximate Galerkin and nonlinear closures and identifies reflection symmetry as an obstruction; the narrowly evaluated two-site theorem gives an exact rational stationary current and an if-and-only-if global sign theorem, which are not entailed by an approximate generic existence result or a necessary symmetry condition. The earlier 2025/2026 Sakai–Akimoto bulk-field paper concerns a distinct bias-reversal operation. published-finding corpus and public-source searches did not return an equivalent exact two-site sign theorem, but failed search is not proof of priority. Direct primary full-text access was unavailable, so an unindexed or implicit specialization remains the principal risk.

## Value: PASS
The two-site chain is the minimal nontrivial channel where exclusion, two heterogeneous waiting times, and independently driven reservoirs interact. The exact sign theorem resolves a natural small-system boundary of a recent approximation-led rectification analysis for every reservoir gradient: breaking reflection symmetry is sufficient here, and the direction of the asymmetry is parameter-rigid. Unlike a numerical example, the result classifies the entire positive rate parameter space and distinguishes exact effects from approximation artifacts. It does not claim a longer-chain theorem.

Self-review: passed. Independent audit: not yet performed.
