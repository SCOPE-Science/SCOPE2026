# Independent mathematical audit

## correctness

PASS

Verified symbolically, without executing the frozen verifier. Each of the four pairs of adjacent increments gives one free color-rotation orbit of proper triples, so the rule is center color plus g(u,v); every increment triple extends bilaterally. Thus v+g(v,w)−g(u,v) must never be zero mod 3. Normalize g(−,−)=0 and call the other entries b,c,d in order (−,+),(+,−),(+,+). The test reduces to b≠1, c≠2, c−b≠2, d−b≠2, d−c≠1. In (b,c) order (0,0),(2,0),(0,1),(2,1), the allowed d sets are {0},{0,2},{0,1},∅, respectively. This is exactly the five listed classes modulo constant offsets; all are distinct on admissible triples and each has three color translates. The increment rule for T+ on bits (a,b,c) is (a AND NOT b) OR (b AND c), hence 184, and T− gives its bit-complement conjugate, 226. For 184 reading 1100 from all predecessor pairs leaves successively {00,01,11}, {11}, {10}, and ∅; the complementary witness gives 0011 for 226. Every binary sequence has a proper coloring lift, so a missing edge cylinder implies nonsurjectivity of each lift; the remaining nine maps have explicit shift/rotation inverses. Reflection x↦−x conjugates T+ to T− and excludes both distinct traffic classes, and negates the constant rotations while preserving the spatial shifts. Together with cyclic symmetry this leaves exactly three maps. The frozen script's finite ring checks are supplementary; the local constraints and predecessor witnesses apply to bilateral configurations, only within the stated centered radius.

## originality

PASS

The supported distinct contribution is the whole low-radius proper-coloring classification, including exactly which classical binary rules are induced and the consequent surjectivity and full-permutation subcounts. Neither the traffic update itself nor the general extension framework is credited as new. The primary extension result and the strongest indexed traffic-image match do not classify local rules that preserve this particular constrained shift.

## value

PASS

This is a complete classification at the first nontrivial locality radius for a natural nearest-neighbor constraint and natural color symmetry. It shows a structural dichotomy between isomorphisms and a specific pair of traffic factors, and explains why enforcing all color permutations removes the noninvertible maps. That content is more informative than the bare count 15 or a small-ring census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
