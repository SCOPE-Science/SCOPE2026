# Independent mathematical audit

## correctness

PASS

An extension of a matching is a perfect matching on the unused rows and columns with the remaining diagonal deleted. For residual order m≥3, even after excluding a specified further off-diagonal edge, a row has ≥m−2 neighbors, two rows have ≥m−1 neighbors (at most one column loses both edges), and ≥3 rows see every column. Hall gives existence and avoidance of every candidate forced extra cell. For m=2 there are just two completions before exclusions; the one or two diagonal forbiddances remove just one of them when present, and otherwise the two completions share no edge. At m=1 the final cell must be off diagonal, and m=0 is a full derangement. Nonmatchings have no extensions. Inclusion–exclusion gives the rook and derangement counts; for the remaining closed two-hole matchings, choose disjoint unordered unused row and column pairs in binom(n,2)binom(n−2,2) ways, then forbid the n−4 diagonal positions in the remaining board. The atom join detects exactly same-row/column conflicts, including n=4 since every compatible pair has a completion. The maximal conflict cliques are precisely the stars of the crown graph, each of size n−1≥3, and their intersection graph recovers the connected bipartite crown graph. Its missing cross pairs force identical row and column permutations up to a side swap. Atom actions determine the whole lattice action and all the listed actions are realized. For Horn sufficiency, use conflict-pair rules and the exceptional two-hole premises. From an (n−1)-matching with missing row i and column j≠i, remove the cell in row j: the reduced premise has intersecting unused labels and forces the true last cell. If the missing position is (i,i), remove any retained off-diagonal (u,v); the reduced premise forces (u,i) and (i,v), which conflict with (u,v) in the full input, yielding top by chaining. For necessity, a derangement on any n−2 labels gives a nonclosed matching all of whose proper subsets are closed; no smaller sound premise can initiate a new conclusion. This verifies the optimal unit-rule width for iterated chaining. Read both supporting files without executing the supplied script. Its finite closure/count tests, Horn replays and generator checks support different claims and ranges; the review does not treat them as an all-order proof or an exhaustive automorphism search. A replay requires Python 3.10+ for int.bit_count.

## originality

PASS

The closed-intent classification and count have material overlapping coverage, through prior crown-graph forcing subsets and the catalogue's trace-extension classification; the rook and derangement counts are not original. The distinct contribution supported here is the lattice-specific full automorphism reconstruction and sharp complete iterative unit-Horn arity, including the two-hole rules reaching top from a diagonal singleton hole. The inspected results on forcing or traces do not themselves supply those conclusions, and the ordinary permutation-board implication theorem has different closure and width.

## value

PASS

The result explains how a natural single forbidden matching changes consequence propagation relative to the complete assignment board: two holes can force completion, and those same implications plus conflict rules suffice even for an unextendible near-completion. The first-step lower bound proves the compression is sharp under arbitrary forward chaining. The symmetry reconstruction also gives the full automorphism group, rather than just an obvious action on the models. This is useful structural information about the closure and its presentations, not just a recomputation of derangement counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
