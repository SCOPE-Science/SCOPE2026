# Scientific review

## Correctness — PASS

The claim concerns simple random walks on centered, finite, reflected odd paths with an independent geometric reset decision at every unit step. The renewal identity is derived with resetting duration included and with previous coverage retained. The first phase solves a two-absorbing-endpoint recurrence; the second phase solves a one-absorbing, one-reflecting recurrence. The exact formula follows by the strong Markov property. Strict convexity in reset odds follows from the positive Chebyshev-coefficient recurrence and a nonnegative discounted-survival series. The graph-size threshold follows from the exact derivative at zero. Uniform Taylor expansion plus coercivity proves the limiting optimization and the order-one lattice correction. A second construction of the finite-state process has been checked with exact rational arithmetic for five graph sizes and four reset probabilities; the optional numerical asymptotic tests are not substituted for proofs.

A boundary detail is essential: the three-vertex case has an affine, strictly increasing mean in reset odds, not a strictly convex mean; strict convexity is claimed only for paths with at least five vertices. Reset events consume time, and non-reset steps from endpoints move inward deterministically. The limiting diffusion coefficient is the unit-step symmetric walk's standard one-half.

## Originality — PASS, qualified

The most relevant primary source, Linn and Lawley (2024), gives an exact continuous reflecting-interval formula and frequent-reset network asymptotics, not an exact finite discrete graph cover-time optimization. The continuum function in this finding is explicitly identified as already known, rather than claimed original. Das and Giuggioli (2022) give general resetting renewal and bounded-lattice first-passage formulas, using a different stay-or-move convention at reflecting endpoints and investigating a *single* target rather than the time to visit both endpoints. Michelitsch and coauthors (2024) develop network first-hitting statistics, not this two-endpoint cover and strict odds-convexity threshold. Pal and Prasad (2018) consider Brownian interval exit, stopping at the first endpoint, not full coverage.

Targeted published-record searches for equivalences, stronger graph-level results, exact tables and parameter changes returned only distinct mathematical objects or broader first-passage frameworks. The latest available historical ledger's recoverable claims were compared and no same claim found. These comparisons establish a qualified best-knowledge originality assessment, not a proof of global priority. A general unpublished or differently indexed theorem could still imply the finite path optimization; that is a residual risk.

## Value — PASS

The natural mathematical question is whether stochastic resetting really benefits finite exhaustive path exploration and, if so, whether its optimum is unique. The result gives the exact first graph size at which the answer changes, proves global uniqueness for *all* positive integer half-lengths, and quantifies how optimal finite-graph performance differs at order one from the established diffusion limit. This is a structural optimization and finite-size statement, not merely a new name for a known Brownian formula, an isolated numerical example, or a routine parameter substitution.

## Limitations

The conclusions are specific to a central reset, a graph-neighbor reflected walk, and independent per-step geometric resetting. The prior continuous limiting function is credited. The decimal constants are non-certified approximations. Both independent audit and definitive historical priority remain outstanding.

Self-review: passed. Independent audit: not yet performed.
