# Scientific review

## Correctness — PASS
The two choices in reshuffling and four ordered IID choices are explicitly enumerated. Exact matrix products show cancellation of off-diagonal risk differences and give two factorized diagonal coefficients. In the stated interval \(0<h<1/b\), the second coefficient is strictly positive; the first has a unique zero \(h_*=2(b-a)/(2a(b-a)+c^2)\). The exact-rational example uses component-Lipschitz-admissible steps and strictly contractive component maps (positive-definite squared-norm defects). `verify.py` reproduces the universal symbolic factorization and 191 independent rational checks. This is an algebraic proof, not an inference from finite tests.

## Originality — PASS (publication priority remains uncertain)
The closest direct method is the simultaneous shuffled SGDA of Das–Schölkopf–Muehlebach (2022), which proves multi-epoch convergence-rate bounds rather than an exact comparison of RR and IID after two component uses. Cho–Yun (2022) also gives SGDA reshuffling convergence bounds; Emmanouilidis–Vidal–Loizou (2024) uses a different, extragradient map. De Sa (2020) proves known non-dominance examples for different, symmetric-matrix optimization constructions, and its small-step dominance result assumes symmetry; the present sharp two-component nonsymmetric saddle-risk law is not an implication. Liu (2026) treats convergence-rate domination for convex minimization, not this pointwise saddle-game risk. Mathematical-record and preceding-claim searches using reshuffling, two components, bilinear coupling, equivalent four-path matrix comparison, and noncommutative means found no covering result; this is not an assertion of global uniqueness.

## Value — PASS
This exact boundary answers a motivated finite-budget stochastic minimax-design question left unresolved by convergence bounds: is reshuffling always at least as safe as independent sampling after one pass if all components share the saddle? It fails in the smallest nontrivial game and at arbitrarily small steps. The full direction-dependent risk matrix and sharp crossover show a non-obvious transition, even with strict individual-step contractivity, that a mere numerical counterexample would not explain. The result is intentionally restricted to the two-component quadratic family and squared Euclidean error.

## Limitations and priority risks
The literature may contain an uncatalogued equivalent special-case identity. No claim is made about more than one epoch, other metrics, component counts or nonsimultaneous descent-ascent. The broader fact that reshuffling may underperform is already known; originality attaches to the exact saddle-family sign classification and crossover. No external scientific validation is claimed.

Self-review: passed. Independent audit: not yet performed.
