# Review of sharp low-budget power domination on Cartesian clique paths

## Correctness — PASS

The deterministic theorem follows from a two-way structural argument. Meeting an endpoint clique or two consecutive cliques makes propagation sweep the entire strip. If neither condition occurs with at most \(n-2\) seeds, at least two columns contain no seeds; their initially white vertices remain permanently white in every unoccupied layer, because each observed vertex either has at least two white clique neighbors or at least two white vertical neighbors, unless it can force only inside already represented columns. The \(n-1\)-seed second-layer witness proves sharpness. The independent-set substitution counts every and only the failing low-budget layer occupancy pattern; the Bernoulli result follows by a binomial-tail sandwich. Exhaustive direct propagation checks cover 257,426 subsets for \(3\leq n\leq6\), \(3\leq L\leq7\); the universal proof is not inferred from finite tests.

## Originality — PASS, subject to priority uncertainty

Koh and Soh's Cartesian-product article gives the existing singleton-minimum observation for this graph family; it does not supply the growing window of exact subset counts. Brimkov et al.'s power-domination polynomial paper supplies the counting framework and standard reductions but no formula for these clique-path products in its inspected family classification. Anderson, Kuenzel, and Schuerger establish Cartesian-product lower bounds and failed-partition methods but no corresponding all-subset enumeration. Fort-neighborhood duality does not automatically evaluate the current obstruction family. Searches considered equivalent notations, stronger generic graph-product coverage, small-graph coefficient tables and implications from the nearest sources. There remains a genuine possibility of differently formulated or unindexed prior work, and some display mathematics in the accessible Koh--Soh article could not be inspected.

## Mathematical value — PASS

This is a sharp qualitative description of all feasible sparse sensor configurations on an arbitrary-length natural clique strip, together with exact coefficients through \(n-2\), layer-sensitive counting, an explicit first failing budget, and a fixed-length Poisson-sensor reliability limit. These statements distinguish successful and unsuccessful multisensor deployment patterns that the known minimum power domination number does not distinguish.

## Limitations

No complete polynomial at degrees \(n-1\) and above is asserted. The asymptotic random-sensor result fixes strip length while the number of columns grows. The low-dimensional checker is corroborating evidence, not an infinite verification or an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
