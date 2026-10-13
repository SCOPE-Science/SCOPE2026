# Self-review

## Correctness
PASS. The proof reduces exact reachability to a cyclic-boundary reverse-extension lemma. Every proper nonempty subset has an excluded-to-included boundary; its least boundary gives a predecessor one state larger using a word of length at most \(n\). Equality in that step forces the canonical cyclic interval. For the canonical interval, a reverse path cannot increase cardinality until \(n-1\) inverse rotations have occurred, after which the unique larger predecessor is the next canonical interval. Induction gives both the upper and lower bounds. Exhaustive power-automaton BFS for \(2\le n\le12\) independently checks all exact distances and equality cases.

## Originality
PASS. The 2016 primary source proves the \(n(n-k)\) upper bound but does not classify its equality cases. The closest 2026 source states layerwise sharpness for the Černý family and gives only the \(n=4\) worst subsets in the inspected material. Searches for exact-image equality, reaching-threshold equality, aliases, and the nearby avoiding formulation returned no source stating the all-\(n\) uniqueness theorem. The closest nearby result is an avoiding-threshold classification; it does not imply exact-image reachability because avoiding a forbidden set allows any image contained in its complement.

## Value
PASS. Equality structure for Don's natural reaching bound is a structural invariant of the canonical extremal synchronizing family, not an arbitrary finite census. The theorem resolves every cardinality layer simultaneously, gives a strict one-step separation from all other exact images, and supplies a reusable extremal template for comparisons in complete reachability.

## Closest literature and limitations
The closest primary sources are Don (2016), DOI 10.37236/5616, and Ferens–Szykuła (2026), DOI 10.1145/3798283. Residual risk is an obscure or unindexed source containing the same all-layer equality classification. The theorem is restricted to the standard Černý family.

Self-review: passed. Independent audit: not yet performed.
