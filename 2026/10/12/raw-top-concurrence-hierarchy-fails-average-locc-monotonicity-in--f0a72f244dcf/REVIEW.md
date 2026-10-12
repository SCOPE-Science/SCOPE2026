# Review of Raw top concurrence hierarchy fails average LOCC monotonicity in every dimension \(d\ge 3\)

## Correctness
**PASS.** The proof is exact. Kraus completeness, branch probabilities, branch Schmidt spectra, and raw top concurrences are computed algebraically. The gain factor is \(3^{d-1}/(2d+1)\), and strict positivity above one for every \(d\ge3\) follows by induction. The bundled exact-rational checker reproduces representative cases but is not used to infer the infinite statement.

## Originality
**PASS.** The primary source defines the unrooted hierarchy and proves deterministic pure-to-pure monotonicity via Nielsen majorization. The closest inspected later work, Gour's concurrence-monotone family, explicitly uses a slightly different definition: normalized \(k\)-th roots of the elementary symmetric functions, with concavity used to establish strong monotonicity. Targeted searches for the raw hierarchy, average LOCC monotonicity, local-measurement counterexamples, exact Schmidt patterns, and \(G\)-concurrence found no implication-equivalent all-dimension counterfamily. The main residual risk is an obscure later note that may have made the same distinction.

## Value
**PASS.** This is not a renaming or a numerical edge case. It separates deterministic majorization monotonicity from average measurement monotonicity for a canonical published family, gives a uniform counterexample in every dimension \(d\ge3\), and shows an unbounded multiplicative violation. The comparison with Gour's rooted family identifies a concrete mathematical reason the root is essential.

## Closest literature and limitations
The closest source is G. Gour, *Family of Concurrence Monotones and its Applications* (2005), which replaces the raw elementary symmetric functions by normalized roots and proves the resulting functions concave. That construction does not state the present counterfamily because it studies a different functional. The finding is limited to the raw top member on pure bipartite states; lower raw members and mixed-state extensions are not classified.

Self-review: passed. Independent audit: not yet performed.
