# Independent mathematical audit

## correctness

PASS

The triple edges of a de Bruijn cycle have one cyclic successor permutation, so neither a fixed point from aaaa nor a two-cycle from both abab and baba can occur for q³>2. Removing all unequal alternating triples leaves a balanced graph; the retained abb reaches a diagonal, xxy and xyy connect diagonals, and xxy reaches every off-diagonal from its source diagonal. For any chosen orientations, put a distinguished loop for each ordered pair of alternating edges at the appropriate off-diagonal. This preserves balance and connectivity; contracting and expanding disjoint two-edge blocks gives a rotation-respecting bijection to the desired extrema. The unchanged a₀a₀a₀ edge is a unique first edge under rotation. In a fixed-first-edge BEST count the last exits from nonroot vertices form an in-arborescence, and each vertex contributes (d−1)! from ordering the remaining exits or, at the root, fixing the first one. Added loops cannot affect arborescences or the Laplacian. Exactly q+binom(q,2) vertices have degree q and binom(q,2) degree q−1, proving the factor even at q=2. Independent integer cofactors give 1,108,3538944 for q=2,3,4. Literal Euler-tour exhaustion through q=3 gives one binary cycle per orientation and 6912 ternary cycles per orientation, totaling 55296 ternary extrema. Replay: /workspace/branches/ff311abc-2d88-4ea7-8b87-0804cec4890f/reproduce_square_checks.py and reproduction_results.txt in that directory. The supplied verifier was inspected, not executed; exhaustive enumeration was only binary and ternary.

## originality

PASS

The supported distinct claim is simultaneous free orientation of all alternating square pairs at the sharp packing bound, and uniform exact enumeration of those constrained full de Bruijn cycles. A same-day indexed theorem already covers individual occurrence/nonoccurrence, and another indexed theorem covers the tree cofactor exactly. Neither gives the interaction between all the prescribed local transitions within a single full tour. BEST and its cofactors are not original contributions here.

## value

PASS

The problem asks how many local repetitions a fully universal cycle can pack, whether their choices interact, and how many maximizers there are. The joint realization and exact equidistribution of an exponentially large family of prescribed transition sets is a natural structural classification, not a lookup of the cofactor or a small-cycle census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
