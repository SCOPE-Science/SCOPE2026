# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 25–56. Three guards cover at most 12 of 14 vertices. A four-set with p points covers at most 12−2p points and 4+2p lines, so p=2. The two point guards meet five distinct lines, forcing the other two lines as the line guards. Their intersection is the third point on the line of the point pair: the two other lines through that third point avoid both occupied points, and no other lines do. Conversely these two lines cover the five unoccupied points, giving all 21 states indexed by incident flags. When two flags share a point, both new point destinations can only receive the guard from the one source line equal to the new flag's line. When the flags share a line, both new line destinations can only receive the one source guard on the new flag's point. Both are matching obstructions. Flag-transitivity and the verified sixteen routes from (0,L0) give all remaining moves. Independent replay `python3 /workspace/review_evidence/heawood_replay.py` checked all four-sets, all 210 unordered state pairs by subset DP, the 16 literal witness tuples and all 210 state/attack cases without running the submitted scripts. It recovered 168 shift edges. Under the flag bijection each vertex has four other flags sharing an endpoint, so degree 16, and each nonadjacent pair has a common neighbor; diameter is 2. After any attack there is a reachable state containing that vertex, still in the same family; reiteration is an infinite defense from each state. The domination lower bound gives optimality. The frozen cyclic and vector source scripts and stored outputs are consistent with this argument.

## originality

PASS

The supported distinct claim is the natural identification of the entire simultaneous-shift graph, not the 21-set census, the game rule, or merely equality of two domination numbers. The nearest indexed claim uses the very same set census but takes a shattering complex on individual vertices. The broader inspected eternal-domination results do not determine the one-step adjacency predicate for Heawood. No implication-equivalent classification was established in the bounded comparisons; the inaccessible papers remain explicit access risks.

## value

PASS

Heawood is the natural Fano incidence graph and optimal all-guards dynamics are a motivated state system. The exact identification explains its otherwise nonobvious pattern of 42 blocked pairs, supplies every admissible one-turn move and shows eternal defense from every minimum state. It adds structural information that neither the minimum-set census nor an optimum guard number supplies. The result stays within the stated finite graph and movement rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
