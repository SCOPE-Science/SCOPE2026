# Independent mathematical audit

## correctness

PASS

Reconstructed the specified J5 using the short and long rims and the spokes. In any perfect matching the selected rim edges must be disjoint on each rim, and the remaining rim vertices must include exactly one at each of the five spoke centres. The latter condition determines all the spokes, so the independent enumeration in /workspace/branches/replay/r5_rim.py is exhaustive. It found 32 matchings, no three-cover, 200 four-covers, and tested all pairs of four-covers directly for three common matchings. It recovered 220 exchange edges and 42 components and matched every edge, matching, cover, exchange and component list in the supplied JSON certificate. Exhaustive degree-preserving relabelling gave one isomorphism type each at orders 1, 5, 7, 10, with multiplicities 10, 20, 10, 2 and edge counts 0, 5, 9, 15; global degrees were 0^10, 1^50, 2^50, 3^70, 4^20. The local covering multiplicities at each vertex must be 2,1,1, so the double edges are a matching; the recomputation found extension frequencies 5^10, 6^10, 7^10, 10^2. This is a finite result for the specified J5 only. No uploaded code was executed.

## originality

PASS

The exact single-matching exchange classification and doubled-matching extension frequencies are distinct from the inspected work. The optimum size, number of perfect matchings, and local doubling lemma are not original and are not used to justify this pass.

## value

PASS

At the canonical five-petal flower snark, the known optimum four does not say whether all optima can be reached by feasible single-matching replacements. Ten isolated optima and the complete set of 42 components answer that natural reachability question exactly; the extension frequencies additionally describe how optima are distributed over the known doubling invariant. This is a usable finite benchmark and obstruction, without claiming an implication for every snark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
